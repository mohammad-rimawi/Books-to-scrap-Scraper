# Books to Scrape Scraper

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Playwright](https://img.shields.io/badge/Playwright-Installed-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**Books to Scrape Scraper** is a Python tool that uses [Playwright](https://playwright.dev/python/docs/intro) to scrape book data from [Books to Scrape](https://books.toscrape.com/).

---

## Features

- Scrape book information including:
  - Title
  - Price
  - Rating
- Save scraped data into a CSV file (`data/books.csv`).
- Specify the number of books to scrape.
- Supports pagination to scrape multiple pages.
- Works on Windows, Linux, and MacOS.

---

## Requirements

- Python 3.9 or higher
- Required Python packages:
```bash
pip install playwright pandas
playwright install
