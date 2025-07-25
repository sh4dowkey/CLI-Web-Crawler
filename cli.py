from crawler.core import start_crawl
import argparse

parser = argparse.ArgumentParser(description="Simple CLI Web Crawler")
parser.add_argument("url", help="Starting URL")
parser.add_argument("--depth", type=int, default=2, help="Maximum depth to crawl")
parser.add_argument("--max-pages", type=int, default=100, help="Maximum number of pages to crawl")
parser.add_argument("--search", help="Keyword to search in page content")
parser.add_argument("--internal-only", action="store_true", help="Crawl only internal links")
parser.add_argument("--external-only", action="store_true", help="Crawl only external links")
parser.add_argument("--user-agent", help="Custom User-Agent header")
parser.add_argument("--verbose", action="store_true", help="Print verbose output for each page")
parser.add_argument("--output", help="Save results to a file")

args = parser.parse_args()
start_crawl(args)

