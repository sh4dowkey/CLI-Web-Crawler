# 📘 Usage Guide – CLI Web Crawler

A Python-based command-line web crawler that supports keyword search, internal/external link control, `robots.txt` handling, and output saving — all with a simple interface.

---

## 🚀 Quick Start

### 🔧 Installation

```bash
git clone https://github.com/your-username/cli-web-crawler.git
cd cli-web-crawler
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🕹️ Basic Usage

```bash
python cli.py <url> [options]
```

- `<url>`: The starting URL to crawl (required)

---

## ⚙️ Available Options

| Option | Description |
|--------|-------------|
| `--depth <int>`         | Max crawl depth (default: 2) |
| `--max-pages <int>`     | Max number of pages to crawl (default: 100) |
| `--output <filename>`   | Save results to a text file |
| `--search <keyword>`    | Search for a keyword in page content |
| `--user-agent <string>` | Use a custom `User-Agent` string |
| `--internal-only`       | Only crawl links from the same domain |
| `--external-only`       | Only crawl external links |
| `--verbose`             | Enable detailed logs while crawling |
| `--color`               | Use colorized terminal output |

---

## 🧪 Example Commands

### 🔍 Crawl a Site Verbosely

```bash
python cli.py https://example.com --verbose
```

### 📁 Save Crawl Output to File

```bash
python cli.py https://example.com --output results.txt
```

### 🔎 Search for a Keyword

```bash
python cli.py https://example.com --search login
```

### 🔐 Use a Custom User-Agent

```bash
python cli.py https://example.com --user-agent "MyCrawlerBot/1.0"
```

### 🕸️ Crawl Internal Pages Only (Single Depth)

```bash
python cli.py https://example.com --internal-only --depth 1
```

---

## 🤖 Robots.txt Behavior

- This crawler fully respects each site's `robots.txt`.
- If a page is **disallowed**, it will be skipped with a log:

```
[robots.txt] Disallowed: https://example.com/secret
```

- If no `robots.txt` is found or unreachable, the crawler **defaults to allow** (fail-open policy).
- Caching is used per-domain for performance.

---

## 🖨️ Output Format

Terminal or saved file output includes:

```text
https://example.com/page1
Title: Welcome to Page 1
Keyword found: ✔️

https://example.com/page2
Title: Contact
Keyword found: ❌
```

---

## 📁 Project Layout

```
cli-web-crawler/
├── cli.py              # Main CLI entry
├── crawler/
│   ├── core.py         # Crawl loop, argument handling
│   ├── fetcher.py      # HTTP requests, response handling
│   ├── utils.py        # Link extraction, robots.txt check, helpers
├── requirements.txt
├── USAGE.md            # ← You're reading this
```

---

## 🧠 Notes

- Works on Python 3.7+
- Lightweight and dependency-minimal
- Designed for learning, testing, or integrating into automation workflows

---

## 📜 License

MIT License © 2025  
Crafted with ❤️ by sh4dowkey

---
