import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

def listar_habitos_por_usuario(usuario_id):
    cursor.execute(
        "SELECT id, nome, frequencia, meta FROM habitos WHERE usuario_id=?",
        (usuario_id,)
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


def cadastrar():
    print("\nCADASTRAR NOVO HÁBITO")

    try:
        usuario_id = int(input("Digite o ID do usuário: "))
        nome = input("Nome do hábito: ")
        descricao = input("Descrição (opcional): ")

        print("\nEscolha a frequência:")
        print("1 - Diária")
        print("2 - Semanal")
        print("3 - Mensal")

        op = input("Opção: ")

        if op == "1":
            frequencia = "Diária"
        elif op == "2":
            frequencia = "Semanal"
        elif op == "3":
            frequencia = "Mensal"
        else:
            print("Opção inválida!")
            return

        meta = int(input("Meta (número de vezes): "))

        cursor.execute(
            """
            INSERT INTO habitos
            (usuario_id, nome, descricao, frequencia, meta)
            VALUES (?, ?, ?, ?, ?)
            """,
            (usuario_id, nome, descricao, frequencia, meta)
        )

        conexao.commit()
        print("\nHábito cadastrado com sucesso!")

    except ValueError:
        print("Digite apenas números onde for solicitado.")


def listar():
    try:
        usuario_id = int(input("Digite o ID do usuário: "))
        listar_habitos_por_usuario(usuario_id)

    except ValueError:
        print("Digite um ID válido.")


def editar():
    try:
        usuario_id = int(input("Digite o ID do usuário: "))

        if not listar_habitos_por_usuario(usuario_id):
            return

        id_habito = int(input("\nDigite o ID do hábito: "))

        cursor.execute(
            """
            SELECT nome, descricao, frequencia, meta
            FROM habitos
            WHERE id=? AND usuario_id=?
            """,
            (id_habito, usuario_id)
        )

        habito = cursor.fetchone()

        if habito is None:
            print("Hábito não encontrado.")
            return

        print("\nPressione ENTER para manter o valor atual.")

        nome = input(f"Nome [{habito[0]}]: ") or habito[0]
        descricao = input(f"Descrição [{habito[1]}]: ") or habito[1]
        frequencia = input(f"Frequência [{habito[2]}]: ") or habito[2]

        meta = input(f"Meta [{habito[3]}]: ")
        if meta == "":
            meta = habito[3]
        else:
            meta = int(meta)

        cursor.execute(
            """
            UPDATE habitos
            SET nome=?, descricao=?, frequencia=?, meta=?
            WHERE id=?
            """,
            (nome, descricao, frequencia, meta, id_habito)
        )

        conexao.commit()
        print("\nHábito atualizado com sucesso!")

    except ValueError:
        print("Digite apenas números onde for solicitado.")


def deletar():
    try:
        usuario_id = int(input("Digite o ID do usuário: "))

        if not listar_habitos_por_usuario(usuario_id):
            return

        id_habito = int(input("\nDigite o ID do hábito: "))

        confirma = input(
            "Deseja realmente excluir este hábito? (s/n): "
        )

        if confirma.lower() == "s":
            cursor.execute(
                "DELETE FROM habitos WHERE id=?",
                (id_habito,)
            )

            conexao.commit()
            print("Hábito excluído com sucesso!")
        else:
            print("Operação cancelada.")

    except ValueError:
        print("Digite apenas números onde for solicitado.")


def menu_habitos():
    while True:
        print("\n===== HÁBITOS =====")
        print("1 - Cadastrar Novo Hábito")
        print("2 - Listar Hábitos")
        print("3 - Editar Hábito")
        print("4 - Deletar Hábito")
        print("0 - Sair")

        op = input("\nEscolha uma opção: ")

        if op == "1":
            cadastrar()
        elif op == "2":
            listar()
        elif op == "3":
            editar()
        elif op == "4":
            deletar()
        elif op == "0":
            print("Programa encerrado!")
            break
        else:
            print("Opção inválida!")

    conexao.close()

menu_habitos()
