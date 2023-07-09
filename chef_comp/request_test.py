from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto('https://www.baldorfood.com/users/default/new-login')
    page.fill('input#EmailLoginForm_email', '')
    page.fill('input#EmailLoginForm_password', '')
    page.click('input[type=submit]')
    page.goto('https://www.baldorfood.com/products/fruits/avocados')
    cookies = page.context.cookies()

    for cookie in cookies:
        if cookie['name'] == 'PHPSESSID':
            cookie_value = cookie['value']
        else:
            continue
    
    print(cookie_value)

