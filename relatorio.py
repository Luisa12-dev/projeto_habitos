import webbrowser
from datetime import date
from banco import conectar


def _escolher_usuario():
    """Mostra a lista de usuários e pede o ID. Retorna o ID ou None."""
    conn = conectar()
    usuarios = conn.execute("SELECT * FROM usuarios ORDER BY nome").fetchall()
    conn.close()

    if not usuarios:
        print("Nenhum usuário cadastrado ainda.")
        return None

    print(f"\n{'ID':<5} {'Nome':<25} {'E-mail'}")
    print("─" * 55)
    for u in usuarios:
        print(f"{u['id']:<5} {u['nome']:<25} {u['email']}")

    try:
        id_usuario = int(input("\nDigite o ID do usuário: ").strip())
    except ValueError:
        print("❌  ID inválido.")
        return None

    conn = conectar()
    usuario = conn.execute("SELECT * FROM usuarios WHERE id = ?", (id_usuario,)).fetchone()
    conn.close()

    if not usuario:
        print("❌  Usuário não encontrado.")
        return None

    return id_usuario


def _calcular_taxa(realizados, total):
    """Calcula porcentagem evitando divisão por zero."""
    if total == 0:
        return 0
    return round((realizados / total) * 100)



def calcular_resumo_geral(id_usuario):
    """
    Busca todos os hábitos do usuário e calcula, para cada um,
    o total de registros, quantos foram 'Realizado' e a taxa de sucesso.
    Retorna o usuário e uma lista de dicionários prontos para exibir
    ou jogar no HTML.
    """
    conn = conectar()

    usuario = conn.execute("SELECT * FROM usuarios WHERE id = ?", (id_usuario,)).fetchone()
    habitos = conn.execute(
        "SELECT * FROM habitos WHERE id_usuario = ? ORDER BY nome", (id_usuario,)
    ).fetchall()

    resultado = []
    for h in habitos:
        total = conn.execute(
            "SELECT COUNT(*) FROM registros WHERE id_habito = ?", (h["id"],)
        ).fetchone()[0]

        
        realizados = conn.execute(
            "SELECT COUNT(*) FROM registros WHERE id_habito = ? AND status = 'Realizado'",
            (h["id"],),
        ).fetchone()[0]

        resultado.append({
            "nome": h["nome"],
            "frequencia": h["frequencia"],
            "total": total,
            "realizados": realizados,
            "taxa": _calcular_taxa(realizados, total),
        })

    conn.close()
    return usuario, resultado


def relatorio_resumo_geral():
    """Versão para o terminal — mostra o resumo geral com print()."""
    print("\n── Resumo Geral por Usuário ──")
    id_usuario = _escolher_usuario()
    if id_usuario is None:
        return

    usuario, habitos = calcular_resumo_geral(id_usuario)

    if not habitos:
        print("Esse usuário ainda não tem hábitos cadastrados.")
        return

    print(f"\n👤  {usuario['nome']}")
    print(f"{'Hábito':<25} {'Total':<8} {'Realizados':<12} {'Taxa'}")
    print("─" * 60)
    for h in habitos:
        print(f"{h['nome']:<25} {h['total']:<8} {h['realizados']:<12} {h['taxa']}%")



def calcular_evolucao_7_dias(id_usuario):
    """
    Busca os registros dos últimos 7 dias do usuário, com o nome do hábito.
    Retorna uma lista de dicionários: data, nome_habito, status.
    """
    conn = conectar()
    registros = conn.execute(
        """
        SELECT r.data, r.status, h.nome AS nome_habito
        FROM registros r
        JOIN habitos h ON h.id = r.id_habito
        WHERE h.id_usuario = ?
          AND r.data >= date('now', '-6 days')
        ORDER BY r.data DESC, h.nome
        """,
        (id_usuario,),
    ).fetchall()
    conn.close()

    return [dict(r) for r in registros]


def relatorio_evolucao_7_dias():
    """Versão para o terminal."""
    print("\n── Evolução dos Últimos 7 Dias ──")
    id_usuario = _escolher_usuario()
    if id_usuario is None:
        return

    registros = calcular_evolucao_7_dias(id_usuario)

    if not registros:
        print("Nenhum registro nos últimos 7 dias.")
        return

    print(f"\n{'Data':<14} {'Hábito':<25} {'Status'}")
    print("─" * 55)
    for r in registros:
        
        icone = "✅" if r["status"] == "Realizado" else "❌"
        print(f"{r['data']:<14} {r['nome_habito']:<25} {icone} {r['status']}")



