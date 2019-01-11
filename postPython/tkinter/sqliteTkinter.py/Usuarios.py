from Banco import Banco

class Usuarios(object):

    def __init__(self, idusuario = 0, nome = '', telefone = '', email = '', usuario = '', senha = ''):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    ##Método para inserir usuário na tabela
    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("insert into usuarios (nome, telefone, email, usuario, senha) values ('" + self.nome + "', '" + self.telefone + "', '" + self.email + "', '" + self.usuario + "', '" + self.senha + "' )") 

            banco.conexao.commit()
            c.close()

            return 'Usuário cadastrado com sucesso!'
        except:
            return 'Ocorreu um erro na inserção do usuário!'

    ##Método para atualizar usuário no banco.
    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("update usuarios set nome = '" + self.nome + "', telefone = '" + self.telefone + "', email = '" + self.email + "', usuario = '" + self.usuario + "', senha = '" + self.senha + "' where idusuario = " + self.idusuario + " ")
  
            banco.conexao.commit()
            c.close()

            return 'Usuário atualizado com sucesso!'
        except:
            return 'Ocorreu um erro na alteração do usuário!'

    ##Método para deletar usuario no banco.
    def deleteUser(self):
        banco = Banco()
        try:
            c = banco.coenxao.cursor()

            c.execute('delete from usuarios where idusuario = ' + self.idusuario + ' ')

            banco.conexao.commit()
            c.close()

            return 'Usuário excluído com sucesso!'

        except:
            return 'Ocorreu um erro na eclusão do usuário'

    ##Método para selecionar um usuario no banco.
    def selectUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute('select * from usuarios where idusuario = ' + idusuario + ' ')

            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()

            return 'Busca feita com sucesso!'

        except:
            return 'Ocorreu um erro na busca do usuário'