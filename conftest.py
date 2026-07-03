from playwright.sync_api import sync_playwright,Page,expect
from pages.Homepage import homepage
from pages.Loginpage import loginpage
import pytest
import json

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
    with open("testdata\crendentials.json") as data :
        testdata = json.load(data)
    loginpageobj.enterUsername(testdata["positiveCrendentials"]["username"])
    loginpageobj.ClickOnContinue()
    loginpageobj.enterPassword(testdata["positiveCrendentials"]["password"])
    loginpageobj.ClickOnSignIn()

@pytest.fixture()
def homepageobj(page):
    homepageobj = homepage(page)
    return homepageobj