def calcular_ranking(id_usuario):
    """
    Lista os hábitos do usuário ordenados pela taxa de sucesso,
    do mais cumprido para o menos cumprido.
    """
    conn = conectar()
    habitos = conn.execute(
        "SELECT * FROM habitos WHERE id_usuario = ?", (id_usuario,)
    ).fetchall()

    ranking = []
    for h in habitos:
        total = conn.execute(
            "SELECT COUNT(*) FROM registros WHERE id_habito = ?", (h["id"],)
        ).fetchone()[0]

        # 🔧 AJUSTE AQUI se o status não for exatamente 'Realizado'
        realizados = conn.execute(
            "SELECT COUNT(*) FROM registros WHERE id_habito = ? AND status = 'Realizado'",
            (h["id"],),
        ).fetchone()[0]

        ranking.append({
            "nome": h["nome"],
            "total": total,
            "realizados": realizados,
            "taxa": _calcular_taxa(realizados, total),
        })

    conn.close()
    
    ranking.sort(key=lambda h: h["taxa"], reverse=True)
    return ranking


def relatorio_ranking():
    """Versão para o terminal."""
    print("\n── Ranking de Hábitos Mais Cumpridos ──")
    id_usuario = _escolher_usuario()
    if id_usuario is None:
        return

    ranking = calcular_ranking(id_usuario)

    if not ranking:
        print("Esse usuário ainda não tem hábitos cadastrados.")
        return

    print(f"\n{'#':<4} {'Hábito':<25} {'Realizados':<12} {'Taxa'}")
    print("─" * 55)
    for i, h in enumerate(ranking, 1):
        print(f"{i:<4} {h['nome']:<25} {h['realizados']:<12} {h['taxa']}%")



