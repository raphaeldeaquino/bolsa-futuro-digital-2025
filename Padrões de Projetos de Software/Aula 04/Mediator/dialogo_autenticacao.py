from botao import Botao
from caixa_selecao import CaixaSelecao
from caixa_texto import CaixaTexto
from mediador import Mediador

class DialogoAutenticacao(Mediador):
    """
    A classe mediadora concreta.

    A rede entrelaçada de conexões entre componentes individuais
    foi desentrelaçada e movida para dentro do mediador.
    """

    def __init__(self):
        """
        Cria todos os objetos componentes e passa o atual mediador
        em seus construtores para estabelecer links.
        """
        self.titulo = ""

        self.caixa_login_ou_registro = CaixaSelecao(self)

        self.usuario_login = CaixaTexto(self)
        self.senha_login = CaixaTexto(self)

        self.usuario_registro = CaixaTexto(self)
        self.senha_registro = CaixaTexto(self)
        self.email_registro = CaixaTexto(self)

        self.botao_ok = Botao(self)
        self.botao_cancelar = Botao(self)

    def notificar(self, remetente, evento):
        """
        Quando algo acontece com um componente, ele notifica o mediador.
        Ao receber a notificação, o mediador pode fazer alguma coisa por
        conta própria ou passar o pedido para outro componente.
        """

        # Evento do checkbox: alternar entre Login e Registro
        if remetente == self.caixa_login_ou_registro and evento == "marcar":
            if self.caixa_login_ou_registro.marcado:
                self.titulo = "Login"
                """
                1. Mostra componentes de formulário de login.
                2. Esconde componentes de formulário de registro.
                """
            else:
                self.titulo = "Registro"
                """
                1. Mostra componentes de formulário de registro.
                2. Esconde componentes de formulário de login.
                """

        # Evento do botão OK
        if remetente == self.botao_ok and evento == "clicar":
            if self.caixa_login_ou_registro.marcado:
                """
                Tenta encontrar um usuário usando as credenciais de login.
                """
                encontrado = False  # simula busca

                if not encontrado:
                    """
                    Mostra uma mensagem de erro acima do campo login.
                    """
            else:
                """
                1. Cria uma conta de usuário usando dados dos campos de registro.
                2. Loga aquele usuário.
                """
                pass