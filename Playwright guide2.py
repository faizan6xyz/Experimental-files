"""
================================================================================
  PLAYWRIGHT PYTHON - COMPLETE ADVANCED REFERENCE
  Covers: Basics, Scraping, Auth, API, Stealth, Tracing, Video, Events,
          Accessibility Tree, Frames, Mouse/Keyboard, Network, Multi-tab,
          Geolocation, Mocking, Storage State, Async, Devices
================================================================================
"""

import asyncio
import json
from playwright.sync_api import sync_playwright, Playwright
from playwright.async_api import async_playwright


# ============================================================
# 1. BASICS — launch, context, page, screenshot
# ============================================================
def basics():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        context = browser.new_context(
            viewport={"width": 1280, "height": 720},
            locale="en-US",
            timezone_id="Asia/Kolkata",
        )
        page = context.new_page()

        page.goto("https://example.com")
        print("Title:", page.title())
        print("URL  :", page.url)
        print("HTML :", page.content()[:200])

        page.screenshot(path="homepage.png")
        page.screenshot(path="fullpage.png", full_page=True)

        browser.close()


# ============================================================
# 2. NAVIGATION
# ============================================================
def navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://example.com")
        page.goto("https://google.com", wait_until="domcontentloaded")
        page.go_back()
        page.go_forward()
        page.reload()

        browser.close()


# ============================================================
# 3. LOCATORS & SELECTORS
# ============================================================
def locators():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com")

        # recommended locator methods
        page.get_by_text("Login").click()
        page.get_by_role("button", name="submit")
        page.get_by_placeholder("Username")
        page.get_by_label("Email")

        # css / xpath
        page.locator(".quote")
        page.locator("//h1")

        # chaining
        page.locator(".quote").locator(".author")

        # nth element
        page.locator(".quote").nth(0).inner_text()

        # all elements
        quotes = page.locator(".quote").all()
        for q in quotes:
            print(q.locator(".text").inner_text())
            print(q.locator(".author").inner_text())

        # count
        print("Total quotes:", page.locator(".quote").count())

        # loop by index
        items = page.locator(".quote")
        for i in range(items.count()):
            print(items.nth(i).inner_text())

        browser.close()


# ============================================================
# 4. INPUT ACTIONS — fill, click, keyboard, mouse
# ============================================================
def input_actions():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com/login")

        # fill input
        page.fill("#username", "myuser")
        page.fill("#password", "mypassword")

        # type char by char (more human-like)
        page.type("#username", "myuser", delay=50)

        # click
        page.click("button[type=submit]")
        page.dblclick("#item")
        page.hover(".menu")

        # keyboard
        page.keyboard.press("Enter")
        page.keyboard.press("Control+A")
        page.keyboard.press("Control+C")
        page.keyboard.type("Hello World", delay=30)
        page.keyboard.down("Shift")
        page.keyboard.press("ArrowRight")
        page.keyboard.up("Shift")

        # mouse
        page.mouse.move(200, 300)
        page.mouse.click(200, 300)
        page.mouse.dblclick(200, 300)
        page.mouse.wheel(0, 500)       # scroll down

        # drag and drop
        page.drag_and_drop("#source", "#target")

        # form controls
        page.check("input[type=checkbox]")
        page.uncheck("input[type=checkbox]")
        page.select_option("select#country", "India")
        page.set_checked("input[type=checkbox]", True)

        browser.close()


# ============================================================
# 5. WAITING STRATEGIES
# ============================================================
def waiting():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")

        # wait fixed time (avoid if possible)
        page.wait_for_timeout(2000)

        # wait for element state
        page.wait_for_selector("#dashboard")
        page.locator("#submit").wait_for(state="visible")
        page.locator("#submit").wait_for(state="attached")
        page.locator("#submit").wait_for(state="hidden")

        # wait for page load state
        page.wait_for_load_state("load")
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_load_state("networkidle")

        # expect_ pattern — proper way to wait for events
        with page.expect_navigation():
            page.click("a")

        with page.expect_response("**/api/data") as res_info:
            page.click("#load-data")
        print(res_info.value.json())

        with page.expect_download() as dl_info:
            page.click("text=Download")
        dl_info.value.save_as("downloaded_file.pdf")

        browser.close()


