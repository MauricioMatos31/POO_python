import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QMessageBox
  
def botaoClicado():
    print("voce clicou no botão")
    QMessageBox.information(janelinha, "texto digitado", f"voce digitou: {caixaTexto.text()}")

app = QApplication(sys.argv)

#criando tela
janelinha = QWidget()

janelinha.setWindowTitle("primeira aplicação front end")

janelinha.setGeometry(900, 350, 450, 420)

#criando rotulo
textoRotulo = QLabel("clique no botão abaixo", janelinha )

textoRotulo.move(150, 20)

#criando botao
botao = QPushButton("clique aqui", janelinha )

botao.move(170, 80)

botao.clicked.connect(botaoClicado)

#criando caixa de texto
caixaTexto = QLineEdit(janelinha, placeholderText = 'digite algo aqui')

caixaTexto.move(130, 120)




#exibindo a janela
janelinha.show()

sys.exit(app.exec_())

app_.exec_()


