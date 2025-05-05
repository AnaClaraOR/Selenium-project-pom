import conftest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CarrinhoPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.botao_continuar_comprando = (By.ID, "continue-shopping")
        self.botao_continua_compra = (By.ID, "checkout")
        self.primeiro_nome_field = (By.ID, "first-name")
        self.sobrenome_field = (By.ID, "last-name")
        self.cep_field = (By.ID, "postal-code")
        self.botao_continuar = (By.ID, "continue")
        self.botao_finalizar_compra = (By.ID, "finish")
        self.msg_fim_de_compra = (By.XPATH, "//*[@data-test='complete-header']")
        # Busca de item utilizando o contains
        self.item_inventario = (By.XPATH, "//*[contains(@class, 'inventory_item_name') and text()='{}']")


    def verificar_produto_carrinho_existe(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.verificar_se_elemento_existe(item)

    def clicar_continuar_comprando(self):
        self.clicar(self.botao_continuar_comprando)

    # Implementação Clara
    def clicar_continuar_compra(self):
        self.clicar(self.botao_continua_compra)

    def fazer_compra(self, nome, sobrenome, cep):
        self.escrever(self.primeiro_nome_field, nome)
        self.escrever(self.sobrenome_field, sobrenome)
        self.escrever(self.cep_field, cep)
        self.clicar(self.botao_continuar)

    def finalizar_compra(self):
        self.clicar(self.botao_finalizar_compra)

    def verificar_texto_mensagem_final_da_compra(self, msg_esperado):
        msg_encontrado = self.pegar_texto_elemento(self.msg_fim_de_compra)
        assert msg_encontrado == msg_esperado, f"O texto encontrado foi '{msg_encontrado}', mas era esperado o texto '{msg_esperado}'."