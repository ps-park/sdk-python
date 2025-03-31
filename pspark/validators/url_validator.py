from urllib.parse import urlparse


def validate_url(url):
    parsed_url = urlparse(url)
    if not all([parsed_url.scheme, parsed_url.netloc]):
        raise ValueError(f"Invalid URL: {url}")
