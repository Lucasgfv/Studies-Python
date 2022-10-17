def Dissecando(a):
    result = type(a)
    print(f'O tipo primitivo de {a} valor é {result}')
    print('So tem espaços? ', a.isspace())
    print('É um numero? ', a.isnumeric())
    print('É alfanumerico? ', a.isalnum())
    print('É alfabetico?', a.isalpha())

valor = input("Digite um valor: ")
Dissecando(valor)