import tkinter as tk
from adicionar import  adicionar_nova_cor
import json
import os
import subprocess



janela = tk.Tk()
janela.geometry("600x600", )
janela.title("Adicionar")
janela.config(bg="#1C60E6")


tk.Label(janela,text="Boas vindas").pack(pady=10)

tk.Label(janela, text="Informações chaves").pack(pady=10, anchor='w', padx=20 )

#Divs
div1 = tk.Frame(janela, bd=1, relief="solid")
div1.pack(anchor='w',padx=20)

tk.Label(janela, text="Informações de caracteristica").pack(pady=(50,10), anchor='w', padx=20 )

div2 = tk.Frame(janela, bd=1, relief="solid" )
div2.pack(anchor='w', padx=20, pady=10)

#INFO keys

info = tk.Label(div1, text="Adicione seu produto")
info.grid(row=1, column=1, pady=10, padx=10, sticky='w')

info2 = tk.Label(div1, text="Adicione a cor")
info2.grid(row=2,column=1, pady=10, padx=10, sticky='w')

info3 = tk.Label(div1, text="Adicione o tamanho")
info3.grid(row=3,column=1, pady=10, padx=10, sticky='w')



#INFO dicionario

informacao1 = tk.Label(div2, text="Informe o nome")
informacao1.grid(row=1, column=1, padx=10, sticky='w')

informacao2 = tk.Label(div2, text="Quantidade")
informacao2.grid(row=2, column=1, padx=10, sticky='w')

informacao4 = tk.Label(div2, text="Valor")
informacao4.grid(row=3, column=1, padx=10, sticky='w')

informacao5 = tk.Label(div2, text="Custo do PRODUTO")
informacao5.grid(row=4, column=1, padx=10, sticky='w')

#ENTRADA keys

entrada = tk.Entry(div1)
entrada.grid(row=1,column=2, pady=10, padx=(10,40))

entrada2 = tk.Entry(div1)
entrada2.grid(row=2,column=2, pady=10, padx=(10,40))

entrada3 = tk.Entry(div1)
entrada3.grid(row=3,column=2, pady=10, padx=(10,40))

custo = tk.Entry(div2)
custo.grid(row=4, column=2, padx=10, pady=10)
#ENTRADA dicionario

dicionario1 = tk.Entry(div2)
dicionario1.grid(row=1, column=2, padx=10, pady=10)

dicionario2 = tk.Entry(div2)
dicionario2.grid(row=2, column=2, padx=10, pady=10)

dicionario4 = tk.Entry(div2)
dicionario4.grid(row=3, column=2, padx=10, pady=10)





#Variaveis
soma = []
qnt = []
desc = []
gastos = 0.0




#FUNÇÔES 

# Adicionar valores separados
def add():
    global gastos

    transform = dicionario4.get().strip()
    integer = float(transform) 
    

    soma.append(integer)

    transforms = dicionario2.get().strip()
    integers = int(transforms)

    qnt.append(integers)

    transforma = custo.get().strip()
    inteiro = float(transforma)

    gastos = inteiro

    botao2 = tk.Button(div2, text="Adicione & atualize",
                     command= salva)
    botao2.grid(row=4, column=4, padx=10, pady=10)

    botao3.config(text="Adicione mais valores")

    dicionario4.delete(0, tk.END)
    dicionario2.delete(0, tk.END)
  
# Adicionar tudo
def salva():

    with open("produtos.json", 'r', encoding="utf-8") as f:
        estoque = json.load(f)
    
    

    desc = []

    for x in soma:
        if x < 79.90:
            resultado = round(x - (x * 0.18) - (x * 0.02) - 4, 2)
        else:
            resultado = round(x - (x * 0.14) - (x * 0.02) - 20, 2)
        
        desc.append(resultado)



    
    custo = list(map(lambda x: round((x*gastos),2), qnt))
    total = list(map(lambda x,y: round((x - y),2), desc, custo))
   
    print(gastos)
    print(custo)
    print(total)

    somas = soma
    quantidade = qnt

    contagem = len(estoque)
    nova_id = contagem + 1

    dados = {
        "id": 1,
        "nome": dicionario1.get(),
        "quantidade": quantidade,
        "valor": somas,
        "lucro": total
    }

    adicionar_nova_cor(entrada.get().lower(), entrada2.get(), entrada3.get(),dados)

def abrir_janela_adicionar():
     if os.path.exists("launcher.exe"):
         subprocess.Popen(["launcher.exe"])
     else:
        subprocess.Popen(["python", "launcher.py"])

      
    
     janela.destroy()


#BOTOES


botao4 = tk.Button(janela, text="sair",
                      command= abrir_janela_adicionar)
botao4.pack()

botao3 = tk.Button(div2, text="Adicione os valores",
                     command= add)
botao3.grid(row=4, column=3, padx=10)










janela.mainloop()