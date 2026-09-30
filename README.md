# Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento

**Disciplina:** Algoritmos e Lógica de Programação  
**Instituição:** UniFECAF  
**Linguagem:** Python 3.8+ (Sem dependências externas)

---

## 1. Sobre o Projeto

Este projeto consiste em um sistema de automação para controle de produção, inspeção de qualidade e armazenamento inteligente de peças industriais fabricadas em linha de montagem.

O software substitui o processo manual de inspeção por um fluxo digital automatizado que:
- Avalia cada peça segundo parâmetros rígidos de qualidade (**peso**, **cor** e **comprimento**);
- Separa peças aprovadas e peças reprovadas, detalhando os motivos de não conformidade;
- Armazena as peças aprovadas em caixas de capacidade limitada a **10 peças**;
- Fecha automaticamente a caixa ao atingir a capacidade máxima e inicia uma nova caixa;
- Gera relatórios consolidados de produção com métricas de desempenho industrial.

---

## 2. Critérios de Qualidade da Peça

Para que uma peça seja classificada como **APROVADA**, ela deve satisfazer **simultaneamente** a todos os seguintes critérios:

| Parâmetro | Faixa / Valor Aceito | Condição de Reprovação |
| :--- | :--- | :--- |
| **Peso** | Entre `95.0g` e `105.0g` (inclusive) | Menor que `95.0g` ou maior que `105.0g` |
| **Cor** | `Azul` ou `Verde` (case-insensitive) | Qualquer cor diferente de azul ou verde |
| **Comprimento** | Entre `10.0cm` e `20.0cm` (inclusive) | Menor que `10.0cm` ou maior que `20.0cm` |

Caso descumpra qualquer um dos critérios, a peça é marcada como **REPROVADA** e o sistema armazena a descrição detalhada de cada não conformidade.

---

## 3. Funcionalidades do Menu Interativo

O sistema conta com um menu interativo pelo terminal com as seguintes opções:

1. **Cadastrar nova peça:** Solicita ID, peso, cor e comprimento, processa a aprovação e aloca na caixa se aprovada.
2. **Listar peças aprovadas/reprovadas:** Exibe listagem formatada com todos os dados e motivos de reprovação.
3. **Remover peça cadastrada:** Exclui uma peça por ID e recalcula automaticamente o estoque e caixas.
4. **Listar caixas fechadas:** Apresenta todas as caixas que já atingiram a capacidade máxima de 10 peças e a caixa atual em andamento.
5. **Gerar relatório final:** Apresenta balanço geral da linha de produção (totais, taxa de aprovação, caixas usadas e motivos de falha agrupados).
0. **Sair do programa:** Encerra a execução de forma segura.

---

## 4. Como Rodar o Programa (Passo a Passo)

### Pré-requisitos
- Ter o **Python 3.8 ou superior** instalado no computador.
- Não é necessária a instalação de nenhuma biblioteca de terceiros (`pip`), pois o projeto utiliza apenas os módulos nativos do Python.

### Execução no Terminal

1. Abra o terminal (PowerShell, Prompt de Comando, Git Bash ou Terminal do VS Code/IDE).
2. Navegue até a pasta do projeto:
   ```bash
   cd "c:\Trabalhos Unifecaf\Trabalho 2"
   ```
3. Execute o script principal:
   ```bash
   python main.py
   ```

### Execução dos Testes Automatizados

Para certificar a integridade do código e a validação de todas as regras de negócio:
```bash
python -m unittest test_sistema.py -v
```

### Simulação de Produção Automatizada (Entradas Aleatórias)

Para simular o funcionamento contínuo de uma esteira industrial em tempo real com peças aleatórias, fechamento de caixas e relatório automático:
```bash
python simulador.py
```
*(Você também pode definir a quantidade de peças a simular, por exemplo: `python simulador.py 30`)*

---

## 5. Exemplos de Entradas e Saídas

### Exemplo 1: Cadastro de Peça Aprovada
**Entrada no Menu (Opção 1):**
```text
Digite o ID / Código da peça: PEC-101
Digite o peso da peça em gramas (ex: 100): 102.5
Digite a cor da peça (ex: azul, verde): azul
Digite o comprimento da peça em cm (ex: 15): 14.8
```

**Saída Gerada:**
```text
  [✓] RESULTADO: PEÇA APROVADA!
      - ID: PEC-101
      - Peso: 102.50g | Cor: Azul | Comprimento: 14.80cm
      - Alocada na: Caixa #1
      Espaço restante na caixa atual: 9 peça(s).
```

---

### Exemplo 2: Cadastro de Peça Reprovada (Múltiplas Não Conformidades)
**Entrada no Menu (Opção 1):**
```text
Digite o ID / Código da peça: PEC-102
Digite o peso da peça em gramas (ex: 100): 90.0
Digite a cor da peça (ex: azul, verde): vermelho
Digite o comprimento da peça em cm (ex: 15): 25.0
```

**Saída Gerada:**
```text
  [✗] RESULTADO: PEÇA REPROVADA!
      - ID: PEC-102
      - Peso: 90.00g | Cor: Vermelho | Comprimento: 25.00cm
      - Motivo(s) da reprovação:
        • Peso (90.00g) fora da faixa permitida [95.0g a 105.0g]
        • Cor 'vermelho' inválida (permitidas apenas: azul, verde)
        • Comprimento (25.00cm) fora da faixa permitida [10.0cm a 20.0cm]
```

---

### Exemplo 3: Fechamento Automático de Caixa (Ao Atingir 10 Peças Aprovadas)
Ao cadastrar a 10ª peça aprovada na Caixa #1:
```text
  [✓] RESULTADO: PEÇA APROVADA!
      - ID: PEC-110
      - Peso: 98.00g | Cor: Verde | Comprimento: 16.00cm
      - Alocada na: Caixa #1

  [★] ATENÇÃO: A Caixa #1 atingiu 10 peças e foi FECHADA com sucesso!
      Uma nova caixa (Caixa #2) foi iniciada.
```

---

### Exemplo 4: Relatório Final Consolidado (Opção 5)
```text
=================================================================
                    5. RELATÓRIO FINAL CONSOLIDADO                
=================================================================
  • Total de peças inspecionadas: 12
  • Peças Aprovadas:              10
  • Peças Reprovadas:             2
  • Taxa de Aprovação:            83.3%
  --------------------------------------------------
  • Caixas Fechadas (10 peças):   1
  • Peças na Caixa Atual:         0/10
  • Total de Caixas Utilizadas:   1

  --- DETALHAMENTO DE MOTIVOS DE REPROVAÇÃO ---
  • Peso (90.00g) fora da faixa permitida [95.0g a 105.0g] -> 1 ocorrência(s)
  • Cor 'vermelho' inválida (permitidas apenas: azul, verde) -> 2 ocorrência(s)
```

---

## 6. Estrutura do Repositório

```
├── main.py                     # Código fonte principal com lógica e interface
├── test_sistema.py             # Bateria de testes unitários automatizados
├── README.md                   # Instruções de instalação, uso e exemplos
├── PARTE_TEORICA.md            # Documento acadêmico de análise e discussão
├── ROTEIRO_PITCH.md            # Roteiro cronometrado para apresentação em vídeo
└── INSTRUCOES_TRABALHO.md      # Transcrição das diretrizes da UniFECAF
```
