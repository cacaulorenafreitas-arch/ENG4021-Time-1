# Prompt para o Claude Design — Wireframes e Protótipos

> Copie tudo abaixo da linha e cole no Claude Design.

---

Você vai produzir dois entregáveis para um projeto acadêmico de desenvolvimento de software da PUC-Rio: **3 wireframes de baixa fidelidade** e, a partir deles, **3 protótipos de alta fidelidade** das mesmas telas.

O produto se chama **Timeline** — uma plataforma de organização da rotina estudantil. O diferencial dela não é exibir compromissos, e sim **ajudar o aluno a decidir o que fazer, quando fazer, em que ordem e quanto tempo reservar**, além de remontar o plano quando algo dá errado.

Formato de tela: **mobile, 390 × 844 px**. O público-alvo são alunos de graduação, e as entrevistas mostraram que a organização acontece majoritariamente no celular.

---

## PARTE 0 — CONTEXTO E CRITÉRIO DE ESCOLHA DAS TELAS

O sistema tem 15 requisitos funcionais. As três telas escolhidas não são as três "mais bonitas" — são as que fecham o **ciclo mínimo de valor** do produto, cobrindo as três etapas do macroprocesso:

| Etapa do processo | Tela | Requisitos cobertos |
|---|---|---|
| **Entrada de dados** | Cadastro de Atividade | RF03, RF05, RF10 |
| **Motor de planejamento** | Planejamento Semanal | RF06, RF07, RF11 |
| **Execução e ajuste** | Hoje | RF08, RF12, RF14 |

Sem qualquer uma das três, o produto não entrega valor: sem cadastro não há dados, sem planejamento é só uma lista de tarefas, e sem a tela de execução o aluno não fecha o ciclo nem alimenta o histórico.

---

## PARTE 1 — OS 3 WIREFRAMES (baixa fidelidade)

**Regras obrigatórias de baixa fidelidade:**
- Escala de cinza apenas. Nada de cor de marca, nenhum roxo.
- Imagens e ícones representados por retângulo com um X diagonal.
- Texto real onde a informação importa (títulos, rótulos de botão, nomes de campo). Texto genérico em barras cinzas onde o conteúdo é ilustrativo.
- Traço simples de 1px, cantos retos ou levemente arredondados.
- Sem sombra, sem gradiente, sem tipografia decorativa.
- **Anotações numeradas** ao lado de cada tela: círculos numerados sobre os elementos-chave, com a legenda ao lado explicando a função e o requisito atendido. Isso é o que transforma o wireframe em documento de ideação — não pule.

### Wireframe 1 — Cadastro de Atividade

Estrutura vertical:
1. Cabeçalho com botão de voltar à esquerda, título "Nova atividade", botão "Salvar" à direita
2. Campo de texto grande: "Nome da atividade"
3. Seletor horizontal de tipo, em pílulas: Prova · Trabalho · Lista · Leitura · Projeto
4. Campo de seleção: "Disciplina"
5. Campo de data e hora: "Prazo"
6. **Divisor com rótulo expansível: "Detalhar (opcional)"** — colapsado por padrão, com seta indicando expansão
7. Área revelada ao expandir, mostrada aberta no wireframe com fundo levemente destacado: Dificuldade (escala 1–5), Peso na nota (%), Importância (escala 1–5), Duração estimada
8. Aviso de conflito: faixa fina com ícone e texto "Conflito de horário detectado"
9. Botão primário largura total: "Salvar atividade"

**Anotações:**
1. Apenas três campos são obrigatórios: nome, tipo e prazo. Atende o RNF02 e responde à hipótese 11 refutada — se o cadastro exigir oito campos, o aluno abandona.
2. O bloco "Detalhar" é progressivo. Se não preenchido, o sistema aplica valores padrão por tipo de atividade.
3. Os campos opcionais alimentam o cálculo do score de prioridade (RF06). Quanto mais preenchido, melhor o planejamento.
4. Detecção de conflito em tempo real (RF10), não só na hora de salvar.

### Wireframe 2 — Planejamento Semanal

