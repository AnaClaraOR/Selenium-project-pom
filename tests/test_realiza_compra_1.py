import pytest
from selenium.webdriver.common.by import By
import conftest


@pytest.mark.usefixtures("setup_teardown")
class TestCT04:
    def test_ct04_realiza_compra_1(self):
        driver = conftest.driver

        # Login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Adicionando o primeiro produto ao carrinho
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

        # Verificando o carrinho
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//*[text()='Sauce Labs Backpack']").is_displayed()

        # Dar continuidade na compra
        driver.find_element(By.ID, "checkout").click()

        # Informa os dados do comprador
        driver.find_element(By.ID, "first-name").send_keys("Ana")
        driver.find_element(By.ID, "last-name").send_keys("Kiss")
        driver.find_element(By.ID, "postal-code").send_keys("12345678")
        driver.find_element(By.ID, "continue").click()

        # Valida o resumo de compra
        assert driver.find_element(By.XPATH, "//*[text()='Sauce Labs Backpack']").is_displayed()

        # Finaliza a compra
        driver.find_element(By.ID, "finish").click()
        assert driver.find_element(By.XPATH, "//*[text()='Thank you for your order!']").is_displayed()