# ============================================================
# 6. SCRAPING
# ============================================================
def scraping():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com")

        # inner text
        title = page.locator("h1").inner_text()
        print("H1:", title)

        # get attribute
        links = page.locator("a").all()
        for link in links[:5]:
            print(link.get_attribute("href"))

        # run javascript to extract data
        data = page.evaluate("() => document.title")
        print("JS title:", data)

        all_text = page.evaluate("""
            () => Array.from(document.querySelectorAll('.quote .text'))
                       .map(el => el.textContent)
        """)
        print(all_text)

        # eval on specific element
        h1_text = page.eval_on_selector("h1", "el => el.textContent")
        print(h1_text)

        # paginate
        while True:
            quotes = page.locator(".quote").all()
            for q in quotes:
                print(q.locator(".text").inner_text())
            if page.locator("li.next a").count() == 0:
                break
            page.click("li.next a")
            page.wait_for_load_state("domcontentloaded")

        browser.close()


# ============================================================
# 7. AUTH — login and save session (storage state)
# ============================================================
def auth_and_storage_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # login once
        page.goto("https://quotes.toscrape.com/login")
        page.fill("input[name=username]", "admin")
        page.fill("input[name=password]", "admin")
        page.click("input[type=submit]")
        page.wait_for_load_state("networkidle")

        # save session to file
        context.storage_state(path="auth.json")
        print("Session saved to auth.json")

        browser.close()

    # reuse session — no login needed
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()
        page.goto("https://quotes.toscrape.com")
        print("Logged in as:", page.locator("a.nav-link").first.inner_text())
        browser.close()


# ============================================================
# 8. COOKIES
# ============================================================
def cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://example.com")

        # get all cookies
        all_cookies = context.cookies()
        print(json.dumps(all_cookies, indent=2))

        # add cookies manually
        context.add_cookies([{
            "name": "session_id",
            "value": "abc123",
            "domain": "example.com",
            "path": "/",
            "httpOnly": True,
            "secure": False,
        }])

        # clear cookies
        context.clear_cookies()

        browser.close()


# ============================================================
# 9. NETWORK INTERCEPTION & MOCKING
# ============================================================
def network_interception():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # log all requests
        def handle_request(request):
            print("REQ:", request.method, request.url)

        def handle_response(response):
            print("RES:", response.status, response.url)

        page.on("request",  handle_request)
        page.on("response", handle_response)

        # block images and ads to speed up
        def block_resources(route):
            if route.request.resource_type in ["image", "media", "font"]:
                route.abort()
            else:
                route.continue_()

        page.route("**/*", block_resources)

        # mock an API endpoint
        def mock_api(route):
            if "api/users" in route.request.url:
                route.fulfill(
                    status=200,
                    content_type="application/json",
                    body=json.dumps([{"id": 1, "name": "Faizan"}])
                )
            else:
                route.continue_()

        page.route("**/*", mock_api)

        # abort specific requests
        page.route("**/ads/**", lambda route: route.abort())

        page.goto("https://example.com")
        browser.close()


# ============================================================
# 10. EVENT LISTENERS
# ============================================================
def event_listeners():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.on("console",   lambda msg:  print("CONSOLE:", msg.type, msg.text))
        page.on("pageerror", lambda err:  print("ERROR:", err))
        page.on("request",   lambda req:  print("REQ:", req.url))
        page.on("response",  lambda res:  print("RES:", res.status))
        page.on("dialog",    lambda d:    d.accept())   # auto-accept alerts
        page.on("download",  lambda dl:   print("DOWNLOAD:", dl.suggested_filename))

        # inject JS
        page.add_script_tag(content="console.log('Script injected')")
        page.add_init_script("console.log('Runs before page load')")

        page.goto("https://example.com")
        browser.close()


# ============================================================
# 11. POPUPS, DIALOGS, NEW TABS
# ============================================================
def popups_and_tabs():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://example.com")

        # handle alert / confirm / prompt dialogs
        page.on("dialog", lambda dialog: dialog.accept())
        page.on("dialog", lambda dialog: dialog.dismiss())
        page.on("dialog", lambda dialog: dialog.fill("input text"))

        # open new tab
        with context.expect_page() as new_page_info:
            page.click("text=Open in new tab")
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        print("New tab URL:", new_page.url)

        # all open pages
        all_pages = context.pages
        print("Open tabs:", len(all_pages))

        new_page.close()
        browser.close()


# ============================================================
# 12. FRAMES / IFRAMES
# ============================================================
def frames():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")

        # by name attribute
        frame = page.frame(name="my_frame")

        # by url
        frame = page.frame(url="**/iframe-content**")

        # frame_locator (recommended)
        frame_loc = page.frame_locator("iframe#payment")
        frame_loc.locator("input[name=cardnumber]").fill("4111111111111111")
        frame_loc.locator("button").click()

        # nested iframes
        nested = page.frame_locator("iframe#outer").frame_locator("iframe#inner")
        nested.locator("button").click()

        browser.close()


