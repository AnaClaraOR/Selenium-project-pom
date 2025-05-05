import pytest

from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class TestCT04:
    def test_ct04_realiza_compra_1(self):
        mensagem_final_da_compra = "Thank you for your order!"

        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        produto_1 = "Sauce Labs Backpack"

        # Login
        login_page.fazer_login("standard_user", "secret_sauce")

        # Adicionando o primeiro produto ao carrinho
        home_page.adicionar_ao_carrinho(produto_1)

        # Verificando o carrinho
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)

        # Dar continuidade na compra
        carrinho_page.clicar_continuar_compra()

        # Informa os dados do comprador
        carrinho_page.fazer_compra("Ana", "Kiss", "12345678")

        # Valida o resumo de compra
        carrinho_page.verificar_produto_carrinho_existe(produto_1)

        # Finaliza a compra
        carrinho_page.finalizar_compra()

        # Verifica o texto da mensagem de erro
        carrinho_page.verificar_texto_mensagem_final_da_compra(mensagem_final_da_compra)
