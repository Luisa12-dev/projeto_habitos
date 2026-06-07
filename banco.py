import sqlite3
import os

BANCO = os.path.join(os.path.dirname(__file__), "habitos.db")

def conectar():
    conn = sqlite3.connect(BANCO)
    conn.row_factory = sqlite3.Row
    return conn

def inicializar_banco():
    conn = conectar()
    cursor = conn.cursor()
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            data_cadastro TEXT NOT NULL
         );
        CREATE TABLE IF NOT EXISTS habitos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER NOT NULL,
            nome TEXT NOT NULL,
            descricao TEXT,
            frequencia TEXT NOT NULL,
            meta TEXT NOT NULL
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
        );
        CREATE TABLE IF NOT EXISTS registros (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario  INTEGER NOT NULL,
            id_habito   INTEGER NOT NULL,
            data        TEXT    NOT NULL,
            status      TEXT    NOT NULL,
            observacao  TEXT,
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
            FOREIGN KEY (id_habito) REFERENCES habitos(id)
        );    
    """)
    conn.commit()
    conn.close()