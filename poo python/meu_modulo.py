import math 

def calculadora():
    operador = input("Digite o operador (+, -, *, /): ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        return num1 / num2 if num2 != 0 else "Divisão por zero não é permitida"

print(calculadora())
