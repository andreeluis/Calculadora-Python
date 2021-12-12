import calccmd


print('-*-'*12)
print('BEM VINDO A CALCULADORA MULTITOOLS')
print('-*-'*12)

modo = str(input('Você quer usar qual modo? [Gráfica/Comando] '))

if modo in "gG":
    pass

elif modo in "cC":
    calccmd.calc_comando()