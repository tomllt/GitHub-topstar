"""Markdown report generator for GitHub TopStar."""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional
from jinja2 import Environment, BaseLoader

from . import config

logger = logging.getLogger(__name__)


# Markdown templates
DAILY_REPORT_TEMPLATE = """---
layout: default
title: {{ date }} 每日报告
---

# {{ date }} Star 增长 TOP 20

> 更新时间: {{ generated_at }}

## 今日 Star 飙升 TOP 20

| 排名 | 项目 | 语言 | 今日增长 | 总 Star | 描述 |
|------|------|------|----------|---------|------|
{% for repo in daily_top[:20] -%}
| {{ loop.index }} | [{{ repo.full_name }}]({{ repo.url }}) | {{ repo.language or '-' }} | {% if repo.stars_today %}+{{ repo.stars_today }}{% else %}-{% endif %} | {{ repo.stars | format_stars }} | {{ repo.description | truncate(50) }} |
{% endfor %}

---

## Trending 热门推荐

### 全语言 TOP 10

| 排名 | 项目 | 语言 | 今日 Star | 描述 |
|------|------|------|-----------|------|
{% for repo in trending_all[:10] -%}
| {{ loop.index }} | [{{ repo.full_name }}]({{ repo.url }}) | {{ repo.language or '-' }} | +{{ repo.stars_today }} | {{ repo.description | truncate(50) }} |
{% endfor %}

{% for lang, repos in trending_by_lang.items() if repos %}
### {{ lang | title }} TOP 5

| 排名 | 项目 | 今日 Star | 描述 |
|------|------|-----------|------|
{% for repo in repos[:5] -%}
| {{ loop.index }} | [{{ repo.full_name }}]({{ repo.url }}) | +{{ repo.stars_today }} | {{ repo.description | truncate(50) }} |
{% endfor %}

{% endfor %}

---

## TOP 5 项目详情

{% for repo in daily_top[:5] %}
### {{ loop.index }}. [{{ repo.full_name }}]({{ repo.url }})

> {{ repo.description }}

| 语言 | Stars | Forks | Issues | License |
|------|-------|-------|--------|---------|
| {{ repo.language or '-' }} | {{ repo.stars | format_stars }} | {{ repo.forks | format_stars }} | {{ repo.open_issues }} | {{ repo.license or '-' }} |

{% if repo.topics %}**Topics**: {% for topic in repo.topics[:5] %}`{{ topic }}` {% endfor %}{% endif %}

{% if repo.readme %}
<details>
<summary>README 摘要</summary>

{{ repo.readme | truncate(1000) }}

</details>
{% endif %}

---

{% endfor %}

[← 返回索引](index.md)
"""

INDEX_TEMPLATE = """---
layout: default
title: {{ title }}
---

# {{ title }}

{% for year, months in archives.items() | sort(reverse=true) %}
## {{ year }}年

{% for month, days in months.items() | sort(reverse=true) %}
### {{ month }}月

| 日期 | 链接 |
|------|------|
{% for day in days | sort(reverse=true) -%}
| {{ day }} | [查看]({{ day }}.md) |
{% endfor %}

{% endfor %}
{% endfor %}
"""

HOME_TEMPLATE = """---
layout: default
title: GitHub TopStar
---

# GitHub TopStar 排行榜

> 最后更新: {{ generated_at }}

## 今日 Star 飙升 TOP 10

| # | 项目 | 语言 | 今日 Star | 总 Star | 简介 |
|---|------|------|----------|---------|------|
{% for repo in daily_top[:10] -%}
| {{ loop.index }} | [{{ repo.full_name }}]({{ repo.url }}) | {{ repo.language or '-' }} | {% if repo.stars_today %}+{{ repo.stars_today }}{% else %}-{% endif %} | {{ repo.stars | format_stars }} | {{ repo.description | truncate(40) }} |
{% endfor %}

[查看完整每日榜单 →](daily/)

---

## Trending 热门推荐

| # | 项目 | 语言 | 今日 Star | 简介 |
|---|------|------|----------|------|
{% for repo in trending_all[:10] -%}
| {{ loop.index }} | [{{ repo.full_name }}]({{ repo.url }}) | {{ repo.language or '-' }} | +{{ repo.stars_today }} | {{ repo.description | truncate(40) }} |
{% endfor %}

[查看更多 →](trending/)

---

## 导航

- [每日榜单](daily/) - 每日 Star 增长 TOP 20
- [每周榜单](weekly/) - 每周 Star 增长统计
- [每月榜单](monthly/) - 每月 Star 增长统计
- [Trending](trending/) - GitHub Trending 热门推荐

---

*数据由 GitHub Actions 自动更新*
"""

