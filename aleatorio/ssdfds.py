import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QStackedWidget
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt



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

app = QApplication(sys.argv)

cadastro = QWidget()
cadastro.setWindowTitle("Cadastro")
cadastro.setGeometry(850, 300, 300, 800)


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


botaoConsultarCep = QPushButton("Consultar CEP", cadastro)
botaoConsultarCep.move(102, 610)
botaoConsultarCep.clicked.connect(tratarCep)

cadastro.show()
sys.exit(app.exec_())