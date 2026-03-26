import sqlite3

COLUNAS_VALIDAS = {
    "nome", "idade", "usaFones", "tempoFones", "volumeUso",
    "somAltoSemUso", "fonesAmbienteBarulhento", "aumentaVolumeAbafar",
    "zumbido", "dificuldadeEntenderFala", "volumeTvCelular",
    "dorAposSomAlto", "audicaoAbafada", "lugaresSomMuitoAlto",
    "usaProtecao", "otiteOuInfeccao", "fezExameAudicao",
    "ouvidoTampado", "familiaProblemasAuditivos"
}

def receber_dados_da_api(dados: dict) -> None:
    
    dados_filtrados = {k: v for k, v in dados.items() if k in COLUNAS_VALIDAS}

    if "idade" in dados_filtrados:
        dados_filtrados["idade"] = int(dados_filtrados["idade"])

    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS respostas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER,
    usaFones TEXT,
    tempoFones TEXT,
    volumeUso TEXT,
    somAltoSemUso TEXT,
    fonesAmbienteBarulhento TEXT,
    aumentaVolumeAbafar TEXT,
    zumbido TEXT,
    dificuldadeEntenderFala TEXT,
    volumeTvCelular TEXT,
    dorAposSomAlto TEXT,
    audicaoAbafada TEXT,
    lugaresSomMuitoAlto TEXT,
    usaProtecao TEXT,
    otiteOuInfeccao TEXT,
    fezExameAudicao TEXT,
    ouvidoTampado TEXT,
    familiaProblemasAuditivos TEXT
)
""")

    colunas = ', '.join(dados_filtrados.keys())
    placeholders = ', '.join(['?'] * len(dados_filtrados))

    query = f"INSERT INTO respostas ({colunas}) VALUES ({placeholders})"

    cursor.execute(query, tuple(dados_filtrados.values()))

    conexao.commit()
    conexao.close()