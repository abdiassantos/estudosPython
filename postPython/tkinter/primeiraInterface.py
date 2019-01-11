from tkinter import *

class Application:
    def __init__(self, master=None):
        
        ##Texto dentro do widget.
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text = 'Primeiro Widget')
        self.msg['font'] = ('Verdana', '10', 'italic', 'bold')
        self.msg.pack()

        ##Botão de sair.
        self.sair = Button(self.widget1)
        self.sair['text'] = 'Clique Aqui'
        self.sair['font'] = ('Calibri', '9')
        self.sair['width'] = 10
        self.sair['command'] = self.mudaTexto
        ## self.sair.bind('<Button-1>', self.mudar) nos parametros passar self e event.
        self.sair.pack()

    def mudaTexto(self):
        if self.msg['text'] == 'Primeiro Widget':
            self.msg['text'] = 'O botão recebeu um clique'
        else:
            self.msg['text'] = 'Primeiro Widget'

root = Tk()
Application(root)
root.mainloop()