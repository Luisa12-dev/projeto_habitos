import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()


def listar_habitos_por_usuario(usuario_id):
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


def cadastrar():
    print("\nCADASTRAR NOVO HÁBITO")

    try:
        usuario_id = int(input("Digite o ID do usuário: "))
        nome = input("Nome do hábito: ").strip()
        if not nome:
            print("O nome do hábito não pode ser vazio.")
            return

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
            (usuario_id, nome, descricao, frequencia, meta),
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
            (id_habito, usuario_id),
        )

        habito = cursor.fetchone()

        if habito is None:
            print("Hábito não encontrado para este usuário.")
            return

        print("\nPressione ENTER para manter o valor atual.")

        nome = input(f"Nome [{habito[0]}]: ").strip() or habito[0]
        descricao = input(f"Descrição [{habito[1]}]: ") or habito[1]

        print(f"Frequência atual: {habito[2]}")
        print("1 - Diária | 2 - Semanal | 3 - Mensal | ENTER - Manter")
        op_freq = input("Opção: ")

        if op_freq == "1":
            frequencia = "Diária"
        elif op_freq == "2":
            frequencia = "Semanal"
        elif op_freq == "3":
            frequencia = "Mensal"
        else:
            frequencia = habito[2]

        meta_input = input(f"Meta [{habito[3]}]: ")
        meta = habito[3] if meta_input == "" else int(meta_input)

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


def deletar():
    try:
        usuario_id = int(input("Digite o ID do usuário: "))

        if not listar_habitos_por_usuario(usuario_id):
            return

        id_habito = int(input("\nDigite o ID do hábito: "))

        # Verifica se o hábito realmente pertence ao usuário antes de deletar
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
    finally:
        conexao.close()


menu_habitos()