# ============================================================
# 13. FILE UPLOAD & DOWNLOAD
# ============================================================
def file_upload_download():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com/upload")

        # single file upload
        page.set_input_files("input[type=file]", "myfile.txt")

        # multiple files
        page.set_input_files("input[type=file]", ["file1.txt", "file2.pdf"])

        # clear file input
        page.set_input_files("input[type=file]", [])

        # download
        with page.expect_download() as dl_info:
            page.click("text=Download Report")
        download = dl_info.value
        download.save_as("report.pdf")
        print("Downloaded:", download.suggested_filename)

        browser.close()


# ============================================================
# 14. ACCESSIBILITY TREE (key for browser agents)
# ============================================================
def accessibility_tree():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")

        # full accessibility snapshot
        snapshot = page.accessibility.snapshot()
        print(json.dumps(snapshot, indent=2))

        # snapshot of a specific element only
        element = page.locator("nav")
        nav_snapshot = page.accessibility.snapshot(root=element.element_handle())
        print(json.dumps(nav_snapshot, indent=2))

        # useful fields in each node:
        # role, name, value, checked, focused, expanded, children
        def walk_tree(node, depth=0):
            indent = "  " * depth
            role  = node.get("role", "")
            name  = node.get("name", "")
            value = node.get("value", "")
            print(f"{indent}[{role}] {name} {value}")
            for child in node.get("children", []):
                walk_tree(child, depth + 1)

        walk_tree(snapshot)
        browser.close()


# ============================================================
# 15. TRACING (record & replay)
# ============================================================
def tracing():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        page = context.new_page()
        page.goto("https://example.com")
        page.click("a")

        context.tracing.stop(path="trace.zip")
        print("Trace saved. View with: playwright show-trace trace.zip")

        browser.close()


# ============================================================
# 16. VIDEO RECORDING
# ============================================================
def video_recording():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            record_video_dir="videos/",
            record_video_size={"width": 1280, "height": 720}
        )
        page = context.new_page()
        page.goto("https://example.com")
        page.click("a")

        context.close()  # video is saved on context close
        print("Video saved in videos/ folder")
        print("Video path:", page.video.path())

        browser.close()


# ============================================================
# 17. GEOLOCATION & PERMISSIONS
# ============================================================
def geolocation_permissions():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            geolocation={"latitude": 28.6139, "longitude": 77.2090},  # Delhi
            permissions=["geolocation", "notifications"],
        )
        page = context.new_page()
        page.goto("https://maps.google.com")

        # grant / revoke permission for a specific origin
        context.grant_permissions(["camera"], origin="https://example.com")
        context.clear_permissions()

        browser.close()


