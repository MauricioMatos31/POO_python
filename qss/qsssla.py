import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5 import uic

app = QApplication(sys.argv)

janela = uic.loadUi("janela.ui")

def enviar_nome():
    nome = janela.caixaTexto.text()
    janela.labelTexto.setText(f"Olá, {nome}!")


janela.btnenviar.clicked.connect(enviar_nome)
janela.show()

sys.exit(app.exec_())