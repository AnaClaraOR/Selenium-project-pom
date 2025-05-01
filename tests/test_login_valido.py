import pytest
import conftest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_ct01_login_valido(self):
        driver = conftest.driver
        login_page = LoginPage()

        login_page.fazer_login("standard_user", "secret_sauce")

        assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()
