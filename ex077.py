palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
print('Leitor de vogais')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')