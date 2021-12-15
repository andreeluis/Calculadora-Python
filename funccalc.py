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