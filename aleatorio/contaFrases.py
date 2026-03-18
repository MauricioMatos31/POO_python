import sys

def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)

if __name__ == "__main__":
    frase = input("Digite uma frase: ")
    quantidade = contar_palavras(frase)
    print(f"A frase contém {quantidade} palavras.")