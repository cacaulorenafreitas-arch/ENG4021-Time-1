print("Hello, World!")


def calcula_soma(x, y):
    return x + y


def calcula_subtracao(x, y):
    return x - y


def calcula_multiplicacao(x, y):
    return x * y


def calcula_divisao(x, y):
    return x / y


def calcula_divisao_inteira(x, y):
    return x // y


def calcula_resto(x, y):
    return x % y


print("Escolha uma das opcoes abaixo:")
print("1 - Adicao")
print("2 - Subtracao")
print("3 - Multiplicacao")
print("4 - Divisao")
print("5 - Divisao inteira")
print("6 - Resto")
print("0 - Sair do programa")

opcao = input("Digite a opcao desejada: ")

while opcao != "0":
    if opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4" or opcao == "5" or opcao == "6":
        x = float(input("Digite o valor de x: "))
        y = float(input("Digite o valor de y: "))

        if opcao == "1":
            print("Resultado:", calcula_soma(x, y))
        elif opcao == "2":
            print("Resultado:", calcula_subtracao(x, y))
        elif opcao == "3":
            print("Resultado:", calcula_multiplicacao(x, y))
        elif opcao == "4":
            if y != 0:
                print("Resultado:", calcula_divisao(x, y))
            else:
                print("Nao e possivel dividir por zero.")
        elif opcao == "5":
            if y != 0:
                print("Resultado:", calcula_divisao_inteira(x, y))
            else:
                print("Nao e possivel dividir por zero.")
        elif opcao == "6":
            if y != 0:
                print("Resultado:", calcula_resto(x, y))
            else:
                print("Nao e possivel dividir por zero.")
    else:
        print("Opcao invalida.")

    print("\nEscolha uma das opcoes abaixo:")
    print("1 - Adicao")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    print("5 - Divisao inteira")
    print("6 - Resto")
    print("0 - Sair do programa")

    opcao = input("Digite a opcao desejada: ")

print("Programa encerrado.")