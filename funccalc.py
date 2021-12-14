global resultado
global display

global temp_num1
global temp_num2
global temp_sinal
global temp_op

temp_num1 = ''
temp_num2 = ''
temp_sinal = ''
temp_op = ''

def adicao(termo1 , termo2):
    global resultado
    resultado = termo1 + termo2

def subtração(termo1 , termo2):
    global resultado
    resultado = termo1 - termo2

def multiplicacao(termo1 , termo2):
    global resultado
    resultado = termo1 * termo2

def divisao(termo1 , termo2):
    global resultado
    resultado = termo1 / termo2

def get_operacao(operacao, termo1, termo2):
    global resultado
    if operacao in '+' or operacao == 'plus':
        adicao(termo1 , termo2)
    elif operacao in '-' or operacao == 'minus':
        subtração(termo1 , termo2)
    elif operacao in 'xX*' or operacao == 'multi':
        multiplicacao(termo1 , termo2)
    elif operacao in '/d' or operacao == 'div':
        divisao(termo1 , termo2)
    return resultado

def press_button(digit):
    global temp_num1
    global temp_sinal
    global temp_num2
    global temp_op
    global display


    if temp_num1 == '' and digit == 'minus':
        temp_sinal = '-'

    elif digit == 'equal':
        num1 = float(str(0) + temp_num1)
        num2 = float(str(0) + temp_num2)

        get_operacao(temp_op, num1, num2)

    elif temp_num1 != '' and temp_op == '' and (str(digit)== 'plus' or str(digit)== 'minus' or str(digit)== 'div' or str(digit)== 'multi'):

        temp_op = digit


    elif temp_num1 != '' and  temp_op != '' and ((digit == 'float' and temp_num2.count('float') ==0) or float(digit) or digit =='0'):

        temp_num2= temp_num2 + str(digit).replace('float','.')


    elif (digit == 'float' and temp_num2.count('float') ==0) or float(digit) or digit=='0':
        temp_num1 = temp_num1 + str(digit).replace('float','.')

    display = temp_num1 + 'op' + temp_num2
    return