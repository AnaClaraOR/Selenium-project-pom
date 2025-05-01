import pytest
import conftest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
class TestCT03:
    def test_ct03_adicionar_produtos_carrinho(self):
        driver = conftest.driver
        login_page = LoginPage()

        # Login
        login_page.fazer_login("standard_user", "secret_sauce")

        # Adicionando o primeiro produto ao carrinho
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

        # Verificando o carrinho
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//*[text()='Sauce Labs Backpack']").is_displayed()

        # Retornando aos produtos
        driver.find_element(By.ID, "continue-shopping").click()

        # Adicionando um novo produto ao carrinho
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Bolt T-Shirt']").click()
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

        # Verificando o carrinho novamente com vários produtos
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//*[text()='Sauce Labs Backpack']").is_displayed()
        assert driver.find_element(By.XPATH, "//*[text()='Sauce Labs Bolt T-Shirt']").is_displayed()
