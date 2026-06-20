import sqlite3
from banco import conectar


def relatorio_por_usuario():
    print("\n================= RELATÓRIO GERAL POR USUÁRIO =================")
    try:
        id_usuario = int(input("Digite o ID do usuário: "))

        conn = conectar()
        conn.row_factory = sqlite3.Row
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
                        OR registros.status = 'CUMPRIDA'
                        OR registros.status = 'CUMPRIDAS'
                        OR registros.status = 'CUMPRIDO'
                        OR registros.status = 'CUMPRIDOS'
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
        
        acumulador_total_dias = 0
        acumulador_total_feitos = 0

        for habito in habitos:
            nome = habito['nome_habito']
            total_dias = habito['total_registros']
            feitos = habito['realizados'] if habito['realizados'] else 0

            acumulador_dias_monitorados += total_dias
            acumulador_dias_cumpridos += feitos

            taxa_progresso = (feitos / total_dias * 100) if total_dias > 0 else 0.0
            print(f"Hábito :           {nome}")
            print(f"Dias monitorados:  {total_dias}")
            print(f"Dias cumpridos:    {feitos}")
            print(f"Taxa de progresso: {taxa_progresso:.1f}%")

            if acumulador_total_dias > 0:
                indice_geral = (acumulador_dias_cumpridos / acumulador_dias_monitorados) * 100
                print(f"ÍNDICE GERAL DE AUTOCUIDADO: {indice_geral:.1f}%")
                
                if indice_geral >= 80:
                    print("\nExcelente! Sua rotina demonstra um ótimo cuidado com a saúde.")
                elif indice_geral >= 50:
                    print("\nBom progresso! Continue firme em busca de mais consistência.")
                else:
                    print("\nLembrete: Pequenas ações diárias mudam sua saúde a longo prazo.")
            else:
                print("\nNenhuma atividade registrada nos hábitos ainda. Comece hoje!")
            print("=" * 63)

    except ValueError:
        print("\nOcorreu um erro ao gerar o relatório.\n ID inválido.")
    except Exception as e:
        print(f"\nErro inesperado: {e}")
'''
def relatorio_ultimos_7_dias():
    print("\n=================== Evolução dos Últimos 7 Dias ==================")
    try:
        conn = conectar()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute()










def menu_relatorios():
    while True:
        print("\n=================== RELATÓRIOS GERAIS ===================")
        print(" 1 - Resumo Geral por Usuário")
        print(" 2 - Evolução dos Últimos 7 Dias")
        print(" 3 - Ranking de Hábitos")
        print(" 4 - Total de usuários cadastrados")
        print(" 5 - Total de hábitos registrados")
        print(" 6 - Total de hábitos com status 'Concluído'")
        print(" 7 - Total de hábitos com status 'Não Concluído'")
        print(" 8 - Total de hábitos com status 'Parcialmente Concluído'")
        print(" 0 - voltar")
        
        selecione = input("Escolha a opção desejada: ").upper()

        if selecione == "1":
            relatorio_por_usuario()
            
        elif selecione == "2":
            relatorio_ultimos_7_dias()
            
        elif selecione == "3":
            relatorio_ranking()
            
        elif selecione == "4":
            # Aqui você pode chamar a função que criamos lá no começo
            # Ex: mostrar_total_usuarios() ou rodar o bloco direto
            pass 
            
        elif selecione == "5":
            # Ex: mostrar_total_habitos()
            pass
            
        elif selecione == "6":
            # Filtra por 'CONCLUÍDO'
            pass
            
        elif selecione == "7":
            # Filtra por 'NÃO CONCLUÍDO'
            pass
            
        elif selecione == "8":
            # Filtra por 'PARCIALMENTE CONCLUÍDO'
            pass
            
        elif selecione == "0":
            print("Voltando ao menu principal...")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

        if selecione in['1', 'OPÇÃO 1', 'OPCAO 1', 'USUÁRIOS CADASTRADOS', 'USUARIOS CADASTRADOS', 'TOTAL DE USUARIOS CADASTRADOS', 'TOTAL DE USUÁRIOS CADASTRADOS']:

            conn.row_factory = sqlite3.Row
            conn = conectar()
            cursor = conn.cursor()

            cursor.execute('SELECT nome FROM usuarios')
            usuarios = cursor.fetchall()

            print(f"\nTotal de usuários no sistema: {len(usuarios)}\n")
            
            print("USUÁRIOS CADASTRADOS")
            for usuario in usuarios:
                print(f"- {usuario['nome']}") 
            
            conn.close()'''
        

# 1. Conecte ao banco (conn = conectar())
# 2. Crie o cursor
# 3. Execute o SQL: "SELECT COUNT(*) FROM usuarios"
# 4. Pegar o resultado: resultado = cursor.fetchone()
# 5. Dar um print legível, buscando a posição 0: resultado[0]
# 6. Fechar a conexão (conn.close())
#pass # Apague o pass quando escrever seu código  