from Usuario import Usuarios
from tkinter import *

class Application:
    def __init__(self, master = None):
        ##Declarando a fonte padrão a ser usada.
        self.fonte = ('Verdana', '8')

        ##Declarando todos os containers.
        self.container1 = Frame(master)
        self.container1['pady'] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2['padx'] = 20
        self.container2['pady'] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3['padx'] = 20
        self.container3['pady'] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4['padx'] = 20
        self.container4['pady'] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5['padx'] = 20
        self.container5['pady'] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6['padx'] = 20
        self.container6['pady'] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7['padx'] = 20
        self.container7['pady'] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8['padx'] = 20
        self.container8['pady'] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9['pady'] = 15
        self.container9.pack()

        ##Título do formulário.
        self.titulo = Label(self.container1, text = 'Informe os dados: ')
        self.titulo['font'] = ('Calibri', '9', 'bold')
        self.titulo.pack()

        ##Id do usuário para buscar os dados e botão para buscar.
        self.lblIdUsuario = Label(self.container2, text = 'idUsuario:', font = self.fonte, width = 10)
        self.lblIdUsuario.pack()

        self.txtIdUsuario = Entry(self.container2)
        self.txtIdUsuario['width'] = 10
        self.txtIdUsuario['font'] = self.fonte
        self.txtIdUsuario.pack(side = LEFT)

        self.btnBuscar = Button(self.container2, text = 'Buscar', font = self.fonte, width = 10)
        self.btnBuscar['command'] = self.buscarUsuario
        self.btnBuscar.pack(side = RIGHT)

        ##Nome do usuário buscado ou a cadastrar, editar ou excluir.
        self.lblNome = Label(self.container3, text = 'Nome:', font = self.fonte, width = 10)
        self.lblNome.pack(side = LEFT)

        self.txtNome = Entry(self.container3)
        self.txtNome['width'] = 25
        self.txtNome['font'] = self.fonte
        self.txtNome.pack(side = LEFT)

        ##Telefone do usuário buscado ou a cadastrar, editar ou excluir.
        self.lblTelefone = Label(self.container4, text = 'Telefone:', font = self.fonte, width = 10)
        self.lblTelefone.pack(seide = LEFT)

        self.txtTelefone = Entry(self.container4)
        self.txtTelefone['width'] = 25
        self.txtTelefone['font'] = self.fonte
        self.txtTelefone.pack(side = LEFT)

        ##Email do usuário buscado ou a cadastrar, editar ou excluir

