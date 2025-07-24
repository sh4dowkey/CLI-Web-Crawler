# CLI Web Crawler

A powerful, feature-rich command-line web crawler written in Python.

## Features

- Recursive internal link crawling
- Multi-threaded crawling
- Keyword content search
- Export to TXT, JSON, or CSV
- Sitemap generation
- Progress bar
- Robots.txt respect
- Max pages limit
- Internal/external filtering
- Custom User-Agent support
- Logs errors and status

## Usage

```bash
pip install -r requirements.txt
python cli.py https://example.com --depth 2 --output result.json --format json --search login --max-pages 50 --internal-only
```
