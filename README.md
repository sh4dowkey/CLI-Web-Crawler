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


### Crawl only external links:
```bash
python cli.py https://example.com --external-only
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

## 📖 Usage

For detailed usage instructions and examples, see the [Usage Guide](usage.md).

---


## 📜 License

MIT License © 2025  
Crafted with ❤️ by sh4dowkey


