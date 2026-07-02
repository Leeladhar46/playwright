from playwright.sync_api import sync_playwright,Page,expect

class homepage:
    def __init__(self,page):
        self.searchBoxLocator = page.locator("//input[@type='text']")
        self.logoButton = page.locator("//a[@id='nav-logo-sprites']")
        self.languageBTn = page.locator("//div[text()='EN']")
        self.ordersBtn = page.locator("#nav-orders")
        self.cartBtn = page.locator("//span[@class='nav-cart-icon nav-sprite']")
        self.signinBtn = page.locator("//span[contains(text(),'Account & Lists')]")
        self.ExpanderBtn = page.locator("//button[@aria-label='Expand Account and Lists']")
        self.SignInBtnLocator = page.locator("//span[@class='nav-action-inner']")

    def val_SearchBox(self):
        expect(self.searchBoxLocator).to_be_visible()

    def val_LogoBtn(self):
        expect(self.logoButton).to_be_visible()

    def val_LangBtn(self):
        expect(self.languageBTn).to_be_visible()

    def val_OrdersBtn(self):
        expect(self.ordersBtn).to_be_visible()

    def val_CartBtn(self):
        expect(self.cartBtn).to_be_visible()

    def val_SignInBtn(self):
        expect(self.signinBtn).to_be_visible()
    
    def validateSignInExpander(self):
        (self.ExpanderBtn).hover()

    def ClickSIgnInBtn(self):
        (self.SignInBtnLocator).click()