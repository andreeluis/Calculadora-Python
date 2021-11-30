import func

print('-*-'*10)
print('-*- CALCULADORA EM PYTHON *-*-')

while True:
    termo1 = float(input('Digite o primeiro termo: '))
    operacao = str(input('Qual operação? ( + , - , x , / ) '))
    termo2 = float(input('Digite o segundo termo: '))
    
    func.getOperacao(operacao, termo1, termo2)

    continuar = str(input('Mais algum cálculo? ( S / N )'))

    if continuar in 'nN':
        break