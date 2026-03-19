import tkinter as tk
from tkinter import ttk
import json
import os
import subprocess





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

     cores = list(ficha[item].keys())

     cor = cores[0]
     tamanho = list(ficha[item][cor].keys())


     

     entrada2['values'] = tamanho
     entrada2.set("Agora Escolha o tamanho")

     entrada3['values'] = cores
     entrada3.set("Agora Escolha o tamanho")
     

"DIVs"

bloco_um = tk.Frame(janela)
bloco_um.pack()

bloco_dois = tk.Frame(janela)
bloco_dois.pack()

bloco_tres = tk.Frame(janela)
bloco_tres.pack(ipadx= 100, ipady=100, pady=(10,20), padx=20)

"""Label"""

intro = tk.Label(bloco_um, text="Bem vindo")
intro.pack()

digite = tk.Label(bloco_dois, text="Digite algo o produto ao lado:", font=('Arial',13),)
digite.grid(row=2, column=1, padx=(10,0) )

digite2 = tk.Label(bloco_dois, text="Digite a variação ao lado:", font=('Arial',13))
digite2.grid(row=3, column=1,  padx=(10,0), sticky='w')






"""Variaveis"""






"""Entrada"""
entrada = ttk.Combobox(bloco_dois, values=opcao)
entrada.grid(row= 2, column=2, pady=20, padx=10,)
entrada.set("Selecione o produto")



entrada2 = ttk.Combobox(bloco_dois,values="")
entrada2.grid(row= 3, column=2, pady=20, padx=10,)
entrada2.set("Selecione o produto")

entrada.bind("<<ComboboxSelected>>", atualiza)


entrada3 = ttk.Combobox(bloco_dois,values="")
entrada3.grid(row= 4, column=2, pady=20, padx=10,)
entrada3.set("Selecione o produto")

entrada.bind("<<ComboboxSelected>>", atualiza)


"Botôes"

def enviar():
    
    
    valor = entrada.get()
    valor2 = entrada2.get()
    Ver= entrada3.get()



    Info = tk.Label(bloco_tres,text="Nome:", font=('Arial',13))
    Info.grid(row=1,column=1, pady=(10,2), sticky="w", padx=10)

    Info2 = tk.Label(bloco_tres,text="Quantidade:", font=('Arial',13))
    Info2.grid(row=3,column=1, pady=2, sticky="w", padx=10)

    Info3 = tk.Label(bloco_tres,text="Valor:", font=('Arial',13))
    Info3.grid(row=5,column=1, pady=2, sticky="w", padx=10)

    Info4 = tk.Label(bloco_tres,text="Lucro:", font=('Arial',13))
    Info4.grid(row=7,column=1, pady=2, sticky="w", padx=10)

    Info5 = tk.Label(bloco_dois,text="Informe a cor:", font=('Arial',13))
    Info5.grid(row=4,column=1, pady=2, sticky="w", padx=10)




    "Label de Saida"

    nome = tk.Label(bloco_tres,text="", width=20, relief='raised',bd=3)
    nome.grid(row = 2, column=1, pady=10, padx=10)
   
    

    
       
    if valor in ficha and Ver in ficha[valor] and valor2 in ficha[valor][Ver]:
        dic = ficha[valor][Ver][valor2]
        nome.config(text=dic["nome"])

        for i, qtd in enumerate(dic["quantidade"]):
            lbl = tk.Label(bloco_tres, text=qtd, relief='raised', bd=2, width=10)
            lbl.grid(row=4, column=i+1, padx=5, pady=10)

        for i, val in enumerate(dic["valor"]):
            lbl = tk.Label(bloco_tres, text=val, relief='raised', bd=2, width=10)
            lbl.grid(row=6, column=i+1, padx=5, pady=10)

        for i, luc in enumerate(dic["lucro"]):
            lbl = tk.Label(bloco_tres, text=luc, relief='raised', bd=2, width=10)
            lbl.grid(row=8, column=i+1, padx=5, pady=(10,5))

       

    else:
         nome.config(text="")
         quantidade.config(text="")
         valores.config(text="")
         lucro.config(text="")

         
def abrir_janela_adicionar():
    caminho_atual = os.path.dirname(__file__)

    arquivo = os.path.join(caminho_atual,"launcher.py")
   
    subprocess.Popen(["python", arquivo])    
    
    janela.destroy()


#BOTOES

botao = tk.Button(bloco_dois, text="Enviar", command=enviar)
botao.grid(row=4, column=4)



botao4 = tk.Button(janela, text="sair",
                      command= abrir_janela_adicionar)
botao4.pack()

"Checagem"
   
# var_check = tk.IntVar()   
# var_check2 = tk.IntVar()   




# checar = tk.Checkbutton(bloco_dois,text="Vermelho",variable=var_check,command=enviar, font=('arial',10))
# checar.grid(row=5,column=2, pady=10,sticky='w')

# checar2 = tk.Checkbutton(bloco_dois,text="Preto",variable=var_check2,command=enviar, font=('arial',10))
# checar2.grid(row=5,column=2, pady=10, padx=(100,0), sticky='w')




janela.mainloop()

