from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    context = browser.new_context()

    page = browser.new_page()

    page.goto('https://www.baldorfood.com/users/default/new-login')
    page.fill('input#EmailLoginForm_email', '')
    page.fill('input#EmailLoginForm_password', '')
    submit_button = page.get_by_role('button', name='SIGN IN')
    submit_button.click()

    page.wait_for_load_state()
    
    cookies = page.context.cookies()
    context.add_cookies(cookies)

    page.goto('https://www.baldorfood.com/products/fruits/avocados')

    page.wait_for_timeout(10000)

    context.close()
    browser.close()
    

    for cookie in cookies:
        if cookie['name'] == 'PHPSESSID':
            cookie_value = cookie['value']
        else:
            continue
    
    # print(cookie_value)

    for cookie in cookies:
        print(cookie['name'], " : ", cookie['value'])
