"""Scraper for GitHub Trending page."""

import re
import time
import logging
from typing import Optional
import requests
from bs4 import BeautifulSoup

from . import config

logger = logging.getLogger(__name__)

TRENDING_URL = "https://github.com/trending"


class TrendingScraper:
    """Scraper for GitHub Trending page."""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
        })
    
    def _parse_stars_today(self, text: str) -> int:
        """Parse stars today from text like '1,234 stars today'."""
        if not text:
            return 0
        match = re.search(r"([\d,]+)\s+stars?\s+(?:today|this week|this month)", text, re.I)
        if match:
            return int(match.group(1).replace(",", ""))
        return 0
    
    def _parse_total_stars(self, text: str) -> int:
        """Parse total stars from text."""
        if not text:
            return 0
        text = text.strip().replace(",", "")
        try:
            return int(text)
        except ValueError:
            return 0
    
    def scrape_trending(
        self,
        language: str = "",
        since: str = "daily"
    ) -> list:
        """Scrape GitHub Trending page.
        
        Args:
            language: Programming language filter (empty for all)
            since: Time range - 'daily', 'weekly', or 'monthly'
            
        Returns:
            List of trending repositories
        """
        url = TRENDING_URL
        if language:
            url = f"{url}/{language}"
        
        params = {}
        if since == "weekly":
            params["since"] = "weekly"
        elif since == "monthly":
            params["since"] = "monthly"
        # daily is default, no param needed
        
        try:
            time.sleep(config.REQUEST_DELAY)
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Failed to fetch trending page: {e}")
            return []
        
        return self._parse_trending_page(response.text)
    
    def _parse_trending_page(self, html: str) -> list:
        """Parse trending page HTML."""
        soup = BeautifulSoup(html, "html.parser")
        repos = []
        
        # Find all repo articles
        articles = soup.select("article.Box-row")
        
        for rank, article in enumerate(articles, 1):
            try:
                repo = self._parse_repo_article(article, rank)
                if repo:
                    repos.append(repo)
            except Exception as e:
                logger.error(f"Failed to parse repo article: {e}")
                continue
        
        return repos
    
    def _parse_repo_article(self, article, rank: int) -> Optional[dict]:
        """Parse a single repo article element."""
        # Get repo name
        name_elem = article.select_one("h2 a")
        if not name_elem:
            return None
        
        href = name_elem.get("href", "").strip("/")
        if "/" not in href:
            return None
        
        parts = href.split("/")
        owner = parts[0]
        name = parts[1] if len(parts) > 1 else ""
        full_name = f"{owner}/{name}"
        
        # Get description
        desc_elem = article.select_one("p")
        description = desc_elem.get_text(strip=True) if desc_elem else ""
        
        # Get language
        lang_elem = article.select_one("[itemprop='programmingLanguage']")
        language = lang_elem.get_text(strip=True) if lang_elem else ""
        
        # Get total stars
        star_elem = article.select_one("a[href$='/stargazers']")
        total_stars = 0
        if star_elem:
            total_stars = self._parse_total_stars(star_elem.get_text())
        
        # Get stars today/this week/this month
        stars_today_elem = article.select_one("span.d-inline-block.float-sm-right")
        stars_today = 0
        if stars_today_elem:
            stars_today = self._parse_stars_today(stars_today_elem.get_text())
        
        # Get forks
        fork_elem = article.select_one("a[href$='/forks']")
        forks = 0
        if fork_elem:
            forks = self._parse_total_stars(fork_elem.get_text())
        
        # Get built by (contributors)
        contributors = []
        built_by = article.select("span.d-inline-block a img")
        for img in built_by[:5]:  # Max 5 contributors
            alt = img.get("alt", "").lstrip("@")
            if alt:
                contributors.append(alt)
        
        return {
            "rank": rank,
            "full_name": full_name,
            "owner": owner,
            "name": name,
            "description": description,
            "language": language,
            "stars": total_stars,
            "stars_today": stars_today,
            "forks": forks,
            "url": f"https://github.com/{full_name}",
            "contributors": contributors,
        }
    
    def get_all_trending(self, languages: list = None) -> dict:
        """Get trending repos for all periods and languages.
        
        Returns dict with structure:
        {
            "daily": {"all": [...], "python": [...], ...},
            "weekly": {...},
            "monthly": {...}
        }
        """
        languages = languages or ["", "python", "javascript", "typescript", "go", "rust"]
        result = {}
        
        for period in ["daily", "weekly", "monthly"]:
            result[period] = {}
            for lang in languages:
                lang_key = lang or "all"
                logger.info(f"Scraping {period} trending for {lang_key}...")
                repos = self.scrape_trending(language=lang, since=period)
                result[period][lang_key] = repos
                time.sleep(2)  # Be nice to GitHub
        
        return result
