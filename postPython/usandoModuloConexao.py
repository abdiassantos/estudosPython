from moduloConexao import Conexao 

con=Conexao('localhost', 'postpython', 'postgres', 'Voljin!555')

sql = "insert into cidade values (default, 'Rio de Janeiro', 'RJ')"

if con.manipular(sql):
    print('Inserido com sucesso')

print(con.proximaPK('cidade', 'id'))
rs = con.consultar("select * from cidade")

for linha in rs:
    print(linha)
con.fechar()
