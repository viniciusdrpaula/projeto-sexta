import pymysql

# Dados de conexão com o MySQL
host = 'localhost'
usuario = 'root'
nome_banco = 'projeto_flask'

# Conectando ao servidor MySQL sem senha
conexao = pymysql.connect(host=host, user=usuario)
cursor = conexao.cursor()

# Comando para criar o banco se não existir
sql = f"CREATE DATABASE IF NOT EXISTS {nome_banco} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
cursor.execute(sql)

print(f"✅ Banco de dados '{nome_banco}' criado (ou já existia).")

# Encerrando conexão
cursor.close()
conexao.close()
