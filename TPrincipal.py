from tkinter import *

janela = Tk()
janela.title("Escolha a função desejada")
janela.geometry("150x150")

texto_funcao = Label(janela, text="Escolha a Função abaixo")

texto_funcao.grid(column=0, row=0, padx=10, pady=10)

botaolivro = Button(janela, text="Cadastrar Livro")
botaolivro.grid(column=0, row=1)

botaoprofissional = Button(janela, text="Cadastrar Profissional")
botaoprofissional.grid(column=0, row=2)

botaoconferir = Button(janela, text="Cadastrar Cliente")
botaoconferir.grid(column=0, row=3)



janela.mainloop()