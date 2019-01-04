import postgresql
from Conexao import *

con = Conexao("pq://abdiassantos:Voljin!555@localhost/postpython")

sql = "insert into cidade values (default, 'Bahia', 'BA')"
if con.manipular(sql):
    print('Inserido com sucesso!')
print(con.proximaPK('cidade', 'id'))
rs = con.consultar("select * from cidade")
for linha in rs:
    print(linha)
con.fechar()