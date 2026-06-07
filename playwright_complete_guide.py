"""
╔══════════════════════════════════════════════════════════════════════════════╗
║          PLAYWRIGHT — COMPLETE AUTOMATION & WEB SCRAPING GUIDE              ║
║                  Python · Sync + Async · All Features                       ║
╚══════════════════════════════════════════════════════════════════════════════╝

Install:
    pip install playwright
    playwright install          # downloads Chromium, Firefox, WebKit binaries
    playwright install-deps    # system dependencies (Linux only)

Run this file:
    python playwright_complete_guide.py

Sections
────────
 1.  Browser Launch Options       (Chromium / Firefox / WebKit, headless, proxy)
 2.  Page Navigation              (goto, back, forward, reload, wait strategies)
 3.  Locators & Selectors         (CSS, XPath, text, role, label, test-id)
 4.  Interactions                 (click, type, fill, hover, drag-drop, upload)
 5.  Keyboard & Mouse             (key combos, mouse move, wheel)
 6.  Web Scraping                 (text, attributes, tables, pagination, infinite scroll)
 7.  Frames & iFrames             (nested frames, shadow DOM)
 8.  Dialogs                      (alert, confirm, prompt, file chooser)
 9.  Network Interception         (route, mock, abort, HAR recording)
10.  Authentication               (cookies, storage, HTTP auth, session reuse)
11.  Screenshots & Videos         (full-page, element, clip, PDF)
12.  Multiple Pages & Contexts    (tabs, incognito, multi-user)
13.  Waiting Strategies           (network idle, selectors, custom conditions)
14.  JavaScript Execution         (evaluate, expose function, add script tag)
15.  Downloads & Uploads          (file handling)
16.  Geolocation & Permissions    (GPS, camera, notifications)
17.  Async Playwright             (asyncio-based usage)
18.  Browser Contexts             (cookies isolation, storage state)
19.  Device Emulation             (mobile, tablet, viewport)
20.  Error Handling & Retries     (try/except, expect assertions)
"""

# ─────────────────────────────────────────────────────────────────────────────
# IMPORTS
# ─────────────────────────────────────────────────────────────────────────────
import asyncio
import json
import os
import re
import time
from pathlib import Path
from typing import Any

from playwright.sync_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
    Response,
    Route,
    sync_playwright,
    expect,
)
from playwright.async_api import async_playwright


# ═════════════════════════════════════════════════════════════════════════════
# 1. BROWSER LAUNCH OPTIONS
# ═════════════════════════════════════════════════════════════════════════════
def section_01_browser_launch():
    """
    Launch Chromium, Firefox, or WebKit with various options.
    Demonstrates: headless, slow_mo, proxy, args, downloads path.
    """
    print("\n── 1. BROWSER LAUNCH OPTIONS ──────────────────────────────────")

    with sync_playwright() as p:

        # ── Chromium (default) ─────────────────────────
        browser = p.chromium.launch(
            headless=True,           # False → opens visible browser window
            slow_mo=50,              # milliseconds between actions (good for debugging)
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-blink-features=AutomationControlled",  # hide automation flag
            ],
            downloads_path="./downloads",
        )
        page = browser.new_page()
        page.goto("https://example.com")
        print("Chromium title:", page.title())
        browser.close()

        # ── Firefox ────────────────────────────────────
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")
        print("Firefox title:", page.title())
        browser.close()

        # ── WebKit (Safari engine) ─────────────────────
        browser = p.webkit.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")
        print("WebKit title:", page.title())
        browser.close()

        # ── With Proxy ────────────────────────────────
        # browser = p.chromium.launch(
        #     proxy={"server": "http://myproxy:8080",
        #            "username": "user", "password": "pass"}
        # )

        # ── Connect to existing browser via CDP ───────
        # browser = p.chromium.connect_over_cdp("http://localhost:9222")


