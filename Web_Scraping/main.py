from scrapers.static_scraper import scrape_quotes
from scrapers.dynamic_scraper import scrape_dynamic_titles
from scrapers.storage import save_to_json, save_to_csv


def main():
    print("Scraping quotes (static)...")
    quotes = scrape_quotes("https://quotes.toscrape.com")
    save_to_json(quotes, "data/quotes.json")
    save_to_csv(quotes, "data/quotes.csv", fieldnames=["text", "author"])

    print("Scraping book titles (dynamic)...")
    titles = scrape_dynamic_titles("https://books.toscrape.com", selector="h3 a")
    save_to_json(titles, "data/book_titles.json")

    print("Done.")

if __name__ == "__main__":
    main()