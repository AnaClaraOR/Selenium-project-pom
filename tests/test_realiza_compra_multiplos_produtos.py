import pytest
import conftest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage


@pytest.mark.usefixtures("setup_teardown")
class TestCT05:
    def test_ct05_realiza_compra_multiplos_produtos(self):
        mensagem_final_da_compra = "Thank you for your order!"

        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        produto_1 = "Sauce Labs Backpack"
        produto_2 = "Sauce Labs Bolt T-Shirt"

        # Login
        login_page.fazer_login("standard_user", "secret_sauce")

        # Adicionando o primeiro produto ao carrinho
        home_page.adicionar_ao_carrinho(produto_1)

        # Verificando o carrinho
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)

        # Retornando aos produtos
        carrinho_page.clicar_continuar_comprando()

        # Adicionando um novo produto ao carrinho
        home_page.adicionar_ao_carrinho(produto_2)

        # Verificando o carrinho novamente com vários produtos
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)
        carrinho_page.verificar_produto_carrinho_existe(produto_2)

        # Continuidade na compra
        carrinho_page.clicar_continuar_compra()

        # Informa os dados do comprador
        carrinho_page.fazer_compra("Anastacia", "Jaime", "12345678")

        # Valida o resumo de compra
        carrinho_page.verificar_produto_carrinho_existe(produto_1)
        carrinho_page.verificar_produto_carrinho_existe(produto_2)

        # Finaliza a compra
        carrinho_page.finalizar_compra()

        # Verifica o texto da mensagem de erro
        carrinho_page.verificar_texto_mensagem_final_da_compra(mensagem_final_da_compra)
