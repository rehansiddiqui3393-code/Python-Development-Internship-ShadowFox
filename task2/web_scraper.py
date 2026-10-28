# Task 2 (Intermediate) - Q1: Web Scraper using Requests + Beautiful Soup
# Target: https://quotes.toscrape.com (a website made for scraping practice)
# Extracts: quote text, author, tags  -> saves to quotes.csv

import csv
import time
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com"
HEADERS = {"User-Agent": "Mozilla/5.0 (Python scraper for internship task)"}


def parse_quotes(html):
    """Parse one page of HTML and return (list_of_quotes, next_page_link)."""
    soup = BeautifulSoup(html, "html.parser")
    quotes = []
    for block in soup.find_all("div", class_="quote"):
        text = block.find("span", class_="text").get_text(strip=True)
        author = block.find("small", class_="author").get_text(strip=True)
        tags = [t.get_text(strip=True) for t in block.find_all("a", class_="tag")]
        quotes.append({"quote": text, "author": author, "tags": ", ".join(tags)})

    next_btn = soup.find("li", class_="next")
    next_link = next_btn.find("a")["href"] if next_btn else None
    return quotes, next_link


def scrape_all(max_pages=5):
    all_quotes = []
    url = BASE_URL + "/"
    page = 1
    while url and page <= max_pages:
        print(f"Scraping page {page}: {url}")
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        quotes, next_link = parse_quotes(response.text)
        all_quotes.extend(quotes)
        url = BASE_URL + next_link if next_link else None
        page += 1
        time.sleep(1)  # be polite to the server
    return all_quotes


def save_to_csv(quotes, filename="quotes.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["quote", "author", "tags"])
        writer.writeheader()
        writer.writerows(quotes)
    print(f"Saved {len(quotes)} quotes to {filename}")


if __name__ == "__main__":
    try:
        data = scrape_all(max_pages=5)
        save_to_csv(data)

        # Small summary
        authors = {}
        for q in data:
            authors[q["author"]] = authors.get(q["author"], 0) + 1
        top = max(authors, key=authors.get)
        print("Total quotes:", len(data))
        print("Unique authors:", len(authors))
        print("Most quoted author:", top, f"({authors[top]} quotes)")
    except requests.exceptions.RequestException as e:
        print("Network error:", e)
