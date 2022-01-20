from tkinter import *
from importbdprofissional import  imporbdprofissional
class Profissional:
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

            self.titul = Label(self.first, text="                Dados do Profissional")
            self.titul["font"] = ("Arial", "10", "bold")
            self.titul.pack()

            self.salario1 = Label(self.third, text="Salário         ", font=self.fonte)
            self.salario1.pack(side=LEFT)
            self.salario1 = Entry(self.third)
            self.salario1["width"] = 30
            self.salario1["font"] = self.fonte
            self.salario1.pack(side=LEFT)

            self.cpf1 = Label(self.second, text="Cpf          ", font=self.fonte)
            self.cpf1.pack(side=LEFT)
            self.cpf1 = Entry(self.second)
            self.cpf1["width"] = 30
            self.cpf1["font"] = self.fonte
            self.cpf1.pack(side=LEFT)

            self.inserir = Button(self.tenth)
            self.inserir["text"] = "Excluir"
            self.inserir["font"] = ("Arial", "10")
            self.inserir["width"] = 30
            self.inserir["command"] = self.excluirProfissional
            self.inserir.pack()

            self.inserir = Button(self.tenth)
            self.inserir["text"] = "Cadastrar"
            self.inserir["font"] = ("Arial", "10")
            self.inserir["width"] = 30
            self.inserir["command"] = self.InserProfissional
            self.inserir.pack()

            self.inserir = Button(self.tenth)
            self.inserir["text"] = "Buscar"
            self.inserir["font"] = ("Arial", "10")
            self.inserir["width"] = 30
            self.inserir["command"] = self.buscarProfissional
            self.inserir.pack()

            self.sair = Button(self.tenth)
            self.sair["text"] = "Sair"
            self.sair["font"] = ("Arial", "10")
            self.sair["width"] = 30
            self.sair["command"] = self.tenth.quit
            self.sair.pack()

            from conectar import bd

            class importbdprofissional(object):

                def __init__(self, salario="", cpf=""):
                    self.info = {}
                    self.cpf = cpf
                    self.salario = salario

                def inserirProfissional(self):

                    try:
                        curs = bd.conectar.cursor()
                        curs.execute("INSERT INTO daniel_teixeira.empregado (salario, cpf) VALUES (%s, %s)")
                        curs.commit()
                        curs.close()
                        return "Erro."
                    except:
                        return "Profissional cadastrado."

                @property
                def attProfissional(self):

                    hi = bd()
                    try:
                        curso = hi.conectar.cursor()
                        hi = bd()
                        curso = hi.conectar.cursor()
                        up = """Update daniel_teixeira.empregado set salario = %s where cpf = %s"""
                        curso.execute(up, (self.salario, self.cpf))
                        hi.conectar.commit()
                        curso.close()
                        return "Erro."
                    except:
                        return "Profissional atualizado."

                def deleteProfissional(self):
                    hi = bd()
                    try:
                        curso = hi.conectar.cursor()
                        curso.execute("DELETE from daniel_teixeira.empregado where cpf = %s")
                        hi.conectar.commit()
                        curso.close()
                        return "Ocorreu um erro!"
                    except:
                        return "Profissional excluído."

                    hi = bd()
                    curso = hi.conectar.cursor()
                    curso.execute("SELECT * from daniel_teixeira.empregado where cpf = %s")
                    curso.close()

            self.teste = Label(self.ponto, text="")
            self.teste.pack()

    def InserProfissional(self):
        use = importbdprofissional()
        use.salario = self.salario1.get()
        self.salario1.delete(0, END)

        use.cpf = self.cpf1.get()
        self.cpf1.delete(0, END)

        use.salario = self.salario1.get()
        self.salario1.delete(0, END)

        self.teste["text"] = use.inserirProfissional()

    def altProfissional(self):
        use = importbdprofissional()

        use.salario = self.salario1.get()
        self.salario1.delete(0, END)

        use.cpf = self.cpf1.get()
        self.cpf1.delete(0, END)

        self.teste["text"] = use.attProfissional

    def excluirProfissional(self):
        use = importbdprofissional()
        use.cpf = self.cpf1.get()
        self.cpf1.delete(0, END)

        use.salario = self.salario1.get()
        self.salario1.delete(0, END)

        self.teste["text"] = use.deleteProfissional()

    def buscarProfissional(self):
        use = importbdprofissional()
        cpf = self.cpf1.get()
        self.salario1.delete(0, END)
        self.salario1.insert(INSERT, use.salario1)
        cpf == self.cpf1.get()
        self.cpf1.delete(0, END)
        self.cpf1.insert(INSERT, use.cpf)
        self.salario1.delete(0, END)
        self.salario1.insert(INSERT, use.autor)
        self.teste["text"] = use.selectProfissional


janela = Tk()
janela.wm_title("Dados do Profissional")
Profissional(janela)
janela.mainloop()