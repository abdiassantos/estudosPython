from tkinter import *

class Application:
    def __init__(self, master = None):
        ##Criando os containers onde ficarão os widgets da aplicação.
        ##Primeiro.
        self.fontePadrao = ('Arial', '10')
        self.primeiroContainer = Frame(master)
        self.primeiroContainer['pady'] = 10
        self.primeiroContainer.pack()
        ##Segundo.
        self.segundoContainer = Frame(master)
        self.segundoContainer['padx'] = 20
        self.segundoContainer.pack()
        ##Terceiro.
        self.terceiroContainer = Frame(master)
        self.terceiroContainer['padx'] = 20
        self.terceiroContainer.pack()
        ##Quarto
        self.quartoContainer = Frame(master)
        self.quartoContainer['pady'] = 20
        self.quartoContainer.pack()

        ##Inserindo título no primeiro container.
        self.titulo = Label(self.primeiroContainer, text = 'Dados do Usuário')
        self.titulo['font'] = ('Arial', '10', 'bold')
        self.titulo.pack()

        ##Inserindo nome de usuário no segundo container.
        self.nomeLabel = Label(self.segundoContainer, text = 'Nome', font = self.fontePadrao)
        self.nomeLabel.pack(side = LEFT)
        
        self.nome = Entry(self.segundoContainer)
        self.nome['width'] = 30
        self.nome['font'] = self.fontePadrao
        self.nome.pack(side = LEFT)

        ##Inserindo senha do usuário no terceiro container.
        self.senhaLabel = Label(self.terceiroContainer, text = 'Senha', font = self.fontePadrao)
        self.senhaLabel.pack(side = LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha['width'] = 30
        self.senha['font'] = self.fontePadrao
        self.senha['show'] = '*'
        self.senha.pack(side = LEFT)

        ##Inserindo botão para autenticar no quarto container e texto de sucesso ou falha da autenticação.
        self.autenticar = Button(self.quartoContainer)
        self.autenticar['text'] = 'Autenticar'
        self.autenticar['font'] = ('Calibri', '8')
        self.autenticar['width'] = 12
        self.autenticar['command'] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text = '', font = self.fontePadrao)
        self.mensagem.pack()

    ##Método que verifica senha e autentica.
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()

        if usuario == 'admin.sistema' and senha == 'adminsistema':
            self.mensagem['text'] = 'Autenticado'
        else:
            self.mensagem['text'] = 'Erro na Autenticação'

root = Tk()
Application(root)
root.mainloop()



