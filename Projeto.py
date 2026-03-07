import tkinter as tk
from tkinter import ttk
import json




"""janela principal"""

janela = tk.Tk()
janela.title("Estoque")
janela.geometry("600x600")

"Funções"

def carregar():
    
        return json.load(open("produtos.json", "r", encoding="utf-8"))

ficha = carregar()

opcao = list(ficha.keys())

def atualiza(event):
     
     item = entrada.get()

     v = list(ficha[item].keys())[0]
     tamanho = list(ficha[item][v].keys())

     entrada2['values'] = tamanho
     entrada2.set("Agora Escolha o tamanho")
     

"DIVs"

bloco_um = tk.Frame(janela)
bloco_um.pack()

bloco_dois = tk.Frame(janela)
bloco_dois.pack()

bloco_tres = tk.Frame(janela)
bloco_tres.pack(ipadx= 100, ipady=100, pady=20, padx=20)

"""Label"""

intro = tk.Label(bloco_um, text="Bem vindo")
intro.pack()

digite = tk.Label(bloco_dois, text="Digite algo o produto ao lado:", font=('Arial',13),)
digite.grid(row=2, column=1, padx=(10,0) )

digite2 = tk.Label(bloco_dois, text="Digite a variação ao lado:", font=('Arial',13))
digite2.grid(row=3, column=1,  padx=(10,0), sticky='w')

"Label de Informações"

Info = tk.Label(bloco_tres,text="Nome:", font=('Arial',13))
Info.grid(row=1,column=1, pady=(10,2), sticky="w", padx=10)

Info2 = tk.Label(bloco_tres,text="Quantidade:", font=('Arial',13))
Info2.grid(row=3,column=1, pady=2, sticky="w", padx=10)

Info3 = tk.Label(bloco_tres,text="Valor:", font=('Arial',13))
Info3.grid(row=5,column=1, pady=2, sticky="w", padx=10)

Info4 = tk.Label(bloco_tres,text="Lucro:", font=('Arial',13))
Info4.grid(row=7,column=1, pady=2, sticky="w", padx=10)

Info5 = tk.Label(bloco_dois,text="Informe a cor:", font=('Arial',13))
Info5.grid(row=5,column=1, pady=2, sticky="w", padx=10)




"Label de Saida"

nome = tk.Label(bloco_tres,text="", width=20, relief='raised',bd=3)
nome.grid(row = 2, column=1, pady=10, padx=10)

quantidade = tk.Label(bloco_tres,text="", width=20, relief='raised',bd=3)
quantidade.grid(row = 4, column=1, pady=10, padx=10)

valores = tk.Label(bloco_tres,text="", width=20, relief='raised',bd=3)
valores.grid(row = 6, column=1, pady=10, padx=10)

lucro = tk.Label(bloco_tres,text="", width=20, relief='raised',bd=3)
lucro.grid(row = 8, column=1, pady=10, padx=10)


"""Variaveis"""

quantidade1 = tk.Label(bloco_tres,text="", width=10,relief='raised',bd = 2)
quantidade1.grid(row = 4, column=2, pady=10, padx=20)

quantidade2 = tk.Label(bloco_tres,text="", width=10,relief='raised',bd = 2)
quantidade2.grid(row = 4, column=3, pady=10, padx=20)

quantidade3 = tk.Label(bloco_tres,text="", width=10,relief='raised',bd = 2)
quantidade3.grid(row = 4, column=4, pady=10, padx=20)

valores1 = tk.Label(bloco_tres,text="", width=10,relief='raised',bd = 2)
valores1.grid(row = 6, column=2, pady=10, padx=20)

valores2 = tk.Label(bloco_tres,text="", width=10,relief='raised',bd = 2)
valores2.grid(row = 6, column=3, pady=10, padx=20)

valores3 = tk.Label(bloco_tres,text="", width=10,relief='raised',bd = 2)
valores3.grid(row = 6, column=4, pady=10, padx=20)

lucro1 = tk.Label(bloco_tres,text="", width=10,relief='raised',bd = 2)
lucro1.grid(row = 8, column=2, pady=10, padx=20)

lucro2 = tk.Label(bloco_tres,text="", width=10,relief='raised',bd = 2)
lucro2.grid(row = 8, column=3, pady=10, padx=20)

lucro3 = tk.Label(bloco_tres,text="", width=10,relief='raised',bd = 2)
lucro3.grid(row = 8, column=4, pady=10, padx=20)





"""Entrada"""
entrada = ttk.Combobox(bloco_dois, values=opcao)
entrada.grid(row= 2, column=2, pady=20, padx=10,)
entrada.set("Selecione o produto")



entrada2 = ttk.Combobox(bloco_dois,values="")
entrada2.grid(row= 3, column=2, pady=20, padx=10,)
entrada2.set("Selecione o produto")

entrada.bind("<<ComboboxSelected>>", atualiza)


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

        quantidade.config(text=dic["Quantidade"][0])
        quantidade1.config(text=dic["Quantidade"][1])
        quantidade2.config(text=dic["Quantidade"][2])
        quantidade3.config(text=dic["Quantidade"][3])
        
        valores.config(text=f"R$ {dic['Valor'][0]}")
        valores1.config(text=f"R$ {dic['Valor'][1]}")
        valores2.config(text=f"R$ {dic['Valor'][2]}")
        valores3.config(text=f"R$ {dic['Valor'][3]}")

        lucro.config(text=f"R$ {dic['Lucro'][0]}") 
        lucro1.config(text=f"R$ {dic['Lucro'][1]}")
        lucro2.config(text=f"R$ {dic['Lucro'][2]}")
        lucro3.config(text=f"R$ {dic['Lucro'][3]}")
        

       

    else:
         nome.config(text="")
         quantidade.config(text="")
         valores.config(text="")
         lucro.config(text="")
         





"Checagem"
   
var_check = tk.IntVar()   
var_check2 = tk.IntVar()   




checar = tk.Checkbutton(bloco_dois,text="Vermelho",variable=var_check,command=enviar, font=('arial',10))
checar.grid(row=5,column=2, pady=10,sticky='w')

checar2 = tk.Checkbutton(bloco_dois,text="Preto",variable=var_check2,command=enviar, font=('arial',10))
checar2.grid(row=5,column=2, pady=10, padx=(100,0), sticky='w')




janela.mainloop()

print(valores)