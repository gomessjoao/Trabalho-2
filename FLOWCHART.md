# Fluxograma do Sistema: Automação Digital e Controle de Qualidade

**Aluno:** João Pedro Gomes da Silva  
**Matrícula:** 284437  
**Disciplina:** Algoritmos e Lógica de Programação  
**Instituição:** Centro Universitário UniFECAF  

> [!TIP]
> **Como visualizar o fluxograma na IDE:**  
> Pressione **`Ctrl + Shift + V`** (ou clique no ícone de lupa/pré-visualização **"Open Preview to the Side"** no canto superior direito do editor) para abrir o renderizador nativo de Markdown e ver o diagrama completo interativo.

---

## Fluxograma Geral (Flowchart TD)

```mermaid
flowchart TD
    %% Estilo dos Nós
    classDef startEnd fill:#0ea5e9,stroke:#0284c7,stroke-width:2px,color:#fff;
    classDef menuNode fill:#1e293b,stroke:#64748b,stroke-width:2px,color:#f8fafc;
    classDef optNode fill:#334155,stroke:#94a3b8,stroke-width:2px,color:#f8fafc;
    classDef aprNode fill:#059669,stroke:#10b981,stroke-width:2px,color:#fff;
    classDef repNode fill:#dc2626,stroke:#ef4444,stroke-width:2px,color:#fff;
    classDef boxNode fill:#7c3aed,stroke:#8b5cf6,stroke-width:2px,color:#fff;

    START(["Início do Programa"]):::startEnd --> MENU["Menu Principal Interativo<br/>Opções 0 a 5"]:::menuNode

    MENU --> OPT{"Qual a opção<br/>selecionada?"}:::menuNode

    %% ---------------------------------------------------------
    %% OPÇÃO 1: CADASTRAR PEÇA
    %% ---------------------------------------------------------
    OPT -->|"Opção 1"| C1["Cadastrar Nova Peça"]:::optNode
    C1 --> C2[/"Entrada de Dados:<br/>ID, Peso, Cor, Comprimento"/]
    C2 --> C3{"O ID já existe<br/>cadastrado?"}
    
    C3 -->|"Sim"| C_ERR["Exibir Erro: ID Duplicado"]:::repNode --> MENU
    
    C3 -->|"Não"| C4{"Validação de Qualidade:<br/>• Peso entre 95g e 105g?<br/>• Cor é Azul ou Verde?<br/>• Comp. entre 10cm e 20cm?"}
    
    %% Fluxo de Aprovação
    C4 -->|"Sim (100% Conforme)"| C_APR["Status: APROVADA"]:::aprNode
    C_APR --> C_BOX["Inserir Peça na Caixa Atual"]:::boxNode
    C_BOX --> C5{"Caixa Atual atingiu<br/>10 peças?"}
    
    C5 -->|"Sim"| C6["Fechar Caixa Atual<br/>Mover para Caixas Fechadas<br/>Iniciar Nova Caixa"]:::boxNode
    C6 --> C_OK1["Exibir Confirmação ao Usuário"] --> MENU
    
    C5 -->|"Não"| C7["Permanecer na Caixa Atual<br/>Exibir Vagas Restantes"]
    C7 --> C_OK1

    %% Fluxo de Reprovação
    C4 -->|"Não (Fora do Padrão)"| C_REP["Status: REPROVADA"]:::repNode
    C_REP --> C_MOTIV["Registrar Motivos da Falha<br/>(Peso, Cor e/ou Comprimento)"]
    C_MOTIV --> C_HIST["Armazenar no Histórico de Refugo"]
    C_HIST --> C_OK2["Exibir Motivos ao Usuário"] --> MENU

    %% ---------------------------------------------------------
    %% OPÇÃO 2: LISTAR PEÇAS
    %% ---------------------------------------------------------
    OPT -->|"Opção 2"| L1["Listar Peças"]:::optNode
    L1 --> L2["Exibir Peças Aprovadas com Número da Caixa"]
    L2 --> L3["Exibir Peças Reprovadas com Motivos de Falha"]
    L3 --> MENU

    %% ---------------------------------------------------------
    %% OPÇÃO 3: REMOVER PEÇA
    %% ---------------------------------------------------------
    OPT -->|"Opção 3"| R1["Remover Peça Cadastrada"]:::optNode
    R1 --> R2[/"Digitar ID da Peça a Remover"/]
    R2 --> R3{"Peça localizada<br/>pelo ID?"}
    
    R3 -->|"Não"| R_FAIL["Exibir: Peça não encontrada"]:::repNode --> MENU
    R3 -->|"Sim (Reprovada)"| R_DEL1["Excluir do Histórico de Refugo"] --> R_SUCC["Exibir Sucesso"] --> MENU
    R3 -->|"Sim (Aprovada)"| R_DEL2["Remover de Aprovadas e<br/>Retirar da Caixa Correspondente"] --> R_SUCC

    %% ---------------------------------------------------------
    %% OPÇÃO 4: LISTAR CAIXAS
    %% ---------------------------------------------------------
    OPT -->|"Opção 4"| CX1["Listar Caixas"]:::optNode
    CX1 --> CX2["Exibir Caixas Fechadas (10 peças cada)"]:::boxNode
    CX2 --> CX3["Exibir Status da Caixa Atual em Andamento"]
    CX3 --> MENU

    %% ---------------------------------------------------------
    %% OPÇÃO 5: GERAR RELATÓRIO FINAL
    %% ---------------------------------------------------------
    OPT -->|"Opção 5"| REL1["Gerar Relatório Final"]:::optNode
    REL1 --> REL2["Calcular Total de Peças e Taxa de Qualidade %"]
    REL2 --> REL3["Contabilizar Caixas Fechadas e Utilizadas"]
    REL3 --> REL4["Agrupar e Contar Ocorrências por Motivo de Descarte"]
    REL4 --> REL5["Exibir Resumo Estatístico Consolidado"]
    REL5 --> MENU

    %% ---------------------------------------------------------
    %% OPÇÃO 0: SAIR DO SISTEMA
    %% ---------------------------------------------------------
    OPT -->|"Opção 0"| FIM(["Encerrar o Programa"]):::startEnd
```

---

## Resumo das Decisões e Entidades

| Decisão / Ação | Condição | Resultado Lógico |
| :--- | :--- | :--- |
| **Aprovação da Peça** | `95.0 <= peso <= 105.0` e `cor in ['azul', 'verde']` e `10.0 <= comp <= 20.0` | Peça aprovada e direcionada à caixa |
| **Reprovação da Peça** | Qualquer condição violada | Registro da não conformidade na lista de refugo |
| **Fechamento de Caixa** | `len(caixa_atual) == 10` | Caixa é selada, adicionada a `caixas_fechadas` e nova caixa vazia é aberta |
| **Remoção de Peça** | ID existente na lista | Exclusão do cadastro e readequação de caixas |