Estrutura vertical:
1. Cabeçalho: título "Sua semana", subtítulo com o intervalo de datas, ícone de regenerar à direita
2. **Faixa de alerta de carga**: barra horizontal com rótulo à esquerda, indicador percentual à direita, e uma linha de texto de recomendação abaixo
3. Seletor de dias: sete itens horizontais (S T Q Q S S D) com o dia ativo destacado
4. **Linha do tempo vertical** — elemento central da tela. Coluna estreita de horários à esquerda (08:00 a 22:00), e à direita os blocos empilhados cronologicamente. Três naturezas visuais distintas:
   - Bloco de aula: hachurado ou com borda dupla, marcado como fixo
   - Bloco de atividade alocada pelo sistema: contorno simples, com ícone de "gerado automaticamente"
   - Bloco de compromisso pessoal: contorno tracejado
   - Uma janela vazia entre blocos, rotulada "45 min livres" com um botão pequeno "Ver sugestões"
5. Ao pé, resumo: "12h alocadas · 4h livres"

**Anotações:**
1. Alerta de sobrecarga (RF11) calculado por horas necessárias sobre horas disponíveis. Aparece antes da semana começar, não durante.
2. Aulas e compromissos fixos são imóveis — o motor agenda ao redor deles.
3. Blocos de atividade são gerados automaticamente pelo motor (RF07), ordenados por score de prioridade (RF06), e podem ser fragmentados quando a atividade é longa.
4. Janelas curtas viram oportunidade de encaixe (RF14) em vez de espaço morto.

### Wireframe 3 — Hoje

Estrutura vertical:
1. Cabeçalho: saudação com nome, data por extenso abaixo, ícone de notificação à direita
2. **Cartão de foco**: bloco destacado com rótulo "Agora" ou "A seguir", nome da atividade, disciplina, horário e duração
3. **Barra de progresso** com indicação numérica: "3 de 7 tarefas"
4. Linha do tempo compacta do dia — versão reduzida da tela 2, mostrando apenas as próximas horas
5. **Lista de tarefas pendentes**: cada item é um cartão com checkbox à esquerda, nome da tarefa, tag da disciplina, tag de prioridade, prazo e duração estimada
6. Botão flutuante circular de adicionar, no canto inferior direito
7. Barra de navegação inferior com cinco itens: Hoje · Agenda · Adicionar · Calendário · Perfil

**Anotações:**
1. A tela responde três perguntas em menos de cinco segundos: o que tenho hoje, o que é mais importante, quanto já concluí.
2. O cartão de foco elimina a decisão do usuário — é o item de maior score no momento presente.
3. Marcar conclusão (RF12) registra o tempo real gasto, que alimenta a calibração das estimativas futuras (RF15).
4. Navegação híbrida: barra inferior no celular, menu lateral no desktop.

---

## PARTE 2 — OS 3 PROTÓTIPOS (alta fidelidade)

Agora refaça exatamente as mesmas três telas, mesma estrutura e mesma hierarquia, aplicando o design system abaixo. **Não invente elementos novos nem reorganize o layout** — o valor do exercício é mostrar a evolução do wireframe para o protótipo.

### Design system do Timeline

**Cores primárias**
- Lavender Blue `#7477E8` — marca, ação principal, blocos gerados pelo sistema
- Deep Lavender `#5558C9` — títulos, ênfase
- Soft Lavender `#ECECFF` — fundos de blocos e áreas destacadas
- Light Lavender `#F6F5FF` — fundos sutis

**Neutras**
- Ink `#202238` (texto) · Slate `#62657A` (secundário) · Muted `#9699AA` (legendas) · Border `#E3E4EC` · Surface `#FFFFFF` · Background `#F8F8FC`

**Semânticas**
- Sucesso `#3EAD87` · Alerta `#E8A63A` · Erro `#D95D6A` · Informação `#4389D8`

**Tipografia**
- Manrope para títulos e destaques
- Inter para corpo e interface
- Base 16px, espaçamento vertical de 24px entre blocos

**Grid mobile:** 4 colunas, margens de 16px, gutter de 16px.

