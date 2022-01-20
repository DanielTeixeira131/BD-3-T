from tkinter import *
from importbdcliente import importbdcliente
if __name__ == "__main__":
    class Cliente:
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

            self.nome1 = Label(self.first, text="                Dados do cliente")
            self.nome1["font"] = ("Arial", "12", "bold")
            self.nome1.pack()

            self.cpf1 = Label(self.second, text="CPF            ", font=self.fonte)
            self.cpf1.pack(side=LEFT)
            self.cpf1 = Entry(self.second)
            self.cpf1["width"] = 45
            self.cpf1["font"] = self.fonte
            self.cpf1.pack(side=LEFT)

            self.nome1 = Label(self.third, text="Nome         ", font=self.fonte)
            self.nome1.pack(side=LEFT)
            self.nome1 = Entry(self.third)
            self.nome1["width"] = 45
            self.nome1["font"] = self.fonte
            self.nome1.pack(side=LEFT)

            self.hdc1 = Label(self.sixth, text="Historico de Compras     ", font=self.fonte)
            self.hdc1.pack(side=LEFT)
            self.hdc1 = Entry(self.sixth)
            self.hdc1["width"] = 34
            self.hdc1["font"] = self.fonte
            self.hdc1.pack(side=LEFT)

            self.qdc = Label(self.seventh, text="Quantidade de vezes que comprou            ", font=self.fonte)
            self.qdc.pack(side=LEFT)
            self.qdc = Entry(self.seventh)
            self.qdc["width"] = 19
            self.qdc["font"] = self.fonte
            self.qdc.pack(side=LEFT)

            self.inserir = Button(self.tenth)
            self.inserir["text"] = "Excluir"
            self.inserir["font"] = ("Arial", "10")
            self.inserir["width"] = 30

            def excluirCliente(self):
                use = importbdcliente()
                use.isbn = self.isbn1.get()
                self.isbn1.delete(0, END)
            self.inserir.pack()

            self.inserir = Button(self.tenth)
            self.inserir["text"] = "Cadastrar"
            self.inserir["font"] = ("Arial", "10")
            self.inserir["width"] = 30
            self.inserir["command"] = self.InserCliente
            self.inserir.pack()

            self.inserir = Button(self.tenth)
            self.inserir["text"] = "Buscar"
            self.inserir["font"] = ("Arial", "10")
            self.inserir["width"] = 30
            self.inserir["command"] = self.buscarCliente
            self.inserir.pack()

            self.sair = Button(self.tenth)
            self.sair["text"] = "Sair"
            self.sair["font"] = ("Arial", "10")
            self.sair["width"] = 30
            self.sair["command"] = self.tenth.quit
            self.sair.pack()

            from conectar import bd

            class importbdcliente(object):

                def __init__(self, nome="", cpf=""):
                    self.info = {}
                    self.cpf = cpf
                    self.nome = nome

            def InserCliente(self):
                use = importbdcliente()
                use.nome = self.nome1.get()
                self.nome1.delete(0, END)

                use.cpf = self.cpf1.get()
                self.cpf1.delete(0, END)

                use.cpf = self.autor1.get()
                self.autor1.delete(0, END)

                self.teste["text"] = use.inserirCliente()

            def altCliente(self):
                use = importbdcliente()

                use.nome = self.nome1.get()
                self.nome1.delete(0, END)

                use.cpf = self.cpf1.get()
                self.cpf1.delete(0, END)

                self.teste["text"] = use.attCliente

            def excluirCliente(self):
                use = importbdcliente()
                use.cpf = self.cpf1.get()
                self.cpf1.delete(0, END)

                use.nome = self.nome1.get()
                self.nome1.delete(0, END)

                self.teste["text"] = use.excluirCliente()

            def buscarCliente(self):
                use = importbdcliente()
                cpf = self.cpf1.get()
                self.nome1.delete(0, END)
                self.nome1.insert(INSERT, use.nome)
                cpf == self.cpf1.get()
                self.cpf1.delete(0, END)
                self.cpf1.insert(INSERT, use.cpf)
                self.autor1.delete(0, END)
                self.autor1.insert(INSERT, use.autor)
                self.teste["text"] = use.selectCliente

janela = Tk()
janela.wm_title("Dados do Cliente")
Cliente(janela)
janela.mainloop()
