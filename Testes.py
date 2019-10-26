import pandas as pd
#  from tkinter import *

# janela = Tk()

# top = Toplevel(janela)
# def correct(inp):
#     if inp.isalpha():
#         return True
#     elif inp is "":
#         return True
#     else:
#         return False

# e = Entry(top)
# e.pack(side=TOP)

# reg = top.register(correct)
# e.config(validate="key", validatecommand=(reg, '%S'))

# mainloop()

try:
    planilha = pd.read_excel("Tabela\Palavras.xlsx")

    print(planilha)
except:
    print('Planilha Palavras.xlsx nao foi encontrada')
    
    
