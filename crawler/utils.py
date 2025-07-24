import urllib.robotparser
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

_robot_parsers = {}

def is_allowed_by_robots(url, user_agent="*"):
    domain = urlparse(url).netloc
    scheme = urlparse(url).scheme
    robots_url = f"{scheme}://{domain}/robots.txt"

    if domain not in _robot_parsers:
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(robots_url)
        try:
            rp.read()
        except Exception:
            return True  # Fail open if robots.txt cannot be reached
        _robot_parsers[domain] = rp
    else:
        rp = _robot_parsers[domain]

    return rp.can_fetch(user_agent, url)

def extract_links(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    links = set()
    for tag in soup.find_all("a", href=True):
        href = tag.get("href")
        if href.startswith("#") or href.lower().startswith("javascript:"):
            continue
        absolute_url = urljoin(base_url, href)
        links.add(absolute_url)
    return links

def is_internal_link(base_url, target_url):
    return urlparse(base_url).netloc == urlparse(target_url).netloc

