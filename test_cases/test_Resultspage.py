from playwright.sync_api import expect,Page
from pages.Homepage import homepage
from pages.Loginpage import loginpage
import pytest

@pytest.mark.smoke()
def test_ValidateResultsPage(page:Page,LoginTOAmazon):
    loginpageobj = loginpage(page)
    loginpageobj.ValidateAmazonSearchBox("iphone")
    loginpageobj.clickOnGoBtn() 
    page.wait_for_timeout(5000)