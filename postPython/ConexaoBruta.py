import postgresql

##Endereço da conexão com o banco de dados.
db = postgresql.open("pq://abdiassantos:Voljin!555@localhost/postpython")

##Criando tabela dentro do banco de dados conectado.
sql = 'create table cidade (id serial primary key, nome varchar(100), uf varchar(2))'
##Executa código SQL passado como parâmetro.
db.execute(sql)

##Realiza inserção de valores dentro da tabela criada, dentro de um bloco TRY, para tratar erro caso aconteça.
sql = "insert into cidade values (default, 'Curitiba', 'PR')"
try:
    db.execute(sql)
except:
    print("Erro!")

##Faz consulta com o parâmetro SQL.
sql = "select * from cidade"
rs = db.prepare(sql)
for linha in rs:
    print(linha)

##Fecha conexão com o banco de dados.
db.close()