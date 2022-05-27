from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
idades = int(input('Ano de nacimento: '))
pessoa['idade'] = datetime.now().year - idades
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['ctps'] == 0:
    for k, v in pessoa.items():
        print(f'{k} tem o valor {v}')
if pessoa['ctps'] != 0:
    pessoa['Contratação'] = int(input(('Ano de Contratação: ')))
    pessoa['Salario'] = float(input('Salario: '))
    for k, v in pessoa.items():
        print(f'{k} tem o valor {v}')
