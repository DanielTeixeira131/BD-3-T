from tkinter import *
from importbdlivro import importbdlivro
class Livro:
    if __name__ == "__main__":
        def __init__(self, master=None):
            self.fonte = ("Arial", "10")
            self.first = Frame(master)
            self.first["pady"] = 10
            self.first.pack()

            self.second = Frame(master)
            self.second["padx"] = 20
            self.second.pack()

            self.third = Frame(master)
            self.third["padx"] = 20
            self.third.pack()

            self.fourth = Frame(master)
            self.fourth["padx"] = 20
            self.fourth.pack()

            self.fifth = Frame(master)
            self.fifth["padx"] = 20
            self.fifth.pack()

            self.sixth = Frame(master)
            self.sixth["padx"] = 20
            self.sixth.pack()

            self.seventh = Frame(master)
            self.seventh["padx"] = 20
            self.seventh.pack()

            self.eighth = Frame(master)
            self.eighth["padx"] = 20
            self.eighth.pack()

            self.ninth = Frame(master)
            self.ninth["padx"] = 20
            self.ninth.pack()

            self.tenth = Frame(master)
            self.tenth["padx"] = 20
            self.tenth["pady"] = 20
            self.tenth.pack()

            self.ponto = Frame(master)
            self.ponto["pady"] = 20
            self.ponto.pack()

            self.titul = Label(self.first, text="                Dados do Livro")
            self.titul["font"] = ("Arial", "10", "bold")
            self.titul.pack()

            self.titulo1 = Label(self.third, text="Título         ", font=self.fonte)
            self.titulo1.pack(side=LEFT)
            self.titulo1 = Entry(self.third)
            self.titulo1["width"] = 30
            self.titulo1["font"] = self.fonte
            self.titulo1.pack(side=LEFT)

            self.autor1 = Label(self.sixth, text="Autor         ", font=self.fonte)
            self.autor1.pack(side=LEFT)
            self.autor1 = Entry(self.sixth)
            self.autor1["width"] = 30
            self.autor1["font"] = self.fonte
            self.autor1.pack(side=LEFT)



            self.isbn1 = Label(self.second, text="ISBN          ", font=self.fonte)
            self.isbn1.pack(side=LEFT)
            self.isbn1 = Entry(self.second)
            self.isbn1["width"] = 30
            self.isbn1["font"] = self.fonte
            self.isbn1.pack(side=LEFT)

            self.inserir = Button(self.tenth)
            self.inserir["text"] = "Excluir"
            self.inserir["font"] = ("Arial", "10")
            self.inserir["width"] = 30
            self.inserir["command"] = self.excluirLivro
            self.inserir.pack()

            self.inserir = Button(self.tenth)
            self.inserir["text"] = "Cadastrar"
            self.inserir["font"] = ("Arial", "10")
            self.inserir["width"] = 30
            self.inserir["command"] = self.InserLivro
            self.inserir.pack()

            self.inserir = Button(self.tenth)
            self.inserir["text"] = "Buscar"
            self.inserir["font"] = ("Arial", "10")
            self.inserir["width"] = 30
            self.inserir["command"] = self.buscarLivro
            self.inserir.pack()

            self.sair = Button(self.tenth)
            self.sair["text"] = "Sair"
            self.sair["font"] = ("Arial", "10")
            self.sair["width"] = 30
            self.sair["command"] = self.tenth.quit
            self.sair.pack()

            from conectar import bd

            class importbdlivro(object):

                def __init__(self, titulo="", isbn=""):
                    self.info = {}
                    self.isbn = isbn
                    self.titulo = titulo

                def inserirLivro(self):

                    try:
                        curs = bd.conectar.cursor()
                        curs.execute("INSERT INTO daniel_teixeira.livro (titulo, autor, isbn) VALUES (%s, &s, %s)")
                        curs.commit()
                        curs.close()
                        return "Ocorreu um erro no cadastro!"
                    except:
                        return "Livro cadastrado."

                @property
                def attLivro(self):

                    hi = bd()
                    try:
                        curso = hi.conectar.cursor()
                        hi = bd()
                        curso = hi.conectar.cursor()
                        up = """Update daniel_teixeira.livro set titulo = %s where isbn = %s"""
                        curso.execute(up, (self.titulo, self.isbn))
                        hi.conectar.commit()
                        curso.close()
                        return "Erro."
                    except:
                        return "Livro atualizado."

                def deleteLivro(self):
                    hi = bd()
                    try:
                        curso = hi.conectar.cursor()
                        curso.execute("DELETE from daniel_teixeira.livro where isbn = %s")
                        hi.conectar.commit()
                        curso.close()
                        return "Ocorreu um erro!"
                    except:
                        return "Livro excluído."

                    hi = bd()
                    curso = hi.conectar.cursor()
                    curso.execute("SELECT * from daniel_teixeira.livro where isbn = %s")
                    curso.close()

            self.teste = Label(self.ponto, text="")
            self.teste.pack()

    def InserLivro(self):
        use = importbdlivro()
        use.titulo = self.titulo1.get()
        self.titulo1.delete(0, END)

        use.isbn = self.isbn1.get()
        self.isbn1.delete(0, END)

        use.isbn = self.autor1.get()
        self.autor1.delete(0, END)

        self.teste["text"] = use.inserirLivro()

    def altLivro(self):
        use = importbdlivro()

        use.titulo = self.titulo1.get()
        self.titulo1.delete(0, END)

        use.isbn = self.isbn1.get()
        self.isbn1.delete(0, END)

        self.teste["text"] = use.attLivro

    def excluirLivro(self):
        use = importbdlivro()
        use.isbn = self.isbn1.get()
        self.isbn1.delete(0, END)

        use.titulo = self.titulo1.get()
        self.titulo1.delete(0, END)

        self.teste["text"] = use.deleteLivro()

    def buscarLivro(self):
        use = importbdlivro()
        isbn = self.isbn1.get()
        self.titulo1.delete(0, END)
        self.titulo1.insert(INSERT, use.titulo)
        isbn == self.isbn1.get()
        self.isbn1.delete(0, END)
        self.isbn1.insert(INSERT, use.isbn)
        self.autor1.delete(0, END)
        self.autor1.insert(INSERT, use.autor)
        self.teste["text"] = use.selectLivro


janela = Tk()
janela.wm_title("Dados do Livro")
Livro(janela)
janela.mainloop()