from tkinter import *
from tkinter import ttk
import funccalc


class Grafica:
    def __init__(self):
        root = Tk()
        janela = ttk.Frame(root,padding=30)
        janela.grid()
        ttk.Label(janela, text='CALCULADORA').grid(column=0, row=0, columnspan=4)
        ttk.Separator(janela, orient='horizontal').grid(row=1, columnspan=4, sticky='ew')

        Label(janela, text='oi').grid(column=0, columnspan=4, row=2)

        ttk.Separator(janela, orient='horizontal').grid(row=3, columnspan=4, sticky='ew')

        ttk.Button(janela, text='9', command= lambda:funccalc.press_button(9)).grid(column=2, row=4)
        ttk.Button(janela, text='8', command= lambda:funccalc.press_button(8)).grid(column=1, row=4)
        ttk.Button(janela, text='7', command= lambda:funccalc.press_button(7)).grid(column=0, row=4)

        ttk.Button(janela, text='6', command= lambda:funccalc.press_button(6)).grid(column=2, row=5)
        ttk.Button(janela, text='5', command= lambda:funccalc.press_button(5)).grid(column=1, row=5)
        ttk.Button(janela, text='4', command= lambda:funccalc.press_button(4)).grid(column=0, row=5)

        ttk.Button(janela, text='3', command= lambda:funccalc.press_button(3)).grid(column=2, row=6)
        ttk.Button(janela, text='2', command= lambda:funccalc.press_button(2)).grid(column=1, row=6)
        ttk.Button(janela, text='1', command= lambda:funccalc.press_button(1)).grid(column=0, row=6)

        ttk.Button(janela, text='0', command= lambda:funccalc.press_button('0')).grid(column=1, row=7)
        ttk.Button(janela, text='.', command= lambda:funccalc.press_button('float')).grid(column=2, row=7)
        ttk.Button(janela, text='=', command= lambda:funccalc.press_button('equal')).grid(column=3, row=8)

        ttk.Button(janela, text='/', command= lambda:funccalc.press_button('div')).grid(column=3, row=4)
        ttk.Button(janela, text='x', command= lambda:funccalc.press_button('multi')).grid(column=3, row=5)
        ttk.Button(janela, text='-', command= lambda:funccalc.press_button('minus')).grid(column=3, row=6)
        ttk.Button(janela, text='+', command= lambda:funccalc.press_button('plus')).grid(column=3, row=7)

        ttk.Button(janela, text='FECHAR', command=root.destroy).grid(column=0, row=8, columnspan=3, sticky= 'ew')

        root.mainloop() 

    def change():
        pass
Grafica()