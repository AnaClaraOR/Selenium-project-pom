import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class TestCT02:
    def test_ct02_login_invalido(self):
        # Instancia os objetos a serem utilizados nos testes
        login_page = LoginPage()

        # Faz o login
        login_page.fazer_login("standard_user", "12345")

        # Verifica se o login não foi realizado e a mensagem de erro apresentada
        login_page.verificar_mensagem_erro_login()
