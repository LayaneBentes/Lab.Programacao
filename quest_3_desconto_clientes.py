while True:
    produto = float(input('Informe o valor do porduto: '))
    print('')
    desconto = (produto * 9)/100 
    novo_valor = produto - desconto
    print(f'Novo valor: {novo_valor :.2f}')
    print(f'Valor do desconto: {desconto :.2f}')