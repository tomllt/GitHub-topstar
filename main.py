#!/usr/bin/env python3
"""
GitHub TopStar Tracker - Main entry point.

Fetches GitHub trending repositories and generates Markdown reports.
"""

import argparse
import logging
import sys
from datetime import datetime, timezone

from src import config
from src.github_api import GitHubAPIClient
from src.trending_scraper import TrendingScraper
from src.generator import MarkdownGenerator, DataManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
    ]
)
logger = logging.getLogger(__name__)


def merge_repo_data(api_repos: list, trending_repos: list) -> list:
    """Merge API data with trending data, preferring trending stars_today."""
    # Create lookup for trending repos
    trending_lookup = {r["full_name"]: r for r in trending_repos}
    
    merged = []
    seen = set()
    
    # First add trending repos (they have stars_today)
    for repo in trending_repos:
        merged.append(repo)
        seen.add(repo["full_name"])
    
    # Then add API repos not in trending
    for repo in api_repos:
        if repo["full_name"] not in seen:
            merged.append(repo)
            seen.add(repo["full_name"])
    
    # Sort by stars_today (if available) then by total stars
    merged.sort(key=lambda x: (x.get("stars_today", 0), x.get("stars", 0)), reverse=True)
    
    return merged


def run_tracker():
    """Main tracker function."""
    logger.info("Starting GitHub TopStar Tracker...")
    
    # Ensure directories exist
    config.ensure_dirs()
    
    # Initialize components
    api_client = GitHubAPIClient()
    scraper = TrendingScraper()
    generator = MarkdownGenerator()
    data_manager = DataManager()
    
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    logger.info(f"Processing date: {today}")
    
    # Step 1: Scrape GitHub Trending (doesn't use API quota)
    logger.info("Scraping GitHub Trending...")
    trending_data = scraper.get_all_trending(
        languages=["", "python", "javascript", "typescript", "go", "rust"]
    )
    
    # Step 2: Get top repos from API
    logger.info("Fetching top repos from GitHub API...")
    api_data = {}
    
    if config.GITHUB_TOKEN:
        api_data = api_client.get_all_top_repos(
            languages=["", "python", "javascript", "go", "rust"]
        )
    else:
        logger.warning("No GITHUB_TOKEN set, skipping API data fetch")
    
    # Step 3: Merge data - prefer trending data for stars_today
    daily_trending = trending_data.get("daily", {}).get("all", [])
    daily_api = api_data.get("daily", {}).get("all", [])
    daily_top = merge_repo_data(daily_api, daily_trending)
    
    # Step 4: Fetch README for top 5 repos
    logger.info("Fetching README for top repos...")
    readmes = {}
    
    if config.GITHUB_TOKEN:
        for repo in daily_top[:5]:
            full_name = repo["full_name"]
            
            # Try cache first
            cached = data_manager.load_readme(full_name)
            if cached:
                readmes[full_name] = cached
                continue
            
            # Fetch from API
            readme = api_client.get_readme(full_name)
            if readme:
                readmes[full_name] = readme
                data_manager.save_readme(full_name, readme)
    
    # Step 5: Save raw data
    raw_data = {
        "date": today,
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "daily_top": daily_top[:config.TOP_N],
        "trending": trending_data,
    }
    data_manager.save_daily_data(today, raw_data)
    
    # Step 6: Generate daily report
    logger.info("Generating daily report...")
    report_content = generator.generate_daily_report(
        date=today,
        daily_top=daily_top,
        trending_data=trending_data,
        readmes=readmes,
    )
    data_manager.save_report("daily", f"{today}.md", report_content)
    
    # Step 7: Update index pages
    logger.info("Updating index pages...")
    data_manager.update_index("daily", generator)
    
    # Step 8: Update home page
    logger.info("Updating home page...")
    trending_all = trending_data.get("daily", {}).get("all", [])
    data_manager.update_home(daily_top, trending_all, generator)
    
    # Step 9: Update trending page
    logger.info("Updating trending page...")
    data_manager.update_trending_page(trending_data, generator)
    
    logger.info("GitHub TopStar Tracker completed successfully!")
    
    # Print summary
    print("\n" + "=" * 50)
    print("Summary")
    print("=" * 50)
    print(f"Date: {today}")
    print(f"Total repos tracked: {len(daily_top)}")
    print(f"Reports generated: docs/daily/{today}.md")
    print("=" * 50)


def main():
    """Entry point with argument parsing."""
    parser = argparse.ArgumentParser(
        description="GitHub TopStar Tracker - Track trending GitHub repositories"
    )
    parser.add_argument(
        "--mode",
        choices=["daily", "weekly", "monthly", "all"],
        default="daily",
        help="Report mode (default: daily)"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging"
    )
    
    args = parser.parse_args()
    
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        run_tracker()
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
