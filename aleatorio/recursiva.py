import sys

def recursiva_Fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursiva_Fibonacci(n - 1) + recursiva_Fibonacci(n - 2)
    
if __name__ == "__main__":
    n = int(input("Digite um número inteiro para calcular o Fibonacci: "))
    resultado = recursiva_Fibonacci(n)
    print(f"O {n}º número de Fibonacci é: {resultado}")