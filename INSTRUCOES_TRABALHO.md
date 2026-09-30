# Orientações: Entrega de Trabalho - UniFECAF

## 1. Título do Projeto
**Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento**

---

## 2. O Desafio

Você foi convidado por uma empresa do setor industrial para prototipar uma solução de automação digital que auxilie no controle de produção e qualidade das peças fabricadas em sua linha de montagem. Atualmente, o processo de inspeção é feito manualmente, o que gera atrasos, falhas de conferência e aumento no custo de operação.

### Missão
Desenvolver em **Python** um sistema lógico capaz de:

- **Receber os dados de cada peça produzida:**
  - `id` (identificador da peça)
  - `peso`
  - `cor`
  - `comprimento`
- **Avaliar automaticamente se a peça está aprovada ou reprovada**, de acordo com critérios pré-definidos:
  - **Peso:** entre `95g` e `105g` (inclusive)
  - **Cor:** `azul` ou `verde`
  - **Comprimento:** entre `10cm` e `20cm` (inclusive)
- **Armazenar as peças aprovadas em caixas de capacidade limitada:**
  - Limite de **10 peças por caixa**.
- **Gerenciar caixas:**
  - Fechar a caixa atual assim que atingir a capacidade máxima (10 peças) e iniciar uma nova caixa automaticamente.
- **Gerar relatórios consolidados contendo:**
  - Total de peças aprovadas;
  - Total de peças reprovadas e o motivo detalhado de cada reprovação;
  - Quantidade total de caixas utilizadas/fechadas.

---

## 3. Fontes de Pesquisa

- Conteúdo da disciplina: **Algoritmos e Lógica de Programação**
- Documentação oficial do Python: [https://docs.python.org/3/](https://docs.python.org/3/)
- Comunidade Python Brasil: [https://python.org.br/](https://python.org.br/)

---

## 4. Entregáveis

O trabalho é composto por 3 partes principais:

### 4.1. Parte Teórica – Análise e Discussão
Documento dissertativo contendo:
1. **Contextualização do desafio:** por que a automação é importante na indústria moderna.
2. **Estruturação do raciocínio lógico:** breve explicação de como foram organizados os conceitos de tomada de decisão (`if/elif/else`), modularização/funções (`def`), validação de condições e estruturas de repetição (`while/for`).
3. **Benefícios e desafios:** benefícios percebidos na solução desenvolvida somados aos desafios enfrentados durante a implementação.
4. **Reflexão final:** como esse protótipo em Python poderia ser expandido para um cenário industrial real (ex.: integração com sensores físicos de peso/comprimento, visão computacional/IA para detecção de cor e integração com esteiras/CLP).

---

### 4.2. Parte Prática – Código Fonte
Código Python completo hospedado em repositório GitHub, contemplando:

#### Menu Interativo Totalmente Funcional:
1. **Cadastrar nova peça** (solicita ID, peso, cor e comprimento, valida e classifica em aprovada/reprovada, alocando na caixa se aprovada);
2. **Listar peças aprovadas/reprovadas** (exibe as listas com dados e motivos de rejeição);
3. **Remover peça cadastrada** (permite excluir uma peça cadastrada previamente);
4. **Listar caixas fechadas** (exibe o status e conteúdo das caixas que atingiram 10 peças);
5. **Gerar relatório final** (resumo geral da produção).

#### Arquivo `README.md` no Repositório com:
- Explicação clara do funcionamento do sistema.
- Passo a passo de como rodar o programa no terminal/IDE.
- Exemplos de entradas e saídas esperadas.

---

### 4.3. Vídeo Pitch (Até 4 Minutos)
Gravação de apresentação da solução contendo:
- Qual problema industrial foi solucionado;
- Explicação da lógica do sistema (critérios de aprovação, lógica de caixas e relatórios);
- Técnicas e boas práticas de programação adotadas;
- Demonstração prática do programa rodando no terminal ou IDE;
- Link de compartilhamento público ou não listado (YouTube, LinkedIn, Loom, Google Drive, etc.).

---

## 📋 Tabela Resumo dos Critérios de Qualidade

| Parâmetro | Faixa / Valor Aceito | Condição de Reprovação |
| :--- | :--- | :--- |
| **Peso** | 95g a 105g | < 95g ou > 105g |
| **Cor** | Azul ou Verde | Qualquer cor diferente |
| **Comprimento** | 10cm a 20cm | < 10cm ou > 20cm |
| **Capacidade da Caixa** | 10 peças aprovadas | Fecha ao atingir 10 e abre nova |
