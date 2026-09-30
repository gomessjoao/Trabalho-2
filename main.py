"""
Sistema de Gestão de Peças, Controle de Qualidade e Armazenamento
Disciplina: Algoritmos e Lógica de Programação - UniFECAF
"""

import sys

# Garante suporte a caracteres especiais no terminal Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


# =====================================================================
# ESTRUTURAS DE DADOS (ARMAZENAMENTO EM MEMÓRIA)
# =====================================================================
pecas_aprovadas = []    # Lista de peças que atenderam a todos os critérios
pecas_reprovadas = []   # Lista de peças reprovadas e seus motivos
caixas_fechadas = []    # Lista de caixas que atingiram o limite de 10 peças
caixa_atual = []        # Caixa atualmente sendo preenchida (máximo 10 peças)


# =====================================================================
# FUNÇÕES DE REGRAS DE NEGÓCIO E VALIDAÇÃO
# =====================================================================

def validar_peca(peso: float, cor: str, comprimento: float):
    """
    Avalia a peça segundo os critérios de qualidade estabelecidos:
    - Peso entre 95g e 105g (inclusivo)
    - Cor azul ou verde
    - Comprimento entre 10cm e 20cm (inclusivo)

    Retorna: (aprovado: bool, lista_de_motivos: list)
    """
    motivos = []
    cor_limpa = cor.strip().lower()

    if peso < 95.0 or peso > 105.0:
        motivos.append(f"Peso ({peso:.1f}g) fora do intervalo permitido [95g a 105g]")

    if cor_limpa not in ["azul", "verde"]:
        motivos.append(f"Cor '{cor.strip()}' inválida (aceito apenas: azul ou verde)")

    if comprimento < 10.0 or comprimento > 20.0:
        motivos.append(f"Comprimento ({comprimento:.1f}cm) fora do intervalo permitido [10cm a 20cm]")

    aprovado = len(motivos) == 0
    return aprovado, motivos


def buscar_peca_por_id(id_peca: str):
    """Retorna a peça caso exista nas aprovadas ou reprovadas."""
    id_peca = id_peca.strip()
    for peca in pecas_aprovadas:
        if peca["id"] == id_peca:
            return peca
    for peca in pecas_reprovadas:
        if peca["id"] == id_peca:
            return peca
    return None


def processar_cadastro_peca(id_peca: str, peso: float, cor: str, comprimento: float):
    """
    Processa o cadastro, valida qualidade e gerencia a alocação em caixas.
    Retorna um dicionário com o resultado do processamento.
    """
    id_peca = id_peca.strip()
    if not id_peca:
        return {"sucesso": False, "mensagem": "O ID da peça não pode ser vazio."}

    if buscar_peca_por_id(id_peca) is not None:
        return {"sucesso": False, "mensagem": f"Já existe uma peça cadastrada com o ID '{id_peca}'."}

    aprovado, motivos = validar_peca(peso, cor, comprimento)
    cor_formatada = cor.strip().capitalize()

    if aprovado:
        # Número da caixa em que a peça será guardada
        num_caixa = len(caixas_fechadas) + 1

        peca = {
            "id": id_peca,
            "peso": peso,
            "cor": cor_formatada,
            "comprimento": comprimento,
            "status": "Aprovada",
            "caixa": num_caixa
        }
        pecas_aprovadas.append(peca)
        caixa_atual.append(peca)

        # Se a caixa atingir 10 peças, fecha a caixa e abre uma nova
        caixa_fechou = False
        if len(caixa_atual) == 10:
            caixas_fechadas.append(list(caixa_atual))
            caixa_atual.clear()
            caixa_fechou = True

        return {
            "sucesso": True,
            "aprovado": True,
            "peca": peca,
            "caixa_fechou": caixa_fechou,
            "numero_caixa": num_caixa
        }
    else:
        peca = {
            "id": id_peca,
            "peso": peso,
            "cor": cor_formatada,
            "comprimento": comprimento,
            "status": "Reprovada",
            "motivos": motivos
        }
        pecas_reprovadas.append(peca)
        return {
            "sucesso": True,
            "aprovado": False,
            "peca": peca,
            "motivos": motivos
        }


