from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.google.com")
        print(f"Page title: {page.title()}")
        browser.close()

if __name__ == "__main__":
    run()
