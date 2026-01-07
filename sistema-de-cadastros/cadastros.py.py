import tkinter as tk
from tkinter import messagebox
import sys
import os

def caminho_absoluto(relativo):
    try:
        base = sys._MEIPASS
    except Exception:
        base = os.path.abspath(".")
    return os.path.join(base, relativo)


# criando a janela
janela = tk.Tk()
janela.title("Sistema de Cadastro de Clientes")
janela.geometry("320x365")
janela.config(bg="#f2f2f2")
janela.resizable(False, False)
janela.iconbitmap(caminho_absoluto("3977661_1.ico"))
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)

#as labels e entry
titulo = tk.Label(janela,text="Sistema de Cadastro",font="Arial 13 bold",bg="#f2f2f2",fg="#2c3e50")
titulo.grid(row=1, column=0, columnspan=2, pady=15)


cadastro_nome = tk.Label(janela, text="Nome do cliente", font=("Arial", 10), bg="#f2f2f2", fg="#2c3e50")
cadastro_nome.grid(row=2, column=0, columnspan=2, pady=(5, 2))

entry_nome = tk.Entry(janela, font=("Arial", 10), bg="#ffffff", fg="#2c3e50", width=28)
entry_nome.grid(row=3, column=0, columnspan=2, pady=5)

cadastro_email = tk.Label(janela, text="Email do cliente", font=("Arial", 10), bg="#f2f2f2", fg="#2c3e50")
cadastro_email.grid(row=4, column=0, columnspan=2, pady=(5, 2))

entry_email = tk.Entry(janela, font=("Arial", 10), bg="#ffffff", fg="#2c3e50", width=28)
entry_email.grid(row=5, column=0, columnspan=2, pady=(5, 2))

cadastro_telefone = tk.Label(janela, text="Telefone do cliente", font=("Arial", 10), bg="#f2f2f2", fg="#2c3e50")
cadastro_telefone.grid(row=6, column=0, columnspan=2,)

entry_telefone = tk.Entry(janela, font=("Arial", 10), bg="#ffffff", fg="#2c3e50", width=28)
entry_telefone.grid(row=7, column=0, columnspan=2)

# espaço visual (respiro)
tk.Label(janela, bg="#f2f2f2").grid(row=8, column=0, columnspan=2, pady=6)

#funções 

def validar_dados():
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    telefone = entry_telefone.get().strip()

    if nome == "":
        messagebox.showerror("Erro", "O nome não pode ficar vazio!")
        return

    if any(char.isdigit() for char in nome):
        messagebox.showerror("Erro", "O nome não pode conter números!")
        return

    if len(nome) < 2:
        messagebox.showerror("Erro", "O nome deve ter pelo menos 2 letras!")
        return

    if "@" not in email or "." not in email:
        messagebox.showerror("Erro", "Email inválido!")
        return

    if not telefone.isdigit() or len(telefone) < 8:
        messagebox.showerror("Erro", "Telefone inválido!")
        return

    # SALVAR NO ARQUIVO
    with open("cadastros.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome} | {email} | {telefone}\n")

    messagebox.showinfo("Sucesso", "Cadastro salvo com sucesso!")

    # LIMPAR CAMPOS
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)


def mostrar_cadastros():
    try:
        with open("cadastros.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()

        if conteudo.strip() == "":
            messagebox.showinfo("Cadastros", "Nenhum cadastro encontrado.")
        else:
            messagebox.showinfo("Cadastros", conteudo)

    except FileNotFoundError:
        messagebox.showinfo("Cadastros", "Nenhum cadastro encontrado.")

def excluir_cadastros():
    resposta = messagebox.askyesno(
        "Confirmar",
        "Tem certeza que deseja excluir TODOS os cadastros?"
    )

    if resposta:
        with open("cadastros.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("")

        messagebox.showinfo("Sucesso", "Todos os cadastros foram excluídos!")

def excluir_cadastro_especifico():
    email_excluir = entry_email.get().strip()

    if email_excluir == "":
        messagebox.showerror("Erro", "Digite o email para excluir!")
        return

    try:
        with open("cadastros.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        novas_linhas = []
        encontrado = False

        for linha in linhas:
            if email_excluir.lower() in linha.lower():
                encontrado = True
            else:
                novas_linhas.append(linha)

        if not encontrado:
            messagebox.showinfo("Aviso", "Nenhum cadastro com esse email foi encontrado.")
            return

        resposta = messagebox.askyesno(
            "Confirmar",
            "Deseja realmente excluir este cadastro?"
        )

        if resposta:
            with open("cadastros.txt", "w", encoding="utf-8") as arquivo:
                arquivo.writelines(novas_linhas)

            messagebox.showinfo("Sucesso", "Cadastro excluído com sucesso!")

    except FileNotFoundError:
        messagebox.showinfo("Aviso", "Nenhum cadastro encontrado.")

def editar_cadastro():
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    telefone = entry_telefone.get().strip()

    if nome == "" or email == "" or telefone == "":
        messagebox.showerror("Erro", "Preencha todos os campos para editar!")
        return

    try:
        with open("cadastros.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        novas_linhas = []
        encontrado = False

        for linha in linhas:
            if email.lower() in linha.lower():
                novas_linhas.append(f"{nome} | {email} | {telefone}\n")
                encontrado = True
            else:
                novas_linhas.append(linha)

        if not encontrado:
            messagebox.showinfo("Aviso", "Cadastro não encontrado para edição.")
            return

        resposta = messagebox.askyesno(
            "Confirmar",
            "Deseja realmente editar este cadastro?"
        )

        if resposta:
            with open("cadastros.txt", "w", encoding="utf-8") as arquivo:
                arquivo.writelines(novas_linhas)

            messagebox.showinfo("Sucesso", "Cadastro editado com sucesso!")

    except FileNotFoundError:
        messagebox.showinfo("Aviso", "Nenhum cadastro encontrado.")




# botões do app de cadastro

botao_cadastrar = tk.Button(janela, text="Cadastrar", bg="#2ecc71", fg="white", font=("Arial", 10, "bold"), command=validar_dados)
botao_cadastrar.grid(row=9, column=0, padx=5, pady=8, sticky="ew")

botao_mostrar = tk.Button(janela, text="Ver Cadastros", bg="#3498db", fg="white", font=("Arial", 10, "bold"), command=mostrar_cadastros)
botao_mostrar.grid(row=9, column=1, pady=5, padx=5, sticky="ew")
botao_mostrar.config(width=18)

botao_excluir = tk.Button(janela, text="Excluir Cadastros", bg="#e74c3c", fg="white", font=("Arial", 10, "bold"), command=excluir_cadastros)
botao_excluir.grid(row=10, column=0, padx=5, pady=5, sticky="ew")

botao_excluir_especifico = tk.Button(janela,text="Excluir por Email",fg="white",bg="#e67e22",command=excluir_cadastro_especifico)
botao_excluir_especifico.grid(row=10, column=1, pady=5, padx=5, sticky="ew")
botao_excluir_especifico.config(width=18)

botao_editar = tk.Button(janela,text="Editar Cadastro",fg="white",bg="#2980b9",command=editar_cadastro)
botao_editar.grid(row=11, column=0, columnspan=2, pady=5)
botao_editar.config(width=18)

janela.mainloop()