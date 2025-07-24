from urllib.parse import urlparse

def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.scheme) and bool(parsed.netloc)

def is_internal(base_url, target_url):
    return urlparse(base_url).netloc == urlparse(target_url).netloc
