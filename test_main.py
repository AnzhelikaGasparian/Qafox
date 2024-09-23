import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature('Menu Navigation')
@allure.suite('UI Tests')
@allure.title('Test Menu Item Navigation')
@allure.description('Verifies that each menu item on the homepage navigates to the correct page and displays the correct heading.')
@allure.severity(allure.severity_level.CRITICAL)
def test_menu_item(driver):

    with allure.step("Opening the homepage"):
        driver.get("https://tutorialsninja.com/demo/")


    expected_menu_items = ["Desktops", "Laptops & Notebooks", "Components", "Tablets", "Software", "Phones & PDAs",  "Cameras", "MP3 Players"]

    with allure.step(f"Clicking on menu item: {expected_menu_items[0]}"):
        menu_item1 = driver.find_element(By.LINK_TEXT, expected_menu_items[0])
        menu_item1.click()

    with allure.step(f"Clicking on menu item: {expected_menu_items[1]}"):
        menu_item2 = driver.find_element(By.LINK_TEXT, expected_menu_items[1])
        menu_item2.click()

    with allure.step(f"Clicking on menu item: {expected_menu_items[2]}"):
        menu_item3 = driver.find_element(By.LINK_TEXT, expected_menu_items[2])
        menu_item3.click()

    with allure.step(f"Clicking on menu item: {expected_menu_items[3]}"):
        menu_item4 = driver.find_element(By.LINK_TEXT, expected_menu_items[3])
        menu_item4.click()

    with allure.step(f"Verifying the page heading for {expected_menu_items[3]}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[3], 'Page heading does not match menu item'

    with allure.step(f"Clicking on menu item: {expected_menu_items[4]}"):
        menu_item5 = driver.find_element(By.LINK_TEXT, expected_menu_items[4])
        menu_item5.click()

    with allure.step(f"Verifying the page heading for {expected_menu_items[4]}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[4], 'Page heading does not match menu item'

    with allure.step(f"Clicking on menu item: {expected_menu_items[5]}"):
        menu_item6 = driver.find_element(By.LINK_TEXT, expected_menu_items[5])
        menu_item6.click()

    with allure.step(f"Verifying the page heading for {expected_menu_items[5]}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[5], 'Page heading does not match menu item'

    with allure.step(f"Clicking on menu item: {expected_menu_items[6]}"):
        menu_item7 = driver.find_element(By.LINK_TEXT, expected_menu_items[6])
        menu_item7.click()

    with allure.step(f"Verifying the page heading for {expected_menu_items[6]}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[6], 'Page heading does not match menu item'

    with allure.step(f"Clicking on menu item: {expected_menu_items[7]}"):
        menu_item8 = driver.find_element(By.LINK_TEXT, expected_menu_items[7])
        menu_item8.click()


@pytest.mark.parametrize("menu_locator, submenu_locator, result_text", [
    (
            (By.PARTIAL_LINK_TEXT, 'Desktops'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[1]/a'),
            'PC'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Desktops'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a'),
            'Mac'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Laptops & Notebooks'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[1]/a'),
            'Macs'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Laptops & Notebooks'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[2]/a'),
            'Windows'
    )
])

@allure.feature('Menu Navigation')
@allure.suite('UI Tests')
@allure.title('Test Nested Menu Navigation')
@allure.description('Verifies the functionality of nested menu navigation.')
@allure.severity(allure.severity_level.CRITICAL)
def test_nested_menu(driver, menu_locator, submenu_locator, result_text):
    with allure.step("Opening the homepage"):
        driver.get("https://tutorialsninja.com/demo/")
    with allure.step('Locating the menu'):
        menu = driver.find_element(*menu_locator)
    with allure.step('Locating the submenu'):
        submenu = driver.find_element(*submenu_locator)
    with allure.step('Hovering over the menu and clicking submenu'):
        ActionChains(driver).move_to_element(menu).click(submenu).perform()
    with allure.step('Verifying the submenu result text'):
        assert driver.find_element(By.TAG_NAME, 'h2').text == result_text, 'Submenu navigation failed'


@allure.feature('Search Functionality')
@allure.suite('UI Tests')
@allure.title('Test Product Search Functionality')
@allure.description('Verifies the search functionality by searching for a specific product.')
@allure.severity(allure.severity_level.CRITICAL)
def test_search_product(driver):
    with allure.step('Opening the homepage'):
        driver.get("https://tutorialsninja.com/demo/")
    with allure.step('Locating the search bar'):
        search = driver.find_element(By.NAME, 'search')
    with allure.step('Entering search query'):
        search.send_keys('MacBook')
    with allure.step('Clicking search button'):
        button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.btn-lg')
    with allure.step('Submitting search'):
        button.click()

    with allure.step('Collecting search results'):
        products = driver.find_elements(By.TAG_NAME, 'h4')
    with allure.step('Filtering search results'):
        new_list = [elem.text for elem in products if 'MacBook' in elem.text]
    with allure.step('Verifying search results match query'):
        assert len(products) == len(new_list), 'Some products in the results do not match the search term'


@allure.feature('Add to Cart Functionality')
@allure.suite('UI Tests')
@allure.title('Test Add to Cart Functionality')
@allure.description('Verifies the functionality of adding products to the shopping cart.')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart(driver):
    with allure.step('Opening the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Locating the first product and adding to cart'):
        product = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[1]')
        product.click()

    with allure.step('Verifying success message'):
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success"))
        )
    with allure.step('Asserting success message'):
        assert "Success: You have added" in success_message.text, 'Add to cart failed'

    with allure.step('Verifying cart item count'):
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "cart-total"), "1 item(s)")
        )

    with allure.step('Opening cart'):
        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "cart"))
        )
        cart_button.click()

    with allure.step('Verifying cart contents'):
        cart_contents = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.dropdown-menu.pull-right"))
        )

    with allure.step('Asserting product in cart'):
        assert "MacBook" in cart_contents.text, "Expected 'MacBook' in cart, but got different contents"


