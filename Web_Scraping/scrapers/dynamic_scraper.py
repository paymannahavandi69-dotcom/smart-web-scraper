from playwright.sync_api import sync_playwright


def scrape_dynamic_titles(url: str, selector: str = "h3 a", timeout: int = 30000) -> list[str]:
    """
    Scrape titles from a dynamic website using Playwright.
    Waits for the network to be idle before extracting content.
    """
    titles = []

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        try:
            page.goto(url, wait_until="networkidle", timeout=timeout)
            elements = page.locator(selector)
            titles = elements.all_text_contents()
        except Exception as e:
            print(f"Scraping error: {e}")
        finally:
            browser.close()

    return titles