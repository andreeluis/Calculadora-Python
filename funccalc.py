global resultado

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

def getOperacao(operacao, termo1, termo2):
    global resultado
    if operacao in '+':
        adicao(termo1 , termo2)
    elif operacao in '-':
        subtração(termo1 , termo2)
    elif operacao in 'xX*':
        multiplicacao(termo1 , termo2)
    elif operacao in '/d':
        divisao(termo1 , termo2)
    print(f'O resultado é: {resultado}')