import tkinter as tk
import subprocess 
import os
from PIL import Image, ImageTk


janela = tk.Tk()
janela.geometry("900x500")
janela.title("Launcher")


titulo = tk.Label(janela,text="Escolha o APP", font="Arial, 15")
titulo.pack(pady=(20,0))

#DIVs

cont = tk.Frame(janela)
cont.pack(expand=True)

div1 = tk.Frame(cont, width=350,height=350, bd=2, relief='solid')
div1.pack(side='left', padx=30)
div1.pack_propagate(False)

div2 = tk.Frame(cont, width=350,height=350, bd=2, relief='solid')
div2.pack(side='left', padx=30)
div2.pack_propagate(False)

#FUNÇÃO PARA ABRIR APP
def abrir_janela_adicionar():
    caminho_atual = os.path.dirname(__file__)

    arquivo = os.path.join(caminho_atual,"janela_de_adicionar.py")
   
    subprocess.Popen(["python", arquivo])

    janela.destroy()

def abrir_Projeto():
    caminho_atual = os.path.dirname(__file__)

    arquivo = os.path.join(caminho_atual,"Projeto.py")
   
    subprocess.Popen(["python", arquivo])
    janela.destroy()


caminho_atual = os.path.dirname(__file__)
caminho_imagem = os.path.join(caminho_atual, "folder.png")

caminho_imagem2 = os.path.join(caminho_atual, "plus.png")

imagem_dimensiona2 = Image.open(caminho_imagem2)
imagem_dimensiona = Image.open(caminho_imagem)
tamanho = (100,100)


img_dim = imagem_dimensiona.resize(tamanho)
img_dim2 = imagem_dimensiona2.resize(tamanho)

imagem_tk = ImageTk.PhotoImage(img_dim)
imagem_tks = ImageTk.PhotoImage(img_dim2)





btn = tk.Button(div1, text="Adicionar item",
                 image=imagem_tks, bd=0, relief='flat',highlightthickness=0 ,command= abrir_janela_adicionar)
btn.place(relx=0.5, rely=0.5, anchor="center")
btn.imagem = imagem_tk

lbl = tk.Label(div1, text="Abra o aplicativo de adicionar produtos")
lbl.place(rely=0.8, relx=0.5, anchor="center")

btn2 = tk.Button(div2, text="Consultar item",
                 image=imagem_tk,bd=0, relief='flat',highlightthickness=0, command= abrir_Projeto)
btn2.place(relx=0.5, rely=0.5, anchor="center")

lbl2 = tk.Label(div2, text="Abra o aplicativo de Consultador produtos")
lbl2.place(rely=0.8, relx=0.5, anchor="center")


janela.mainloop()