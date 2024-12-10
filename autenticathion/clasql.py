import sqlite3 as sq
import hashlib as hl


class SQLITE:
    def __init__(self, nome_banco: str):
        self.nome_banco = nome_banco

    def conectar_banco(self):
        database = sq.connect(f"assets/databases/{self.nome_banco}.db")
        cursor = database.cursor()

        return database, cursor

    def criar_tabela(self, nome_tabela, colunas: list, tipo_coluna: list):
        if type(colunas) == list and type(tipo_coluna) == list:
            if len(colunas) == len(tipo_coluna):
                database, cursor = self.conectar_banco()
                _colunas = []

                for i in range(len(colunas)):
                    _colunas.append(f"{colunas[i]} {tipo_coluna[i]}")

                coluna_sql = ",".join(_colunas)

                cursor.execute(
                    f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({coluna_sql})"
                )

            else:
                print("Impossível criar tabela")
        else:
            print("Impossível criar tabela")

    def inserir_dados(self, nome_tabela: str, colunas: list, dados: list):
        if type(colunas) == list and type(dados) == list:
            if len(colunas) == len(dados):
                database, cursor = self.conectar_banco()
                Dados = []

                for dado in dados:
                    if type(dado) == str:
                        Dados.append(f"'{dado}'")
                    else:
                        Dados.append(str(dado))

                colunas_sql = ",".join(colunas)
                dados_sql = ",".join(Dados)

                print(f"INSERT INTO {nome_tabela} ({colunas_sql}) VALUES ({dados_sql})")

                cursor.execute(
                    f"INSERT INTO {nome_tabela} ({colunas_sql}) VALUES ({dados_sql})"
                )
                database.commit()
                database.close()
            else:
                print("Impossível salvar os dados")
        else:
            print("Impossível salvar os dados")

    def editar_dados(
        self, nome_tabela: str, coluna: str, valor: str, conditions: str = ""
    ):

        database, cursor = self.conectar_banco()

        if conditions == "":
            cursor.execute(f"UPDATE {nome_tabela} SET {coluna} = {valor}")
        else:
            cursor.execute(
                f"UPDATE {nome_tabela} SET {coluna} = {valor} WHERE {conditions}"
            )

        database.commit()
        database.close()

    def apagar_dados(self, nome_tabela: str, str, conditions: str = ""):
        database, cursor = self.conectar_banco()

        if conditions == "":
            cursor.execute(f"DELETE TABLE {nome_tabela}")
        else:
            cursor.execute(f"DELETE TABLE {nome_tabela} WHERE {conditions}")

        database.commit()
        database.close()

    def ver_dados(self, nome_tabela: str, colunas: list = "*", conditions: str = ""):
        database, cursor = self.conectar_banco()
        coluna_sql = ",".join(colunas)

        if conditions == "":
            cursor.execute(f"SELECT {coluna_sql} FROM {nome_tabela}")
        else:
            cursor.execute(f"SELECT {coluna_sql} FROM {nome_tabela} WHERE {conditions}")

        dados = cursor.fetchall()
        database.commit()
        database.close

        return dados

    def encrypt_password(self, senha: str):
        hash = hl.sha512()
        hash.update(bytes(senha, "UTF-8"))

        password_hashed = hash.hexdigest()

        return password_hashed


# sqlite = SQLITE("users")
# sqlite.criar_tabela(
#     nome_tabela="usuarios",
#     colunas=["nome", "idade", "senha"],
#     tipo_coluna=["TEXT", "INTEGER", "TEXT"],
# )

# senha = sqlite.encrypt_password(senha="senha123")

# sqlite.inserir_dados(
#     nome_tabela="usuarios",
#     colunas=["nome", "idade", "senha"],
#     dados=["Djalma", "58", senha],
# )

# sqlite.editar_dados(
#     nome_tabela="usuarios", coluna="idade", valor="46", conditions="idade = 35"
# )

# print(sqlite.ver_dados("usuarios"))
