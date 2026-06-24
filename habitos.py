from banco import conectar


def listar_habitos_por_usuario(id_usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id, nome, frequencia, meta FROM habitos WHERE id_usuario = ?",
        (id_usuario,)
    )

    habitos = cursor.fetchall()
    conexao.close()

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
    conexao = conectar()
    cursor = conexao.cursor()

    print("\nCADASTRAR NOVO HÁBITO")

    try:
        id_usuario = int(input("Digite o ID do usuário: "))
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
            conexao.close()
            return

         meta = input("Meta (ex: 30 minutos, 2 litros, 10 páginas): ").strip()
         if not meta:
             print("A meta não pode ser vazia.")
             conexao.close()
              return

        cursor.execute(
            """
            INSERT INTO habitos
            (id_usuario, nome, descricao, frequencia, meta)
            VALUES (?, ?, ?, ?, ?)
            """,
            (id_usuario, nome, descricao, frequencia, meta)
        )

        conexao.commit()
        print("\nHábito cadastrado com sucesso!")

    except ValueError:
        print("Digite apenas números onde for solicitado.")

    conexao.close()


def listar():
    try:
        id_usuario = int(input("Digite o ID do usuário: "))
        listar_habitos_por_usuario(id_usuario)

    except ValueError:
        print("Digite um ID válido.")


def editar():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        id_usuario = int(input("Digite o ID do usuário: "))

        if not listar_habitos_por_usuario(id_usuario):
            conexao.close()
            return

        id_habito = int(input("\nDigite o ID do hábito: "))

        cursor.execute(
            """
            SELECT nome, descricao, frequencia, meta
            FROM habitos
            WHERE id = ? AND id_usuario = ?
            """,
            (id_habito, id_usuario)
        )

        habito = cursor.fetchone()

        if habito is None:
            print("Hábito não encontrado.")
            conexao.close()
            return

        print("\nPressione ENTER para manter o valor atual.")

        nome = input(f"Nome [{habito[0]}]: ") or habito[0]
        descricao = input(f"Descrição [{habito[1]}]: ") or habito[1]
        frequencia = input(f"Frequência [{habito[2]}]: ") or habito[2]
        meta = input(f"Meta [{habito[3]}]: ").strip() or habito[3]

        cursor.execute(
            """
            UPDATE habitos
            SET nome = ?, descricao = ?, frequencia = ?, meta = ?
            WHERE id = ?
            """,
            (nome, descricao, frequencia, meta, id_habito)
        )

        conexao.commit()
        print("\nHábito atualizado com sucesso!")

    except ValueError:
        print("Digite apenas números onde for solicitado.")

    conexao.close()


def deletar():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        id_usuario = int(input("Digite o ID do usuário: "))

        if not listar_habitos_por_usuario(id_usuario):
            conexao.close()
            return

        id_habito = int(input("\nDigite o ID do hábito: "))

        confirma = input("Deseja realmente excluir este hábito? (s/n): ")

        if confirma.lower() == "s":
            cursor.execute(
                "DELETE FROM habitos WHERE id = ? AND id_usuario = ?",
                (id_habito, id_usuario)
            )

            conexao.commit()
            print("Hábito excluído com sucesso!")
        else:
            print("Operação cancelada.")

    except ValueError:
        print("Digite apenas números onde for solicitado.")

    conexao.close()


def menu_habitos():
    while True:
        print("\n===== HÁBITOS =====")
        print("1 - Cadastrar Novo Hábito")
        print("2 - Listar Hábitos")
        print("3 - Editar Hábito")
        print("4 - Deletar Hábito")
        print("0 - Voltar")

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
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu_habitos()