def gerar_relatorio_html(id_usuario):
    
    usuario, habitos_resumo = calcular_resumo_geral(id_usuario)
    evolucao = calcular_evolucao_7_dias(id_usuario)
    ranking = calcular_ranking(id_usuario)

    if not habitos_resumo:
        print("Esse usuário ainda não tem hábitos cadastrados. Não foi possível gerar o relatório.")
        return

    
    total_geral = sum(h["total"] for h in habitos_resumo)
    realizados_geral = sum(h["realizados"] for h in habitos_resumo)
    taxa_geral = _calcular_taxa(realizados_geral, total_geral)

    
    linhas_resumo = ""
    for h in habitos_resumo:
        cor = "#1D9E75" if h["taxa"] >= 70 else "#BA7517" if h["taxa"] >= 40 else "#A32D2D"
        linhas_resumo += f"""
        <tr>
            <td>{h['nome']}</td>
            <td>{h['frequencia']}</td>
            <td>{h['total']}</td>
            <td>{h['realizados']}</td>
            <td><span class="badge" style="background:{cor}1A; color:{cor};">{h['taxa']}%</span></td>
        </tr>
        """

    
    linhas_evolucao = ""
    if evolucao:
        for r in evolucao:
            # 🔧 AJUSTE AQUI se o status não for exatamente 'Realizado'
            icone = "✅" if r["status"] == "Realizado" else "❌"
            linhas_evolucao += f"""
            <tr>
                <td>{r['data']}</td>
                <td>{r['nome_habito']}</td>
                <td>{icone} {r['status']}</td>
            </tr>
            """
    else:
        linhas_evolucao = "<tr><td colspan='3' class='vazio'>Nenhum registro nos últimos 7 dias.</td></tr>"

    
    linhas_ranking = ""
    for i, h in enumerate(ranking, 1):
        cor = "#1D9E75" if h["taxa"] >= 70 else "#BA7517" if h["taxa"] >= 40 else "#A32D2D"
        linhas_ranking += f"""
        <tr>
            <td>{i}º</td>
            <td>{h['nome']}</td>
            <td>{h['realizados']} / {h['total']}</td>
            <td><span class="badge" style="background:{cor}1A; color:{cor};">{h['taxa']}%</span></td>
        </tr>
        """

    conteudo_html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Relatório de Hábitos - {usuario['nome']}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #F4F1E8;
                padding: 30px;
                color: #2C2C2A;
            }}
            .container {{
                max-width: 700px;
                margin: 0 auto;
            }}
            .header {{
                margin-bottom: 24px;
            }}
            .header h1 {{
                color: #1B5E20;
                margin: 0 0 4px;
            }}
            .header p {{
                color: #5F5E5A;
                margin: 0;
            }}
            .cards {{
                display: flex;
                gap: 16px;
                margin-bottom: 28px;
            }}
            .card {{
                background: white;
                border-radius: 12px;
                padding: 16px 20px;
                flex: 1;
                box-shadow: 0 1px 4px rgba(0,0,0,0.08);
            }}
            .card p {{
                margin: 0;
            }}
            .card .label {{
                font-size: 13px;
                color: #5F5E5A;
                margin-bottom: 4px;
            }}
            .card .numero {{
                font-size: 26px;
                font-weight: bold;
                color: #1565C0;
            }}
            .secao {{
                background: white;
                border-radius: 12px;
                padding: 20px;
                margin-bottom: 20px;
                box-shadow: 0 1px 4px rgba(0,0,0,0.08);
            }}
            .secao h2 {{
                margin-top: 0;
                color: #1B5E20;
                font-size: 18px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 12px;
            }}
            th {{
                text-align: left;
                font-size: 13px;
                color: #5F5E5A;
                padding: 8px 6px;
                border-bottom: 1px solid #E0DED5;
            }}
            td {{
                padding: 10px 6px;
                border-bottom: 1px solid #EFEDE5;
                font-size: 14px;
            }}
            .badge {{
                padding: 4px 10px;
                border-radius: 6px;
                font-size: 13px;
                font-weight: bold;
            }}
            .vazio {{
                text-align: center;
                color: #888780;
                padding: 16px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1> Relatório de Hábitos Saudáveis</h1>
                <p>Usuário: {usuario['nome']} · Gerado em {date.today().strftime('%d/%m/%Y')}</p>
            </div>

            <div class="cards">
                <div class="card">
                    <p class="label">Hábitos cadastrados</p>
                    <p class="numero">{len(habitos_resumo)}</p>
                </div>
                <div class="card">
                    <p class="label">Taxa geral de sucesso</p>
                    <p class="numero">{taxa_geral}%</p>
                </div>
            </div>

            <div class="secao">
                <h2>Resumo geral por hábito</h2>
                <table>
                    <tr>
                        <th>Hábito</th>
                        <th>Frequência</th>
                        <th>Registros</th>
                        <th>Realizados</th>
                        <th>Taxa</th>
                    </tr>
                    {linhas_resumo}
                </table>
            </div>

            <div class="secao">
                <h2>Evolução dos últimos 7 dias</h2>
                <table>
                    <tr>
                        <th>Data</th>
                        <th>Hábito</th>
                        <th>Status</th>
                    </tr>
                    {linhas_evolucao}
                </table>
            </div>

            <div class="secao">
                <h2>Ranking de hábitos mais cumpridos</h2>
                <table>
                    <tr>
                        <th>#</th>
                        <th>Hábito</th>
                        <th>Realizados</th>
                        <th>Taxa</th>
                    </tr>
                    {linhas_ranking}
                </table>
            </div>
        </div>
    </body>
    </html>
    """

    with open("relatorio.html", "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo_html)

    webbrowser.open("relatorio.html")
    print("✅  Relatório HTML gerado e aberto no navegador!")



def menu_relatorios():
    opcoes = {
        "1": ("Resumo geral por usuário",          relatorio_resumo_geral),
        "2": ("Evolução dos últimos 7 dias",        relatorio_evolucao_7_dias),
        "3": ("Ranking de hábitos mais cumpridos",  relatorio_ranking),
        "4": ("Gerar relatório completo em HTML",   None),  # tratado abaixo
    }
    while True:
        print("\n── Menu: Relatórios ──")
        for k, (label, _) in opcoes.items():
            print(f"  {k}. {label}")
        print("  0. Voltar")

        escolha = input("\nOpção: ").strip()

        if escolha == "0":
            break
        elif escolha == "4":
            id_usuario = _escolher_usuario()
            if id_usuario is not None:
                gerar_relatorio_html(id_usuario)
        elif escolha in opcoes:
            opcoes[escolha][1]()
        else:
            print("❌  Opção inválida.")
