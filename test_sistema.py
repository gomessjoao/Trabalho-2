"""
Testes automatizados simplificados para o Sistema de Gestão de Peças
"""

import unittest
import main


class TestSistemaPecas(unittest.TestCase):

    def setUp(self):
        # Limpa os dados da memória antes de cada teste
        main.limpar_dados()

    def test_peca_aprovada(self):
        # Peça com valores perfeitamente dentro dos limites
        res = main.processar_cadastro_peca("P01", 100.0, "azul", 15.0)
        self.assertTrue(res["aprovado"])
        self.assertEqual(res["peca"]["status"], "Aprovada")
        self.assertEqual(len(main.pecas_aprovadas), 1)
        self.assertEqual(len(main.pecas_reprovadas), 0)

    def test_limites_peso(self):
        # 95g (mínimo) deve ser aprovado
        res_min = main.processar_cadastro_peca("P_MIN", 95.0, "verde", 15.0)
        self.assertTrue(res_min["aprovado"])

        # 105g (máximo) deve ser aprovado
        res_max = main.processar_cadastro_peca("P_MAX", 105.0, "verde", 15.0)
        self.assertTrue(res_max["aprovado"])

        # 94.9g deve ser reprovado
        res_abaixo = main.processar_cadastro_peca("P_INF", 94.9, "verde", 15.0)
        self.assertFalse(res_abaixo["aprovado"])

        # 105.1g deve ser reprovado
        res_acima = main.processar_cadastro_peca("P_SUP", 105.1, "verde", 15.0)
        self.assertFalse(res_acima["aprovado"])

    def test_validacao_cores(self):
        # Azul com letras maiúsculas/espaços
        res_azul = main.processar_cadastro_peca("P_AZUL", 100.0, "  AZUL  ", 15.0)
        self.assertTrue(res_azul["aprovado"])

        # Verde com letras minúsculas
        res_verde = main.processar_cadastro_peca("P_VERDE", 100.0, "verde", 15.0)
        self.assertTrue(res_verde["aprovado"])

        # Cor inválida (vermelho)
        res_invalida = main.processar_cadastro_peca("P_INV", 100.0, "vermelho", 15.0)
        self.assertFalse(res_invalida["aprovado"])

    def test_limites_comprimento(self):
        # 10cm (mínimo) deve ser aprovado
        self.assertTrue(main.processar_cadastro_peca("C_MIN", 100.0, "azul", 10.0)["aprovado"])

        # 20cm (máximo) deve ser aprovado
        self.assertTrue(main.processar_cadastro_peca("C_MAX", 100.0, "azul", 20.0)["aprovado"])

        # 9.9cm e 20.1cm devem ser reprovados
        self.assertFalse(main.processar_cadastro_peca("C_INF", 100.0, "azul", 9.9)["aprovado"])
        self.assertFalse(main.processar_cadastro_peca("C_SUP", 100.0, "azul", 20.1)["aprovado"])

    def test_reprovacao_multiplos_defeitos(self):
        # Peça reprovada por peso, cor e comprimento simultaneamente
        res = main.processar_cadastro_peca("P_RUIM", 80.0, "amarelo", 30.0)
        self.assertFalse(res["aprovado"])
        self.assertEqual(len(res["motivos"]), 3)

    def test_armazenamento_e_fechamento_caixas(self):
        # Cadastrar 9 peças aprovadas (devem ficar na Caixa 1 em aberto)
        for i in range(1, 10):
            res = main.processar_cadastro_peca(f"P_{i}", 100.0, "azul", 15.0)
            self.assertFalse(res["caixa_fechou"])
            self.assertEqual(len(main.caixa_atual), i)

        self.assertEqual(len(main.caixas_fechadas), 0)

        # 10ª peça deve fechar a Caixa 1
        res_10 = main.processar_cadastro_peca("P_10", 100.0, "verde", 15.0)
        self.assertTrue(res_10["caixa_fechou"])
        self.assertEqual(len(main.caixas_fechadas), 1)
        self.assertEqual(len(main.caixa_atual), 0)

        # 11ª peça deve abrir e entrar na Caixa 2
        res_11 = main.processar_cadastro_peca("P_11", 100.0, "azul", 15.0)
        self.assertEqual(res_11["numero_caixa"], 2)
        self.assertEqual(len(main.caixa_atual), 1)

    def test_remocao_de_peca(self):
        main.processar_cadastro_peca("PECA_01", 100.0, "azul", 15.0)
        main.processar_cadastro_peca("PECA_02", 50.0, "preto", 5.0)

        # Remover aprovada
        sucesso, _ = main.processar_remocao_peca("PECA_01")
        self.assertTrue(sucesso)
        self.assertEqual(len(main.pecas_aprovadas), 0)

        # Remover reprovada
        sucesso, _ = main.processar_remocao_peca("PECA_02")
        self.assertTrue(sucesso)
        self.assertEqual(len(main.pecas_reprovadas), 0)

    def test_evitar_id_duplicado(self):
        main.processar_cadastro_peca("ID_REPETIDO", 100.0, "azul", 15.0)
        res_duplicado = main.processar_cadastro_peca("ID_REPETIDO", 102.0, "verde", 16.0)
        self.assertFalse(res_duplicado["sucesso"])

    def test_relatorio_final(self):
        main.processar_cadastro_peca("P1", 100.0, "azul", 15.0)  # Aprovada
        main.processar_cadastro_peca("P2", 100.0, "verde", 15.0) # Aprovada
        main.processar_cadastro_peca("P3", 80.0, "azul", 15.0)   # Reprovada (peso)

        dados = main.obter_dados_relatorio()
        self.assertEqual(dados["total_geral"], 3)
        self.assertEqual(dados["total_aprovadas"], 2)
        self.assertEqual(dados["total_reprovadas"], 1)
        self.assertAlmostEqual(dados["taxa_aprovacao"], 66.7, places=1)
        self.assertEqual(dados["caixas_utilizadas"], 1)


if __name__ == "__main__":
    unittest.main()