# ═════════════════════════════════════════════════════════════════════════════
# 2. PAGE NAVIGATION
# ═════════════════════════════════════════════════════════════════════════════
def section_02_navigation(page: Page):
    print("\n── 2. PAGE NAVIGATION ─────────────────────────────────────────")

    # Basic navigation
    page.goto("https://example.com")
    page.goto("https://example.com", wait_until="domcontentloaded")
    # wait_until options: "load" | "domcontentloaded" | "networkidle" | "commit"

    page.goto("https://example.com", timeout=30_000)  # 30 s timeout

    # History
    page.go_back()
    page.go_forward()
    page.reload()

    # Current URL & title
    print("URL:  ", page.url)
    print("Title:", page.title())

    # Wait for URL change (e.g. after form submit redirect)
    # page.wait_for_url("**/dashboard")
    # page.wait_for_url(re.compile(r".*dashboard.*"))


# ═════════════════════════════════════════════════════════════════════════════
# 3. LOCATORS & SELECTORS
# ═════════════════════════════════════════════════════════════════════════════
def section_03_locators(page: Page):
    print("\n── 3. LOCATORS & SELECTORS ────────────────────────────────────")
    page.goto("https://playwright.dev/")

    # ── CSS selector ──────────────────────────────
    heading = page.locator("h1")
    print("H1 text:", heading.text_content())

    # ── XPath ─────────────────────────────────────
    link = page.locator("xpath=//a[@href='/docs/intro']")

    # ── Text content ──────────────────────────────
    page.locator("text=Get started")
    page.get_by_text("Get started", exact=True)

    # ── ARIA role ─────────────────────────────────
    page.get_by_role("button", name="Search")
    page.get_by_role("link", name="Docs")
    page.get_by_role("heading", level=1)

    # ── Label (for form fields) ───────────────────
    page.get_by_label("Email address")

    # ── Placeholder ───────────────────────────────
    page.get_by_placeholder("Search docs")

    # ── Alt text (images) ─────────────────────────
    page.get_by_alt_text("Playwright logo")

    # ── Title attribute ───────────────────────────
    page.get_by_title("Toggle dark mode")

    # ── data-testid ───────────────────────────────
    page.get_by_test_id("submit-btn")

    # ── Chaining / filtering ──────────────────────
    nav = page.locator("nav")
    nav.get_by_role("link")                       # links inside nav
    page.locator("ul > li").filter(has_text="API")  # filter list items
    page.locator("li").nth(2)                     # 3rd item (0-indexed)
    page.locator("li").first
    page.locator("li").last

    # ── Count ─────────────────────────────────────
    count = page.locator("a").count()
    print("Total links on page:", count)

    # ── All matching elements ─────────────────────
    items = page.locator("nav a").all()
    for item in items[:3]:
        print("Nav link:", item.text_content())


# ═════════════════════════════════════════════════════════════════════════════
# 4. INTERACTIONS
# ═════════════════════════════════════════════════════════════════════════════
def section_04_interactions(page: Page):
    print("\n── 4. INTERACTIONS ────────────────────────────────────────────")
    page.goto("https://playwright.dev/")

    # Click
    page.locator("a[href='/docs/intro']").click()
    page.locator("button").click(button="right")       # right-click
    page.locator("button").dblclick()                  # double-click
    page.locator("button").click(modifiers=["Shift"])  # shift+click

    # Typing
    page.goto("https://playwright.dev/")
    search = page.get_by_placeholder("Search")
    if search.count():
        search.click()
        search.fill("locators")         # clears and fills
        search.type("locators", delay=50)   # types character-by-character
        search.clear()

    # Select dropdown
    # page.get_by_label("Country").select_option("US")
    # page.get_by_label("Country").select_option(label="United States")
    # page.get_by_label("Color").select_option(["red", "blue"])  # multi-select

    # Checkbox & radio
    # page.get_by_label("Accept terms").check()
    # page.get_by_label("Accept terms").uncheck()
    # print(page.get_by_label("Accept terms").is_checked())

    # Hover
    page.locator("nav").hover()

    # Focus / blur
    # page.get_by_label("Email").focus()
    # page.get_by_label("Email").blur()

    # Tap (touch devices)
    # page.locator("button").tap()

    # Drag and drop
    # page.locator("#source").drag_to(page.locator("#target"))
    # page.drag_and_drop("#source", "#target")

    # Scroll element into view
    page.locator("footer").scroll_into_view_if_needed()


