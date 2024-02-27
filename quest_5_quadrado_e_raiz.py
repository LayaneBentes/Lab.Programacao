while True:

    num1 = float(input('1° valor: '))
    num2 = float(input('2° valor: '))

    if num1 > num2:
        raiz_quadrada = num1 ** (1/2)
        potenciacao = num2 ** 2

        if num1 < 0:
            print(f'{potenciacao:.2f}')
        else:
            print(f'{potenciacao:.2f} {raiz_quadrada:.2f}')


    else:
        raiz_quadrada = num2 ** (1/2)
        potenciacao = num1 ** 2

        if num2 < 0:
            print(f'{potenciacao:.2f}')
        else:
            print(f'{potenciacao:.2f} {raiz_quadrada:.2f}')