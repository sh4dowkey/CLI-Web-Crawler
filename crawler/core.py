import httpx
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from crawler.utils import is_valid_url, is_internal
from tqdm import tqdm
import json
import csv

visited = set()
results = []
errors = []

def fetch(url, headers):
    try:
        return httpx.get(url, headers=headers, timeout=10)
    except Exception as e:
        errors.append((url, str(e)))
        return None

def crawl(url, base_url, depth, max_depth, keyword, internal_only, external_only, max_pages, headers, bar):
    if len(visited) >= max_pages or url in visited or depth > max_depth:
        return

    visited.add(url)
    response = fetch(url, headers)
    if not response or not response.text:
        return

    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string.strip() if soup.title else ""
    contains_keyword = keyword.lower() in response.text.lower() if keyword else False

    results.append({"url": url, "title": title, "keyword_found": contains_keyword})
    bar.update(1)

    for tag in soup.find_all("a", href=True):
        href = urljoin(url, tag["href"])
        if not is_valid_url(href):
            continue
        if internal_only and not is_internal(base_url, href):
            continue
        if external_only and is_internal(base_url, href):
            continue
        crawl(href, base_url, depth + 1, max_depth, keyword, internal_only, external_only, max_pages, headers, bar)

def save_results(output, fmt):
    if not output:
        return
    if fmt == "txt":
        with open(output, "w") as f:
            for item in results:
                f.write(item["url"] + "\n")
    elif fmt == "json":
        with open(output, "w") as f:
            json.dump(results, f, indent=2)
    elif fmt == "csv":
        with open(output, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["url", "title", "keyword_found"])
            writer.writeheader()
            writer.writerows(results)

def save_sitemap(output):
    if not output:
        return
    with open("sitemap.xml", "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for item in results:
            f.write(f"  <url><loc>{item['url']}</loc></url>\n")
        f.write('</urlset>')

def start_crawl(args):
    headers = {"User-Agent": args.user_agent}
    print(f"Crawling {args.url} with max depth={args.depth} and max pages={args.max_pages}")
    with tqdm(total=args.max_pages) as bar:
        crawl(args.url, args.url, 0, args.depth, args.search, args.internal_only, args.external_only, args.max_pages, headers, bar)

    print(f"\nCrawled {len(results)} pages. {len(errors)} errors.")
    if args.output:
        save_results(args.output, args.format)
        print(f"Results saved to {args.output}")
    if args.sitemap:
        save_sitemap("sitemap.xml")
        print("Sitemap saved as sitemap.xml")
