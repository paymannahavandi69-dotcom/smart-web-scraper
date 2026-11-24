# 🕷️ Smart Web Scraper

A robust, Python-based web scraping toolkit designed to collect data from both static and dynamic websites. It extracts data and stores it in structured formats (JSON and CSV), making it perfectly ready to be fed into AI, Data Analysis, or RAG (Retrieval-Augmented Generation) pipelines.

## 🚀 Features

- **Static Scraping:** Efficiently scrape static websites using `requests` and `BeautifulSoup`.
- **Dynamic Scraping:** Scrape JavaScript-rendered websites using `Playwright`.
- **Data Storage:** Automatically save extracted data as JSON or CSV files.
- **Robust Error Handling:** Built-in timeout handling and error management for reliable scraping.
- **RAG-Ready:** Output files are formatted cleanly, ready for vectorization and AI model ingestion.

## 📁 Project Structure

```text
web-scraping-project/
│
├── README.md                  # Project documentation
├── requirements.txt           # Dependencies
├── .gitignore                 # Ignored files (env, venv, data outputs)
├── main.py                    # Entry point of the application
│
├── scrapers/                  # Core scraping modules
│   ├── __init__.py            # Package initializer
│   ├── static_scraper.py      # Logic for static sites
│   ├── dynamic_scraper.py     # Logic for dynamic sites (Playwright)
│   └── storage.py             # JSON/CSV save helpers
│
└── data/                      # Output directory for scraped data
    └── .gitkeep               # Keeps folder in Git
```

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/paymannahavandi69-dotcom/smart-web-scraper.git
cd smart-web-scraper
```

2. Create a virtual environment (Optional but recommended):
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Install the Playwright browser binaries:
```bash
playwright install chromium
```

## 💻 Usage

Run the main script:
```bash
python main.py
```

## 📊 Output

After a successful run, the scraped data will be saved in the `data/` directory:
- `data/quotes.json` & `data/quotes.csv` (Static Scraping Output)
- `data/book_titles.json` (Dynamic Scraping Output)

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **HTTP Requests:** `requests`
- **HTML Parsing:** `BeautifulSoup4`
- **Dynamic Rendering:** `Playwright`
- **Data Formatting:** `json`, `csv`

## 📄 License

This project is licensed under the MIT License.
