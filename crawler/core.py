from .fetcher import fetch
from .utils import extract_links, is_internal_link, is_allowed_by_robots
from urllib.parse import urlparse
from tqdm import tqdm
import sys

visited = set()
def start_crawl(args):
    queue = [(args.url, 0)]
    results = []
    user_agent = args.user_agent or "*"

    print(f"Crawling {args.url} with max depth={args.depth} and max pages={args.max_pages}")
    pbar = tqdm(total=args.max_pages)
    
    while queue and len(visited) < args.max_pages:
        url, depth = queue.pop(0)
        if url in visited or depth > args.depth:
            continue

        if not is_allowed_by_robots(url, user_agent=user_agent):
            if args.verbose:
                print(f"[robots.txt] Disallowed: {url}")
            continue

        visited.add(url)

        content, title = fetch(url, user_agent=user_agent)
        if content is None:
            continue

        keyword_found = False
        if args.search:
            keyword_found = args.search.lower() in content.lower()

        results.append((url, title, keyword_found))

        if args.verbose:
            print(f"Visited: {url} | Title: {title} | Keyword: {'✔️' if keyword_found else '❌'}")

        links = extract_links(content, base_url=url)
        for link in links:
            if args.internal_only and not is_internal_link(args.url, link):
                continue
            if args.external_only and is_internal_link(args.url, link):
                continue
            if link not in visited:
                queue.append((link, depth + 1))

        pbar.update(1)

    pbar.close()

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            for url, title, keyword_found in results:
                f.write(f"{url}\nTitle: {title}\nKeyword found: {'✔️' if keyword_found else '❌'}\n\n")
    else:
        print("\n--- Crawl Summary ---")
        for url, title, keyword_found in results:
            print(f"{url}\nTitle: {title}\nKeyword found: {'✔️' if keyword_found else '❌'}\n")

