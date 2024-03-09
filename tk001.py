import tkinter as tk

janela = tk.Tk()

# modificações
janela.title("janela principal")

# cor de fundo
janela["background"] = "gray"

# Largura x Altura + Distancia X + Distancia y
janela.geometry("800x600+100+100")



janela.mainloop()