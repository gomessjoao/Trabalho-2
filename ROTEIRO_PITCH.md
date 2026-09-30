# Roteiro para Gravação do Vídeo Pitch (Até 4 Minutos)
## Desafio de Automação Digital - UniFECAF

Este guia foi elaborado para auxiliá-lo na gravação do vídeo pitch de apresentação do seu trabalho acadêmico. O roteiro está cronometrado para totalizar aproximadamente **3 minutos e 30 segundos**, garantindo margem de segurança dentro do limite máximo de 4 minutos exigido pela instituição.

---

## ⏱️ Grade de Tempo Sugerida

| Bloco | Tempo Estimado | Conteúdo Principal | O Que Mostrar na Tela |
| :---: | :---: | :--- | :--- |
| **1** | 00:00 - 00:40 | Apresentação pessoal e o problema industrial resolvido | Rosto / Slide de Apresentação |
| **2** | 00:40 - 01:30 | Estrutura da lógica do sistema e regras de negócio | Diagrama de fluxo ou código (`main.py`) |
| **3** | 01:30 - 02:15 | Técnicas e boas práticas de programação aplicadas | Trechos de funções no VS Code / IDE |
| **4** | 02:15 - 03:30 | Demonstração prática do programa em funcionamento | Terminal interativo rodando |
| **5** | 03:30 - 03:50 | Conclusão, expansão futura e encerramento | Rosto / Terminal com Relatório Final |

---

## 🎙️ Roteiro de Fala Passo a Passo

### Bloco 1: Abertura e Problema Industrial (00:00 – 00:40)
- **O que falar:**
  > *"Olá, professor(a) e avaliadores! Meu nome é [Seu Nome], sou aluno da UniFECAF na disciplina de Algoritmos e Lógica de Programação. Hoje vou apresentar a solução desenvolvida para o Desafio de Automação Digital.*  
  > *Na indústria moderna, a inspeção manual de peças em linhas de montagem gera gargalos, atrasos e falhas humanas na conferência de padrões de qualidade. Para resolver esse problema, desenvolvi um sistema em Python que automatiza a conferência de peso, cor e dimensões das peças, além de gerenciar o armazenamento inteligente em caixas industriais."*

---

### Bloco 2: Estrutura da Lógica do Sistema (00:40 – 01:30)
- **O que falar:**
  > *"A lógica do sistema foi estruturada em três grandes pilares:*  
  > *Primeiro: Validação de Qualidade com critérios pré-definidos. Para ser aprovada, a peça precisa ter peso entre 95g e 105g, cor azul ou verde, e comprimento entre 10cm e 20cm.*  
  > *Segundo: Gestão de Armazenamento. As peças aprovadas são alocadas automaticamente em caixas com capacidade de 10 unidades. Assim que a décima peça entra, a caixa é selada e fechada, e o sistema abre uma nova caixa.*  
  > *Terceiro: Rastreabilidade e Relatórios. Peças reprovadas registram exatamente os motivos de desvio, e o sistema consolida dados em relatórios estatísticos para apoiar a tomada de decisão da fábrica."*

---

### Bloco 3: Boas Práticas e Técnicas de Programação (01:30 – 02:15)
- **O que falar:**
  > *"No desenvolvimento em Python, apliquei diversas boas práticas de programação:*  
  > *- Modularização e responsabilidade única: funções separadas para validar, cadastrar, alocar em caixas e relatórios.*  
  > *- Tratamento robusto de erros e exceções: uso de try/except e validação de strings para evitar que o operador digite letras no lugar de números ou valores incorretos.*  
  > *- Estruturas de dados eficientes: dicionários para representar as características da peça e listas para gerenciar o lote de produção.*  
  > *- Testes automatizados: foi criada uma suite com testes unitários em unittest que valida 100% dos limites e regras de negócio com zero falhas."*

---

### Bloco 4: Demonstração Prática no Terminal (02:15 – 03:30)
- **O que mostrar e falar no Terminal:**
  *(Dica: Abra o terminal com `python main.py` já pronto para demonstrar)*

  1. **Cadastrar Peça Aprovada (Opção 1):**
     > *"Vamos ver o sistema em ação. Vou selecionar a Opção 1 e cadastrar a peça PEC-01 com 100g, cor azul e 15cm. O sistema valida na hora e a classifica como Aprovada, alocando-a na Caixa #1."*
  
  2. **Cadastrar Peça Reprovada com múltiplos motivos (Opção 1):**
     > *"Agora vou cadastrar a peça PEC-02 com peso 90g, cor vermelha e 25cm. Notem que ela é Reprovada e o sistema aponta todos os motivos: peso fora da faixa, cor inválida e comprimento fora da tolerância."*
  
  3. **Listar Peças e Status de Caixas (Opções 2 e 4):**
     > *"Pela Opção 2 temos a listagem completa e transparente de aprovadas e reprovadas. Pela Opção 4 acompanhamos a contagem exata de peças na caixa em andamento."*
  
  4. **Relatório Final (Opção 5):**
     > *"Por fim, na Opção 5 geramos o Relatório Consolidado. Ele calcula a taxa percentual de qualidade, caixas utilizadas e contabiliza a causa raiz de cada falha."*

  *(Dica alternativa: Você também pode rodar `python simulador.py 25` no terminal para demonstrar em segundos a simulação de uma linha de produção com 25 peças, caixas fechando e relatório final automático!)*

---

### Bloco 5: Conclusão e Visão Futura (03:30 – 03:50)
- **O que falar:**
  > *"Como visão futura para a Indústria 4.0, essa mesma lógica pode ser acoplada a células de carga físicas, sensores ópticos de comprimento e visão computacional com IA para inspeção automática na esteira rolante.*  
  > *Muito obrigado pela atenção de todos!"*

---

## 💡 Recomendações Técnicas para a Gravação

1. **Ferramenta de Gravação Sugerida:**
   - **Loom** (grava tela e webcam simultaneamente no canto da tela de forma rápida e gera link na hora); ou
   - **OBS Studio / Clipchamp / Gravação de tela do Windows** (`Win + Alt + R`).
2. **Ambiente:**
   - Deixe o terminal com fonte legível (tamanho 16 ou 18) e fundo escuro.
   - Tenha 2 ou 3 exemplos de peças anotados para digitar com rapidez durante o vídeo.
3. **Entrega do Link:**
   - O trabalho exige link público ou não listado.
   - Opções válidas: YouTube (não listado), Loom (link direto) ou Google Drive (certifique-se de configurar o compartilhamento para *"Qualquer pessoa com o link pode visualizar"*).
