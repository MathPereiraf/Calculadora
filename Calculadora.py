
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não permitida!"


def calculadora():
    print("Calculadora em Python")
    print("Escolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    escolha = input("Digite o número da operação (1/2/3/4): ")
    
    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"{num1} + {num2} = {somar(num1, num2)}")
        elif escolha == '2':
            print(f"{num1} - {num2} = {subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif escolha == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")
    else:
        print("Escolha inválida")


calculadora()

# UNIPE PROJETO PRATICO