def processar_remocao_peca(id_peca: str):
    """Remove uma peça pelo ID e atualiza os registros e caixas."""
    id_peca = id_peca.strip()

    # 1. Procurar nas reprovadas
    for i, p in enumerate(pecas_reprovadas):
        if p["id"] == id_peca:
            pecas_reprovadas.pop(i)
            return True, f"Peça reprovada ID '{id_peca}' removida com sucesso."

    # 2. Procurar nas aprovadas
    for i, p in enumerate(pecas_aprovadas):
        if p["id"] == id_peca:
            num_caixa = p["caixa"]
            pecas_aprovadas.pop(i)

            # Se está na caixa atual
            if p in caixa_atual:
                caixa_atual.remove(p)
            else:
                # Se estava em uma caixa já fechada
                for caixa in caixas_fechadas:
                    for peca_caixa in caixa:
                        if peca_caixa["id"] == id_peca:
                            caixa.remove(peca_caixa)
                            break

            return True, f"Peça aprovada ID '{id_peca}' (da Caixa #{num_caixa}) removida com sucesso."

    return False, f"Nenhuma peça encontrada com o ID '{id_peca}'."


def obter_dados_relatorio():
    """Calcula e retorna as estatísticas consolidadas da produção."""
    total_apr = len(pecas_aprovadas)
    total_rep = len(pecas_reprovadas)
    total_geral = total_apr + total_rep

    caixas_usadas = len(caixas_fechadas) + (1 if len(caixa_atual) > 0 else 0)
    taxa_aprovacao = (total_apr / total_geral * 100) if total_geral > 0 else 0.0

    # Contagem de motivos de reprovação
    motivos_contagem = {}
    for p in pecas_reprovadas:
        for m in p["motivos"]:
            motivos_contagem[m] = motivos_contagem.get(m, 0) + 1

    return {
        "total_geral": total_geral,
        "total_aprovadas": total_apr,
        "total_reprovadas": total_rep,
        "taxa_aprovacao": taxa_aprovacao,
        "caixas_fechadas": len(caixas_fechadas),
        "pecas_na_caixa_atual": len(caixa_atual),
        "caixas_utilizadas": caixas_usadas,
        "motivos_contagem": motivos_contagem
    }


def limpar_dados():
    """Função utilitária para reiniciar os dados (usada nos testes)."""
    pecas_aprovadas.clear()
    pecas_reprovadas.clear()
    caixas_fechadas.clear()
    caixa_atual.clear()


# =====================================================================
# ENTRADA DE DADOS E INTERFACE DO USUÁRIO NO TERMINAL
# =====================================================================

def ler_numero(mensagem: str):
    """Lê um número float com tratamento de erro e suporte a vírgula."""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(entrada)
            if valor <= 0:
                print("  [!] O valor deve ser maior que zero.")
                continue
            return valor
        except ValueError:
            print("  [!] Entrada inválida. Por favor, digite um número (ex: 100.5).")


def menu_cadastrar():
    print("\n" + "-" * 50)
    print(">>> 1. CADASTRAR NOVA PEÇA <<<")
    print("-" * 50)

    id_peca = input("Código / ID da peça: ").strip()
    if not id_peca:
        print("  [!] O ID não pode ser vazio.")
        return

    peso = ler_numero("Peso da peça em gramas (ex: 100): ")
    cor = input("Cor da peça (ex: azul, verde): ").strip()
    comprimento = ler_numero("Comprimento da peça em cm (ex: 15): ")

    res = processar_cadastro_peca(id_peca, peso, cor, comprimento)

    if not res["sucesso"]:
        print(f"\n  [!] {res['mensagem']}")
        return

    peca = res["peca"]
    if res["aprovado"]:
        print(f"\n  [✓] PEÇA APROVADA!")
        print(f"      ID: {peca['id']} | Peso: {peca['peso']:.1f}g | Cor: {peca['cor']} | Comp.: {peca['comprimento']:.1f}cm")
        print(f"      Armazenada na Caixa #{res['numero_caixa']}")

        if res["caixa_fechou"]:
            print(f"  [★] A Caixa #{res['numero_caixa']} atingiu 10 peças e foi FECHADA!")
            print(f"      Uma nova caixa (#{len(caixas_fechadas) + 1}) foi iniciada.")
        else:
            restante = 10 - len(caixa_atual)
            print(f"      Espaço restante na caixa atual: {restante} peça(s).")
    else:
        print(f"\n  [✗] PEÇA REPROVADA!")
        print(f"      ID: {peca['id']} | Peso: {peca['peso']:.1f}g | Cor: {peca['cor']} | Comp.: {peca['comprimento']:.1f}cm")
        print("      Motivo(s) da reprovação:")
        for motivo in res["motivos"]:
            print(f"       • {motivo}")


