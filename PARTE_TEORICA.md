# Trabalho Acadêmico: Desafio de Automação Digital
## Gestão de Peças, Controle de Qualidade e Armazenamento

**Aluno:** João Pedro Gomes da Silva
**Matrícula:** 284437

**Disciplina:** Algoritmos e Lógica de Programação  
**Instituição:** Centro Universitário UniFECAF  

---

## 1. Contextualização do Desafio: A Importância da Automação na Indústria

No ecossistema industrial contemporâneo, amplamente impulsionado pelos pilares da **Indústria 4.0**, a garantia de qualidade e a eficiência operacional são fatores decisivos para a competitividade de mercado. Historicamente, os processos de controle dimensional, pesagem e inspeção visual de peças em linhas de montagem dependiam exclusivamente da ação humana manual. 

Contudo, a inspeção manual apresenta limitações intrínsecas severas:
- **Suscetibilidade à fadiga humana:** A repetição contínua de tarefas monótonas induz à desatenção, resultando na liberação de peças defeituosas (*falsos positivos*) ou descarte indevido de peças conformes (*falsos negativos*).
- **Gargalos produtivos:** A velocidade da checagem humana não acompanha a cadência de esteiras modernas automatizadas de alta velocidade.
- **Aumento de custos e retrabalho:** Falhas não detectadas na linha primária propagam-se para etapas posteriores da montagem ou, pior, chegam ao consumidor final, gerando custos expressivos com *recalls*, garantias e perda de reputação da marca.

A automação digital resolve esses gargalos ao introduzir um sistema lógico determinístico, padronizado e auditável. Cada peça fabricada é submetida aos mesmos critérios milimétricos e de tolerância de massa sem variações de julgamento, operando em tempo real com coleta sistemática de dados para retroalimentação da engenharia de processos.

---

## 2. Estruturação do Raciocínio Lógico

Para transformar o problema de negócio em uma solução de software coesa e manutenível, o raciocínio computacional foi estruturado com base nos paradigmas fundamentais da lógica de programação:

### 2.1. Tomada de Decisão e Condicionais (`if`, `elif`, `else`)
A tomada de decisão é o núcleo do módulo de inspeção. Uma peça só pode ser considerada aprovada se satisfizer **concomitantemente** às três regras de engenharia:
1. **Massa/Peso:** 95.0g <= peso <= 105.0g;
2. **Cor:** Pertencente ao conjunto restrito de aprovação {"azul", "verde"};
3. **Comprimento:** 10.0cm <= comprimento <= 20.0cm .

Em vez de utilizar uma única condicional rígida que apenas descarta a peça, adotou-se uma lógica acumuladora de não conformidades. Uma lista `motivos` registra cada desvio identificado, permitindo que a peça seja reprovada com rastreabilidade total (ex.: registrando simultaneamente que o peso está abaixo do limite e a cor está fora do padrão).

### 2.2. Modularização e Funções (`def`)
O código foi estruturado de forma modular e didática, com separação clara de responsabilidades:
- `validar_peca()`: Isola exclusivamente as regras matemáticas e lógicas de conformidade (peso, cor e comprimento).
- `processar_cadastro_peca()`: Coordena a validação, criação do dicionário da peça e o empacotamento automático na caixa.
- `processar_remocao_peca()`: Trata a exclusão cadastral mantendo a integridade das listas e caixas.
- `obter_dados_relatorio()`: Consolida as métricas de produção, taxa percentual de aprovação e agrupamento de motivos de falha.

### 2.3. Estruturas de Repetição (`while` e `for`)
- **Laço Principal (`while True`):** Mantém o menu interativo ativo, garantindo que o operador da linha possa realizar sucessivos cadastros, consultas e impressões de relatórios sem que o programa aborte inesperadamente.
- **Laços de Validação (`while` de entrada):** Garantem que dados de peso e comprimento sejam números válidos (`float`), interceptando exceções de digitação antes de afetar o cálculo lógico.
- **Laços de Varredura (`for`):** Utilizados para percorrer lotes de peças nas caixas, pesquisar IDs específicos para remoção e consolidar os motivos mais frequentes de reprovação.

