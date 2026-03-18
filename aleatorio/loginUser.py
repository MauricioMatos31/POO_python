import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QStackedWidget
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt



cursor = r"C:\Users\mauricio.msmatos\Downloads\icons8-dedo-do-meio-50.png"



#funcoes
def validarCadastro():
    usuario = inputUsuario.text()
    cpf = inputCpf.text()

    if usuario == "" or cpf == "":
        QMessageBox.warning(cadastro, "Campos vazios", "Por favor, preencha nome e cpf")
        limparCampos()
    elif usuario == cpf:
        QMessageBox.critical(cadastro, "Erro de cadastro", "Nome e cpf não podem ser iguais")
        limparCampos()
    elif usuario == "adm" and cpf == "12345678900":   
        QMessageBox.information(cadastro, "Cadastro bem sucedido", "Bem-vindo!")
        limparCampos()
    else:
        QMessageBox.critical(cadastro, "Erro de cadastro", "Usuário ou CPF inválidos")
        limparCampos()
 

def limparCampos():
    inputUsuario.clear()
    inputCpf.clear()
    inputLogradouro.clear()
    inputNumero.clear()
    inputComplemento.clear()
    inputBairro.clear()
    inputCidade.clear()
    inputUf.clear()
    inputDataNascimento.clear()
    inputNomeMae.clear()
    inputRg.clear()
    inputCpf.setFocus()





#app
app = QApplication(sys.argv)

#tela cadastro

cadastro = QWidget()
cadastro.setWindowTitle("Cadastro")
cadastro.setGeometry(850, 300, 300, 700)

pix_cursor = QPixmap(cursor)
cursor = QCursor(pix_cursor, hotX=0, hotY=0)
cadastro.setCursor(cursor)


labelUsuario = QLabel("Nome Completo: ", cadastro)
labelUsuario.move(80, 35)
inputUsuario = QLineEdit(cadastro)
inputUsuario.move(80, 50)

labelCpf = QLabel("Cpf:", cadastro)
labelCpf.move(80,85)
inputCpf = QLineEdit(cadastro)
inputCpf.move(80, 100)
inputCpf.setMaxLength(11)
inputCpf.setInputMask("000.000.000-00")
inputCpf.setCursorPosition(0)

labelLogradouro = QLabel("Logradouro:", cadastro)
labelLogradouro.move(80, 135)
inputLogradouro = QLineEdit(cadastro)
inputLogradouro.move(80, 150)

labelNumero = QLabel("Numero: ", cadastro)
labelNumero.move(80, 175)
inputNumero = QLineEdit(cadastro)
inputNumero.move(80, 190)
inputNumero.setInputMask("000000")

labelComplemento = QLabel("Complemento: ", cadastro)
labelComplemento.move(80, 220)
inputComplemento = QLineEdit(cadastro)
inputComplemento.move(80, 235)

labelBairro = QLabel("Bairro: ", cadastro)
labelBairro.move(80, 265)
inputBairro = QLineEdit(cadastro)
inputBairro.move(80, 280)

labelCidade = QLabel("Cidade: ", cadastro)
labelCidade.move(80, 320)
inputCidade = QLineEdit(cadastro)
inputCidade.move(80,335)

labelUf = QLabel("UF: ", cadastro)
labelUf.move(80, 365)
inputUf = QLineEdit(cadastro)
inputUf.move(80, 380)
inputUf.setMaxLength(2)


labelDataNascimento = QLabel("Data de Nascimento: ", cadastro)
labelDataNascimento.move(80, 410)
inputDataNascimento = QLineEdit(cadastro)
inputDataNascimento.move(80, 425)
inputDataNascimento.setInputMask("00/00/0000")

labelNomeMae = QLabel("Nome da Mãe: ", cadastro)
labelNomeMae.move(80, 460)
inputNomeMae = QLineEdit(cadastro)
inputNomeMae.move(80, 475)

labelRg = QLabel("RG: ", cadastro)
labelRg.move(80, 510)
inputRg = QLineEdit(cadastro)
inputRg.move(80, 525)
inputRg.setInputMask("00.000.000-0")
inputRg.setCursorPosition(0)

#botao cadastrar

botaoCadastrar = QPushButton("Cadastrar", cadastro)
botaoCadastrar.move(102, 580)
botaoCadastrar.clicked.connect(validarCadastro)

#botao limpar
botaoLimpar = QPushButton("Limpar", cadastro)  
botaoLimpar.move(102, 620)
botaoLimpar.clicked.connect(limparCampos)


#rodando tela de cadastro
cadastro.show()
sys.exit(app.exec_())
