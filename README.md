# API de armazenamento de dados de um formulario
É uma API bem simples, ela recebe dados de um [formulario](https://github.com/gabicjo/formulario) com perguntas já definidas.
## Funcionalidades:
- Receber dados pelo endpoint `/enviar_dados`
- Guardar dados em um banco de dados relacional local (sqlite3)
## Tecnologias:
- Python
- Flask
- SQL
- sqlite3
## Como rodar?
```
git clone https://github.com/gabicjo/pesquisa-api.git
cd pesquisa-api
pip install -r requirements.txt
python server.py
```
## Possiveis melhorias:
- Metodo GET para exibir os usuarios que já responderam
- Criar uma tabela nova caso as opções não correspondam a tabela atual
- Metodo DELETE para excluir respostas dos usuarios
