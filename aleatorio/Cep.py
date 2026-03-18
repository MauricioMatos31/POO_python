import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QStackedWidget
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt

cursor = r"C:\Users\mauricio.msmatos\Downloads\icons8-dedo-do-meio-50.png"

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


def tratarCep(codigoCep):
    url = f"https://viacep.com.br/ws/{codigoCep}/json/"
    
    try:
        response = requests.get(url)

        if response.status_code == 200:
            dados = response.json()

            if dados.get("erro") == "true":
                QMessageBox.warning(cadastro, "CEP inválido", "O CEP informado é inválido. Por favor, verifique e tente novamente.")
            else:
                inputLogradouro.setText(dados.get("logradouro", ""))
                inputBairro.setText(dados.get("bairro", ""))
                inputCidade.setText(dados.get("localidade", ""))
                inputUf.setText(dados.get("uf", ""))
                QMessageBox.information(cadastro, "CEP encontrado", "Endereço preenchido com sucesso!")
        else:
            QMessageBox.critical(cadastro, "Erro de conexão", f"Erro na requisição. Código de status: {response.status_code}")
    except Exception as e:
            QMessageBox.critical(cadastro, "Erro", f"Ocorreu uma exceção: {str(e)}")




   
#app
app = QApplication(sys.argv)

#tela cadastro

cadastro = QWidget()
cadastro.setWindowTitle("Cadastro")
cadastro.setGeometry(850, 300, 300, 800)

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

labelCep = QLabel('Cep: ', cadastro)
labelCep.move(80,120)
inputCep = QLineEdit(cadastro)
inputCep.move(80,135)



labelLogradouro = QLabel("Logradouro:", cadastro)
labelLogradouro.move(80, 165)
inputLogradouro = QLineEdit(cadastro)
inputLogradouro.move(80, 180)
inputLogradouro.setEnabled(False)

labelNumero = QLabel("Numero: ", cadastro)
labelNumero.move(80, 205)
inputNumero = QLineEdit(cadastro)
inputNumero.move(80, 220)
inputNumero.setInputMask("000000")

labelComplemento = QLabel("Complemento: ", cadastro)
labelComplemento.move(80, 260)
inputComplemento = QLineEdit(cadastro)
inputComplemento.move(80, 275)

labelBairro = QLabel("Bairro: ", cadastro)
labelBairro.move(80, 305)
inputBairro = QLineEdit(cadastro)
inputBairro.move(80, 325)
inputBairro.setEnabled(False)


labelCidade = QLabel("Cidade: ", cadastro)
labelCidade.move(80, 360)
inputCidade = QLineEdit(cadastro)
inputCidade.move(80,375)
inputCidade.setEnabled(False)   


labelUf = QLabel("UF: ", cadastro)
labelUf.move(80, 400)
inputUf = QLineEdit(cadastro)
inputUf.move(80, 415)
inputUf.setMaxLength(2)
inputUf.setEnabled(False)

labelDataNascimento = QLabel("Data de Nascimento: ", cadastro)
labelDataNascimento.move(80, 450)
inputDataNascimento = QLineEdit(cadastro)
inputDataNascimento.move(80, 465)
inputDataNascimento.setInputMask("00/00/0000")

labelNomeMae = QLabel("Nome da Mãe: ", cadastro)
labelNomeMae.move(80, 500)
inputNomeMae = QLineEdit(cadastro)
inputNomeMae.move(80, 515)

labelRg = QLabel("RG: ", cadastro)
labelRg.move(80, 550)
inputRg = QLineEdit(cadastro)
inputRg.move(80, 565)
inputRg.setInputMask("00.000.000-0")
inputRg.setCursorPosition(0)

#botao cadastrar

botaoCadastrar = QPushButton("Cadastrar", cadastro)
botaoCadastrar.move(102, 650)
botaoCadastrar.clicked.connect(validarCadastro)

#botao limpar
botaoLimpar = QPushButton("Limpar", cadastro)  
botaoLimpar.move(102, 680)
botaoLimpar.clicked.connect(limparCampos)

#botao consultar cep
botaoConsultarCep = QPushButton("Consultar CEP", cadastro)
botaoConsultarCep.move(102, 610)
botaoConsultarCep.clicked.connect(tratarCep)
#rodando tela de cadastro
cadastro.show()
sys.exit(app.exec_())