import calculadora


print('-*-'*12)
print('BEM VINDO A CALCULADORA MULTITOOLS')
print('-*-'*12)

modo = str(input('Você quer usar qual modo? [Gráfica/Comando] '))

if modo in "gG":
    print('teste')

elif modo in "cC":
    calculadora.calcComando()