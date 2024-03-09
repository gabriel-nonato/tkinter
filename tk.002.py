import tkinter as tk

janela = tk.Tk()

lb = tk.Label(janela, text="OLAAA!!!")

lb.place(x=100, y=100)

janela.geometry("300x300+100+100")

janela.mainloop()

