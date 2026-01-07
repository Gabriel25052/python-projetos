import tkinter as tk 



janela = tk.Tk()

janela.title("calculadora")
janela.geometry("250x350+200+90")
janela.config(bg="#777777")
janela.resizable(False,False)
janela.iconbitmap('Calculator_icon-icons.com_54972.ico')

for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

for i in range(1, 6):
    janela.grid_rowconfigure(i, weight=1)  



visor_calculadora = tk.Entry(janela, font="Arial 40", bg="#000000", readonlybackground="#000000", fg="white", justify="right")
visor_calculadora.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=3, pady=3)
visor_calculadora.config(state="readonly")

primeiro_numero = ""
operacao = ""

def adicionar_ponto():
    visor_calculadora.config(state="normal")
    atual = visor_calculadora.get()

    if "." not in atual:
        if atual == "":
            visor_calculadora.insert(0, "0.")
        else:
            visor_calculadora.insert(tk.END, ".")
    
    visor_calculadora.config(state="readonly")

def adicionar_numero(numero):
    visor_calculadora.config(state="normal")
    atual = visor_calculadora.get()
    visor_calculadora.delete(0, tk.END)
    visor_calculadora.insert(0, atual + numero)
    visor_calculadora.config(state="readonly")

def apagar_visor():
    visor_calculadora.config(state="normal")
    visor_calculadora.delete(0, tk.END)
    visor_calculadora.config(state="readonly")

def clicar_soma():
    global primeiro_numero
    global operacao

    primeiro_numero = visor_calculadora.get()
    operacao = "+"

    apagar_visor()

def clicar_subtracao():
    global primeiro_numero
    global operacao

    primeiro_numero = visor_calculadora.get()
    operacao = "-"

    apagar_visor()

def clicar_multiplicacao():
    global primeiro_numero
    global operacao

    primeiro_numero = visor_calculadora.get()
    operacao = "X"

    apagar_visor()

def clicar_divisao():
    global primeiro_numero
    global operacao

    primeiro_numero = visor_calculadora.get()
    operacao = "÷"

    apagar_visor()
    

def clicar_igual():
    segundo_numero = visor_calculadora.get()

    if operacao == "+":
        resultado = float(primeiro_numero) + float(segundo_numero)

    elif operacao == "-":
        resultado = float(primeiro_numero) - float(segundo_numero)

    elif operacao == "X":
        resultado = float(primeiro_numero) * float(segundo_numero)

    elif operacao == "÷":
        if float(segundo_numero) == 0:
            resultado = "Erro"
        else:
            resultado = float(primeiro_numero) / float(segundo_numero)

    if isinstance(resultado, float) and resultado.is_integer():
        resultado = int(resultado)

    visor_calculadora.config(state="normal")
    visor_calculadora.delete(0, tk.END)
    visor_calculadora.insert(0, str(resultado))
    visor_calculadora.config(state="readonly")


botao_9 = tk.Button(janela, font="Arial 10", bg="#FACE3E", fg="#000000", text="9", command=lambda:adicionar_numero("9"))
botao_9.grid(padx=3, pady=3, row= 1, column= 2, sticky="nsew")

botao_8 = tk.Button(janela, font="Arial 10", bg="#FACE3E", fg="#000000", text="8", command=lambda:adicionar_numero("8"))
botao_8.grid(padx=3, pady=3, row= 1, column= 1, sticky="nsew")

botao_7 = tk.Button(janela, font="Arial 10", bg="#FACE3E", fg="#000000", text="7", command= lambda:adicionar_numero("7"))
botao_7.grid(padx=3, pady=3, row= 1, column= 0, sticky="nsew")

botao_6 = tk.Button(janela, font="Arial 10", bg="#FACE3E", fg="#000000", text="6", command=lambda:adicionar_numero("6"))
botao_6.grid(padx=3, pady=3, row= 2, column= 2, sticky="nsew")

botao_5 = tk.Button(janela, font="Arial 10", bg="#FACE3E", fg="#000000", text="5", command=lambda:adicionar_numero("5"))
botao_5.grid(padx=3, pady=3, row= 2, column= 1, sticky="nsew")

botao_4 = tk.Button(janela, font="Arial 10", bg="#FACE3E", fg="#000000", text="4", command=lambda:adicionar_numero("4"))
botao_4.grid(padx=3, pady=3, row= 2, column= 0, sticky="nsew")

botao_3 = tk.Button(janela, font="Arial 10", bg="#FACE3E", fg="#000000", text="3", command=lambda:adicionar_numero("3"))
botao_3.grid(padx=3, pady=3, row= 3, column= 2, sticky="nsew")

botao_2 = tk.Button(janela, font="Arial 10", bg="#FACE3E", fg="#000000", text="2", command=lambda:adicionar_numero("2"))
botao_2.grid(padx=3, pady=3, row= 3, column= 1, sticky="nsew")

botao_1 = tk.Button(janela, font="Arial 10", bg="#FACE3E", fg="#000000", text="1", command=lambda:adicionar_numero("1"))
botao_1.grid(padx=3, pady=3, row= 3, column= 0, sticky="nsew")

botao_0 = tk.Button(janela, font="Arial 10", bg="#FACE3E", fg="#000000", text="0", command=lambda:adicionar_numero("0"))
botao_0.grid(row=4, column=0, sticky="nsew", padx=3, pady=3)

botao_C = tk.Button(janela, font="Arial 10", bg="#FACE3E", fg="#000000", text="C", command=lambda:apagar_visor())
botao_C.grid(row=5,column=0,columnspan=4,sticky="nsew",padx=3,pady=3)

botao_igual = tk.Button(janela, font="Arial 10", bg="#FACE3E", fg="#000000", text="=", command=clicar_igual)
botao_igual.grid(row=4, column=2, sticky="nsew", padx=3, pady=3)

botao_mais = tk.Button(janela, font="Arial 10", bg="#FACE3E", fg="#000000", text="+", command=clicar_soma)
botao_mais.grid(row=4, column=3, sticky="nsew", padx=3, pady=3)

botao_menos = tk.Button(janela, font="Arial 10", bg="#FACE3E", fg="#000000", text="-", command=clicar_subtracao)
botao_menos.grid(padx=3, pady=3, row= 3, column= 3, sticky="nsew")

botao_vezes = tk.Button(janela, font="Arial 10", bg="#FACE3E", fg="#000000", text="X", command=clicar_multiplicacao)
botao_vezes.grid(padx=3, pady=3, row= 2, column= 3, sticky="nsew")

botao_divisao = tk.Button(janela, font="Arial 10", bg="#FACE3E", fg="#000000", text="÷", command=clicar_divisao)
botao_divisao.grid(padx=3, pady=3, row= 1, column= 3, sticky="nsew")

botao_ponto = tk.Button(janela,font="Arial 10",bg="#FACE3E",fg="#000000",text=".",command=adicionar_ponto)
botao_ponto.grid(row=4, column=1, sticky="nsew", padx=3, pady=3)

janela.mainloop()