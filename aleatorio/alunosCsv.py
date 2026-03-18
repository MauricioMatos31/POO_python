import csv
import os

alunos = [
    ['nome', 'idade', 'nota']
]

while True:
 if not os.path.exists('alunos.csv'):
    with open('alunos.csv', 'w', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo)
        escritor_csv.writerows(alunos)

 with open('alunos.csv', 'r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    for linha in leitor_csv:
        print(linha)

 opçao = input("Digite 1 para adicionar um aluno, 2 para ler os alunos, ou 3 para sair: ")
 if opçao == '1':
    nome = input("Digite o nome do aluno: ")
    idade = input("Digite a idade do aluno: ")
    nota = input("Digite a nota do aluno: ")
    with open('alunos.csv', 'a', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo)
        escritor_csv.writerow([nome, idade, nota])
 elif opçao == '2':
    with open('alunos.csv', 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for linha in leitor_csv:
            print(linha)
 elif opçao == '3':
    break
 else:
    print("Opção inválida. Tente novamente.")