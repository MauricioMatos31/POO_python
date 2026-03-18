import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox 

def saudacao(nome):
    return f"Olá, {nome}!"

input_nome = input("Digite seu nome: ")
print(saudacao(input_nome))
