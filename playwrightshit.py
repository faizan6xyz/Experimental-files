# ✅ Sync API → simple, beginner-friendly
from playwright.sync_api import sync_playwright , Playwright , APIRequest  , APIRequestContext
def main():
    with sync_playwright() as p:   #  same as   p = sync_playwright().start()
        # 🔹 Launch browser
        browser = p.chromium.launch(headless=False) # lauches a fresh page , without the earlier content
        # for earlier content browser context = p.chromium.launch_persistent_context( user_data_dir="user_data", headless=False )
        # creates a new browser context , we can add parameter in this 
        context = browser.new_context(timeout=5000) # 5 second 
        # creates a new tab / page in the browser
        page = context.new_page()
        # 🔹 1. Open website
        page.goto("https://example.com")
        print("Title:", page.title())
        # 🔹 Screenshot
        page.screenshot(path="homepage.png")
        # 🔹 2. Google Search
        page.goto("https://www.google.com")
        page.fill('textarea[name="q"]', "Playwright Python")
        page.keyboard.press("Enter")
        page.wait_for_timeout(3000)
        print("Google Title:", page.title())
        # wiat for the element 
        page.wait_for_selector("#dashboard")
        # 🔹 3. Scraping Example
        page.goto("https://quotes.toscrape.com")
        quotes = page.locator(".quote").all()
        print("\nQuotes:\n")
        # click button
        page.locator("text=Login").click()
        # type username 
        page.locator("#username").fill("admin")
        for q in quotes:
            text = q.locator(".text").inner_text()
            author = q.locator(".author").inner_text()
            print(text, "-", author)
        # 🔹 4. Click Example (Next Page)
        if page.locator("text=Next").count() > 0:
            page.click("text=Next")
            page.wait_for_timeout(2000)
        # add javascript to the page
        page.add_script_tag(content="console.log('Hi')")
        # runs javascript before the content load 
        page.add_init_script("console.log('Runs first')")
        # 🔹 5. Login Example (Dummy)
        page.goto("https://example.com/login")
        try:
            page.fill("#username", "myuser")
            page.fill("#password", "mypassword")
            page.click("button[type=submit]")
            print("Login attempted")
        except:
            print("Login page not available (example site)")
        # 🔹 6. Auto wait example
        try:
            page.click("text=Login")
        except:
            pass
        # 🔹 7. Extract all links
        links = page.locator("a").all()
        print("\nLinks found:", len(links))
        for link in links[:5]:  # limit output
            try:
                print(link.get_attribute("href"))
            except:
                pass
        # 🔹 Close browser
        browser.close()

        '''
        goto() → open page
        click() → click
        fill() → type
        locator() → find element
        context → session'''

# Terminates this instance of Playwright in case it was created bypassing the Python context manager.
Playwright.stop()
# we need to write async in function cause of await , it lets the await puases it and let other task run meanwhile .we need await inside the async function Because Python needs  permission to: Pause execution and Resume later
# ⚡ Async API → faster, scalable, professional use
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch() # no UI
        page = await browser.new_page()
        await page.goto("https://example.com")
        print(await page.title())
        await browser.close()
asyncio.run(main())



# device in sync API 
def run(playwright: Playwright):
    # This object can be used to launch or connect to WebKit, returning instances of Browser.
    webkit = playwright.webkit   # WebKit is a browser engine means: It is the core software that renders websites
    iphone = playwright.devices["iPhone 13"]  # Returns a dictionary of devices
    browser = webkit.launch()
    context = browser.new_context(**iphone)   
    '''
    **iphone means 
    { 
    "viewport": {"width": 390, "height": 844},
    "user_agent": "...",
    "is_mobile": True,
    "has_touch": True
    }


    for manual setup 
    context = browser.new_context(
    viewport={"width": 375, "height": 667},
    user_agent="MyCustomAgent",
    is_mobile=True
)
    '''
    page = context.new_page()
    page.goto("http://example.com")
    # other actions...
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


# devices in the async API 
async def run(playwright: Playwright):
    webkit = playwright.webkit
    iphone = playwright.devices["iPhone 13"]
    browser = await webkit.launch()
    context = await browser.new_context(**iphone)
    page = await context.new_page()
    await page.goto("http://example.com")
    # other actions...
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())

