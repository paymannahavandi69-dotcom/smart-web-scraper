import requests
from bs4 import BeautifulSoup


def scrape_quotes(url: str, timeout: int = 10) -> list[dict]:
    """
    Scrape quotes from a static website.
    Returns a list of dicts with 'text' and 'author'.
    """
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print(f"Timeout while requesting {url}")
        return []
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []

    for quote in soup.find_all("div", class_="quote"):
        text_tag = quote.find("span", class_="text")
        author_tag = quote.find("small", class_="author")

        if text_tag and author_tag:
            quotes.append({
                "text": text_tag.text.strip(),
                "author": author_tag.text.strip()
            })

    return quotes


def scrape_titles(url: str, tag: str = "h2", timeout: int = 10) -> list[str]:
    """
    Scrape all text content of a given tag from a static website.
    """
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    return [element.text.strip() for element in soup.find_all(tag)]