TRENDING_TEMPLATE = """---
layout: default
title: GitHub Trending
---

# GitHub Trending 热门推荐

> 更新时间: {{ generated_at }}

## 今日热门 (全语言)

| 排名 | 项目 | 语言 | 今日 Star | 总 Star | 描述 |
|------|------|------|-----------|---------|------|
{% for repo in daily_all[:20] -%}
| {{ loop.index }} | [{{ repo.full_name }}]({{ repo.url }}) | {{ repo.language or '-' }} | +{{ repo.stars_today }} | {{ repo.stars | format_stars }} | {{ repo.description | truncate(50) }} |
{% endfor %}

---

{% for lang, repos in daily_by_lang.items() if repos %}
## {{ lang | title }}

| 排名 | 项目 | 今日 Star | 总 Star | 描述 |
|------|------|-----------|---------|------|
{% for repo in repos[:10] -%}
| {{ loop.index }} | [{{ repo.full_name }}]({{ repo.url }}) | +{{ repo.stars_today }} | {{ repo.stars | format_stars }} | {{ repo.description | truncate(50) }} |
{% endfor %}

---

{% endfor %}

## 本周热门

| 排名 | 项目 | 语言 | 本周 Star | 描述 |
|------|------|------|-----------|------|
{% for repo in weekly_all[:10] -%}
| {{ loop.index }} | [{{ repo.full_name }}]({{ repo.url }}) | {{ repo.language or '-' }} | +{{ repo.stars_today }} | {{ repo.description | truncate(50) }} |
{% endfor %}

---

## 本月热门

| 排名 | 项目 | 语言 | 本月 Star | 描述 |
|------|------|------|-----------|------|
{% for repo in monthly_all[:10] -%}
| {{ loop.index }} | [{{ repo.full_name }}]({{ repo.url }}) | {{ repo.language or '-' }} | +{{ repo.stars_today }} | {{ repo.description | truncate(50) }} |
{% endfor %}
"""


class MarkdownGenerator:
    """Generator for Markdown reports."""
    
    def __init__(self):
        self.env = Environment(loader=BaseLoader())
        self.env.filters["format_stars"] = self._format_stars
        self.env.filters["truncate"] = self._truncate
    
    @staticmethod
    def _format_stars(num: int) -> str:
        """Format star count (e.g., 45231 -> 45.2k)."""
        if num >= 1000000:
            return f"{num/1000000:.1f}M"
        elif num >= 1000:
            return f"{num/1000:.1f}k"
        return str(num)
    
    @staticmethod
    def _truncate(text: str, length: int = 100) -> str:
        """Truncate text to specified length."""
        if not text:
            return ""
        text = text.replace("\n", " ").replace("|", "/")
        if len(text) <= length:
            return text
        return text[:length-3] + "..."
    
    def render(self, template_str: str, **kwargs) -> str:
        """Render a template with given context."""
        template = self.env.from_string(template_str)
        return template.render(**kwargs)
    
    def generate_daily_report(
        self,
        date: str,
        daily_top: list,
        trending_data: dict,
        readmes: dict = None
    ) -> str:
        """Generate daily report markdown."""
        # Add README to top repos
        if readmes:
            for repo in daily_top:
                repo["readme"] = readmes.get(repo["full_name"], "")
        
        trending_all = trending_data.get("daily", {}).get("all", [])
        trending_by_lang = {
            k: v for k, v in trending_data.get("daily", {}).items()
            if k != "all"
        }
        
        return self.render(
            DAILY_REPORT_TEMPLATE,
            date=date,
            generated_at=datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
            daily_top=daily_top,
            trending_all=trending_all,
            trending_by_lang=trending_by_lang,
        )
    
    def generate_index(self, title: str, archives: dict) -> str:
        """Generate index page for reports."""
        return self.render(INDEX_TEMPLATE, title=title, archives=archives)
    
    def generate_home(self, daily_top: list, trending_all: list) -> str:
        """Generate home page."""
        return self.render(
            HOME_TEMPLATE,
            generated_at=datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
            daily_top=daily_top,
            trending_all=trending_all,
        )
    
    def generate_trending_page(self, trending_data: dict) -> str:
        """Generate trending page."""
        daily = trending_data.get("daily", {})
        weekly = trending_data.get("weekly", {})
        monthly = trending_data.get("monthly", {})
        
        daily_by_lang = {k: v for k, v in daily.items() if k != "all"}
        
        return self.render(
            TRENDING_TEMPLATE,
            generated_at=datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
            daily_all=daily.get("all", []),
            daily_by_lang=daily_by_lang,
            weekly_all=weekly.get("all", []),
            monthly_all=monthly.get("all", []),
        )