# Exposes API that can be used for the Web API testing.
playwright.request
# Selectors can be used to install custom selector engines.
playwright.selectors
# using API request content , Creates new instances of APIRequestContext.
async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        api_context = await p.request.new_context()            # p.request is an API request engine
        response = await api_context.get("https://api.github.com")
        print(await response.json())
asyncio.run(main())   
# share cookies between browser and the API
async def main ():
    with async_playwright() as p:   #  same as   p = sync_playwright().start()
        browser = p.chromium.launch(headless=False)   # visible browser
        context = await browser.new_context()
        # create a session object for request 
        page = await context.new_page()
        # login via browser
        await page.goto("https://example.com/login")
        # use same session for API
        api_context = await p.request.new_context()
        storage_state=await context.storage_state()   # storage_state = saved browser session data
        response = await api_context.get("https://example.com/api/user")
        delo = p.request.context.delete()
        print(await response.json())
        await response.json()     # JSON data
        await response.text()     # raw text
        response.status           # status code
        response.headers          # headers
        response.get( data={ "username": "test", "password": "123" }) # to send data and call API
# The assert keyword in Python is used for debugging and testing conditions. It helps you check if something is true while your program runs.
with sync_playwright() as p:
    context = playwright.request.new_context()
    response = context.get("https://example.com/user/repos")
    assert response.ok
    assert response.status == 200
    assert response.headers["content-type"] == "application/json; charset=utf-8"
    assert response.json()["name"] == "foobar"
    assert response.body() == '{"status": "ok"}'
    browser = p.chromium.launch()
    context =browser.new_context()   # A Browser Context is like a separate browser profile/session inside the same browser.   
    response.dispose() #dispose the body of the response
    context1 = p.chromium.launch_persistent_context(
        user_data_dir="my_profile",  # 📁 stores data here
        headless=False
    ) 
    browser = p.chromium.launch() # no UI
    page = browser.new_page()
# download the values and save them as pdf 
with page.expect_download() as download: 
    page.click("text=Download")
    file = download.value
    file.save_as("file.pdf")
# handling multiple tabs 
with context.expect_page() as new_page_info:
    page.click("text=Open")
new_page = new_page_info.value
new_page.wait_for_load_state()
# file uopload 
page.set_input_files("input[type='file']", "file.txt")
# wait for page load status 
page.goto("https://example.com")
page.wait_for_load_state("networkidle")  # no network requests
# wait for the element status 
page.locator("#submit").wait_for(state="visible")
page.locator("#submit").wait_for(state="attached")
# Count elements
count = page.locator(".product").count()
print(count)
#  Loop Through Elements
items = page.locator(".product")
for i in range(items.count()):
    print(items.nth(i).inner_text())
# Extract Data (Scraping Style)
titles = page.locator(".title")
for i in range(titles.count()):
    print(titles.nth(i).inner_text())
# Handle Popups / Alerts
page.on("dialog", lambda dialog: dialog.accept())
page.click("text=Delete")
# Handle New Windows / Tabs Properly
with context.expect_page() as p:
    page.click("text=Open")
new_page = p.value
new_page.wait_for_load_state()
# Debugging Like a Pro : Pause execution
page.pause() # Opens Playwright inspector
# Slow motion
browser = p.chromium.launch(headless=False, slow_mo=500)
# intercept network request
def handle_route(route):
    print(route.request.url)
    route.continue_()
page.route("**/*", handle_route)
page.route("**/api/*", lambda route: route.abort()) # Modify request
# Working with Cookies
cookies = context.cookies()
print(cookies)
context.add_cookies([
    {"name": "test", "value": "123", "domain": "example.com", "path": "/"}
])
# network interception  . nlocks image , ads , mocks API , test edge cases 

def handle_route(route):
    if "api" in route.request.url:
        route.fulfill( status=200, body='{"message": "mocked"}') 
    else:
        route.continue_()
context.route("**/*", handle_route)   # gives the route of the context 
# Push data into input fields
page.fill("input[name='username']", "your_username")
page.fill("input[name='password']", "your_password")

# Click button
page.click("button[type='submit']")

# Wait to see result
page.wait_for_timeout(3000)



