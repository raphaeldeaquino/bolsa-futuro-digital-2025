from botao import Botao
from dialogo import Dialogo
from painel import Painel

class Aplicacao:
    def criar_ui(self):
        dialogo = Dialogo(url_pagina_wiki="http://...")
        
        # Painel com dimensões (x, y, largura, altura) — 
        # estes valores são apenas armazenados; nada gráfico é desenhado.
        painel = Painel(texto_modal_ajuda="Este painel faz...")
        painel.x, painel.y, painel.largura, painel.altura = 0, 0, 400, 800

        botao_ok = Botao()
        botao_ok.x, botao_ok.y, botao_ok.largura, botao_ok.altura = 250, 760, 50, 20
        botao_ok.texto_tooltip = "Este é um botão OK que..."

        botao_cancelar = Botao()
        botao_cancelar.x, botao_cancelar.y, botao_cancelar.largura, botao_cancelar.altura = 320, 760, 50, 20

        # Constrói a interface
        painel.adicionar(botao_ok)
        painel.adicionar(botao_cancelar)
        dialogo.adicionar(painel)

        # Guarda como atributo, caso necessário depois
        self.dialogo = dialogo

    def ao_pressionar_f1(self):
        componente = self.obter_componente_nas_coordenadas_do_mouse()
        componente.mostrar_ajuda()

    # Método fictício apenas para manter a estrutura
    def obter_componente_nas_coordenadas_do_mouse(self):
        # Em uma aplicação real, calcularia qual componente está sob o cursor.
        # Aqui retornamos apenas o diálogo principal como exemplo.
        return self.dialogo
