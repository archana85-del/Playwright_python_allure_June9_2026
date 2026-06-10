
import allure
from playwright.sync_api import Page, expect

class resultsPage:
    def __init__(self, page: Page):
        self.page = page
        # self.addToCartBtn = page.locator("(//span[contains(text(),'iPhone 17 Pro 256 GB')]/ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']//button[@aria-label='Add to cart'])[1]")
        self.addToCartBtn = lambda product: page.locator(f"(//span[contains(text(),'{product}')]/ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']//button[@aria-label='Add to cart'])[1]")
        self.cartCount = page.locator("#nav-cart-count")
        self.firstProduct = page.locator("#a-autoid-3-announce")
        self.productLink = lambda product_name: page.get_by_role("link", name=product_name, exact=True)
        self.resultsHeading = page.get_by_text("Results", exact=True)
        self.sortDropdown = page.locator('[aria-label*="Sort by"]')
        self.sortButton = page.locator('button:has-text("Featured")')
        self.filterButton = page.locator('//div[@aria-label="filters"]')
        self.priceFilter = page.locator('[aria-label*="price"]')
        self.productContainer = page.locator('[data-component-type="s-search-result"]')
        self.productTitle = lambda index: page.locator(f'[data-component-type="s-search-result"] >> nth={index} h2')
        self.productPrice = lambda index: page.locator(f'[data-component-type="s-search-result"] >> nth={index} [data-a-price]')
        self.productRating = lambda index: page.locator(f'[data-component-type="s-search-result"] >> nth={index} .a-star-small span')

    @allure.step("Add item to cart by name")
    def addAnItmeToCart(self, itemName):
        self.addToCartBtn(itemName).click()

    @allure.step("Get current cart count")
    def getCartCount(self):
        return self.cartCount.text_content()
    
    @allure.step("Click on first product in search results")
    def clickOnFirstProduct(self):
        """Click on the first product in search results"""
        self.firstProduct.click()
    
    @allure.step("Click on product by name")
    def clickOnProductByName(self, product_name):
        """Click on a specific product by its name"""
        self.productLink(product_name).click()
    
    @allure.step("Get search results count")
    def getSearchResultsCount(self):
        """Extract and return the search results count from the heading"""
        results_text = self.resultsHeading.first.text_content()
        # Example: "1-16 of over 60,000 results"
        return results_text
    
    @allure.step("Verify search results are displayed")
    def verifySearchResultsDisplayed(self):
        """Verify that search results heading is visible"""
        expect(self.resultsHeading.first).to_be_visible()
    
    @allure.step("Get total products displayed on page")
    def getTotalProductsOnPage(self):
        """Get count of products currently displayed on the page"""
        return self.productContainer.count()
    
    @allure.step("Get product title by index")
    def getProductTitleByIndex(self, index: int):
        """Get product title at specified index"""
        return self.productTitle(index).text_content()
    
    @allure.step("Get product price by index")
    def getProductPriceByIndex(self, index: int):
        """Get product price at specified index"""
        return self.productPrice(index).text_content()
    
    @allure.step("Get product rating by index")
    def getProductRatingByIndex(self, index: int):
        """Get product rating at specified index"""
        return self.productRating(index).text_content()
    
    @allure.step("Sort results by option")
    def sortResultsBy(self, sort_option: str):
        """Click sort dropdown and select sort option"""
        self.sortButton.click()
        self.page.get_by_role("option", name=sort_option).click()
    
    @allure.step("Verify sort dropdown is available")
    def verifySortDropdownAvailable(self):
        """Verify that sort dropdown is visible"""
        expect(self.sortButton).to_be_visible()
    
    @allure.step("Verify cart count is greater than")
    def verifyCartCountGreaterThan(self, count: int):
        """Verify cart count is greater than specified value"""
        current_count = int(self.getCartCount())
        assert current_count > count, f"Expected cart count > {count}, but got {current_count}"