"""
================ PLAYWRIGHT PAGE METHODS CHEAT SHEET =================

🌐 Navigation
page.goto(url)
page.reload()
page.go_back()
page.go_forward()

📄 Page Info
page.title()
page.url
page.content()

🔍 Locators (Recommended)
page.locator("selector")
page.get_by_text("text")
page.get_by_role("button")
page.get_by_placeholder("Enter name")

🧾 Old Selectors (Less Preferred)
page.query_selector("selector")
page.query_selector_all("selector")

✍️ Input Actions
page.fill("input", "text")
page.type("input", "text")
page.press("input", "Enter")

🖱️ Mouse / Click Actions
page.click("button")
page.dblclick("button")
page.hover("element")

✔️ Form Controls
page.check("input")
page.uncheck("input")
page.select_option("select", "value")
page.set_checked("input", True)

📸 Screenshot
page.screenshot(path="img.png")

⏳ Waiting
page.wait_for_timeout(2000)
page.wait_for_selector("div")
page.wait_for_load_state("load")

⚡ JavaScript Execution
page.evaluate("() => document.title")
page.eval_on_selector("h1", "el => el.textContent")

📜 Inject Scripts / HTML
page.add_script_tag(content="console.log('hi')")
page.add_init_script("console.log('before load')")
page.set_content("<h1>Hello</h1>")

📂 File Upload
page.set_input_files("input[type=file]", "file.txt")

📡 Network Handling
page.on("request", handler)
page.on("response", handler)

🪟 Popups / New Tabs
page.expect_popup()

🧠 Keyboard
page.keyboard.press("Enter")
page.keyboard.type("hello")

🖥️ Frames (iframes)
page.frame(name="frame_name")

====================================================================

🔥 MOST IMPORTANT METHODS:
page.goto()
page.locator()
page.click()
page.fill()
page.title()
page.screenshot()
page.wait_for_selector()
page.evaluate()

💡 TIP:
Prefer locator:
page.locator("button").click()

====================================================================
"""






































# cleaned version
# =========================
# ✅ SYNC PLAYWRIGHT (BEGINNER)
# =========================
from playwright.sync_api import sync_playwright


def sync_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        page = context.new_page()

        # Open website
        page.goto("https://example.com")
        print("Title:", page.title())

        # Screenshot
        page.screenshot(path="homepage.png")

        # Google search
        page.goto("https://www.google.com")
        page.fill('textarea[name="q"]', "Playwright Python")
        page.keyboard.press("Enter")
        page.wait_for_timeout(3000)

        print("Google Title:", page.title())

        # Scraping example
        page.goto("https://quotes.toscrape.com")

        quotes = page.locator(".quote").all()
        print("\nQuotes:\n")

        for q in quotes:
            text = q.locator(".text").inner_text()
            author = q.locator(".author").inner_text()
            print(text, "-", author)

        # Click next page
        if page.locator("text=Next").count() > 0:
            page.click("text=Next")
            page.wait_for_timeout(2000)

        # Dummy login
        page.goto("https://example.com/login")
        try:
            page.fill("#username", "myuser")
            page.fill("#password", "mypassword")
            page.click("button[type=submit]")
            print("Login attempted")
        except:
            print("Login page not available")

        # Extract links
        links = page.locator("a").all()
        print("\nLinks found:", len(links))

        for link in links[:5]:
            print(link.get_attribute("href"))

        browser.close()


# =========================
# ✅ ASYNC PLAYWRIGHT (ADVANCED)
# =========================
import asyncio
from playwright.async_api import async_playwright


async def async_example():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        await page.goto("https://example.com")
        print(await page.title())

        await browser.close()


# =========================
# ✅ DEVICE EMULATION (SYNC)
# =========================
def device_example():
    with sync_playwright() as p:
        iphone = p.devices["iPhone 13"]

        browser = p.webkit.launch()
        context = browser.new_context(**iphone)

        page = context.new_page()
        page.goto("https://example.com")

        browser.close()


# =========================
# ✅ API TESTING (ASYNC)
# =========================
async def api_example():
    async with async_playwright() as p:
        api_context = await p.request.new_context()

        response = await api_context.get("https://api.github.com")
        print(await response.json())


# =========================
# ✅ RUN FUNCTIONS
# =========================
if __name__ == "__main__":
    sync_example()
    asyncio.run(async_example())
    asyncio.run(api_example())