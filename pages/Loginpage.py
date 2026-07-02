from playwright.sync_api import sync_playwright,Page,expect

class loginpage:
    def __init__(self,page:Page):
        self.usernameBox = page.locator("#ap_email_login")
        self.ContinueBox = page.locator("//input[@type='submit']")
        self.passwordBox = page.locator("#ap_password")
        self.signInbox = page.locator("#signInSubmit")
        self.InvalidUser = page.locator("//div[contains(text(),'Invalid email address')]")
        self.InvalidPasswordL = page.locator("//div[contains(text(),'Your password is incorrect')]")
        self.searchAmazonBox = page.locator("//input[@placeholder='Search Amazon.in']")
        self.GoBtn = page.locator("//input[@type='submit']")


    def enterUsername(self,username):
        (self.usernameBox).fill(username)

    def ClickOnContinue(self):
        (self.ContinueBox).click()

    def enterPassword(self,Password):
        (self.passwordBox).fill(Password)

    def ClickOnSignIn(self):
        (self.signInbox).click()

    def ErrorUsernameMsg(self):
        expect(self.InvalidUser).to_be_visible()

    def ErrorPasswordMsg(self):
        expect(self.InvalidPasswordL).to_be_visible()

    def ValidateAmazonSearchBox(self,product):
        self.searchAmazonBox.fill(product)
        
    def clickOnGoBtn(self):
        self.GoBtn.click()
        