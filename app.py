import io
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# ==============================================================================
# CONFIGURAÇÃO GERAL DA PÁGINA
# ==============================================================================
st.set_page_config(
    page_title="Hub do Criador de Apps com IA",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inicializando histórico de dados na memória da sessão (Session State)
# Isso garante que ao adicionar novos registros a tela não 'zere' os dados
if "clientes_db" not in st.session_state:
  st.session_state.clientes_db = pd.DataFrame([
      {
          "Nome": "Ana Silva",
          "Email": "ana@empresa.com",
          "Departamento": "Vendas",
          "Valor_Proposta": 12500.0,
      },
      {
          "Nome": "Carlos Souza",
          "Email": "carlos@gestao.com",
          "Departamento": "RH",
          "Valor_Proposta": 4300.0,
      },
      {
          "Nome": "Beatriz Lima",
          "Email": "beatriz@tech.com",
          "Departamento": "TI",
          "Valor_Proposta": 28000.0,
      },
  ])

# ==============================================================================
# BARRA LATERAL (SIDEBAR)
# ==============================================================================
with st.sidebar:
  st.title("💡 Central do Aluno")
  st.caption("Do Zero ao seu Próprio Sistema com IA")

  st.markdown("---")
  st.markdown("### 🎯 O Novo Modo de Programar")
  st.info(
      "**Você não precisa decorar códigos!**\n\n"
      "O seu papel é ser o **Arquiteto da Solução** (saber o que quer resolver)."
      " A IA é o seu **Programador Sênior** gratuito."
  )

  st.markdown("### 💻 Comandos Essenciais do Terminal")
  with st.expander("Ver comandos do Terminal"):
    st.markdown("**1. Instalar as bibliotecas:**")
    st.code("pip install streamlit pandas matplotlib", language="bash")
    st.markdown("**2. Rodar o seu aplicativo:**")
    st.code("streamlit run app.py", language="bash")
    st.markdown("**3. Parar o aplicativo:**")
    st.caption("Pressione Ctrl + C no terminal.")

  st.markdown("---")
  if st.button("🧹 Limpar Dados de Teste"):
    st.session_state.clientes_db = pd.DataFrame(
        columns=["Nome", "Email", "Departamento", "Valor_Proposta"]
    )
    st.rerun()

# ==============================================================================
# CABEÇALHO PRINCIPAL
# ==============================================================================
st.title("🚀 Hub de Criação: Construa seus Próprios Apps com IA")
st.markdown(
    """
    Seja bem-vindo ao guia prático da turma! Aqui você vai aprender a **pensar, pedir e construir** ferramentas 
    úteis para o seu trabalho e dia a dia, combinando **Python**, **Streamlit**, **Pandas** e **Inteligência Artificial**.
    """
)

# ==============================================================================
# ESTRUTURA DE ABAS DIDÁTICAS
# ==============================================================================
aba_metodo, aba_gerador, aba_bibliotecas, aba_ias_copilot, aba_exemplos = (
    st.tabs([
        "🗺️ O Método (Como Criar)",
        "🪄 Gerador de Super Prompts",
        "📦 As 3 Ferramentas (Bibliotecas)",
        "🤖 Guia IAs & GitHub Copilot",
        "💻 Aplicativos Práticos de Exemplo",
    ])
)

# ==============================================================================
# ABA 1: O MÉTODO (DO ZERO AO APP)
# ==============================================================================
with aba_metodo:
  st.header("🗺️ O Método dos 4 Passos para Criar Qualquer Sistema")
  st.write(
      "Em vez de ficar horas decorando sintaxe, siga esta esteira de trabalho"
      " ágil:"
  )

  col_p1, col_p2, col_p3, col_p4 = st.columns(4)

  with col_p1:
    st.markdown("#### 1️⃣ Definir a Dor")
    st.markdown(
        """
            Antes de abrir qualquer IA, responda:
            - Que problema isso resolve?
            - O que o usuário vai digitar?
            - O que a tela deve calcular ou exibir?
            """
    )
    st.caption(
        "Exemplo: 'Preciso de um simulador de parcelamento para enviar pro"
        " cliente'."
    )

  with col_p2:
    st.markdown("#### 2️⃣ O Super Prompt")
    st.markdown(
        """
            Peça para a IA com estrutura:
            - **Papel:** 'Aja como especialista Python e Streamlit'.
            - **Objetivo:** O que o app faz.
            - **Regras:** Campos na tela, validações, design.
            - **Entrega:** 'Entregue o código completo em um arquivo só'.
            """
    )
    st.caption("Dica: Use a aba 'Gerador de Prompts' deste app!")

  with col_p3:
    st.markdown("#### 3️⃣ Colar e Rodar")
    st.markdown(
        """
            - Crie um arquivo no VS Code (ex: `app.py`).
            - Cole o código gerado pela IA.
            - Abra o Terminal do VS Code (`Ctrl + '`).
            - Digite: `streamlit run app.py`.
            - O navegador abrirá automaticamente!
            """
    )
    st.caption("Se aparecer erro no terminal, veja o passo 4.")

  with col_p4:
    st.markdown("#### 4️⃣ Iterar e Atualizar")
    st.markdown(
        """
            O segredo do Low-Code com IA é a conversa contínua:
            - **Deu erro?** Copie a mensagem inteira do terminal e cole na IA: *'Deu esse erro, conserte para mim'*.
            - **Quer melhorar?** *'Agora adicione um botão para baixar os dados em Excel'*.
            """
    )
    st.caption("Você vai melhorando o app bloco a bloco.")

  st.markdown("---")
  st.subheader("💡 O Conceito de 'Vibe Coding' / Programador-Arquiteto")
  st.success(
      "**Mensagem Importante:** Você não precisa se sentir inseguro por não"
      " saber programar tudo de cabeça. Profissionais modernos que dominam o"
      " uso da IA para criar soluções sob demanda produzem 10x mais rápido. O"
      " seu verdadeiro diferencial é **entender a regra de negócio** da sua"
      " empresa ou área!"
  )

# ==============================================================================
# ABA 2: GERADOR DE SUPER PROMPTS (INTERATIVO)
# ==============================================================================
with aba_gerador:
  st.header("🪄 Gerador Interativo de Prompts para IA")
  st.write(
      "Preencha as opções abaixo para gerar uma instrução perfeita pronta para"
      " colar no ChatGPT, Gemini ou Copilot!"
  )

  col_g1, col_g2 = st.columns([1, 1])

  with col_g1:
    tipo_app = st.selectbox(
        "1. Qual o tipo de ferramenta que você quer criar?",
        [
            (
                "Calculadora ou Simulador de Negócios (Orçamento, Margem,"
                " Financiamento)"
            ),
            "Sistema de Cadastro com Tabela e Exportação para Excel/CSV",
            "Dashboard de Análise com Gráficos e Indicadores (KPIs)",
            "Formulário de Checklist ou Vistoria com Relatório Final",
            "Outro Sistema Personalizado",
        ],
    )

    nome_ferramenta = st.text_input(
        "2. Dê um nome para a sua ferramenta:",
        value="Simulador de Precificação e Vendas",
    )

    st.markdown(
        "**3. Quais recursos você quer que ela tenha? (Marque as opções"
        " desejadas)**"
    )
    recurso_tabela = st.checkbox(
        "Tabela de dados na tela (usando Pandas)", value=True
    )
    recurso_grafico = st.checkbox(
        "Gráficos visuais (usando Matplotlib ou gráficos Streamlit)", value=True
    )
    recurso_download = st.checkbox(
        "Botão para baixar relatório em CSV/Excel", value=True
    )
    recurso_validacao = st.checkbox(
        "Validação de campos (avisar se faltar preencher)", value=True
    )
    recurso_abas = st.checkbox(
        "Organização em abas ou colunas modernas", value=True
    )

  with col_g2:
    campos_regras = st.text_area(
        "4. Descreva com suas próprias palavras os campos e regras do seu"
        " negócio:",
        value=(
            "Quero que o usuário digite o Nome do Produto, o Custo de"
            " Produção, a Margem de Lucro desejada em porcentagem e os"
            " Impostos. O app deve calcular o Preço Final sugerido de venda e o"
            " Lucro Líquido em Reais."
        ),
        height=180,
    )

    # Montando o Super Prompt automaticamente
    recursos_texto = []
    if recurso_tabela:
      recursos_texto.append(
          "- Utilize a biblioteca 'pandas' para estruturar os dados em tabela."
      )
    if recurso_grafico:
      recursos_texto.append(
          "- Crie gráficos visuais claros para ilustrar os resultados."
      )
    if recurso_download:
      recursos_texto.append(
          "- Adicione um botão de download para o usuário baixar a tabela em"
          " formato CSV."
      )
    if recurso_validacao:
      recursos_texto.append(
          "- Faça validação de erros (ex: campos vazios ou divisão por zero)"
          " exibindo st.warning ou st.error."
      )
    if recurso_abas:
      recursos_texto.append(
          "- Organize a interface de forma elegante usando st.tabs ou"
          " st.columns."
      )

    prompt_final = f"""Aja como um Desenvolvedor Python e Streamlit Sênior e crie um aplicativo completo para mim.
Eu não sou programador profissional, portanto o código deve ser direto, bem comentado em português e pronto para rodar em um único arquivo (app.py).

### OBJETIVO DO APLICATIVO:
Criar um(a): {nome_ferramenta} ({tipo_app}).

### REGRAS E CAMPOS DO SISTEMA:
{campos_regras}

### REQUISITOS TÉCNICOS OBRIGATÓRIOS:
- Use a biblioteca 'streamlit' para criar a interface web completa.
{chr(10).join(recursos_texto)}
- Utilize componentes visuais modernos do Streamlit como: st.metric, st.success, st.columns, st.dataframe.
- Mantenha os dados salvos durante o uso usando st.session_state (se houver cadastros ou listas).
- Entregue o código completo de uma só vez, sem omitir partes (sem "coloque seu código aqui").
- No final da resposta, inclua uma instrução rápida de como instalar as bibliotecas necessárias com pip e como rodar no terminal.
"""

  st.markdown("---")
  st.subheader("📋 Seu Super Prompt Pronto para Copiar:")
  st.write(
      "Clique no ícone de copiar no canto superior direito do bloco abaixo e"
      " cole na sua IA favorita (ChatGPT, Gemini, Copilot):"
  )
  st.code(prompt_final, language="markdown")

# ==============================================================================
# ABA 3: AS 3 FERRAMENTAS ESSENCIAIS (BIBLIOTECAS)
# ==============================================================================
with aba_bibliotecas:
  st.header("📦 As 3 Armas Secretas do Criador de Apps")
  st.write(
      "Para criar ferramentas profissionais, você só precisa conhecer o papel"
      " de **três bibliotecas** em Python. A IA escreve a sintaxe complexa, mas"
      " você deve saber o que pedir:"
  )

  card1, card2, card3 = st.columns(3)

  with card1:
    st.subheader("1. 🎨 Streamlit")
    st.caption("A Casca Visual (Interface Web)")
    st.markdown(
        """
            Transforma qualquer script Python em uma página web navegável sem precisar de HTML ou CSS.
            
            **Componentes comuns para pedir à IA:**
            - `st.title()` e `st.header()`: Títulos
            - `st.number_input()`: Campo de números
            - `st.text_input()`: Campo de texto
            - `st.button()`: Botões de ação
            - `st.metric()`: Cards com números destacados
            - `st.columns()` e `st.tabs()`: Organização visual
            """
    )

  with card2:
    st.subheader("2. 🐼 Pandas")
    st.caption("O Excel Invisível do Python")
    st.markdown(
        """
            É a ferramenta oficial para manipular tabelas (chamadas de **DataFrames**).
            
            **Para que serve no seu app:**
            - Armazenar cadastros e registros.
            - Fazer somas, médias e filtros automáticos.
            - Ler e salvar arquivos `.csv` e `.xlsx`.
            - Exibir dados limpos na tela com `st.dataframe()`.
            """
    )

  with card3:
    st.subheader("3. 📊 Matplotlib / Gráficos")
    st.caption("Gráficos e Dashboards")
    st.markdown(
        """
            Permite transformar números brutos em visuais impactantes para tomadas de decisão.
            
            **Tipos comuns de pedir para a IA:**
            - Gráficos de Barras (comparar categorias).
            - Gráficos de Linha (evolução no tempo).
            - Gráficos de Pizza/Rosca (participação percentual).
            - O Streamlit também tem atalhos rápidos: `st.bar_chart()`, `st.line_chart()`.
            """
    )

# ==============================================================================
# ABA 4: GUIA DE IAS GRATUITAS & GITHUB COPILOT
# ==============================================================================
with aba_ias_copilot:
  st.header("🤖 Como Usar as IAs Gratuitas & GitHub Copilot")

  st.markdown(
      """
        Muitos alunos têm dúvida: *'Eu preciso pagar o GitHub Copilot? Posso usar o ChatGPT grátis? Como eles se complementam?'*
        Aqui está a resposta definitiva:
        """
  )

  col_ia1, col_ia2 = st.columns(2)

  with col_ia1:
    st.subheader("🐙 1. GitHub Copilot Free (Gratuito no VS Code)")
    st.markdown(
        """
            **A boa notícia:** O GitHub liberou um plano **100% gratuito** do Copilot para qualquer usuário com conta no GitHub!
            
            **Como configurar:**
            1. Abra o **VS Code**.
            2. Vá na aba de Extensões (`Ctrl + Shift + X`).
            3. Pesquise por **'GitHub Copilot'** e clique em Instalar.
            4. Faça login com a sua conta gratuita do GitHub.
            
            **O que a versão gratuita oferece:**
            - Até **2.000 sugestões de autocompletar código** por mês enquanto você digita (tecla `Tab` para aceitar).
            - Até **50 mensagens de Chat por mês** no painel lateral do VS Code.
            
            **Como usar no dia a dia:**
            - Abra o seu arquivo `app.py`.
            - Pressione `Ctrl + I` para abrir o chat flutuante em cima do código e peça:
              *'Adicione um botão para exportar a tabela para CSV'*.
            - Ele altera o código diretamente no arquivo!
            """
    )

  with col_ia2:
    st.subheader("🌐 2. IAs Externas Gratuitas (ChatGPT, Gemini, Claude)")
    st.markdown(
        """
            As IAs de navegador são suas melhores parceiras para **gerar o projeto do zero** e ter conversas longas:
            
            **As melhores opções gratuitas hoje:**
            - **Google Gemini (gemini.google.com):** Janela de contexto enorme, excelente para códigos Python e gratuito.
            - **ChatGPT Free (chatgpt.com):** Muito rápido e com excelente capacidade lógica.
            - **Claude (claude.ai):** Conhecido pelo refinamento visual e clareza de código.
            
            **A Estratégia Recomendada (O Melhor dos Dois Mundos):**
            1. **Início:** Gere a base completa do app no **Gemini** ou **ChatGPT** usando o *Gerador de Prompts* da Aba 2.
            2. **No VS Code:** Cole o código e rode `streamlit run app.py`.
            3. **Pequenos Ajustes:** Use o **GitHub Copilot Free** no VS Code (`Ctrl + I`) para ajustes pontuais.
            4. **Grandes Modificações ou Erros Complexos:** Se os créditos do Copilot acabarem ou quiser uma aba nova inteira, volte ao Gemini/ChatGPT!
            """
    )

  st.markdown("---")
  st.subheader(
      "🚨 Como Pedir Ajuda para a IA Quando Aparece um Erro (Prompt de Debug)"
  )
  st.write(
      "Quando algo der errado no terminal, não entre em pânico. Copie o modelo"
      " abaixo e envie para a IA:"
  )

  st.code(
      """Estou rodando meu aplicativo Streamlit e apareceu este erro no terminal:

[COLE A MENSAGEM VERMELHA DE ERRO DO TERMINAL AQUI]

Aqui está o meu código atual do app.py:

[COLE SEU CÓDIGO ATUAL AQUI]

Por favor:
1. Explique em português simples o que causou o erro.
2. Forneça o código corrigido completo para eu apenas substituir no meu arquivo.""",
      language="markdown",
  )

# ==============================================================================
# ABA 5: EXEMPLOS PRÁTICOS COMPLETOS (TEMPLATES VIVOS)
# ==============================================================================
with aba_exemplos:
  st.header("💻 Exemplos Práticos que Funcionam na Realidade")
  st.write(
      "Três exemplos reais de ferramentas de trabalho que seus alunos podem usar"
      " como base para criar as suas próprias:"
  )

  ex_aba1, ex_aba2, ex_aba3 = st.tabs([
      "💰 1. Simulador de Preço e Margem",
      "📋 2. Cadastro de Clientes com Pandas e Download CSV",
      "📈 3. Dashboard com Gráfico de Vendas",
  ])

  # --------------------------------------------------------------------------
  # EXEMPLO 1: SIMULADOR FINANCEIRO
  # --------------------------------------------------------------------------
  with ex_aba1:
    st.subheader("Calculadora de Precificação & Margem de Lucro")
    st.caption(
        "Exemplo de ferramenta comercial para calcular o preço de venda ideal."
    )

    c1, c2, c3 = st.columns(3)
    with c1:
      custo_produto = st.number_input(
          "Custo de Fabricação / Compra (R$)",
          min_value=0.0,
          value=150.0,
          step=10.0,
      )
    with c2:
      impostos_pct = st.number_input(
          "Impostos / Taxas (%)",
          min_value=0.0,
          max_value=100.0,
          value=12.0,
          step=1.0,
      )
    with c3:
      margem_desejada_pct = st.number_input(
          "Margem de Lucro Desejada (%)",
          min_value=0.0,
          max_value=100.0,
          value=25.0,
          step=1.0,
      )

    # Cálculo de Margem / Preço de Venda
    fator = 1 - ((impostos_pct + margem_desejada_pct) / 100.0)

    if fator <= 0:
      st.error(
          "⚠️ Atenção: A soma dos impostos e da margem não pode ser igual ou"
          " maior que 100%!"
      )
    else:
      preco_venda = custo_produto / fator
      valor_imposto = preco_venda * (impostos_pct / 100.0)
      lucro_liquido = preco_venda * (margem_desejada_pct / 100.0)

      st.markdown("#### 📊 Resultado da Simulação:")
      m1, m2, m3 = st.columns(3)
      m1.metric("Preço de Venda Sugerido", f"R$ {preco_venda:,.2f}")
      m2.metric("Impostos a Recolher", f"R$ {valor_imposto:,.2f}")
      m3.metric("Lucro Líquido Real", f"R$ {lucro_liquido:,.2f}")

  # --------------------------------------------------------------------------
  # EXEMPLO 2: CADASTRO COM PANDAS E DOWNLOAD
  # --------------------------------------------------------------------------
  with ex_aba2:
    st.subheader("Gerenciador de Oportunidades & Clientes")
    st.caption(
        "Demonstração prática de como usar Pandas e st.session_state para"
        " guardar dados vivos."
    )

    with st.form("form_novo_cliente", clear_on_submit=True):
      f_col1, f_col2 = st.columns(2)
      with f_col1:
        novo_nome = st.text_input("Nome do Cliente:")
        novo_email = st.text_input("E-mail:")
      with f_col2:
        novo_depto = st.selectbox(
            "Departamento:", ["Vendas", "RH", "TI", "Operações", "Financeiro"]
        )
        novo_valor = st.number_input(
            "Valor da Proposta (R$):", min_value=0.0, value=5000.0, step=500.0
        )

      btn_cadastrar = st.form_submit_button("➕ Adicionar à Tabela")

    if btn_cadastrar:
      if not novo_nome.strip() or not novo_email.strip():
        st.warning("Por favor, preencha pelo menos o Nome e o E-mail.")
      else:
        novo_registro = pd.DataFrame([{
            "Nome": novo_nome,
            "Email": novo_email,
            "Departamento": novo_depto,
            "Valor_Proposta": float(novo_valor),
        }])
        st.session_state.clientes_db = pd.concat(
            [st.session_state.clientes_db, novo_registro], ignore_index=True
        )
        st.success(f"Cliente {novo_nome} adicionado com sucesso!")

    st.markdown("#### 📋 Tabela de Clientes em Tempo Real (Pandas DataFrame)")
    st.dataframe(st.session_state.clientes_db, use_container_width=True)

    # Exportação para CSV usando Pandas
    csv_buffer = io.StringIO()
    st.session_state.clientes_db.to_csv(csv_buffer, index=False)
    csv_bytes = csv_buffer.getvalue().encode("utf-8")

    st.download_button(
        label="📥 Baixar Dados da Tabela em CSV (Abre no Excel)",
        data=csv_bytes,
        file_name="relatorio_clientes.csv",
        mime="text/csv",
    )

  # --------------------------------------------------------------------------
  # EXEMPLO 3: DASHBOARD COM PANDAS E GRÁFICO
  # --------------------------------------------------------------------------
  with ex_aba3:
    st.subheader("Dashboard Visual de Desempenho")
    st.caption(
        "Mostra como somar valores por categoria e desenhar gráficos com Pandas"
        " e Streamlit."
    )

    if not st.session_state.clientes_db.empty:
      resumo_depto = st.session_state.clientes_db.groupby("Departamento")[
          "Valor_Proposta"
      ].sum()

      col_metricas, col_grafico = st.columns([1, 2])

      with col_metricas:
        total_geral = st.session_state.clientes_db["Valor_Proposta"].sum()
        qtd_clientes = len(st.session_state.clientes_db)
        ticket_medio = total_geral / qtd_clientes if qtd_clientes > 0 else 0

        st.metric("Total em Negociação", f"R$ {total_geral:,.2f}")
        st.metric("Total de Clientes Ativos", f"{qtd_clientes}")
        st.metric("Ticket Médio por Proposta", f"R$ {ticket_medio:,.2f}")

      with col_grafico:
        st.markdown("**Valor Total por Departamento:**")
        st.bar_chart(resumo_depto)
    else:
      st.info(
          "Nenhum dado cadastrado para exibir no gráfico. Adicione clientes na"
          " aba anterior!"
      )