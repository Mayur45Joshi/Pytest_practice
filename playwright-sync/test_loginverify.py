from playwright.sync_api import Page , expect

def test_login(page:Page):
    page.goto("http://www.automationpractice.pl/index.php")
    page_url=page.url
    print(page_url)
    expect(page).to_have_url("http://www.automationpractice.pl/index.php")

def test_verifytitle(page:Page):
    page.goto("http://www.automationpractice.pl/index.php")
    page_title=page.title()
    print(page_title)
    expect(page).to_have_title("My Shop")