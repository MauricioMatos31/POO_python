import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QMessageBox



def botao_clicado():
    print("voce clicou no botao!")
    QMessageBox.information(janelinha, "textto digitado ", f"Voce digitou: {caixaTexto.text()}")

app = QApplication(sys.argv)
janelinha = QWidget()
janelinha.setWindowTitle("Minha Janela")
janelinha.setGeometry(100, 100, 300, 200)

with open("estilo.qss", "r") as arquivo_qss:
    estilo = arquivo_qss.read()
    app.setStyleSheet(estilo)   

labelTexto = QLabel("clique no botao abaixo", janelinha)
labelTexto.move(130, 30)

botao = QPushButton("Clique aqui", janelinha)
botao.setObjectName('botap customizado')
botao.move(150, 70)

botao2 = QPushButton("botao 1 ", janelinha)
botao2.setObjectName('classeBotao')
botao2.move(80, 70)

botao3 = QPushButton("botao 2 ", janelinha)
botao3.setObjectName('classeBotao')
botao3.move(230, 70)

caixaTexto = QLineEdit(janelinha)
caixaTexto.move(130, 110)

botao.clicked.connect(botao_clicado)
janelinha.show()

sys.exit(app.exec_())