@allure.feature('Menu Navigation')
@allure.suite('UI Tests')
@allure.title('Slider Functionality Test')
@allure.description('Verifies that the slider functionality works correctly by moving to the next and previous images.')
@allure.severity(allure.severity_level.NORMAL)
def test_slider_functionality(driver):
    with allure.step('Opening the homepage'):
        driver.get("https://tutorialsninja.com/demo/")
    with allure.step('Locating the slider element'):
        slider = driver.find_element(By.CLASS_NAME, 'swiper-container')
    with allure.step('Verifying the slider is displayed'):
        assert slider.is_displayed(), "Slider is not visible on the page."

    with allure.step('Getting the first slide image'):
        first_slide = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img")
    with allure.step('Getting the source of the first slide'):
        first_slide_src = first_slide.get_attribute("src")

    with allure.step('Locating the next arrow'):
        next_arrow = driver.find_element(By.CLASS_NAME, 'swiper-button-next')
    with allure.step('Clicking the next arrow'):
        ActionChains(driver).move_to_element(slider).click(next_arrow).perform()

    with allure.step('Waiting for the next slide to be active'):
        WebDriverWait(driver, 10).until_not(
            EC.element_to_be_clickable(first_slide)
        )

    with allure.step('Getting the new active slide image'):
        new_slide = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img")
    with allure.step('Getting the source of the new slide'):
        new_slide_src = new_slide.get_attribute("src")

    with allure.step('Verifying the slider moved to the next image'):
        assert first_slide_src != new_slide_src, "Slider did not move to the next image."

    with allure.step('Locating the previous arrow'):
        prev_arrow = driver.find_element(By.CLASS_NAME, 'swiper-button-prev')
        prev_arrow.click()

    with allure.step('Waiting for the previous slide to be active'):
        WebDriverWait(driver, 10).until_not(
            EC.element_to_be_clickable(new_slide)
        )

    with allure.step('Getting the reverted slide image'):
        reverted_slide_src = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img").get_attribute("src")

    with allure.step('Verifying the slider returned to the first image'):
        assert reverted_slide_src == first_slide_src, "Slider did not return to the first image."


@allure.feature('Menu Navigation')
@allure.suite('UI Tests')
@allure.title('Add to Wishlist Test')
@allure.description('Verifies that a product can be added to the wishlist successfully.')
@allure.severity(allure.severity_level.NORMAL)
def test_add_to_wishlist(driver, login):
    with allure.step('Opening the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Locating the wishlist button'):
        wishlist_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[2]'))
        )

    with allure.step('Clicking the wishlist button'):
        wishlist_button.click()

    with allure.step('Waiting for the success message'):
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success"))
        )

    with allure.step('Verifying the success message'):
        assert "Success: You have added" in success_message.text, "Wishlist add failed"

    with allure.step('Locating the wishlist link'):
        wishlist_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="wishlist-total"]'))
        )
    with allure.step('Clicking the wishlist link'):
        wishlist_link.click()

    with allure.step('Waiting for wishlist contents to be visible'):
        wishlist_contents = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/table/tbody/tr[2]/td[2]/a'))
        )

    with allure.step('Verifying the product is in the wishlist'):
        assert "MacBook" in wishlist_contents.text, "MacBook not found in wishlist"


@pytest.mark.parametrize("button, header, expected_text", [
    (
        (By.XPATH, '/html/body/footer/div/div/div[1]/ul/li[1]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "About Us"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[2]/ul/li[1]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Contact Us"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[2]/ul/li[2]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Product Returns"
    ),
    (
        (By.XPATH, "/html/body/footer/div/div/div[3]/ul/li[1]/a"),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Find Your Favorite Brand"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[3]/ul/li[2]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Purchase a Gift Certificate"
    )
])

@allure.feature('Menu Navigation')
@allure.suite('UI Tests')
@allure.title('Footer Links Test')
@allure.description('Verifies that footer links navigate to the correct pages.')
@allure.severity(allure.severity_level.NORMAL)
def test_footer(driver, button, header, expected_text):
    with allure.step('Opening the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Locating the footer button'):
        footer_button = driver.find_element(*button)
        footer_button.click()

    with allure.step('Getting the header text of the new page'):
        footer_header_text = driver.find_element(*header).text
    with allure.step('Verifying the header text'):
        assert footer_header_text == expected_text, f"Expected '{expected_text}' but got '{footer_header_text}'"

