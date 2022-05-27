aluno = dict()
final = list()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
final.append(aluno.copy())
for k, v in aluno.items():
    print(f"- {k} é igual a {v}")
if aluno['media'] <= 5:
    print("- situação é igual a Reprovado")
elif 5 <= aluno['media'] <= 7:
    print("- situação é igual a Recuperação")
elif 7 < aluno['media']:
    print("- situação é igual a Aprovado")