### 2.4. Estruturas de Dados
Foram empregados **dicionários** (`dict`) para representar a entidade "Peça" com suas propriedades estruturadas (`id`, `peso`, `cor`, `comprimento`, `status`, `numero_caixa`), e **listas** (`list`) dinâmicas para gerenciar o fluxo contínuo de produção e o particionamento em caixas fechadas.

---

## 3. Benefícios Percebidos e Desafios Enfrentados

### 3.1. Benefícios Percebidos
- **Confiabilidade e Imparcialidade:** Eliminação de julgamentos subjetivos na aprovação de peças.
- **Rastreabilidade Ponta a Ponta:** Todo lote produzido possui registro de quais peças compõem cada caixa física fechada.
- **Gestão Inteligente de Estoque:** O empacotamento automatizado em lotes de 10 unidades padroniza a logística de despacho e paletização.
- **Diagnóstico de Falhas:** O relatório agrupado de motivos de reprovação fornece dados imediatos para a equipe de manutenção identificar se o desvio decorre de desgaste de ferramental (comprimento), desregulagem de dosagem de matéria-prima (peso) ou troca indevida de pigmento (cor).

### 3.2. Desafios Enfrentados no Desenvolvimento
- **Tratamento de Dados Imperfeitos do Usuário:** Operadores podem digitar vírgula em vez de ponto decimal (`10,5` em vez de `10.5`) ou digitar cores com variações de caixa e espaços acidentais (`"  Azul  "`). O código foi blindado com métodos de sanitização de strings (`.strip().lower()`) e conversão segura com `try/except`.
- **Integridade das Caixas na Remoção:** Ao permitir a remoção de uma peça cadastrada previamente, surgiu o desafio de manter a contagem da caixa consistente. Se uma peça de uma caixa de 10 unidades for excluída, a caixa correspondente precisa refletir 9 peças para que o estoque físico não fique divergente do sistema digital.
- **Evitar Duplicidade de Identificadores:** Garantir que o sistema impeça o cadastro de dois componentes com o mesmo código identificador (`ID`).

---

## 4. Reflexão Final: Expansão para um Cenário Industrial Real

O protótipo desenvolvido em Python estabelece a base algorítmica fundamental do fluxo produtivo. Em uma planta fabril real de grande escala, este sistema lógico seria integrado ao ecossistema de **Automação e Internet das Coisas Industrial (IIoT)** por meio das seguintes tecnologias:

### 4.1. Sensores Físicos Integrados
- **Pesagem Automática:** Substituição do `input()` manual por uma **célula de carga com módulo conversor A/D (ex.: HX711)** instalada sob a esteira rolante, capturando a massa da peça em frações de segundo.
- **Dimensionamento Linear:** Utilização de **sensores de triangulação laser** ou **barreiras ópticas de medição** que calculam o comprimento da peça durante sua passagem pela esteira com precisão micrométrica.

### 4.2. Visão Computacional e Inteligência Artificial
- **Detecção de Cor e Integridade Superficial:** Instalação de uma câmera industrial posicionada acima da esteira integrada a uma biblioteca de visão computacional (como OpenCV ou modelos de Deep Learning tipo YOLO). A IA não apenas classificará a cor exata da peça (mesmo sob variações de iluminação de fábrica), mas também inspecionará trincas, rebarbas, bolhas e defeitos geométricos não detectáveis por sensores convencionais.

### 4.3. Atuação Mecatrônica e Integração com CLP (Controlador Lógico Programável)
- **Descarte Automatizado:** Ao identificar uma peça reprovada, o algoritmo emite um sinal digital via protocolo industrial (**Modbus**, **MQTT** ou **OPC UA**) para um **pistão pneumático** ou braço robótico que empurra a peça defeituosa diretamente para uma calha de refugo.
- **Paletização e Empacotamento:** Quando o contador atinge 10 peças aprovadas, o sistema comanda um robô cartesiano para selar a caixa, etiquetá-la com código de barras/QR Code e mover uma nova caixa vazia para o posto de abastecimento.

### 4.4. Conclusão
A transição do software em terminal para a fábrica inteligente (Smart Factory) mantém a mesma lógica algorítmica concebida neste projeto, comprovando que o raciocínio lógico bem estruturado é a pedra fundamental sobre a qual toda a infraestrutura da Indústria 4.0 é erguida.
