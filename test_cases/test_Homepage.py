from playwright.sync_api import sync_playwright,Page,expect
from pages.Homepage import homepage
import pytest



def test_validateTheHomePage(page:Page):
    page.goto("https://www.amazon.in/")
    title = page.title()
    page.wait_for_timeout(10000)
    expect(page).to_have_title("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
    print(title)

    homepageobj = homepage(page)
    homepageobj.val_SearchBox()
    homepageobj.val_LogoBtn()
    homepageobj.val_LangBtn()
    homepageobj.val_OrdersBtn()
    homepageobj.val_CartBtn()
    homepageobj.val_SignInBtn()
    homepageobj.validateSignInExpander()
    homepageobj.ClickSIgnInBtn()