# ═════════════════════════════════════════════════════════════════════════════
# 5. KEYBOARD & MOUSE
# ═════════════════════════════════════════════════════════════════════════════
def section_05_keyboard_mouse(page: Page):
    print("\n── 5. KEYBOARD & MOUSE ────────────────────────────────────────")
    page.goto("https://example.com")

    # ── Keyboard ──────────────────────────────────
    page.keyboard.press("Tab")
    page.keyboard.press("Enter")
    page.keyboard.press("Control+a")    # select all
    page.keyboard.press("Control+c")    # copy
    page.keyboard.press("Escape")
    page.keyboard.press("ArrowDown")
    page.keyboard.type("Hello, Playwright!", delay=30)

    # Key down / up (for held keys)
    page.keyboard.down("Shift")
    page.keyboard.press("ArrowRight")   # select one char
    page.keyboard.up("Shift")

    # ── Mouse ─────────────────────────────────────
    page.mouse.move(100, 200)
    page.mouse.click(100, 200)
    page.mouse.dblclick(100, 200)
    page.mouse.down()
    page.mouse.up()

    # Scroll via mouse wheel
    page.mouse.wheel(0, 500)   # scroll down 500px

    # ── Touch / stylus ────────────────────────────
    # page.touchscreen.tap(100, 150)


# ═════════════════════════════════════════════════════════════════════════════
# 6. WEB SCRAPING
# ═════════════════════════════════════════════════════════════════════════════
def section_06_web_scraping(page: Page):
    print("\n── 6. WEB SCRAPING ────────────────────────────────────────────")
    page.goto("https://books.toscrape.com/")

    # ── Text extraction ───────────────────────────
    heading = page.locator("h1").text_content()
    print("Page heading:", heading)

    # ── Attribute extraction ──────────────────────
    first_link_href = page.locator("a").first.get_attribute("href")
    print("First link:", first_link_href)

    # ── Scrape all books on the first page ────────
    books = []
    book_cards = page.locator("article.product_pod").all()
    for card in book_cards:
        title = card.locator("h3 a").get_attribute("title")
        price = card.locator(".price_color").text_content().strip()
        rating = card.locator("p.star-rating").get_attribute("class").split()[-1]
        books.append({"title": title, "price": price, "rating": rating})

    print(f"Scraped {len(books)} books from page 1")
    for book in books[:3]:
        print(f"  {book['rating']:10s} | {book['price']} | {book['title'][:40]}")

    # ── Scrape a TABLE ────────────────────────────
    def scrape_table(page: Page, selector: str) -> list[dict]:
        headers = [
            th.text_content().strip()
            for th in page.locator(f"{selector} thead th").all()
        ]
        rows = []
        for row in page.locator(f"{selector} tbody tr").all():
            cells = [td.text_content().strip() for td in row.locator("td").all()]
            rows.append(dict(zip(headers, cells)))
        return rows

    # ── Pagination scraping ───────────────────────
    def scrape_all_pages(start_url: str, max_pages: int = 3) -> list[dict]:
        all_books = []
        url = start_url
        for page_num in range(1, max_pages + 1):
            page.goto(url)
            cards = page.locator("article.product_pod").all()
            for card in cards:
                title = card.locator("h3 a").get_attribute("title")
                price = card.locator(".price_color").text_content().strip()
                all_books.append({"title": title, "price": price, "page": page_num})

            # Find next page button
            next_btn = page.locator("li.next a")
            if next_btn.count() == 0:
                break
            next_href = next_btn.get_attribute("href")
            url = f"https://books.toscrape.com/catalogue/{next_href}"
            print(f"  Scraped page {page_num}, moving to next …")

        return all_books

    all_books = scrape_all_pages("https://books.toscrape.com/catalogue/page-1.html", max_pages=2)
    print(f"Total books scraped (2 pages): {len(all_books)}")

    # ── Infinite scroll scraping ──────────────────
    def scrape_infinite_scroll(page: Page, item_selector: str, max_scrolls: int = 5):
        items = set()
        for _ in range(max_scrolls):
            current = {el.text_content() for el in page.locator(item_selector).all()}
            items.update(current)
            page.mouse.wheel(0, 3000)      # scroll down
            page.wait_for_timeout(1500)    # wait for new items to load
        return list(items)

    # ── Inner HTML / outer HTML ───────────────────
    html = page.locator("article.product_pod").first.inner_html()
    outer = page.locator("article.product_pod").first.outer_html()

    # ── Input values ──────────────────────────────
    # val = page.get_by_label("Search").input_value()

    # ── Evaluate JS for complex extraction ────────
    all_hrefs = page.evaluate("""
        () => Array.from(document.querySelectorAll('a'))
                   .map(a => a.href)
    """)
    print(f"Total hrefs on page: {len(all_hrefs)}")

    return books


