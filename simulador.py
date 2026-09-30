"""
Simulador de Linha de Produção Industrial
Gera entradas aleatórias de peças e simula o funcionamento automatizado do sistema.
Disciplina: Algoritmos e Lógica de Programação - UniFECAF
"""

import sys
import random
import time
import main

# Garante suporte a caracteres especiais no terminal Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def gerar_dados_peca_aleatoria(indice: int):
    """
    Gera dados aleatórios para uma peça industrial com distribuição realista:
    - ~70% de chance de gerar valores dentro do padrão (aprovada)
    - ~30% de chance de gerar desvios em peso, cor ou dimensão (reprovada)
    """
    id_peca = f"PEC-{indice:03d}"

    tipo_sorteio = random.random()

    if tipo_sorteio < 0.70:
        # Peça padrão (100% conforme)
        peso = round(random.uniform(95.5, 104.5), 1)
        cor = random.choice(["azul", "verde"])
        comprimento = round(random.uniform(11.0, 19.0), 1)
    elif tipo_sorteio < 0.80:
        # Defeito de peso (fora do intervalo 95g - 105g)
        peso = round(random.choice([random.uniform(82.0, 94.5), random.uniform(105.5, 115.0)]), 1)
        cor = random.choice(["azul", "verde"])
        comprimento = round(random.uniform(10.0, 20.0), 1)
    elif tipo_sorteio < 0.90:
        # Defeito de cor
        peso = round(random.uniform(95.0, 105.0), 1)
        cor = random.choice(["vermelho", "amarelo", "preto", "cinza"])
        comprimento = round(random.uniform(10.0, 20.0), 1)
    else:
        # Defeito de comprimento ou múltiplos defeitos
        peso = round(random.uniform(90.0, 110.0), 1)
        cor = random.choice(["azul", "verde", "roxo"])
        comprimento = round(random.choice([random.uniform(5.0, 9.5), random.uniform(20.5, 26.0)]), 1)

    return id_peca, peso, cor, comprimento


def executar_simulacao(total_pecas: int = 25, velocidade: float = 0.1):
    """
    Simula uma esteira industrial contínua de produção:
    1. Limpa os dados em memória
    2. Gera e inspeciona 'total_pecas'
    3. Demonstra fechamento automático de caixas (10 peças cada)
    4. Simula uma remoção de peça
    5. Exibe o relatório final de produção
    """
    main.limpar_dados()

    print("=" * 70)
    print(" INICIANDO SIMULAÇÃO INDUSTRIAL AUTOMATIZADA ".center(70))
    print(f" Total de peças: {total_pecas} | Intervalo: {velocidade}s ".center(70))
    print("=" * 70)
    print(f"{'ID':<9} | {'PESO':<8} | {'COR':<10} | {'COMPR.':<8} | {'STATUS / DESTINO'}")
    print("-" * 70)

    for i in range(1, total_pecas + 1):
        id_peca, peso, cor, comprimento = gerar_dados_peca_aleatoria(i)
        resultado = main.processar_cadastro_peca(id_peca, peso, cor, comprimento)

        if resultado["aprovado"]:
            status_txt = f"[APROVADA] -> Caixa #{resultado['numero_caixa']}"
            if resultado["caixa_fechou"]:
                status_txt += f" *** CAIXA #{resultado['numero_caixa']} FECHADA! ***"
        else:
            motivo_resumo = resultado["motivos"][0] if resultado["motivos"] else "Não conforme"
            status_txt = f"[REPROVADA] {motivo_resumo}"

        print(f"{id_peca:<9} | {peso:>5.1f}g  | {cor.capitalize():<10} | {comprimento:>5.1f}cm | {status_txt}")

        if velocidade > 0:
            time.sleep(velocidade)

    # -------------------------------------------------------------
    # Demonstração de Caixas Fechadas
    # -------------------------------------------------------------
    print("\n" + "=" * 70)
    print(" SITUAÇÃO DO ARMAZENAMENTO DAS CAIXAS ".center(70))
    print("=" * 70)
    if main.caixas_fechadas:
        print(f"Total de caixas fechadas (10 peças cada): {len(main.caixas_fechadas)}")
        for idx, cx in enumerate(main.caixas_fechadas, start=1):
            ids = [p["id"] for p in cx]
            print(f"  [CAIXA #{idx}] Fechada com 10 peças: {', '.join(ids)}")
    else:
        print("Nenhuma caixa atingiu 10 peças ainda.")

    if main.caixa_atual:
        ids_atual = [p["id"] for p in main.caixa_atual]
        num_atual = len(main.caixas_fechadas) + 1
        print(f"  [CAIXA #{num_atual}] Em andamento ({len(main.caixa_atual)}/10 peças): {', '.join(ids_atual)}")

    # -------------------------------------------------------------
    # Simulação da Opção 3 (Remoção de uma peça cadastrada)
    # -------------------------------------------------------------
    print("\n" + "-" * 70)
    print(" SIMULAÇÃO DE REMOÇÃO DE PEÇA PELO OPERADOR (OPÇÃO 3) ".center(70))
    print("-" * 70)
    peca_teste_remover = "PEC-001"
    sucesso, msg = main.processar_remocao_peca(peca_teste_remover)
    print(f"Remover '{peca_teste_remover}': {msg}")

    # -------------------------------------------------------------
    # Exibição do Relatório Final Consolidado
    # -------------------------------------------------------------
    print("\n" + "=" * 70)
    print(" RELATÓRIO FINAL CONSOLIDADO DA PRODUÇÃO ".center(70))
    print("=" * 70)
    relatorio = main.obter_dados_relatorio()
    print(f"  * Total de Peças Inspecionadas: {relatorio['total_geral']}")
    print(f"  * Peças Aprovadas:              {relatorio['total_aprovadas']}")
    print(f"  * Peças Reprovadas:             {relatorio['total_reprovadas']}")
    print(f"  * Taxa de Aprovação / Qualidade: {relatorio['taxa_aprovacao']:.1f}%")
    print("  " + "-" * 50)
    print(f"  * Caixas Fechadas (10 peças):   {relatorio['caixas_fechadas']}")
    print(f"  * Peças na Caixa Atual:         {relatorio['pecas_na_caixa_atual']}/10")
    print(f"  * Total de Caixas Utilizadas:   {relatorio['caixas_utilizadas']}")

    if relatorio["motivos_contagem"]:
        print("\n  --- DETALHAMENTO DE MOTIVOS DE REPROVAÇÃO ---")
        for motivo, count in relatorio["motivos_contagem"].items():
            print(f"  * {motivo} -> {count} ocorrência(s)")

    print("\n[OK] Simulação concluída com sucesso!\n")


if __name__ == "__main__":
    # Permite passar quantidade de peças pela linha de comando: python simulador.py 30
    qtd = 25
    if len(sys.argv) > 1:
        try:
            qtd = int(sys.argv[1])
        except ValueError:
            qtd = 25

    executar_simulacao(total_pecas=qtd, velocidade=0.08)
