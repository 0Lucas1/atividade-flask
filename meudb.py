import sqlite3

class Tabela:
    
    
    def __init__(self,nome: str):
        conn = sqlite3.connect("computer.db")
        cursor = conn.cursor()
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS computador(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nomeComputador VARCHAR(30) NOT NULL,
            descricaoEssencial VARCHAR(30) NOT NULL,
            precoRS REAL NOT NULL
            );
        """)
        self.nome_tabela = nome
        conn.close()
    
    
    def adicionar_computador(self,nome: str, descricao: str, preco: float):
        conn = sqlite3.connect("computer.db")
        cursor = conn.cursor()
        cursor.execute(f"""
        INSERT INTO computador(nomeComputador, descricaoEssencial, precoRS)
        VALUES('{nome}','{descricao}', {preco});  """)
        conn.commit()
        conn.close()
    
        
    def selecionar_todos_registros(self):
        conn = sqlite3.connect("computer.db")
        cursor = conn.cursor()
        selecao = cursor.execute("SELECT * FROM computador")
        registros = []
        for registro in cursor.fetchall():
            registros.append({
                'id': registro[0],
                'nomeComputador': registro[1],
                'descricaoEssencial': registro[2],
                'precoRS': registro[3]
            })
        conn.close()
        return registros
    
    
    def deletar_registro(self, id: int):
        conn = sqlite3.connect("computer.db")
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM computador WHERE id = {id}")
        conn.commit()
        conn.close()
        
        
    def atualizar_registro(self,nome: str, descricao: str, preco: float, id: int):
        conn = sqlite3.connect("computer.db")
        cursor = conn.cursor()
        cursor.execute(f"""
            UPDATE computador SET nomeComputador = '{nome}', descricaoEssencial = '{descricao}', precoRS = {preco}
            WHERE  id = {id}""")
        conn.commit()
        conn.close()
        
        
obj_computador = Tabela("TabelaComputador")
obj_computador.adicionar_computador("supercomputador", "potente",1_500_000_000.0)
obj_computador.adicionar_computador("microcontrolador", "computador pequenino", 70.0)