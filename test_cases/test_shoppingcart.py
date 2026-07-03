from playwright.sync_api import Page,expect
from pages.Resultspage import resultspage
from pages.Loginpage import loginpage
import pytest

@pytest.mark.smoke()
def test_validateShoppingCart(page:Page,LoginTOAmazon,homepageobj):
    loginpageobj = loginpage(page)
    resultspageobj = resultspage(page)
    loginpageobj.ValidateAmazonSearchBox("iphone")
    loginpageobj.clickOnGoBtn() 
    page.wait_for_timeout(3000)
    resultspageobj.ValidateResultsText()
    page.wait_for_timeout(5000)
    title = "Sponsored Ad - iPhone 17e 512 GB: 15.40 cm (6.1″) Super Retina XDR Display, A19 Chip, All-Day Battery Life, 48MP Fusion Camera, 256GB Starting Storage; White"
    resultspageobj.ClickOnAddToCart(title)
    resultspageobj.ClickOnGoToCartBtn()
    page.wait_for_timeout(3000)
