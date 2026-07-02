from playwright.sync_api import sync_playwright,Page,expect
from pages.Homepage import homepage
from pages.Loginpage import loginpage
import pytest

def page():
    with sync_playwright() as p :
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page

@pytest.fixture()
def LoginTOAmazon(page):
    page.goto("https://www.amazon.in/")
    homepageobj = homepage(page)
    homepageobj.validateSignInExpander()
    homepageobj.ClickSIgnInBtn()
    loginpageobj = loginpage(page)
    loginpageobj.enterUsername("trainingplaywright@gmail.com")
    loginpageobj.ClickOnContinue()
    loginpageobj.enterPassword("Welcome@04")
    loginpageobj.ClickOnSignIn()