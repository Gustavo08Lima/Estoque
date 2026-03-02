import tkinter as tk
import json




"""janela principal"""

janela = tk.Tk()
janela.title("Estoque")
janela.geometry("500x500")

"Funções"

def carregar():
    
        return json.load(open("produtos.json", "r", encoding="utf-8"))

ficha = carregar()

"DIVs"

bloco_um = tk.Frame(janela)
bloco_um.pack()

bloco_dois = tk.Frame(janela, relief="solid",bd="2")
bloco_dois.pack()

bloco_tres = tk.Frame(janela, relief="solid",bd="2")
bloco_tres.pack(ipadx= 100, ipady=100, pady=20)

"""Label"""

intro = tk.Label(bloco_um, text="Bem vindo")
intro.pack()

digite = tk.Label(bloco_dois, text="Digite algo o produto ao lado:")
digite.grid(row=2, column=1, padx=5)

digite2 = tk.Label(bloco_dois, text="Digite algo a variação ao lado:")
digite2.grid(row=3, column=1, padx=5)

"Label de Informações"

Info = tk.Label(bloco_tres,text="Nome", relief='solid', bd=1)
Info.grid(row=1,column=1, pady=(10,2), sticky="w", padx=10)

Info2 = tk.Label(bloco_tres,text="Quantidade", relief='solid', bd=1)
Info2.grid(row=3,column=1, pady=2, sticky="w", padx=10)

Info3 = tk.Label(bloco_tres,text="Valor", relief='solid', bd=1)
Info3.grid(row=5,column=1, pady=2, sticky="w", padx=10)

Info4 = tk.Label(bloco_tres,text="Lucro", relief='solid', bd=1)
Info4.grid(row=7,column=1, pady=2, sticky="w", padx=10)


"Label de Saida"

nome = tk.Label(bloco_tres,text="", width=30,bg="green",relief='solid',bd = 1)
nome.grid(row = 2, column=1, pady=10, padx=10)

quantidade = tk.Label(bloco_tres,text="", width=30,bg="green",relief='solid',bd = 1)
quantidade.grid(row = 4, column=1, pady=10, padx=10)

valores = tk.Label(bloco_tres,text="", width=30,bg="green",relief='solid',bd = 1)
valores.grid(row = 6, column=1, pady=10, padx=10)

lucro = tk.Label(bloco_tres,text="", width=30,bg="green",relief='solid',bd = 1)
lucro.grid(row = 8, column=1, pady=10, padx=10)


"""Entrada"""
entrada = tk.Entry(bloco_dois)
entrada.grid(row= 2, column=2, pady=20)

entrada2 = tk.Entry(bloco_dois)     
entrada2.grid(row= 3, column=2, pady=20)



"Botôes"

def enviar():
    
    
    valor = entrada.get().lower().strip()
    valor2 = entrada2.get().lower()
    Ver= var_check.get()
    Pre= var_check2.get()

    if Ver == 1:
         cor = "vermelho"
         var_check2.set(0)
    if Pre == 1:
        cor = "preto"
        var_check.set(0)
       
    if valor in ficha:
        dic = ficha[valor][cor][valor2]
        nome.config(text=dic["nome"])
        quantidade.config(text=dic["Quantidade"])
        valores.config(text=f"R$ {dic['Valor']}")
        lucro.config(text=f"R$ {dic['Lucro']}")

    else:
         nome.config(text="")
         quantidade.config(text="")
         valores.config(text="")
         lucro.config(text="")


"Checagem"
   
var_check = tk.IntVar()   
var_check2 = tk.IntVar()   

checar = tk.Checkbutton(bloco_dois,text="Vermelho",variable=var_check,command=enviar)
checar.grid(row=5,column=2, pady=10)

checar2 = tk.Checkbutton(bloco_dois,text="Preto",variable=var_check2,command=enviar)
checar2.grid(row=5,column=3, pady=10)




janela.mainloop()

print(valores)