# ============================================================
# 18. STEALTH / ANTI-BOT BYPASS
# ============================================================
def stealth():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-infobars",
            ]
        )
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 720},
            locale="en-US",
            timezone_id="Asia/Kolkata",
            java_script_enabled=True,
        )

        # hide webdriver flag
        context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
            window.chrome = { runtime: {} };
            Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3] });
            Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
        """)

        page = context.new_page()
        page.goto("https://bot.sannysoft.com")  # bot detection test page
        page.screenshot(path="stealth_test.png")

        browser.close()


# ============================================================
# 19. PERSISTENT CONTEXT (reuse Chrome profile)
# ============================================================
def persistent_context():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir="my_profile",   # stores cookies, cache, localStorage
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = context.new_page()
        page.goto("https://example.com")
        print("Title:", page.title())
        context.close()


# ============================================================
# 20. DEVICE EMULATION
# ============================================================
def device_emulation():
    with sync_playwright() as p:
        iphone = p.devices["iPhone 13"]
        browser = p.webkit.launch(headless=False)
        context = browser.new_context(**iphone)
        page = context.new_page()
        page.goto("https://example.com")
        page.screenshot(path="mobile_view.png")
        browser.close()

    # list all available devices
    with sync_playwright() as p:
        print(list(p.devices.keys()))


# ============================================================
# 21. JAVASCRIPT — inject, evaluate, clipboard
# ============================================================
def javascript():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")

        # run JS and get return value
        title  = page.evaluate("() => document.title")
        width  = page.evaluate("() => window.innerWidth")
        scroll = page.evaluate("() => window.scrollY")
        print(title, width, scroll)

        # pass python value into JS
        result = page.evaluate("x => x * 2", 21)
        print(result)   # 42

        # eval on a specific element
        text = page.eval_on_selector("h1", "el => el.textContent")
        print(text)

        # scroll to bottom
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

        # inject HTML
        page.set_content("<h1>Hello Faizan</h1>")

        # clipboard (needs permissions in real browser)
        page.evaluate("navigator.clipboard.writeText('copied!')")

        browser.close()


# ============================================================
# 22. API TESTING (no browser needed)
# ============================================================
async def api_testing():
    async with async_playwright() as p:
        # standalone API context
        api = await p.request.new_context(
            base_url="https://jsonplaceholder.typicode.com"
        )

        # GET
        res = await api.get("/todos/1")
        print(res.status, await res.json())

        # POST
        res = await api.post("/posts", data=json.dumps({
            "title": "test", "body": "hello", "userId": 1
        }), headers={"Content-Type": "application/json"})
        print(res.status, await res.json())

        # assert responses
        assert res.ok
        assert res.status == 201
        assert res.headers["content-type"] == "application/json; charset=utf-8"

        await api.dispose()


# ============================================================
# 23. SHARE COOKIES BETWEEN BROWSER AND API
# ============================================================
async def share_cookies_browser_api():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # login via browser
        await page.goto("https://example.com/login")
        await page.fill("#username", "admin")
        await page.fill("#password", "admin")
        await page.click("button[type=submit]")
        await page.wait_for_load_state("networkidle")

        # get session state (cookies + localStorage)
        storage = await context.storage_state()

        # pass same session to API context
        api = await p.request.new_context(storage_state=storage)
        res = await api.get("https://example.com/api/profile")
        print(await res.json())

        await browser.close()


# ============================================================
# 24. ASYNC — full async example
# ============================================================
async def async_example():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://quotes.toscrape.com")
        print("Title:", await page.title())

        quotes = await page.locator(".quote").all()
        for q in quotes:
            text   = await q.locator(".text").inner_text()
            author = await q.locator(".author").inner_text()
            print(text, "-", author)

        await browser.close()


# ============================================================
# 25. DEBUGGING
# ============================================================
def debugging():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://example.com")

        # pause and open Playwright Inspector
        page.pause()

        # take screenshot at any point
        page.screenshot(path="debug_screenshot.png")

        # print full HTML
        print(page.content())

        browser.close()


# ============================================================
# MAIN — run all sync examples
# ============================================================
if __name__ == "__main__":
    print("\n--- 1. BASICS ---")
    basics()

    print("\n--- 2. NAVIGATION ---")
    navigation()

    print("\n--- 3. LOCATORS ---")
    locators()

    print("\n--- 4. INPUT ACTIONS ---")
    # input_actions()   # needs a real login page

    print("\n--- 5. WAITING ---")
    # waiting()

    print("\n--- 6. SCRAPING ---")
    scraping()

    print("\n--- 7. AUTH & STORAGE STATE ---")
    auth_and_storage_state()

    print("\n--- 8. COOKIES ---")
    cookies()

    print("\n--- 9. NETWORK INTERCEPTION ---")
    network_interception()

    print("\n--- 10. EVENT LISTENERS ---")
    event_listeners()

    print("\n--- 11. POPUPS & TABS ---")
    # popups_and_tabs()

    print("\n--- 12. FRAMES ---")
    # frames()

    print("\n--- 13. FILE UPLOAD & DOWNLOAD ---")
    # file_upload_download()

    print("\n--- 14. ACCESSIBILITY TREE ---")
    accessibility_tree()

    print("\n--- 15. TRACING ---")
    tracing()

    print("\n--- 16. VIDEO RECORDING ---")
    # video_recording()

    print("\n--- 17. GEOLOCATION ---")
    # geolocation_permissions()

    print("\n--- 18. STEALTH ---")
    stealth()

    print("\n--- 19. PERSISTENT CONTEXT ---")
    # persistent_context()

    print("\n--- 20. DEVICE EMULATION ---")
    device_emulation()

    print("\n--- 21. JAVASCRIPT ---")
    javascript()

    print("\n--- 22. API TESTING (async) ---")
    asyncio.run(api_testing())

    print("\n--- 23. SHARE COOKIES BROWSER+API (async) ---")
    # asyncio.run(share_cookies_browser_api())

    print("\n--- 24. FULL ASYNC EXAMPLE ---")
    asyncio.run(async_example())

    print("\n--- 25. DEBUGGING ---")
    # debugging()   # uncomment to open inspector

    print("\nDone.")