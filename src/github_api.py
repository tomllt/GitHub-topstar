"""GitHub API client for fetching repository data."""

import base64
import time
import logging
from datetime import datetime, timedelta
from typing import Optional
import requests

from . import config

logger = logging.getLogger(__name__)


class GitHubAPIClient:
    """Client for interacting with GitHub API."""
    
    def __init__(self, token: str = None):
        self.token = token or config.GITHUB_TOKEN
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "GitHub-TopStar-Tracker",
        })
        if self.token:
            self.session.headers["Authorization"] = f"token {self.token}"
        
        self._rate_limit_remaining = 5000
        self._rate_limit_reset = datetime.now()
    
    def _check_rate_limit(self, response: requests.Response):
        """Update rate limit info from response headers."""
        remaining = response.headers.get("X-RateLimit-Remaining")
        reset_time = response.headers.get("X-RateLimit-Reset")
        
        if remaining:
            self._rate_limit_remaining = int(remaining)
        if reset_time:
            self._rate_limit_reset = datetime.fromtimestamp(int(reset_time))
        
        if self._rate_limit_remaining < 100:
            wait_time = (self._rate_limit_reset - datetime.now()).total_seconds()
            if wait_time > 0:
                logger.warning(f"Rate limit low ({self._rate_limit_remaining}), waiting {wait_time:.0f}s")
                time.sleep(min(wait_time, 60))
    
    def _request(self, method: str, url: str, **kwargs) -> Optional[dict]:
        """Make a request with retry logic."""
        for attempt in range(config.MAX_RETRIES):
            try:
                time.sleep(config.REQUEST_DELAY)
                response = self.session.request(method, url, **kwargs)
                self._check_rate_limit(response)
                
                if response.status_code == 200:
                    return response.json()
                elif response.status_code == 403:
                    logger.warning(f"Rate limited, waiting...")
                    time.sleep(config.RETRY_DELAY * (attempt + 1))
                elif response.status_code == 404:
                    logger.debug(f"Not found: {url}")
                    return None
                else:
                    logger.error(f"Request failed: {response.status_code} - {url}")
                    
            except requests.RequestException as e:
                logger.error(f"Request error: {e}")
                time.sleep(config.RETRY_DELAY * (attempt + 1))
        
        return None
    
    def search_repositories(
        self,
        query: str,
        sort: str = "stars",
        order: str = "desc",
        per_page: int = 20
    ) -> list:
        """Search repositories using GitHub Search API."""
        url = f"{config.GITHUB_API_BASE}/search/repositories"
        params = {
            "q": query,
            "sort": sort,
            "order": order,
            "per_page": per_page,
        }
        
        result = self._request("GET", url, params=params)
        if result and "items" in result:
            return result["items"]
        return []
    
    def get_top_starred_repos(
        self,
        period: str = "daily",
        language: str = "",
        top_n: int = None
    ) -> list:
        """Get top starred repositories for a given period.
        
        Args:
            period: 'daily', 'weekly', or 'monthly'
            language: Programming language filter (empty for all)
            top_n: Number of repos to fetch
        """
        top_n = top_n or config.TOP_N
        
        # Calculate date range based on period
        now = datetime.utcnow()
        if period == "daily":
            since = now - timedelta(days=1)
        elif period == "weekly":
            since = now - timedelta(weeks=1)
        elif period == "monthly":
            since = now - timedelta(days=30)
        else:
            since = now - timedelta(days=1)
        
        date_str = since.strftime("%Y-%m-%d")
        
        # Build search query
        query_parts = [f"pushed:>{date_str}", "stars:>100"]
        if language:
            query_parts.append(f"language:{language}")
        
        query = " ".join(query_parts)
        
        repos = self.search_repositories(query, sort="stars", per_page=top_n)
        return self._format_repos(repos)
    
    def _format_repos(self, repos: list) -> list:
        """Format repository data for storage."""
        formatted = []
        for repo in repos:
            formatted.append({
                "full_name": repo.get("full_name", ""),
                "owner": repo.get("owner", {}).get("login", ""),
                "name": repo.get("name", ""),
                "description": repo.get("description", "") or "",
                "language": repo.get("language", "") or "",
                "stars": repo.get("stargazers_count", 0),
                "forks": repo.get("forks_count", 0),
                "open_issues": repo.get("open_issues_count", 0),
                "watchers": repo.get("watchers_count", 0),
                "url": repo.get("html_url", ""),
                "homepage": repo.get("homepage", "") or "",
                "topics": repo.get("topics", []),
                "license": repo.get("license", {}).get("spdx_id", "") if repo.get("license") else "",
                "created_at": repo.get("created_at", ""),
                "updated_at": repo.get("updated_at", ""),
                "pushed_at": repo.get("pushed_at", ""),
            })
        return formatted
    
    def get_repo_detail(self, full_name: str) -> Optional[dict]:
        """Get detailed information for a repository."""
        url = f"{config.GITHUB_API_BASE}/repos/{full_name}"
        repo = self._request("GET", url)
        
        if repo:
            return self._format_repos([repo])[0]
        return None
    
    def get_readme(self, full_name: str) -> Optional[str]:
        """Get README content for a repository."""
        url = f"{config.GITHUB_API_BASE}/repos/{full_name}/readme"
        result = self._request("GET", url)
        
        if result and "content" in result:
            try:
                content = base64.b64decode(result["content"]).decode("utf-8")
                # Truncate if too long
                if len(content) > config.README_MAX_LENGTH:
                    content = content[:config.README_MAX_LENGTH] + "\n\n... (truncated)"
                return content
            except Exception as e:
                logger.error(f"Failed to decode README for {full_name}: {e}")
        
        return None
    
    def get_all_top_repos(self, languages: list = None) -> dict:
        """Get top repos for all periods and languages.
        
        Returns dict with structure:
        {
            "daily": {"all": [...], "python": [...], ...},
            "weekly": {...},
            "monthly": {...}
        }
        """
        languages = languages or config.LANGUAGES
        result = {}
        
        for period in config.TRENDING_PERIODS:
            result[period] = {}
            for lang in languages:
                lang_key = lang or "all"
                logger.info(f"Fetching {period} top repos for {lang_key}...")
                repos = self.get_top_starred_repos(period=period, language=lang)
                result[period][lang_key] = repos
                time.sleep(2)  # Extra delay for Search API rate limit
        
        return result
