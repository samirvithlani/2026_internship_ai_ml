from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        #browser object..
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.myntra.com/")
        #wait...
        page.wait_for_timeout(5000)
        title = page.title()
        print("title",title)
        
        #get head <link>
        #get full heade..
        # head = page.content()
        # print(head)
        #get meta tag,,
        # meta = page.meta()
        # print(meta)
        # meta = page.locator("meta").all()
        # print(meta)

        #desktop-navbar class get all l
        
        # desktop_user = page.locator(".desktop-user")
        # print(desktop_user)
        # desktop_user.hover()
        # page.wait_for_timeout(5000)

        #search bar
        #searc_bar = page.locator("input.desktop-search")
        search_bar = page.fill(".desktop-searchBar","shoes")
        print(search_bar)
        #page.wait_for_timeout(5000)
        

        browser.close()
run()        
    