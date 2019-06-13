# *-*coding: utf-8 *-*
import io
import sqlite3

# conectando...
conn = sqlite3.connect('flask.db')
# definindo um cursor
cur = conn.cursor()

# criando a tabela (schema)
cur.execute("""
        CREATE TABLE uploads (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                file TEXT NOT NULL,
                username TEXT
                );
        """)

print('Tabela flask criada com sucesso.')
# desconectando...
conn.close()
