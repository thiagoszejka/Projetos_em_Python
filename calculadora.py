print('Olá, escolha um operador e os respectivos números para obter o resultado esperado.')

print('Digite a operação escolhida:\n\t+ para soma.\n\t- para subtração.\n\t* para multiplicação.\n\t/ para divisão.')

operador = input('Selecione a operação:')
n1 = input('Digite um valor:')
n2 = input('Digite outro valor:')

equacao = f'{n1} {operador} {n2}'

resultado = eval(equacao)

print(f'{resultado} é o resultado.')