# ═════════════════════════════════════════════════════════════════════════════
# 7. FRAMES & SHADOW DOM
# ═════════════════════════════════════════════════════════════════════════════
def section_07_frames(page: Page):
    print("\n── 7. FRAMES & SHADOW DOM ─────────────────────────────────────")

    # ── iFrame access ─────────────────────────────
    page.goto("https://www.w3schools.com/html/html_iframe.asp")

    # Get frame by URL
    frame = page.frame_locator("iframe[src*='default.asp']")
    if frame:
        text = frame.locator("body").text_content()

    # Get all frames
    all_frames = page.frames
    print(f"Frames on page: {len(all_frames)}")
    for f in all_frames:
        print("  Frame URL:", f.url)

    # Interact inside a frame
    # frame = page.frame(url="**/iframe-content")
    # frame.locator("button").click()

    # ── Nested frames ─────────────────────────────
    # outer = page.frame_locator("#outer-frame")
    # inner = outer.frame_locator("#inner-frame")
    # inner.locator("input").fill("nested value")

    # ── Shadow DOM ────────────────────────────────
    # Playwright pierces shadow DOM automatically with CSS selectors
    # page.locator("my-component >> css=button").click()
    # Or use >> pierce >> for explicit shadow piercing:
    # page.locator("host-element >> pierce >> .shadow-child")


# ═════════════════════════════════════════════════════════════════════════════
# 8. DIALOGS (alert, confirm, prompt, file chooser)
# ═════════════════════════════════════════════════════════════════════════════
def section_08_dialogs(page: Page):
    print("\n── 8. DIALOGS ─────────────────────────────────────────────────")

    # Handle JS dialogs before triggering them
    page.on("dialog", lambda dialog: dialog.accept())        # accept all
    # page.on("dialog", lambda dialog: dialog.dismiss())     # dismiss
    # page.on("dialog", lambda dialog: dialog.accept("my text"))  # for prompts

    # Richer handler
    def handle_dialog(dialog):
        print(f"  Dialog type: {dialog.type}  message: {dialog.message}")
        if dialog.type == "confirm":
            dialog.accept()
        elif dialog.type == "prompt":
            dialog.accept("my answer")
        else:
            dialog.accept()

    page.on("dialog", handle_dialog)

    # Trigger an alert (example)
    page.goto("https://example.com")
    # page.evaluate("alert('Hello!')")

    # ── File chooser (upload trigger) ─────────────
    # with page.expect_file_chooser() as fc_info:
    #     page.locator("input[type=file]").click()
    # file_chooser = fc_info.value
    # file_chooser.set_files("./my_document.pdf")
    # file_chooser.set_files(["file1.pdf", "file2.png"])  # multiple


# ═════════════════════════════════════════════════════════════════════════════
# 9. NETWORK INTERCEPTION
# ═════════════════════════════════════════════════════════════════════════════
def section_09_network(page: Page):
    print("\n── 9. NETWORK INTERCEPTION ────────────────────────────────────")

    # ── Capture all responses ─────────────────────
    responses = []
    page.on("response", lambda r: responses.append({
        "url": r.url, "status": r.status
    }))

    # ── Capture requests ──────────────────────────
    page.on("request", lambda req: print(f"  → {req.method} {req.url[:60]}"))

    # ── Block images & CSS (speed up scraping) ────
    def block_resources(route: Route):
        if route.request.resource_type in ("image", "stylesheet", "font", "media"):
            route.abort()
        else:
            route.continue_()

    page.route("**/*", block_resources)
    page.goto("https://example.com")
    print(f"  Responses captured: {len(responses)}")
    page.unroute("**/*", block_resources)

    # ── Mock an API response ──────────────────────
    def mock_api(route: Route):
        route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps({"users": [{"id": 1, "name": "Mock User"}]}),
        )

    page.route("**/api/users", mock_api)
    # page.goto("https://myapp.com/users") → will receive mock data

    # ── Modify a request before sending ──────────
    def add_auth_header(route: Route):
        headers = {**route.request.headers, "Authorization": "Bearer token123"}
        route.continue_(headers=headers)

    page.route("**/api/**", add_auth_header)

    # ── Wait for a specific network response ──────
    # with page.expect_response("**/api/data") as response_info:
    #     page.click("button#load-data")
    # response = response_info.value
    # data = response.json()

    # ── Wait for request ──────────────────────────
    # with page.expect_request("**/api/submit") as request_info:
    #     page.click("#submit")
    # request = request_info.value
    # print(request.post_data)

    # ── HAR recording (record all traffic) ────────
    # context.record_har("traffic.har")  # set on context, not page

    # ── WebSocket monitoring ──────────────────────
    # page.on("websocket", lambda ws: print("WS opened:", ws.url))


