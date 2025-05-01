import pytest
import conftest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class TestCT02:
    def test_ct02_login_invalido(self):
        driver = conftest.driver
        login_page = LoginPage()

        login_page.fazer_login("standard_user", "12345")

        assert len(driver.find_elements(By.XPATH, "//span[@class='title']")) == 0
