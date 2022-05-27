def area(largura, comprimento):
    area = largura * comprimento
    print(f"A área de um terreno {largura} X {comprimento} é de {area}m².")


print("Controle de Terrenos")
print('-'*30)
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
area(largura, comprimento)
