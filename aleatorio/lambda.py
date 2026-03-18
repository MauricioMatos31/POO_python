import sys

def lambda_quadrados(n):
    return list(map(lambda x: x**2, range(1, n + 1)))
if __name__ == "__main__":
    n = int(input("Digite um número inteiro: "))
    quadrados = lambda_quadrados(n)
    print(f"Os quadrados dos números de 1 a {n} são: {quadrados}")

    