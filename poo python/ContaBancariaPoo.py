import sys


class contaBancaria:
    def __init__ (self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar (self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente")
        else: self.saldo -= valor

    @property
    def saldo(self):
       return self.__saldo
     
    @saldo.setter
    def saldo(self, valor):
       self.__saldo = valor  

c = contaBancaria(input("digite o nome do titular: "), float(input("digite o saldo inicial: ")))
                                         
while True:
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - ver saldo")
    print("4 - Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
      valor = float(input("digite o valor a ser depositado: ", c.depositar(valor)))
    elif opcao == "2":
     valor = float(input("digite o valor a ser sacado: "))
     c.sacar(valor)
    elif opcao == "3":
        print("Saldo atual: ", c.saldo)
    elif opcao == "4":
        print("Saindo...")
        break
    else:
      print("Opção inválida. Tente novamente.")