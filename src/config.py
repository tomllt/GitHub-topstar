"""Configuration management for GitHub TopStar Tracker."""

import os
from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).parent.parent
ARCHIVES_DIR = BASE_DIR / "archives"
REPOS_DIR = ARCHIVES_DIR / "repos"
DOCS_DIR = BASE_DIR / "docs"

# GitHub API configuration
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
GITHUB_API_BASE = "https://api.github.com"

# Rate limiting
REQUEST_DELAY = 1.0  # seconds between requests
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds

# Data fetching settings
TOP_N = 20  # Number of top repositories to fetch
LANGUAGES = ["", "python", "javascript", "typescript", "go", "rust", "java"]

# Trending periods
TRENDING_PERIODS = ["daily", "weekly", "monthly"]

# README settings
README_MAX_LENGTH = 2000  # Maximum characters to store

# Ensure directories exist
def ensure_dirs():
    """Create necessary directories if they don't exist."""
    ARCHIVES_DIR.mkdir(parents=True, exist_ok=True)
    REPOS_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    (DOCS_DIR / "daily").mkdir(exist_ok=True)
    (DOCS_DIR / "weekly").mkdir(exist_ok=True)
    (DOCS_DIR / "monthly").mkdir(exist_ok=True)
    (DOCS_DIR / "trending").mkdir(exist_ok=True)
