#%%
import postgresql as psql
from Conexao import *

con = Conexao("pq://abdiassantos:Voljin!555@localhost/postpython")

opcao = int(2)

if opcao == 1:
    sql = "insert into cidade values (default, 'Bahia', 'BA')"
    if con.manipular(sql):
        print('Inserido com sucesso!')
if opcao == 2:
    sql = "delete from cidade where id = 9"
    if con.manipular(sql):
        print('Deletado com sucesso!')
print(con.proximaPK('cidade', 'id'))
rs = con.consultar("select * from cidade")
for linha in rs:
    print(linha)
con.fechar()