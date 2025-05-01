import pytest
from selenium import webdriver

driver: webdriver.Remote


@pytest.fixture
def setup_teardown():
    # setup
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://saucedemo.com")

    # run test
    yield

    # teardown
    driver.quit()
