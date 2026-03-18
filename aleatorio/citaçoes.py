citação = input("digite sua citação: ")
with open('citaçoes.txt', 'a') as arquivo:
    arquivo.write(citação + '\n')   

with open('citaçoes.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

