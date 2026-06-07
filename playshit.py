from playwright.sync_api import sync_playwright
def get_companies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # keep False for debugging
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.ycombinator.com/companies/location/india")
        companies = page.locator("span[class='text-2xl']")
        company_names = []
        for i in range(companies.count()):
            name = companies.nth(i).inner_text()
            print(name)
            company_names.append(name)
        print("\n--- Opening each company page ---\n")
        for name in company_names[:5]:  # limit for testing
            page1 = context.new_page()
            url_name = name.lower().replace(" ", "-")
            try:
                page1.goto(f"https://www.ycombinator.com/companies/{url_name}")
                desc = page1.locator("div[id='news']").first.inner_text()
                print(f"{name} -> {desc}")
            except Exception as e:
                print(f"Error with {name}: {e}")
        browser.close()
        print(company_names)
get_companies()