**Estilo:** flat minimal. Bordas finas e suaves em cores neutras. Sombras discretas. Fundos em cinza-lavanda muito claro. O conceito da marca é **calma** — apps de produtividade normalmente transmitem urgência e cobrança, e este quer o oposto.

**Botões**
- Primário: fundo Lavender Blue, texto branco
- Secundário: fundo claro, borda lavanda, texto na cor principal
- Terciário: sem fundo, apenas texto ou ícone
- Destrutivo: vermelho, exclusivamente para excluir ou cancelar em definitivo

### Conteúdo realista para os protótipos

Use dados de um aluno de Engenharia de Produção. Nada de "Lorem ipsum" nem "Tarefa 1".

**Disciplinas e cores de tag:** Cálculo III (`#7477E8`) · Física II (`#4389D8`) · Mecânica dos Sólidos (`#3EAD87`) · Estatística (`#E8A63A`)

**Tela Cadastro:** atividade sendo criada — "Lista 4 — Integrais de superfície", tipo Lista, disciplina Cálculo III, prazo quinta, 23h59. Bloco opcional expandido com Dificuldade 4, Peso 10%, Duração estimada 2h.

**Tela Planejamento:** índice de carga em 0,92 — faixa "apertado", em `#E8A63A`, com a recomendação "Semana apertada. Comece o relatório de Física II ainda hoje." Blocos do dia: Cálculo III 08h–10h (aula, imóvel) · Lista 4 de Cálculo 10h15–12h15 (gerada pelo sistema) · Almoço 12h30–13h30 · Física II 14h–16h (aula) · janela livre de 45 min às 16h · Academia 17h–18h30 (pessoal) · Relatório de Física, parte 1 de 3, 19h30–21h (gerada pelo sistema).

**Tela Hoje:** saudação "Bom dia, João" · quinta-feira, 10 de setembro · cartão de foco com "Lista 4 — Integrais de superfície", Cálculo III, agora até 12h15 · progresso "3 de 7 tarefas" · lista pendente com Relatório de Física II (prioridade alta, 3h, prazo segunda), Leitura Cap. 5 — Mecânica dos Sólidos (prioridade média, 40min, prazo sexta), Lista 2 de Estatística (prioridade baixa, 1h30, prazo próxima quarta).

### Elementos que os protótipos devem materializar

- **Tags de disciplina e prioridade:** texto curto, cor suave, cantos bem arredondados.
- **Cartões de tarefa:** checkbox, nome, disciplina, prazo, prioridade, duração estimada, status.
- **Barra de progresso:** sempre com indicação numérica ao lado, nunca só a barra.
- **Linha do tempo:** organiza o dia em ordem cronológica, com distinção visual clara entre bloco fixo (aula, compromisso) e bloco gerado pelo sistema. Sugestão: blocos gerados com fundo `#ECECFF` e uma marca sutil em `#7477E8`; blocos fixos com fundo branco e borda `#E3E4EC`.
- **Alerta de carga:** informa o que aconteceu, qual atividade é afetada e o que o usuário deve fazer.

### Apresentação dos protótipos

Disponha as três telas lado a lado, com o nome de cada uma abaixo. Acima, um cabeçalho com o logotipo: um **círculo aberto** com traço de ~4px em `#7477E8` e cinco pontos distribuídos ao longo do arco — a abertura representa continuidade, é um ciclo de melhoria e não uma meta final; os pontos são as tarefas e eventos. Ao lado, o nome "Timeline" em Manrope e o slogan "Plan today. Move at your pace."

---

## O QUE EVITAR

- Nos wireframes, nenhuma cor de marca. Se aparecer roxo, o wireframe falhou.
- Nos protótipos, não mude a estrutura do wireframe. Mesma ordem, mesma hierarquia, mesmos elementos.
- Nada de texto placeholder genérico nos protótipos.
- Nada de emoji ou ícones de stock coloridos. Ícones em traço simples e uniforme, mesma espessura.
- Não use vermelho fora de erro ou exclusão. Prioridade alta é `#E8A63A`, não vermelho — a marca transmite calma, não pânico.
- Não encha as telas. Espaço em branco é parte do conceito.
