def calcula_divisao_inteira(x, y):
    return x//y

def calcula_resto(x, y):
    return x%y

x= int(input("Digite o valor de x:"))
y= int(input("Digite o valor de y:"))

print("Divisão inteira:", calcula_divisao_inteira(x, y))
print("Resto:", calcula_resto(x, y))
