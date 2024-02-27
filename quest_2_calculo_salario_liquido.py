while True:
    hora_aula = float(input('Valor da hora aula: '))
    n_aulas = int(input('Número de aulas: '))
    inss = float(input('Percentual do INSS: '))

    salario_liquido = hora_aula * n_aulas #calculo salario
    percentual_inss = (inss * salario_liquido)/100 # calculo do percentual
    salario_final = salario_liquido - percentual_inss # subtração do percentual no salario
    print(round(salario_final, 2)) # round formatação de casas decimais
