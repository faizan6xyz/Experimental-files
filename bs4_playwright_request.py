"""
================================================================================
  BS4 vs REQUESTS vs PLAYWRIGHT — Full Comparison
================================================================================

COMPARISON TABLE
----------------
Feature                  | requests          | BeautifulSoup4       | Playwright
-------------------------|-------------------|----------------------|-------------------
What it is               | HTTP client       | HTML parser          | Browser automator
Purpose                  | Send HTTP req     | Parse/extract HTML   | Control real browser
Renders JavaScript       | No                | No                   | Yes
Needs a browser          | No                | No                   | Yes
Speed                    | Fastest           | Fast                 | Slowest
Resource usage           | Minimal           | Minimal              | Heavy
Login / sessions         | Manual            | No (just parsing)    | Yes, natural
Click buttons            | No                | No                   | Yes
Fill forms               | No                | No                   | Yes
Take screenshots         | No                | No                   | Yes
Anti-bot bypass          | No                | No                   | Yes (stealth mode)
API calls                | Yes (best)        | No                   | Yes (overkill)
Parse HTML               | No                | Yes (best)           | Yes (overkill)

================================================================================
HOW THEY RELATE
================================================================================

They are NOT competitors — they do different jobs and are used TOGETHER:

    requests   →  gets the raw HTML / calls APIs
    BS4        →  parses that HTML and extracts data
    Playwright →  does what the above two can't (JS, clicks, auth, screenshots)

================================================================================
WHEN TO USE WHAT
================================================================================

USE requests WHEN:
    - Calling REST APIs
    - Downloading files
    - The page is static (no JS rendering needed)
    - You need speed and low resource usage

USE BeautifulSoup4 WHEN:
    - You already have HTML (from requests or a file)
    - You need to navigate/extract from HTML structure
    - Scraping static sites with no JavaScript

USE Playwright WHEN:
    - Site loads content via JavaScript (React, Vue, Angular)
    - You need to click, scroll, type, hover
    - Login with real sessions and cookies
    - Bot detection needs to be bypassed
    - You are building a browser automation agent

================================================================================
COMMON COMBOS IN REAL PROJECTS
================================================================================

    requests + BS4           →  fast static scraping pipeline
    Playwright + BS4         →  scrape JS sites (Playwright gets HTML, BS4 parses it)
    requests + Playwright    →  API calls + browser automation together
    All three                →  full scraping + automation pipeline

================================================================================
ONE LINE SUMMARY
================================================================================

    requests   →  talk to servers
    BS4        →  read HTML
    Playwright →  be a human using a browser

================================================================================
CODE EXAMPLES
================================================================================
"""

# ── 1. requests — call an API ────────────────────────────────────────────────
import requests

def requests_example():
    print("\n--- requests ---")

    # simple GET
    res = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print("Status :", res.status_code)
    print("JSON   :", res.json())

    # GET with params
    res = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params={"userId": 1}
    )
    print("Posts  :", len(res.json()))

    # POST
    res = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json={"title": "test", "body": "hello", "userId": 1}
    )
    print("Created:", res.status_code, res.json())

    # session — reuse cookies/headers across requests
    session = requests.Session()
    session.headers.update({"User-Agent": "MyBot/1.0"})
    res = session.get("https://jsonplaceholder.typicode.com/todos/1")
    print("Session:", res.json())


# ── 2. BeautifulSoup4 — parse HTML ──────────────────────────────────────────
from bs4 import BeautifulSoup

def bs4_example():
    print("\n--- BeautifulSoup4 ---")

    # get HTML with requests, parse with BS4
    res = requests.get("https://quotes.toscrape.com")
    soup = BeautifulSoup(res.text, "html.parser")

    # find single element
    title = soup.find("h1").text
    print("Title:", title)

    # find all elements
    quotes = soup.find_all("div", class_="quote")
    for q in quotes[:3]:
        text   = q.find("span", class_="text").text
        author = q.find("small", class_="author").text
        print(f"{text} — {author}")

    # CSS selector style
    all_authors = soup.select(".author")
    print("Authors:", [a.text for a in all_authors[:3]])

    # get attribute
    links = soup.find_all("a")
    for link in links[:5]:
        print("href:", link.get("href"))

    # navigate tree
    body    = soup.body
    first_h1 = body.find("h1")
    parent  = first_h1.parent
    sibling = first_h1.next_sibling
    print("Parent tag:", parent.name)


# ── 3. Playwright — browser automation ──────────────────────────────────────
from playwright.sync_api import sync_playwright

def playwright_example():
    print("\n--- Playwright ---")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # open a JS-rendered page
        page.goto("https://quotes.toscrape.com/js")
        page.wait_for_load_state("networkidle")

        # extract after JS renders
        quotes = page.locator(".quote").all()
        for q in quotes[:3]:
            text   = q.locator(".text").inner_text()
            author = q.locator(".author").inner_text()
            print(f"{text} — {author}")

        browser.close()


# ── 4. Combo — Playwright gets HTML, BS4 parses it ──────────────────────────
def playwright_plus_bs4():
    print("\n--- Playwright + BS4 combo ---")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com/js")
        page.wait_for_load_state("networkidle")

        html = page.content()          # get full rendered HTML
        browser.close()

    soup   = BeautifulSoup(html, "html.parser")   # parse with BS4
    quotes = soup.select(".quote")
    for q in quotes[:3]:
        print(q.select_one(".text").text, "—", q.select_one(".author").text)


# ── 5. Combo — requests for API, Playwright for browser ─────────────────────
def requests_plus_playwright():
    print("\n--- requests + Playwright combo ---")

    # step 1: call API to get list of URLs to visit
    res  = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1")
    ids  = [post["id"] for post in res.json()[:2]]
    print("Post IDs from API:", ids)

    # step 2: use Playwright to visit pages that need JS
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page    = browser.new_page()
        page.goto("https://quotes.toscrape.com")
        print("Browser title:", page.title())
        browser.close()


# ── MAIN ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    requests_example()
    bs4_example()
    playwright_example()
    playwright_plus_bs4()
    requests_plus_playwright()