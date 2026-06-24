import sqlite3


def get_conexao():
    conexao = sqlite3.connect("banco.db")
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS habitos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            nome TEXT NOT NULL,
            descricao TEXT,
            frequencia TEXT NOT NULL,
            meta INTEGER NOT NULL
        )
    """)
    conexao.commit()
    return conexao


def listar_habitos_por_usuario(cursor, usuario_id):
    cursor.execute(
        "SELECT id, nome, frequencia, meta FROM habitos WHERE usuario_id=?",
        (usuario_id,),
    )
    habitos = cursor.fetchall()

    if not habitos:
        print("\nNenhum hábito encontrado.")
        return False

    print("\nHÁBITOS:")
    for habito in habitos:
        print(
            f"ID: {habito[0]} | "
            f"Nome: {habito[1]} | "
            f"Frequência: {habito[2]} | "
            f"Meta: {habito[3]}"
        )
    return True


def escolher_frequencia(atual=None):
    if atual:
        print(f"Frequência atual: {atual}")
        print("1 - Diária | 2 - Semanal | 3 - Mensal | ENTER - Manter")
    else:
        print("\nEscolha a frequência:")
        print("1 - Diária")
        print("2 - Semanal")
        print("3 - Mensal")

    op = input("Opção: ")
    opcoes = {"1": "Diária", "2": "Semanal", "3": "Mensal"}

    if op in opcoes:
        return opcoes[op]
    elif atual and op == "":
        return atual
    else:
        return None


def cadastrar(conexao, cursor):
    print("\nCADASTRAR NOVO HÁBITO")
    try:
        usuario_id = int(input("Digite o ID do usuário: "))
        nome = input("Nome do hábito: ").strip()
        if not nome:
            print("O nome do hábito não pode ser vazio.")
            return

        descricao = input("Descrição (opcional): ").strip() or None

        frequencia = escolher_frequencia()
        if not frequencia:
            print("Opção inválida!")
            return

        meta = int(input("Meta (número de vezes): "))
        if meta <= 0:
            print("A meta deve ser um número positivo.")
            return

        cursor.execute(
            """
            INSERT INTO habitos (usuario_id, nome, descricao, frequencia, meta)
            VALUES (?, ?, ?, ?, ?)
            """,
            (usuario_id, nome, descricao, frequencia, meta),
        )
        conexao.commit()
        print("\nHábito cadastrado com sucesso!")

    except ValueError:
        print("Digite apenas números onde for solicitado.")


def listar(cursor):
    try:
        usuario_id = int(input("Digite o ID do usuário: "))
        listar_habitos_por_usuario(cursor, usuario_id)
    except ValueError:
        print("Digite um ID válido.")


def editar(conexao, cursor):
    try:
        usuario_id = int(input("Digite o ID do usuário: "))

        if not listar_habitos_por_usuario(cursor, usuario_id):
            return

        id_habito = int(input("\nDigite o ID do hábito: "))

        cursor.execute(
            "SELECT nome, descricao, frequencia, meta FROM habitos WHERE id=? AND usuario_id=?",
            (id_habito, usuario_id),
        )
        habito = cursor.fetchone()

        if habito is None:
            print("Hábito não encontrado para este usuário.")
            return

        nome_atual, descricao_atual, frequencia_atual, meta_atual = habito
        descricao_atual = descricao_atual or ""

        print("\nPressione ENTER para manter o valor atual.")

        nome = input(f"Nome [{nome_atual}]: ").strip() or nome_atual
        descricao = input(f"Descrição [{descricao_atual}]: ").strip() or descricao_atual or None

        frequencia = escolher_frequencia(atual=frequencia_atual)
        if not frequencia:
            print("Opção inválida!")
            return

        meta_input = input(f"Meta [{meta_atual}]: ").strip()
        if meta_input == "":
            meta = meta_atual
        else:
            meta = int(meta_input)
            if meta <= 0:
                print("A meta deve ser um número positivo.")
                return

        cursor.execute(
            """
            UPDATE habitos
            SET nome=?, descricao=?, frequencia=?, meta=?
            WHERE id=? AND usuario_id=?
            """,
            (nome, descricao, frequencia, meta, id_habito, usuario_id),
        )
        conexao.commit()
        print("\nHábito atualizado com sucesso!")

    except ValueError:
        print("Digite apenas números onde for solicitado.")


def deletar(conexao, cursor):
    try:
        usuario_id = int(input("Digite o ID do usuário: "))

        if not listar_habitos_por_usuario(cursor, usuario_id):
            return

        id_habito = int(input("\nDigite o ID do hábito: "))

        cursor.execute(
            "SELECT id FROM habitos WHERE id=? AND usuario_id=?",
            (id_habito, usuario_id),
        )
        if cursor.fetchone() is None:
            print("Hábito não encontrado para este usuário.")
            return

        confirma = input("Deseja realmente excluir este hábito? (s/n): ")
        if confirma.lower() == "s":
            cursor.execute(
                "DELETE FROM habitos WHERE id=? AND usuario_id=?",
                (id_habito, usuario_id),
            )
            conexao.commit()
            print("Hábito excluído com sucesso!")
        else:
            print("Operação cancelada.")

    except ValueError:
        print("Digite apenas números onde for solicitado.")


def menu_habitos():
    conexao = get_conexao()
    cursor = conexao.cursor()

    try:
        while True:
            print("\n===== HÁBITOS =====")
            print("1 - Cadastrar Novo Hábito")
            print("2 - Listar Hábitos")
            print("3 - Editar Hábito")
            print("4 - Deletar Hábito")
            print("0 - Sair")

            op = input("\nEscolha uma opção: ")

            if op == "1":
                cadastrar(conexao, cursor)
            elif op == "2":
                listar(cursor)
            elif op == "3":
                editar(conexao, cursor)
            elif op == "4":
                deletar(conexao, cursor)
            elif op == "0":
                print("Programa encerrado!")
                break
            else:
                print("Opção inválida!")
    finally:
        conexao.close()


menu_habitos()