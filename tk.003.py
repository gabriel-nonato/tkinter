from tkinter import *
import time
def cor_fundo():
    lb["text"] = "mudanças:\ncor de fundo"
    janela["bg"] = "gray"
    bt["text"] = "clicado"



janela = Tk()

bt = Button(janela,width=10,text="clieque-me",command=cor_fundo)
bt.place(x=100,y=100)

lb = Label(janela,text="ola")
lb.place(x=100,y=140)

janela.geometry("300x300+200+200")
janela.mainloop()