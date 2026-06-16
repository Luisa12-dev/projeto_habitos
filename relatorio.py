import sqlite3
from banco import conectar


def relatorio_por_usuario():
    print("\n============ RELATÓRIO GERAL POR USUÁRIO ============")
    try:
        id_usuario = int(input("Digite o ID do usuário: "))

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute('SELECT nome FROM usuarios WHERE id = ?', (id_usuario,))
        usuario = cursor.fetchone()

        if not usuario:
            print(f"Não existe um usuário com o ID {id_usuario}.")
            conn.close()
            return

        cursor.execute("""
            SELECT 
                habitos.nome AS nome_habito,
                COUNT(registros.id) AS total_registros,
                SUM(CASE 
                       WHEN registros.status = 'CONCLUÍDO' 
                        OR registros.status = 'CONCLUIDO'
                        OR registros.status = 'FEITO'
                        OR registros.status = 'REALIZADO'
                        OR registros.status = 'FEITOS'
                        OR registros.status = 'REALIZADOS'
                        OR registros.status = 'CONCLUÍDA'
                        OR registros.status = 'CONCLUIDA'
                        OR registros.status = 'FEITA'
                        OR registros.status = 'FEITAS'
                        OR registros.status = 'REALIZADAS'
                        OR registros.status = 'REALIZADA'
                    THEN 1 ELSE 0 END) AS realizados
            FROM habitos
            LEFT JOIN registros ON habitos.id = registros.id_habito
            WHERE habitos.id_usuario = ?
            GROUP BY habitos.id""", (id_usuario,))
#o SUM aqui está funcionando como um contador
# o LEFT JOIN junta as duas tabelas ( hábitos e registros)
        habitos = cursor.fetchall()
        conn.close()

        if not habitos:
            print("Não há hábitos registrados para gerar o relatório.")
            return
        
        for habito in habitos:
            nome = habito['nome_habito']
            total_dias = habito['total_registros']
            feitos = habito['realizados'] if habito['realizados'] else 0

            taxa_progresso = (feitos / total_dias * 100) if total_dias > 0 else 0.0
            print(f"Hábito : {nome}")
            print(f"Dias monitorados: {total_dias}")
            print(f"Metas cumpridas: {feitos}")
            print(f"Taxa de progresso: {taxa_progresso:.1f}%")

    except ValueError:
        print("\nOcorreu um erro ao gerar o relatório.\n ID inválido.")
    except Exception as e:
        print(f"\nErro inesperado: {e}")







def menu_relatorios():
    while True:
        print("\n=================== RELATÓRIOS GERAIS ===================")
        print("1. Total de usuários cadastrados")
        print("2. Total de hábitos registrados")
        print("3. Total de hábitos com status 'Concluído'")
        print("4. Total de hábitos com status 'Não Concluído'")
        print("5. Total de hábitos com status 'Parcialmente Concluído'")
        
        print("\n================= RELATÓRIOS POR USUÁRIO =================")
        
        print("=========================================================")