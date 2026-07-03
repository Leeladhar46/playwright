from playwright.sync_api import Page,expect

class resultspage:
    def __init__(self,page:Page):
        self.ResultsText = page.locator("//h2[text()='Results']")
        self.ProductLink = lambda title :page.locator(f"//h2[@aria-label='{title}']//ancestor::div[@data-cy='title-recipe']//following-sibling::div[@class='puisg-row puis-desktop-list-row']//following-sibling::button[@aria-label='Add to cart']")
        self.GoToCartBtn = page.locator("//a[contains(text(),'Go to Cart')]")

    def ValidateResultsText(self):
        expect(self.ResultsText).to_be_visible()

    def ClickOnAddToCart(self,title):
        self.ProductLink(title).click()

    def ClickOnGoToCartBtn(self):
        self.GoToCartBtn.click()
