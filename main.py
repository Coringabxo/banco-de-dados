import tkinter as tk
from tkinter import messagebox

def cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()
    
    # Aqui você pode adicionar lógica para salvar os dados em um banco de dados, por exemplo.
    
    messagebox.showinfo("Cadastro", f"Cadastro realizado com sucesso!\nNome: {nome}\nEmail: {email}")

# Criação da janela principal
janela = tk.Tk()
janela.title("Tela de Cadastro")

# Labels e Entrys
label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

label_email = tk.Label(janela, text="Email:")
label_email.pack()
entry_email = tk.Entry(janela)
entry_email.pack()

label_senha = tk.Label(janela, text="Senha:")
label_senha.pack()
entry_senha = tk.Entry(janela, show="*")
entry_senha.pack()

# Botão de cadastrar
botao_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar)
botao_cadastrar.pack()

# Inicia o loop da interface gráfica
janela.mainloop()