# ═════════════════════════════════════════════════════════════════════════════
# 10. AUTHENTICATION & SESSION MANAGEMENT
# ═════════════════════════════════════════════════════════════════════════════
def section_10_authentication(playwright: Playwright):
    print("\n── 10. AUTHENTICATION & SESSION MANAGEMENT ─────────────────────")
    browser = playwright.chromium.launch(headless=True)

    # ── Cookie injection ──────────────────────────
    context = browser.new_context()
    context.add_cookies([
        {
            "name": "session_id",
            "value": "abc123",
            "domain": "example.com",
            "path": "/",
        }
    ])
    page = context.new_page()
    page.goto("https://example.com")
    cookies = context.cookies()
    print(f"  Cookies set: {len(cookies)}")

    # ── Save & reuse storage state (login once) ───
    # Step 1: Login and save state
    # page.goto("https://myapp.com/login")
    # page.fill("#email", "user@example.com")
    # page.fill("#password", "secret")
    # page.click("[type=submit]")
    # context.storage_state(path="auth_state.json")

    # Step 2: Reuse in subsequent runs (no login needed)
    # context2 = browser.new_context(storage_state="auth_state.json")
    # page2 = context2.new_page()
    # page2.goto("https://myapp.com/dashboard")  # already logged in

    # ── HTTP Basic Auth ───────────────────────────
    context3 = browser.new_context(
        http_credentials={"username": "admin", "password": "secret"}
    )

    # ── Local storage ─────────────────────────────
    context4 = browser.new_context()
    page4 = context4.new_page()
    page4.goto("https://example.com")
    page4.evaluate("localStorage.setItem('token', 'my-jwt-token')")
    token = page4.evaluate("localStorage.getItem('token')")
    print("  Token from localStorage:", token)

    browser.close()


# ═════════════════════════════════════════════════════════════════════════════
# 11. SCREENSHOTS & PDF
# ═════════════════════════════════════════════════════════════════════════════
def section_11_screenshots(page: Page):
    print("\n── 11. SCREENSHOTS & PDF ──────────────────────────────────────")
    page.goto("https://example.com")

    # Full-page screenshot
    page.screenshot(path="./screenshots/full_page.png", full_page=True)

    # Viewport only
    page.screenshot(path="./screenshots/viewport.png")

    # Element screenshot
    page.locator("h1").screenshot(path="./screenshots/heading.png")

    # Specific region (clip)
    page.screenshot(
        path="./screenshots/clipped.png",
        clip={"x": 0, "y": 0, "width": 800, "height": 400},
    )

    # Return as bytes (e.g. for in-memory use)
    image_bytes = page.screenshot(type="png")
    print(f"  Screenshot bytes: {len(image_bytes):,}")

    # JPEG with quality
    page.screenshot(path="./screenshots/compressed.jpg", type="jpeg", quality=80)

    # ── PDF (Chromium only) ───────────────────────
    page.pdf(
        path="./screenshots/page.pdf",
        format="A4",
        print_background=True,
        margin={"top": "1cm", "bottom": "1cm", "left": "1cm", "right": "1cm"},
    )
    print("  PDF saved.")


