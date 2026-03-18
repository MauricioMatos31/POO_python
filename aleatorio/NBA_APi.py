import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFrame
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import commonplayerinfo, playercareerstats, commonteamroster

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

            media_pts = round(pontos / jogos, 1) if jogos > 0 else 0
            media_reb = round(rebotes / jogos, 1) if jogos > 0 else 0
            media_ast = round(assistencias / jogos, 1) if jogos > 0 else 0
            texto_carreira = (
                f"--- TOTAIS NA CARREIRA ---\n"
                f"Jogos: {jogos}\n"
                f"Pontos: {pontos}\n"
                f"Rebotes: {rebotes}\n"
                f"Assistências: {assistencias}\n\n"
                f"--- MÉDIAS POR JOGO ---\n"
                f"PTS: {media_pts}\n"
                f"REB: {media_reb}\n"
                f"AST: {media_ast}"
            )
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

def buscar_elenco():
    nome_time = inputTime.text().lower()
    labelCarreira.setText("")
    labelStatus.setText("")
    labelLogo.clear()

    try:
        lista_times = teams.get_teams()
        time_encontrado = None

        for t in lista_times:
            if nome_time in t['full_name'].lower():
                time_encontrado = t
                break

        if not time_encontrado:
            labelCarreira.setText("Time não encontrado")
            return

        team_id = time_encontrado["id"]
        team_abbr = time_encontrado["abbreviation"]

        
        logo_url = f"https://cdn.nba.com/logos/nba/{team_id}/primary/L/logo.svg"

        try:
            response_logo = requests.get(logo_url)
            if response_logo.status_code == 200:
                pixmap_logo = QPixmap()
                pixmap_logo.loadFromData(response_logo.content)
                labelLogo.setPixmap(
                    pixmap_logo.scaled(
                        120, 120,
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    )
                )
            else:
                labelLogo.setText("Logo não encontrada")
        except Exception:
            labelLogo.setText("Erro ao carregar logo")

        
        roster = commonteamroster.CommonTeamRoster(team_id=team_id)
        df = roster.get_data_frames()[0]

        texto = f'Elenco - {time_encontrado["full_name"]}\n\n'

        for index, row in df.iterrows():
            texto += f"{row['PLAYER']} - {row['POSITION']}\n"

        labelCarreira.setText(texto)
        labelStatus.setText("Elenco carregado com sucesso!")

    except Exception as e:
        labelCarreira.setText(f"Erro: {str(e)}")





def limpar_campos():
    inputNome.clear()
    labelFoto.clear()
    labelFoto.setText("A foto aparecerá aqui")
    labelStatus.clear()
    labelDados.clear()
    labelCarreira.clear()
    labelLogo.clear()

def limparInput():
    inputNome.clear()   


app = QApplication(sys.argv)
app.setStyleSheet("""
    QWidget {
        background-color: #121212;
        color: white;
    }
    QPushButton {
        background-color: #1f6feb;
        color: white;
        border-radius: 8px;
        padding: 6px;
    }
    QPushButton:hover {
        background-color: #388bfd;
    }
    QLineEdit {
        background-color: #1e1e1e;
        border: 1px solid #333;
        padding: 5px;
        border-radius: 5px;
        color: white;
    }
""")

janela = QWidget()
janela.setWindowTitle("NBA Status Simples")
janela.resize(400, 550)

inputNome = QLineEdit()
inputNome.setPlaceholderText("Nome do Jogador: Ex: LeBron James")
btnBuscar = QPushButton("Buscar")
btnLimpar = QPushButton("Limpar Tudo")

labelFoto = QLabel("A foto aparecerá aqui")
labelFoto.setAlignment(Qt.AlignCenter)
labelFoto.setFixedSize(260, 190)

labelLogo = QLabel("")
labelLogo.setAlignment(Qt.AlignCenter)
labelLogo.setFixedSize(120, 120)

labelDados = QLabel("")
labelDados.setAlignment(Qt.AlignCenter)
labelDados.setFont(QFont("Arial", 10, QFont.Bold))

labelCarreira = QLabel("")
labelCarreira.setAlignment(Qt.AlignCenter)

labelStatus = QLabel("")
labelStatus.setAlignment(Qt.AlignCenter)

inputTime = QLineEdit()
inputTime.setPlaceholderText("Nome do Time: Ex: Lakers")
btnElenco = QPushButton("Ver Elenco do Time")



layoutPrincipal = QVBoxLayout()
layoutTopo = QHBoxLayout()

layoutTopo.addWidget(inputNome)
layoutTopo.addWidget(btnBuscar)

layoutPrincipal.addLayout(layoutTopo)
layoutPrincipal.addWidget(inputTime)
layoutPrincipal.addWidget(btnElenco)
layoutPrincipal.addWidget(labelFoto, alignment=Qt.AlignCenter)
layoutPrincipal.addWidget(labelLogo, alignment=Qt.AlignCenter)
layoutPrincipal.addWidget(labelDados)

linha = QFrame()
linha.setFrameShape(QFrame.HLine)
layoutPrincipal.addWidget(linha)

layoutPrincipal.addWidget(labelCarreira)
layoutPrincipal.addStretch() 
layoutPrincipal.addWidget(labelStatus)
layoutPrincipal.addWidget(btnLimpar)


btnBuscar.clicked.connect(buscar_jogador)
btnElenco.clicked.connect(buscar_elenco)
inputNome.returnPressed.connect(buscar_jogador)
inputTime.returnPressed.connect(buscar_elenco)
inputNome.returnPressed.connect(limparInput)
btnLimpar.clicked.connect(limpar_campos)

janela.setLayout(layoutPrincipal)
janela.show()
sys.exit(app.exec_())