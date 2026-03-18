import sys

def soma_produto():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    
    soma = a + b
    produto = a * b
    
    print(f"A soma de {a} e {b} é: {soma}")
    print(f"O produto de {a} e {b} é: {produto}")

if __name__ == "__main__":
    soma_produto()

    