# ═════════════════════════════════════════════════════════════════════════════
# 12. MULTIPLE PAGES, TABS & CONTEXTS
# ═════════════════════════════════════════════════════════════════════════════
def section_12_multi_page(playwright: Playwright):
    print("\n── 12. MULTIPLE PAGES & CONTEXTS ──────────────────────────────")
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Open multiple tabs
    page1 = context.new_page()
    page2 = context.new_page()
    page1.goto("https://example.com")
    page2.goto("https://playwright.dev/")

    print(f"  Tab 1: {page1.title()}")
    print(f"  Tab 2: {page2.title()}")

    # List all open pages
    all_pages = context.pages
    print(f"  Open tabs: {len(all_pages)}")

    # Catch new tab opened by a link (target=_blank)
    with context.expect_page() as new_page_info:
        page1.evaluate("window.open('https://playwright.dev/', '_blank')")
    new_tab = new_page_info.value
    new_tab.wait_for_load_state()
    print(f"  New tab title: {new_tab.title()}")

    # Multiple isolated contexts (e.g. two different users)
    context_user_a = browser.new_context()
    context_user_b = browser.new_context()
    # Each has its own cookies / storage — fully isolated

    page1.close()
    page2.close()
    browser.close()


# ═════════════════════════════════════════════════════════════════════════════
# 13. WAITING STRATEGIES
# ═════════════════════════════════════════════════════════════════════════════
def section_13_waiting(page: Page):
    print("\n── 13. WAITING STRATEGIES ─────────────────────────────────────")
    page.goto("https://example.com")

    # Wait for selector to appear
    page.wait_for_selector("h1", state="visible")         # default
    page.wait_for_selector("h1", state="attached")        # in DOM, may be hidden
    page.wait_for_selector(".spinner", state="detached")  # wait for element to LEAVE

    # Wait for load states
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")    # no network for 500 ms

    # Wait for a fixed time (avoid when possible — prefer smart waits)
    page.wait_for_timeout(500)

    # Wait for URL
    # page.wait_for_url("**/success")

    # Wait for custom JS condition
    page.wait_for_function("document.title !== ''")
    page.wait_for_function("() => window.__LOADED__ === true")

    # Wait for response
    # with page.expect_response(lambda r: r.url.endswith("/api/data") and r.status == 200):
    #     page.click("#fetch-btn")

    # Expect assertions (auto-retrying, up to timeout)
    expect(page.locator("h1")).to_be_visible()
    expect(page.locator("h1")).to_have_text("Example Domain")
    expect(page).to_have_title(re.compile("Example"))
    expect(page).to_have_url("https://example.com/")
    expect(page.locator("h1")).to_have_count(1)


# ═════════════════════════════════════════════════════════════════════════════
# 14. JAVASCRIPT EXECUTION
# ═════════════════════════════════════════════════════════════════════════════
def section_14_javascript(page: Page):
    print("\n── 14. JAVASCRIPT EXECUTION ───────────────────────────────────")
    page.goto("https://example.com")

    # Run JS and return a value
    title = page.evaluate("document.title")
    print("  JS title:", title)

    # Pass Python value into JS
    result = page.evaluate("(x) => x * x", 7)
    print("  7² =", result)

    # Evaluate on a specific element
    el = page.locator("h1")
    text = el.evaluate("node => node.textContent")
    print("  Element text:", text)

    # evaluate_handle → returns a JS object handle
    body_handle = page.evaluate_handle("document.body")
    print("  Body handle:", body_handle)
    body_handle.dispose()

    # Expose a Python function to the browser
    def handle_from_browser(data):
        print("  Browser called Python with:", data)
        return {"status": "ok"}

    page.expose_function("pyFunction", handle_from_browser)
    page.evaluate("pyFunction({msg: 'hello from browser'})")

    # Add a <script> tag to the page
    page.add_script_tag(content="window.__TEST__ = 42;")
    val = page.evaluate("window.__TEST__")
    print("  Injected JS var:", val)

    # Add a <style> tag
    page.add_style_tag(content="body { background: #f0f0f0 !important; }")

    # Scroll to bottom via JS
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")


