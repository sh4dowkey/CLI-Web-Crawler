import argparse
from crawler.core import start_crawl

def main():
    parser = argparse.ArgumentParser(description="Advanced CLI Web Crawler")

    parser.add_argument("url", help="Starting URL")
    parser.add_argument("-d", "--depth", type=int, default=2, help="Crawl depth")
    parser.add_argument("-o", "--output", help="Output file name")
    parser.add_argument("-f", "--format", choices=["txt", "json", "csv"], default="txt", help="Output format")
    parser.add_argument("--search", help="Keyword to search in page content")
    parser.add_argument("--internal-only", action="store_true", help="Crawl only internal links")
    parser.add_argument("--external-only", action="store_true", help="Crawl only external links")
    parser.add_argument("--max-pages", type=int, default=100, help="Maximum pages to crawl")
    parser.add_argument("--sitemap", action="store_true", help="Export results as sitemap.xml")
    parser.add_argument("--user-agent", default="CLIWebCrawler/1.0", help="Custom User-Agent")
    parser.add_argument("--verbose", action="store_true", help="Show detailed logs")

    args = parser.parse_args()

    start_crawl(args)

if __name__ == "__main__":
    main()
