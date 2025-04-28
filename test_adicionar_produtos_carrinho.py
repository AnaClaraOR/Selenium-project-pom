from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://saucedemo.com")

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

# Retornando aos produtos
driver.find_element(By.ID, "continue-shopping").click()

# Adicionando um novo produto ao carrinho
driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Bolt T-Shirt']").click()
driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

# Verificando o carrinho novamente com vários produtos
driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
assert driver.find_element(By.XPATH, "//*[text()='Sauce Labs Backpack']").is_displayed()
assert driver.find_element(By.XPATH, "//*[text()='Sauce Labs Bolt T-Shirt']").is_displayed()
