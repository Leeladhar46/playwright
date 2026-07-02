from playwright.sync_api import sync_playwright,Page,expect
from pages.Homepage import homepage
from pages.Loginpage import loginpage
import pytest

def test_ValidateLoginPage(page:Page):
    page.goto("https://www.amazon.in/")
    homepageobj = homepage(page)
    homepageobj.validateSignInExpander()
    homepageobj.ClickSIgnInBtn()
    loginpageobj = loginpage(page)
    loginpageobj.enterUsername("trainingplaywright@gmail.com")
    loginpageobj.ClickOnContinue()
    loginpageobj.enterPassword("Welcome@04")
    loginpageobj.ClickOnSignIn()

def test_InvalidateUsername(page:Page):
    page.goto("https://www.amazon.in/")
    homepageobj = homepage(page)
    homepageobj.validateSignInExpander()
    homepageobj.ClickSIgnInBtn()
    loginpageobj = loginpage(page)
    loginpageobj.enterUsername("trainingplaywright")
    loginpageobj.ClickOnContinue()
    loginpageobj.ErrorUsernameMsg()
    
def test_InvalidatePassword(page:Page):
    page.goto("https://www.amazon.in/")
    homepageobj = homepage(page)
    homepageobj.validateSignInExpander()
    homepageobj.ClickSIgnInBtn()
    loginpageobj = loginpage(page)
    loginpageobj.enterUsername("trainingplaywright@gmail.com")
    loginpageobj.ClickOnContinue()
    loginpageobj.enterPassword("Welcome@041")
    loginpageobj.ClickOnSignIn()
    loginpageobj.ErrorPasswordMsg()