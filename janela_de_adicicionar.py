import tkinter as tk
from adicionar import  adicionar_nova_cor
import json



janela = tk.Tk()
janela.geometry("600x600")
janela.title("Adicionar")


tk.Label(janela,text="Boas vindas").pack(pady=10)


div1 = tk.Frame(janela, bd=1, relief="solid")
div1.pack()
div2 = tk.Frame(janela, bd=1, relief="solid" )
div2.pack(pady=10)



info = tk.Label(div1, text="Adicione seu produto")
info.grid(row=1, column=1, pady=10)

entrada = tk.Entry(div1)
entrada.grid(row=1,column=2, pady=10)


info2 = tk.Label(div1, text="Adicione a cor")
info2.grid(row=2,column=1, pady=10)

entrada2 = tk.Entry(div1)
entrada2.grid(row=2,column=2, pady=10)

info3 = tk.Label(div1, text="Adicione o tamanho")
info3.grid(row=3,column=1, pady=10)

entrada3 = tk.Entry(div1)
entrada3.grid(row=3,column=2, pady=10)

entrada4= tk.Entry(div1)


informacao1 = tk.Label(div2, text="informe o nome")
informacao1.grid(row=1, column=1, padx=10)

dicionario1 = tk.Entry(div2)
dicionario1.grid(row=1, column=2, padx=10, pady=10)

informacao2 = tk.Label(div2, text="Quantidade")
informacao2.grid(row=2, column=1, padx=10)

dicionario2 = tk.Entry(div2)
dicionario2.grid(row=2, column=2, padx=10, pady=10)

informacao4 = tk.Label(div2, text="Valor")
informacao4.grid(row=3, column=1, padx=10)



dicionario4 = tk.Entry(div2)
dicionario4.grid(row=3, column=2, padx=10, pady=10)




soma = []
qnt = []

def add():
    transform = dicionario4.get().strip()
    integer = int(transform) 

    soma.append(integer)

    transforms = dicionario2.get().strip()
    integers = int(transforms)

    qnt.append(integers)
  








def salva():

    with open("produtos.json", 'r', encoding="utf-8") as f:
        estoque = json.load(f)

    somas = soma
    quantidade = qnt

    contagem = len(estoque)
    nova_id = contagem + 1

    dados = {
        "id": 1,
        "nome": dicionario1.get(),
        "quantidade": quantidade,
        "valor": somas
    }

    
      


    adicionar_nova_cor(entrada.get(), entrada2.get(), entrada3.get(),dados)

    
    




botao3 = tk.Button(div2, text="Adicione os valores",
                     command= add)
botao3.grid(row=3, column=3, padx=10)





botao2 = tk.Button(div2, text="Adicione & atualize",
                     command= salva)
botao2.grid(row=4, column=4, padx=10, pady=10)




janela.mainloop()