class DataManager:
    """Manager for data storage and retrieval."""
    
    def __init__(self, base_dir: Path = None):
        self.base_dir = base_dir or config.BASE_DIR
        self.archives_dir = self.base_dir / "archives"
        self.docs_dir = self.base_dir / "docs"
    
    def save_daily_data(self, date: str, data: dict):
        """Save daily data to JSON archive."""
        year, month, _ = date.split("-")
        archive_dir = self.archives_dir / year / month
        archive_dir.mkdir(parents=True, exist_ok=True)
        
        filepath = archive_dir / f"{date}.json"
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Saved daily data to {filepath}")
    
    def load_daily_data(self, date: str) -> Optional[dict]:
        """Load daily data from JSON archive."""
        year, month, _ = date.split("-")
        filepath = self.archives_dir / year / month / f"{date}.json"
        
        if filepath.exists():
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        return None
    
    def save_readme(self, full_name: str, content: str):
        """Save README content to cache."""
        repos_dir = self.archives_dir / "repos"
        repos_dir.mkdir(parents=True, exist_ok=True)
        
        filename = full_name.replace("/", "_") + ".md"
        filepath = repos_dir / filename
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
    
    def load_readme(self, full_name: str) -> Optional[str]:
        """Load README content from cache."""
        filename = full_name.replace("/", "_") + ".md"
        filepath = self.archives_dir / "repos" / filename
        
        if filepath.exists():
            with open(filepath, "r", encoding="utf-8") as f:
                return f.read()
        return None
    
    def save_report(self, report_type: str, filename: str, content: str):
        """Save markdown report to docs directory."""
        report_dir = self.docs_dir / report_type
        report_dir.mkdir(parents=True, exist_ok=True)
        
        filepath = report_dir / filename
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
        logger.info(f"Saved report to {filepath}")
    
    def get_archive_dates(self, report_type: str = "daily") -> dict:
        """Get all archived dates organized by year/month."""
        archives = {}
        
        for year_dir in sorted(self.archives_dir.glob("[0-9][0-9][0-9][0-9]"), reverse=True):
            year = year_dir.name
            archives[year] = {}
            
            for month_dir in sorted(year_dir.glob("[0-9][0-9]"), reverse=True):
                month = month_dir.name
                dates = []
                
                for json_file in sorted(month_dir.glob("*.json"), reverse=True):
                    dates.append(json_file.stem)
                
                if dates:
                    archives[year][month] = dates
        
        return archives
    
    def update_index(self, report_type: str, generator: MarkdownGenerator):
        """Update index page for a report type."""
        archives = self.get_archive_dates(report_type)
        titles = {
            "daily": "每日报告归档",
            "weekly": "每周报告归档",
            "monthly": "每月报告归档",
        }
        
        content = generator.generate_index(titles.get(report_type, "报告归档"), archives)
        self.save_report(report_type, "index.md", content)
    
    def update_home(self, daily_top: list, trending_all: list, generator: MarkdownGenerator):
        """Update home page."""
        content = generator.generate_home(daily_top, trending_all)
        
        filepath = self.docs_dir / "index.md"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
        logger.info(f"Updated home page")
    
    def update_trending_page(self, trending_data: dict, generator: MarkdownGenerator):
        """Update trending page."""
        content = generator.generate_trending_page(trending_data)
        self.save_report("trending", "index.md", content)
