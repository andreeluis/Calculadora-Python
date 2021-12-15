from tkinter import *
from tkinter import ttk
import funccalc

global temp_num1
global temp_num2
global temp_op
global equal

temp_num1 = ''
temp_num2 = ''
temp_sinal = ''
temp_op = ''
equal = False

class Grafica:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('CALCULADORA')
        self.janela.geometry('320x300')

        self.display = StringVar()

        Label(self.janela, textvariable= self.display).grid(column=0, row=0, columnspan=4)


        ttk.Button(self.janela, text='9', command= lambda:self.press_button(9)).grid(column=2, row=2)
        ttk.Button(self.janela, text='8', command= lambda:self.press_button(8)).grid(column=1, row=2)
        ttk.Button(self.janela, text='7', command= lambda:self.press_button(7)).grid(column=0, row=2)

        ttk.Button(self.janela, text='6', command= lambda:self.press_button(6)).grid(column=2, row=3)
        ttk.Button(self.janela, text='5', command= lambda:self.press_button(5)).grid(column=1, row=3)
        ttk.Button(self.janela, text='4', command= lambda:self.press_button(4)).grid(column=0, row=3)

        ttk.Button(self.janela, text='3', command= lambda:self.press_button(3)).grid(column=2, row=4)
        ttk.Button(self.janela, text='2', command= lambda:self.press_button(2)).grid(column=1, row=4)
        ttk.Button(self.janela, text='1', command= lambda:self.press_button(1)).grid(column=0, row=4)

        ttk.Button(self.janela, text='0', command= lambda:self.press_button('0')).grid(column=1, row=5)
        ttk.Button(self.janela, text='.', command= lambda:self.press_button('float')).grid(column=2, row=5)
        ttk.Button(self.janela, text='=', command= lambda:self.press_button('equal')).grid(column=2, row=6, columnspan=3, sticky= 'ew')

        ttk.Button(self.janela, text='/', command= lambda:self.press_button('div')).grid(column=3, row=2)
        ttk.Button(self.janela, text='x', command= lambda:self.press_button('multi')).grid(column=3, row=3)
        ttk.Button(self.janela, text='-', command= lambda:self.press_button('minus')).grid(column=3, row=4)
        ttk.Button(self.janela, text='+', command= lambda:self.press_button('plus')).grid(column=3, row=5)

        ttk.Button(self.janela, text='FECHAR', command=self.janela.destroy).grid(column=0, row=7, columnspan=4, sticky= 'ew')
        
        self.change_display
        self.janela.mainloop() 
        

    def press_button(self, digit):
        global temp_num1
        global temp_num2
        global temp_op
        global equal

        if temp_num1 == '' and digit == 'minus':
            temp_num1 = '-'


        elif digit == 'equal':
            equal = True
            
        elif temp_num1 != '' and temp_op == '' and (str(digit)== 'plus' or str(digit)== 'minus' or str(digit)== 'div' or str(digit)== 'multi'):

            temp_op = digit


        elif temp_num1 != '' and  temp_op != '' and ((digit == 'float' and temp_num2.count('float') ==0) or float(digit) or digit =='0'):

            temp_num2= temp_num2 + str(digit).replace('float','.')


        elif (digit == 'float' and temp_num2.count('float') ==0) or float(digit) or digit=='0':
            temp_num1 = temp_num1 + str(digit).replace('float','.')
        

        self.change_display(temp_num1, temp_num2, temp_op)

    def change_display(self, num1, num2, op):
        global equal
        operation = ''

        if op == 'plus':
            operation = '+'

        elif op == 'minus':
            operation = '-'

        elif op == 'multi':
            operation = 'x'

        elif op == 'div':
            operation = '/'


        display = str(num1) + str(operation) + str(num2)

        if equal == True:
            resultado = funccalc.get_operacao(operation, float(num1), float(num2))
            display = display + '=' + str(resultado)

        self.display.set(display)

        
            
Grafica()