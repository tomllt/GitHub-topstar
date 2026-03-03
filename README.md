# GitHub TopStar Tracker

自动追踪 GitHub 上 Star 增长最快的项目，每日更新排行榜。

## 功能

- 每日/每周/每月 Star 增长 TOP 20
- GitHub Trending 热门推荐
- 项目详情和 README 摘要
- 自动部署到 GitHub Pages

## 数据来源

- GitHub REST API (仓库详情、README)
- GitHub Trending 页面爬取 (今日 Star 增量)

## 本地运行

```bash
# 安装依赖
pip install -r requirements.txt

# 设置 GitHub Token (可选，提高 API 限额)
export GITHUB_TOKEN=your_token_here

# 运行
python main.py
```

## GitHub Actions

项目配置了自动化工作流：

- **定时运行**: 每天 UTC 01:00 (北京时间 09:00)
- **手动触发**: 支持 workflow_dispatch
- **自动部署**: 生成的报告自动发布到 GitHub Pages

## 目录结构

```
├── src/                    # 源代码
│   ├── config.py          # 配置管理
│   ├── github_api.py      # GitHub API 封装
│   ├── trending_scraper.py # Trending 爬取
│   └── generator.py       # Markdown 生成
├── archives/              # 历史数据存档 (JSON)
├── docs/                  # GitHub Pages 静态页面
│   ├── daily/            # 每日报告
│   ├── weekly/           # 每周报告
│   ├── monthly/          # 每月报告
│   └── trending/         # Trending 推荐
├── main.py               # 主入口
└── requirements.txt      # Python 依赖
```

## License

MIT