# ═════════════════════════════════════════════════════════════════════════════
# 15. DOWNLOADS & FILE UPLOADS
# ═════════════════════════════════════════════════════════════════════════════
def section_15_downloads_uploads(page: Page):
    print("\n── 15. DOWNLOADS & UPLOADS ────────────────────────────────────")
    page.goto("https://example.com")

    # ── Download a file ───────────────────────────
    # with page.expect_download() as download_info:
    #     page.locator("a#download-btn").click()
    # download = download_info.value
    # print("  Downloaded:", download.suggested_filename)
    # download.save_as("./downloads/" + download.suggested_filename)
    # print("  Path:", download.path())   # temp path before save_as

    # ── Upload a single file ──────────────────────
    # page.set_input_files("#upload", "./myfile.pdf")

    # ── Upload multiple files ─────────────────────
    # page.set_input_files("#upload", ["file1.txt", "file2.txt"])

    # ── Clear file input ──────────────────────────
    # page.set_input_files("#upload", [])

    # ── Upload via drag-and-drop (workaround) ─────
    # file_input = page.locator("input[type=file]")
    # file_input.set_input_files("./myfile.pdf")

    print("  (Download/Upload examples are commented — need real target pages)")


# ═════════════════════════════════════════════════════════════════════════════
# 16. GEOLOCATION, PERMISSIONS & DEVICE EMULATION
# ═════════════════════════════════════════════════════════════════════════════
def section_16_geo_permissions(playwright: Playwright):
    print("\n── 16. GEOLOCATION & PERMISSIONS ──────────────────────────────")
    browser = playwright.chromium.launch(headless=True)

    # ── Geolocation ───────────────────────────────
    context = browser.new_context(
        geolocation={"latitude": 19.0760, "longitude": 72.8777},  # Mumbai
        permissions=["geolocation"],
    )
    page = context.new_page()
    page.goto("https://example.com")
    print("  Geolocation context set (Mumbai)")

    # ── Override permissions ──────────────────────
    context.grant_permissions(["notifications", "camera", "microphone"])
    context.clear_permissions()

    # ── Device emulation ──────────────────────────
    iphone = playwright.devices["iPhone 14"]
    print("  iPhone 14 config:", iphone)
    mobile_context = browser.new_context(**iphone)
    mobile_page = mobile_context.new_page()
    mobile_page.goto("https://example.com")
    print("  Mobile viewport:", mobile_page.viewport_size)

    # ── Custom viewport ───────────────────────────
    desktop_context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        user_agent="Mozilla/5.0 (compatible; MyScraper/1.0)",
        locale="en-IN",
        timezone_id="Asia/Kolkata",
        color_scheme="dark",       # "light" | "dark" | "no-preference"
        has_touch=False,
    )

    browser.close()


# ═════════════════════════════════════════════════════════════════════════════
# 17. ASYNC PLAYWRIGHT
# ═════════════════════════════════════════════════════════════════════════════
async def section_17_async():
    print("\n── 17. ASYNC PLAYWRIGHT ────────────────────────────────────────")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()

        # ── Parallel scraping (multiple pages at once) ─
        async def scrape_page(url: str) -> dict:
            page = await context.new_page()
            await page.goto(url)
            title = await page.title()
            await page.close()
            return {"url": url, "title": title}

        urls = [
            "https://example.com",
            "https://playwright.dev/",
            "https://python.org",
        ]

        tasks = [scrape_page(url) for url in urls]
        results = await asyncio.gather(*tasks)

        for r in results:
            print(f"  {r['url'][:40]:40s} → {r['title']}")

        await browser.close()


# ═════════════════════════════════════════════════════════════════════════════
# 18. BROWSER CONTEXT — ISOLATION & STORAGE
# ═════════════════════════════════════════════════════════════════════════════
def section_18_context(playwright: Playwright):
    print("\n── 18. BROWSER CONTEXTS ───────────────────────────────────────")
    browser = playwright.chromium.launch(headless=True)

    # Each context is a full isolated browser session
    ctx1 = browser.new_context()
    ctx2 = browser.new_context()   # completely separate cookies / storage

    p1 = ctx1.new_page()
    p2 = ctx2.new_page()
    p1.goto("https://example.com")
    p2.goto("https://example.com")

    # Manipulate cookies
    ctx1.add_cookies([{"name": "user", "value": "alice", "domain": "example.com", "path": "/"}])
    cookies = ctx1.cookies("https://example.com")
    print("  ctx1 cookies:", cookies)

    # Clear cookies
    ctx1.clear_cookies()

    # Save session to file
    # ctx1.storage_state(path="alice_session.json")

    # Load session from file
    # ctx_restored = browser.new_context(storage_state="alice_session.json")

    ctx1.close()
    ctx2.close()
    browser.close()


