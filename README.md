# CLI Web Crawler 🕷️

## 🕹 Usage

```bash
python cli.py <url> [OPTIONS]
```

### ⚙️ Options

| Option               | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `<url>`              | Starting URL to crawl (required)                                            |
| `--depth`            | Maximum depth to crawl (default: 2)                                         |
| `--max-pages`        | Maximum number of pages to crawl (default: 100)                             |
| `--search`           | Keyword to search for in page content                                       |
| `--internal-only`    | Crawl only internal links                                                    |
| `--external-only`    | Crawl only external links                                                    |
| `--user-agent`       | Custom User-Agent string                                                     |
| `--verbose`          | Enable verbose output (shows each visited page in terminal)                |
| `--output`           | Save results to specified file                                               |

---

## 📄 Output

- The CLI prints results to the terminal.
- If `--output` is specified, results are saved to the file (in plain text format).
- Each result includes:
  - ✅ URL crawled
  - 📝 Page title
  - 🔍 Keyword match (✔️ Yes / ❌ No)

---

## 📜 Robots.txt Support ✅

- Crawler checks and respects `robots.txt` for each domain.
- Only URLs **allowed** for `User-agent: *` are crawled.

---

## 💡 Example Commands

### Basic crawl:
```bash
python cli.py https://example.com
```

### Search for a keyword:
```bash
python cli.py https://example.com --search login
```

### Save output to a file:
```bash
python cli.py https://example.com --output result.txt
```

### Crawl only internal links:
```bash
python cli.py https://example.com --internal-only
```

### Verbose mode:
```bash
python cli.py https://example.com --verbose
```

---

## 📁 Where are results saved?
If you provide `--output filename.txt`, results are saved in that file.
Otherwise, you’ll only see the results in your terminal.

---

## 🌐 Advanced Features

- ✅ `robots.txt` parsing
- 🔍 Keyword detection
- 🌐 Internal/external link filtering
- 💾 Save to file
- 🎨 GUI support (coming soon)

---

## 👨‍💻 Developer Notes

- Written in Python 3
- Uses `requests`, `beautifulsoup4`, and `tqdm`
- Project structure:
  ```
  ├── cli.py
  ├── crawler/
  │   ├── __init__.py
  │   ├── core.py
  │   ├── fetcher.py
  │   └── utils.py
  ├── README.md
  └── DOCUMENTATION.md
  ```
  
  📘 Full Documentation: [View Usage Guide](./usage.md)


