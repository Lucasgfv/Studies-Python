pessoas = dict()
lista = list()
idades = list()
soma = media = 0

while True:
    pessoas.clear()
    pessoas['Nome'] = str(input("Nome: "))
    pessoas['idade'] = int(input("Idade: "))
    soma += pessoas['idade']
    while True:
        pessoas['sexo'] = str(input("Sexo: [M/F] ")).upper()
        if pessoas['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoas_final = pessoas.copy()
    lista.append(pessoas_final)
    pessoas['media'] = sum(idades)
    while True:
        contin = str(input('Quer continuar? [S/N] ')).upper()
        if contin in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if contin == 'N':
        break
print("-=-"*30)
print(lista)
print("-=-"*30)
print(f'A) Ao todo foram cadastradas {len(lista)} pessoas cadastradas.')
media = soma / len(lista)
print(f'B) A media de idade é de {media:5.2f}')
print('C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["Nome"]}', end='')
print()
print(f'D) Lista de pessoas que estão acima da media: \n')
for p in lista:
    if p['idade'] > media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('<<ENCERRADO>>')