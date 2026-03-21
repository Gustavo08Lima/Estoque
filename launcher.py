import tkinter as tk
import subprocess 
import os
from PIL import Image, ImageTk


janela = tk.Tk()
janela.geometry("900x500")
janela.title("Launcher")
janela.config(bg="#1C60E6")


titulo = tk.Label(janela,text="Escolha o APP", font="Arial, 15 ",fg="white", bg="#1C60E6")
titulo.pack(pady=(20,0))

#DIVs

cont = tk.Frame(janela, bg="#1C60E6")
cont.pack(expand=True)

div1 = tk.Frame(cont, width=350,height=350, bd=2, relief='solid')
div1.pack(side='left', padx=30)
div1.pack_propagate(False)

div2 = tk.Frame(cont, width=350,height=350, bd=2, relief='solid')
div2.pack(side='left', padx=30)
div2.pack_propagate(False)

#FUNÇÃO PARA ABRIR APP
def abrir_janela_adicionar():
    if os.path.exists("janela_de_adicionar.exe"):
        subprocess.Popen(["janela_de_adicionar.exe"])
    else:
        subprocess.Popen(["python", "janela_de_adicionar.py"])

    janela.destroy()

def abrir_Projeto():
    if os.path.exists("Projeto.exe"):
        subprocess.Popen(["Projeto.exe"])
    else:
        subprocess.Popen(["python", "Projeto.py"])
    
    janela.destroy()




caminho_imagem2 = Image.open("imagem/plus.png")
caminho_imagem = Image.open("imagem/folder.png")


tamanho = (100,100)


img_dim = caminho_imagem.resize(tamanho)
img_dim2 = caminho_imagem2.resize(tamanho)

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