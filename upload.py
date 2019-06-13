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
    conn = sqlite3.connect('flask.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
        SELECT * FROM uploads;
        """)

    for linha in cursor.fetchall():
        return linha[1]

    conn.close()