# ═════════════════════════════════════════════════════════════════════════════
# 19. VIDEO RECORDING
# ═════════════════════════════════════════════════════════════════════════════
def section_19_video(playwright: Playwright):
    print("\n── 19. VIDEO RECORDING ─────────────────────────────────────────")
    browser = playwright.chromium.launch(headless=True)

    context = browser.new_context(
        record_video_dir="./videos/",
        record_video_size={"width": 1280, "height": 720},
    )
    page = context.new_page()
    page.goto("https://example.com")
    page.locator("h1").scroll_into_view_if_needed()
    page.wait_for_timeout(1000)

    # The video is saved when context is closed
    context.close()

    video_path = page.video.path()
    print(f"  Video saved to: {video_path}")
    browser.close()


# ═════════════════════════════════════════════════════════════════════════════
# 20. ERROR HANDLING, ASSERTIONS & RETRIES
# ═════════════════════════════════════════════════════════════════════════════
def section_20_error_handling(page: Page):
    print("\n── 20. ERROR HANDLING & ASSERTIONS ────────────────────────────")
    page.goto("https://example.com")

    # ── Playwright expect() assertions ────────────
    # These auto-retry until the condition is met (default 5 s timeout)
    expect(page).to_have_title(re.compile("Example"))
    expect(page.locator("h1")).to_be_visible()
    expect(page.locator("h1")).to_have_text("Example Domain")
    expect(page.locator("a")).to_have_count(2)
    expect(page.locator("h1")).not_to_be_hidden()
    # expect(page.get_by_label("Email")).to_have_value("user@example.com")
    # expect(page.locator("button")).to_be_enabled()
    # expect(page.locator("button")).to_be_disabled()
    # expect(page.locator("input")).to_be_checked()
    print("  All assertions passed.")

    # ── Try/except for graceful error handling ────
    from playwright.sync_api import TimeoutError as PlaywrightTimeout

    try:
        page.locator(".non-existent-element").click(timeout=2000)
    except PlaywrightTimeout:
        print("  Element not found — handled gracefully.")

    # ── Retry wrapper helper ───────────────────────
    def retry(fn, retries: int = 3, delay: float = 1.0) -> Any:
        for attempt in range(1, retries + 1):
            try:
                return fn()
            except Exception as e:
                print(f"  Attempt {attempt} failed: {e}")
                if attempt == retries:
                    raise
                time.sleep(delay)

    result = retry(lambda: page.title(), retries=3)
    print("  Title (with retry):", result)

    # ── Page error events ─────────────────────────
    page.on("pageerror", lambda err: print("  JS error on page:", err))
    page.on("crash", lambda: print("  Page crashed!"))
    page.on("console", lambda msg: None)   # suppress or log console.log


# ═════════════════════════════════════════════════════════════════════════════
# MAIN — RUN ALL SECTIONS
# ═════════════════════════════════════════════════════════════════════════════
def main():
    print("=" * 70)
    print("  PLAYWRIGHT COMPLETE GUIDE — ALL FEATURES")
    print("=" * 70)

    # Create output directories
    Path("./screenshots").mkdir(exist_ok=True)
    Path("./downloads").mkdir(exist_ok=True)
    Path("./videos").mkdir(exist_ok=True)

    section_01_browser_launch()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()

        section_02_navigation(page)
        section_03_locators(page)
        section_04_interactions(page)
        section_05_keyboard_mouse(page)
        books = section_06_web_scraping(page)
        section_07_frames(page)
        section_08_dialogs(page)
        section_09_network(page)
        section_13_waiting(page)
        section_14_javascript(page)
        section_15_downloads_uploads(page)
        section_20_error_handling(page)

        context.close()
        browser.close()

        # Sections that need their own browser/context
        section_10_authentication(p)
        section_12_multi_page(p)
        section_16_geo_permissions(p)
        section_18_context(p)

        # Screenshot section
        browser2 = p.chromium.launch(headless=True)
        ctx2 = browser2.new_context()
        pg2 = ctx2.new_page()
        section_11_screenshots(pg2)
        ctx2.close()
        browser2.close()

    # Async section
    asyncio.run(section_17_async())

    print("\n" + "=" * 70)
    print("  ALL SECTIONS COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
