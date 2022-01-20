from conectar import bd

class imporbdcliente(object):

    def __init__(self, cpf="", nome="", hdc="", qdc=""):
        self.info = {}
        self.cpf = cpf
        self.nome = nome
        self.hdc = hdc
        self.qdc = qdc

    def inserirCliente(self):

        try:
            curs = bd.conectar.cursor()
            curs.execute("INSERT INTO daniel_teixeira.cliente (cpf, nome, hdc, qdc) VALUES (%s, %s, %s, %s)")
            curs.commit()
            curs.close()
            return "Erro."
        except:
            return "Cadastro Realizado."
    @property
    def attCliente(self):

        hi = bd()
        try:
            curso = hi.conectar.cursor()
            hi = bd()
            curso = hi.conectar.cursor()
            up = """UPDATE daniel_teixeira.cliente  set nome = %s where cpf = %s"""
            curso.execute(up, (self.nome, self.cpf))
            hi.conectar.commit()
            curso.close()
            return "Ocorreu algum erro!"
        except:
            return "cliente atualizado!"
    def deleteCliente(self):
        hi = bd()
        try:
            curso = hi.conectar.cursor()
            curso.execute("DELETE from daniel_teixeira.cliente where cpf = %s")
            hi.conectar.commit()
            curso.close()
            return "Erro."
        except:
            return "Cliente excluído."
    def selectCliente(self):
        hi = bd()
        curso = hi.conectar.cursor()
        curso.execute("SELECT * from daniel_teixeira.cliente where cpf = %s")
        curso.close()
