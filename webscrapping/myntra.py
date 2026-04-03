from playwright.sync_api import sync_playwright
import json

products = []
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.myntra.com/")
    page.wait_for_timeout(5000)
    page.fill(".desktop-searchBar","tshirt")
    page.wait_for_timeout(2000)
    page.keyboard.press("Enter")
    page.wait_for_timeout(5000)
    page.locator("label.gender-label",has_text="Men").first.click()
    page.wait_for_timeout(5000)
    #scroll
    #page.mouse.wheel(0,4000)
    # for i in range(3):
    #     page.mouse.wheel(0,2000)

    #products = page.query_selector_all("li.product-base")
    products = page.query_selector_all(".product-base")
    print("products =",len(products))
    for p in products:
        brand = p.query_selector(".product-brand").inner_text()
        title = p.query_selector(".product-product").inner_text()
        price = p.query_selector(".product-price").query_selector("span").inner_text()
        print(brand,title,price)
        products.append({
            "brand":brand,
            "title":title,
            "price":price
        })
        with open("products.json","w") as f:
            json.dump(products,f,indent=4) 



    nextButton = page.locator("text=Next")
    #ifelse
    if nextButton.count()==0:
        print("no next button")
    else:
        nextButton.click()
        page.wait_for_timeout(5000)

    page.wait_for_timeout(10000)
    browser.close()