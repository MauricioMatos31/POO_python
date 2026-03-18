import sys

def divisor():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    
    if b != 0:
        resultado = a / b
        print(f"O resultado de {a} dividido por {b} é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")


if __name__ == "__main__": 
    divisor()   

print(f"O valor de a é: {a}")
