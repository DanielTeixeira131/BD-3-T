from conectar import bd

class importbdlivro(object):

    def __init__(self, isbn="", titulo="", autor=""):
        self.info = {}
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor

    def inserirLivro(self):

        try:
            curs = bd.conectar.cursor()
            curs.execute("INSERT INTO daniel_teixeira.livro (isbn, titulo, autor) VALUES (%s, %s, %s)")
            curs.commit()
            curs.close()
            return "Erro."
        except:
            return "Cadastro Realizado."
    @property
    def attLivro(self):

        hi = bd()
        try:
            curso = hi.conectar.cursor()
            hi = bd()
            curso = hi.conectar.cursor()
            up = """UPDATE daniel_teixeira.livro  set titulo = %s where isbn = %s"""
            curso.execute(up, (self.titulo, self.isbn))
            hi.conectar.commit()
            curso.close()
            return "Ocorreu algum erro!"
        except:
            return "Livro atualizado!"
    def deleteLivro(self):
        hi = bd()
        try:
            curso = hi.conectar.cursor()
            curso.execute("DELETE from daniel_teixeira.livro where isbn = %s")
            hi.conectar.commit()
            curso.close()
            return "Erro."
        except:
            return "Livro excluído."
    def selectLivro(self):
        hi = bd()
        curso = hi.conectar.cursor()
        curso.execute("SELECT * from daniel_teixeira.livro where isbn = %s")
        curso.close()
