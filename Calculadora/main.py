import os

def abertura(texto):
    linhas = "*" * (len(texto) + 4)
    print(linhas)
    print(f"* {texto} *")
    print(linhas)
    print()

def result(operacao, resultado):
    print(f"O resultado da {operacao} é {resultado}\n")

def soma(op):
    abertura(op)
    a, b = map(int, input("Escolha os valores a serem somados: ").split())
    result(op, a + b)
    main()

def subtracao(op):
    abertura(op)
    a, b = map(int, input("Escolha os valores a serem subtraidos: ").split())
    result(op, a - b)
    main()

def multiplica(op):
    abertura(op)
    a, b = map(int, input("Escolha os valores a serem multiplicados: ").split())
    result(op, a * b)
    main()

def divide(op):
    abertura(op)
    a, b = map(int, input("Escolha os valores a serem divididos: ").split())
    result(op, a / b)
    main()

def main():
    abertura("Calculadora")

    print("Selecione a operação desejada:\n")
    print("\t1 - Soma")
    print("\t2 - Subtração")
    print("\t3 - Multiplicação")
    print("\t4 - Divisão")

    option = int(input("\nOperação: "))
    print()

    match option:
        case 1:
            soma("Soma")
        case 2:
            subtracao("Subtração")
        case 3:
            multiplica("Multiplicação")
        case 4:
            divide("Divisão")
        case _:
            os.system("clear")

if __name__ == "__main__":
    os.system("clear")
    main()
    