def menu_listar():
    print("\n" + "-" * 50)
    print(">>> 2. LISTAR PEÇAS APROVADAS E REPROVADAS <<<")
    print("-" * 50)

    print("\n--- PEÇAS APROVADAS ---")
    if not pecas_aprovadas:
        print("  (Nenhuma peça aprovada até o momento)")
    else:
        for p in pecas_aprovadas:
            print(f"  • ID: {p['id']:<8} | Peso: {p['peso']:>5.1f}g | Cor: {p['cor']:<6} | Comp.: {p['comprimento']:>4.1f}cm | Caixa #{p['caixa']}")

    print("\n--- PEÇAS REPROVADAS ---")
    if not pecas_reprovadas:
        print("  (Nenhuma peça reprovada até o momento)")
    else:
        for p in pecas_reprovadas:
            print(f"  • ID: {p['id']:<8} | Peso: {p['peso']:>5.1f}g | Cor: {p['cor']:<6} | Comp.: {p['comprimento']:>4.1f}cm")
            for m in p["motivos"]:
                print(f"    - {m}")


def menu_remover():
    print("\n" + "-" * 50)
    print(">>> 3. REMOVER PEÇA CADASTRADA <<<")
    print("-" * 50)

    id_peca = input("Digite o ID da peça a ser removida: ").strip()
    if not id_peca:
        print("  [!] O ID não pode ser vazio.")
        return

    sucesso, mensagem = processar_remocao_peca(id_peca)
    if sucesso:
        print(f"  [✓] {mensagem}")
    else:
        print(f"  [!] {mensagem}")


def menu_caixas():
    print("\n" + "-" * 50)
    print(">>> 4. LISTAR CAIXAS FECHADAS <<<")
    print("-" * 50)

    if not caixas_fechadas:
        print("  (Nenhuma caixa fechada ainda - capacidade de 10 peças)")
    else:
        for i, caixa in enumerate(caixas_fechadas, start=1):
            ids = [p["id"] for p in caixa]
            print(f"  📦 Caixa #{i} (Fechada com 10 peças):")
            print(f"     Peças: {', '.join(ids)}")

    print(f"\n  📦 Caixa Atual em Aberto (Caixa #{len(caixas_fechadas) + 1}):")
    if not caixa_atual:
        print("     (Caixa vazia - 0/10 peças)")
    else:
        ids_atual = [p["id"] for p in caixa_atual]
        print(f"     Contém {len(caixa_atual)}/10 peças: {', '.join(ids_atual)}")


def menu_relatorio():
    print("\n" + "=" * 50)
    print(">>> 5. RELATÓRIO FINAL CONSOLIDADO <<<")
    print("=" * 50)

    dados = obter_dados_relatorio()

    print(f"  Total de peças inspecionadas: {dados['total_geral']}")
    print(f"  Peças aprovadas:              {dados['total_aprovadas']}")
    print(f"  Peças reprovadas:             {dados['total_reprovadas']}")
    print(f"  Taxa de aprovação:            {dados['taxa_aprovacao']:.1f}%")
    print("-" * 50)
    print(f"  Caixas fechadas (10 peças):   {dados['caixas_fechadas']}")
    print(f"  Peças na caixa atual:         {dados['pecas_na_caixa_atual']}/10")
    print(f"  Total de caixas utilizadas:   {dados['caixas_utilizadas']}")

    if dados["motivos_contagem"]:
        print("\n--- MOTIVOS DAS REPROVAÇÕES ---")
        for motivo, qtd in dados["motivos_contagem"].items():
            print(f"  • {motivo} -> {qtd} peça(s)")
    else:
        print("\n  [✓] Nenhuma reprovação registrada!")


def menu_principal():
    while True:
        print("\n" + "=" * 50)
        print(" SISTEMA DE CONTROLE DE QUALIDADE DE PEÇAS ")
        print(" UniFECAF - Automação Industrial ")
        print("=" * 50)
        print("  1. Cadastrar nova peça")
        print("  2. Listar peças aprovadas/reprovadas")
        print("  3. Remover peça cadastrada")
        print("  4. Listar caixas fechadas")
        print("  5. Gerar relatório final")
        print("  0. Sair do programa")
        print("-" * 50)

        opcao = input("Escolha uma opção (0-5): ").strip()

        if opcao == "1":
            menu_cadastrar()
        elif opcao == "2":
            menu_listar()
        elif opcao == "3":
            menu_remover()
        elif opcao == "4":
            menu_caixas()
        elif opcao == "5":
            menu_relatorio()
        elif opcao == "0":
            print("\nEncerrando o sistema. Até logo!\n")
            break
        else:
            print("\n[!] Opção inválida! Escolha um número de 0 a 5.")


if __name__ == "__main__":
    menu_principal()
