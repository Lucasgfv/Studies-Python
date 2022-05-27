sexo = str(input('Digite seu sexo[M/F]: ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos! Digite novamente seu sexo: ')).upper().strip()
print('Fim! Seu sexo é {}, registrado com sucesso.'.format(sexo))