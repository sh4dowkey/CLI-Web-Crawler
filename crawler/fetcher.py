import requests
from bs4 import BeautifulSoup

def fetch(url, user_agent="MyCrawler"):
    try:
        headers = {"User-Agent": user_agent}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        title_tag = soup.find("title")
        title = title_tag.text.strip() if title_tag else "No title"

        return response.text, title

    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch {url}: {e}")
        return None, None

