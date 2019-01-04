import postgresql

class Conexao(object):
    _db=None;
    
    def __init__(self, banco):
        self._db = postgresql.open(banco)
    
    def manipular(self, sql):
        try:
            self._db.execute(sql)
        except:
            return False;
        return True;

    def consultar(self, sql):
        rs=None
        try:
            rs=self._db.prepare(sql)
        except:
            return None
        return rs

    def proximaPK(self, tabela, chave):
        sql = 'select max('+chave+') from '+tabela
        rs = self.consultar(sql)
        pk = rs.first()
        return pk+1

    def fechar(self):
        self._db.close()