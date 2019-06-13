#*-*coding: utf-8 *-*
import io
import sqlite3

def createUpload(filename, username):  
   conn = sqlite3.connect('flask.db')
   cur = conn.cursor()
   cur.execute("""
        INSERT INTO uploads(file, username)
        VALUES (?,?)
        """,(filename,username))
   conn.commit()
   conn.close()

def getUploads():
    uploads = []
    conn = sqlite3.connect('flask.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
        SELECT * FROM uploads;
        """)

    for linha in cursor.fetchall():
        uploads.append(linha)

    conn.close()

    return uploads

def deleteUpload(id):
        print("ID", id)
        conn = sqlite3.connect('flask.db')
        cursor = conn.cursor()

        # excluindo um registro da tabela
        cursor.execute("""
        DELETE FROM uploads
        WHERE id = ?
        """, (id,))

        conn.commit()

        print('Registro excluido com sucesso.')

        conn.close()

def hello():
    print("teste")