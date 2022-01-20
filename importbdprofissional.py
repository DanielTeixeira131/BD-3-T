from conectar import bd

class imporbdprofissional(object):

    def __init__(self, cpf="", salario=""):
        self.info = {}
        self.salario = salario
        self.cpf = cpf

    def inserirProfissional(self):

        try:
            curs = bd.conectar.cursor()
            curs.execute("INSERT INTO daniel_teixeira.empregado (cpf, salario) VALUES (%s, %s)")
            curs.commit()
            curs.close()
            return "Erro."
        except:
            return "Cadastro Realizado."
    @property
    def attProfissional(self):

        hi = bd()
        try:
            curso = hi.conectar.cursor()
            hi = bd()
            curso = hi.conectar.cursor()
            up = """UPDATE daniel_teixeira.empregado  set salario = %s where cpf = %s"""
            curso.execute(up, (self.salario, self.cpf))
            hi.conectar.commit()
            curso.close()
            return "Erro"
        except:
            return "Profissional atualizado."
    def deleteProfissional(self):
        hi = bd()
        try:
            curso = hi.conectar.cursor()
            curso.execute("DELETE from daniel_teixeira.empregado where cpf = %s")
            hi.conectar.commit()
            curso.close()
            return "Erro."
        except:
            return "Profissional excluído."
    def selectProfissional(self):
        hi = bd()
        curso = hi.conectar.cursor()
        curso.execute("SELECT * from daniel_teixeira.empregado where cpf = %s")
        curso.close()