def calc_comando():
    import funccalc

    print('-*-'*10)
    print('-*- CALCULADORA EM PYTHON *-*-')

    while True:
        termo1 = float(input('Digite o primeiro termo: '))
        operacao = str(input('Qual operação? ( + , - , x , / ) ')).strip()[0]
        termo2 = float(input('Digite o segundo termo: '))
        
        print(funccalc.get_operacao(operacao, termo1, termo2))

        continuar = str(input('Mais algum cálculo? ( S / N )'))

        if continuar in 'nN':
            break