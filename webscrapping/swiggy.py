from playwright.sync_api import sync_playwright


with sync_playwright() as p:
        #browser object..
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.swiggy.com/")
        #wait...
    page.wait_for_timeout(5000)
    title = page.title()
    print("title",title)
