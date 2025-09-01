from playwright.sync_api import sync_playwright
from dataclasses import dataclass, asdict
import pandas as pd
import os

@dataclass
class Book:
    title: str = None
    price: str = None
    rating: str = None

def main():
    nom = int(input("Enter the number of books you want to scrape: "))
    all_books = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) 
        page = browser.new_page()
        page.goto("https://books.toscrape.com/", timeout=60000)

        while len(all_books) < nom:
            page.wait_for_timeout(2000)

            book_blocks = page.locator('//article[@class="product_pod"]')
            count = book_blocks.count()

            for i in range(count):
                if len(all_books) >= nom:
                    break

                book_element = book_blocks.nth(i)
                title = book_element.locator('xpath=.//h3/a').get_attribute('title')
                price = book_element.locator('xpath=.//p[@class="price_color"]').inner_text()
                rating_class = book_element.locator('xpath=.//p[contains(@class, "star-rating")]').get_attribute('class')
                rating = rating_class.split()[-1] if rating_class else "Unknown"

                book = Book(title=title, price=price, rating=rating)
                all_books.append(book)

            next_button = page.locator('//li[@class="next"]/a')
            if len(all_books) < nom and next_button.count() > 0:
                next_button.click()
                page.wait_for_load_state("networkidle")
            else:
                break

        browser.close()

    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame([asdict(book) for book in all_books])
    df.to_csv("data/books.csv", index=False, encoding="utf-8-sig")
    print(f" {len(all_books)} books saved to data/books.csv")

if __name__ == "__main__":
    main()
