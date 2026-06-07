from playwright.sync_api import sync_playwright
import csv
import time
def scrape_yc():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.ycombinator.com/companies")
        # Scroll to load data
        for _ in range(8):
            page.evaluate("window.scrollBy(0 , 5000)")  # because its indepent and runs directly on javascript of the page and fast 
            # page.mouse.wheel(0, 5000)         wheel(x,y) +ve for down and right , -ve for up and left . its mouse dependent and slow 
            time.sleep(2)
        companies = page.locator("a[href*='/companies/']")
        data = [["Company"]]
        for i in range(companies.count()):
            try:
                name = companies.nth(i).inner_text()
                data.append([name])
            except:
                pass
        browser.close()
    # Save CSV
    with open("yc_data.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print("✅ Data extracted!")
scrape_yc()
