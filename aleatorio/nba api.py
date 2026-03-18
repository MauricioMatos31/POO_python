import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFrame
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo, playercareerstats

def buscar_jogador():
    nome = inputNome.text().strip()
    if not nome:
        labelStatus.setText("Por favor, digite o nome de um jogador.")
        return
    
   
    lista_jogadores = players.find_players_by_full_name(nome)

    if lista_jogadores:
       
        jogador_id = lista_jogadores[0]["id"]
        nome_completo = lista_jogadores[0]["full_name"]
      
        foto_url = f"https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/{jogador_id}.png"
        try:
            response = requests.get(foto_url)
            if response.status_code == 200:
                pixmap = QPixmap()
                pixmap.loadFromData(response.content)
                labelFoto.setPixmap(pixmap)
            else:
                labelFoto.setText("Foto não disponível")
        except:
            labelFoto.setText("Erro ao carregar imagem")

        try:
            
            info = commonplayerinfo.CommonPlayerInfo(player_id=jogador_id)
            df = info.get_data_frames()[0]

            altura = df['HEIGHT'][0]
            peso = df['WEIGHT'][0]             
            posicao = df['POSITION'][0]
            time = f"{df['TEAM_CITY'][0]} {df['TEAM_NAME'][0]}"
            num = df['JERSEY'][0]
            metros = round(float(altura.split('-')[0]) * 0.3048 + float(altura.split('-')[1]) * 0.0254, 2)

            labelDados.setText(f"Nome: {nome_completo}\nTime: {time} (#{num})\n"
                               f"Posição: {posicao} | Altura: {altura} ft / {round(metros, 2)} m | Peso: {peso} lbs / {round(float(peso) * 0.453592, 1)} kg")

            
            carreira = playercareerstats.PlayerCareerStats(player_id=jogador_id)
            df_carreira = carreira.get_data_frames()[0]

            pontos = df_carreira['PTS'].sum()
            rebotes = df_carreira['REB'].sum()
            assistencias = df_carreira['AST'].sum()
            jogos = df_carreira['GP'].sum()

            texto_carreira = (f"--- TOTAIS NA CARREIRA ---\n"
                              f"Jogos: {jogos}\n"
                              f"Pontos: {pontos}\n"
                              f"Rebotes: {rebotes}\n"
                              f"Assistências: {assistencias}")
            
            labelCarreira.setText(texto_carreira)
            labelStatus.setText("Jogador encontrado com sucesso!")

        except Exception as e:
            print(f"Erro: {e}")
            labelStatus.setText("Erro ao obter detalhes do jogador.")
    
    else:
        
        labelStatus.setText("Jogador não encontrado.")
        labelDados.clear()
        labelCarreira.clear()
        labelFoto.setText("A foto aparecerá aqui")

def limpar_campos():
    inputNome.clear()
    labelFoto.clear()
    labelFoto.setText("A foto aparecerá aqui")
    labelStatus.clear()
    labelDados.clear()
    labelCarreira.clear()

def limparInput():
    inputNome.clear()   


app = QApplication(sys.argv)
janela = QWidget()
janela.setWindowTitle("NBA Stats Simples")
janela.resize(400, 550)

inputNome = QLineEdit()
inputNome.setPlaceholderText("Nome do Jogador: Ex: LeBron James")
btnBuscar = QPushButton("Buscar")
btnLimpar = QPushButton("Limpar Tudo")

labelFoto = QLabel("A foto aparecerá aqui")
labelFoto.setAlignment(Qt.AlignCenter)
labelFoto.setFixedSize(260, 190)

labelDados = QLabel("")
labelDados.setAlignment(Qt.AlignCenter)
labelDados.setFont(QFont("Arial", 10, QFont.Bold))

labelCarreira = QLabel("")
labelCarreira.setAlignment(Qt.AlignCenter)

labelStatus = QLabel("")
labelStatus.setAlignment(Qt.AlignCenter)

layoutPrincipal = QVBoxLayout()
layoutTopo = QHBoxLayout()

layoutTopo.addWidget(inputNome)
layoutTopo.addWidget(btnBuscar)

layoutPrincipal.addLayout(layoutTopo)
layoutPrincipal.addWidget(labelFoto, alignment=Qt.AlignCenter)
layoutPrincipal.addWidget(labelDados)

linha = QFrame()
linha.setFrameShape(QFrame.HLine)
layoutPrincipal.addWidget(linha)

layoutPrincipal.addWidget(labelCarreira)
layoutPrincipal.addStretch() 
layoutPrincipal.addWidget(labelStatus)
layoutPrincipal.addWidget(btnLimpar)

btnBuscar.clicked.connect(buscar_jogador)
inputNome.returnPressed.connect(buscar_jogador)
inputNome.returnPressed.connect(limparInput)
btnLimpar.clicked.connect(limpar_campos)

janela.setLayout(layoutPrincipal)
janela.show()
sys.exit(app.exec_())