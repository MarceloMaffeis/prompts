# -*- coding: utf-8 -*-
"""
Hub de Criacao de Apps com IA - Aplicativo Educacional Streamlit
Projetado para ensinar alunos sem formacao em computacao a construirem
suas proprias ferramentas de trabalho com auxilio de IA.
"""

import streamlit as st
import pandas as pd
import io

# Importando os modulos locais organizados
from data_bibliotecas import BIBLIOTECAS
from labs import render_lab_machine_learning, render_lab_rag

# ==============================================================================
# CONFIGURACAO DA PAGINA
# ==============================================================================
st.set_page_config(
    page_title="Hub do Criador de Apps com IA",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializando historico de cadastros na memoria da sessao (Session State)
if "clientes_db" not in st.session_state:
    st.session_state.clientes_db = pd.DataFrame([
        {"Nome": "Ana Silva", "Email": "ana@empresa.com", "Departamento": "Vendas", "Valor_Proposta": 12500.0},
        {"Nome": "Carlos Souza", "Email": "carlos@gestao.com", "Departamento": "RH", "Valor_Proposta": 4300.0},
        {"Nome": "Beatriz Lima", "Email": "beatriz@tech.com", "Departamento": "TI", "Valor_Proposta": 28000.0},
        {"Nome": "Daniel Costa", "Email": "daniel@log.com", "Departamento": "Operacoes", "Valor_Proposta": 9800.0},
    ])

# ==============================================================================
# BARRA LATERAL (SIDEBAR)
# ==============================================================================
with st.sidebar:
    st.title("💡 Central do Aluno")
    st.caption("Do Zero ao seu Proprio Sistema com IA")

    st.markdown("---")
    st.markdown("### 🎯 O Novo Modo de Programar")
    st.info(
        "**Voce nao precisa decorar codigos!**\n\n"
        "O seu papel e ser o **Arquiteto da Solucao** (entender o problema de negocio). "
        "A IA e o seu **Programador Senior** gratuito."
    )

    st.markdown("### 💻 Comandos Essenciais do Terminal")
    with st.expander("Ver comandos do Terminal"):
        st.markdown("**1. Instalar as bibliotecas basicas:**")
        st.code("pip install streamlit pandas matplotlib", language="bash")
        st.markdown("**2. Rodar o seu aplicativo:**")
        st.code("streamlit run app.py", language="bash")
        st.markdown("**3. Parar o aplicativo:**")
        st.caption("Pressione Ctrl + C no terminal.")

    st.markdown("---")
    if st.button("🧹 Limpar Dados de Teste"):
        st.session_state.clientes_db = pd.DataFrame(columns=["Nome", "Email", "Departamento", "Valor_Proposta"])
        st.rerun()

# ==============================================================================
# CABECALHO PRINCIPAL
# ==============================================================================
st.title("🚀 Hub de Criacao: Construa seus Proprios Apps com IA")
st.markdown(
    """
    Seja bem-vindo ao **Portal do Criador de Sistemas com IA**! Aqui voce vai aprender a **pensar, pedir e construir** 
    ferramentas e automacoes reais para sua carreira, unindo **Python**, **Streamlit**, **Machine Learning**, **RAG/GPTs**, 
    **Automacoes Web/Desktop** e **Inteligencia Artificial**.
    """
)

# ==============================================================================
# ESTRUTURA DE ABAS DIDATICAS
# ==============================================================================
aba_metodo, aba_gerador, aba_bibliotecas, aba_ias_copilot, aba_exemplos = st.tabs([
    "🗺️ O Metodo (Como Criar)",
    "🪄 Gerador de Super Prompts",
    "📚 Arsenal de Bibliotecas Python",
    "🤖 Guia IAs & GitHub Copilot",
    "💻 Laboratorio Pratico (Exemplos Vivos)"
])

# ==============================================================================
# ABA 1: O METODO (DO ZERO AO APP)
# ==============================================================================
with aba_metodo:
    st.header("🗺️ O Metodo dos 4 Passos para Criar Qualquer Sistema com IA")
    st.write("Em vez de ficar meses decorando sintaxe que muda todo ano, domine esta esteira de construcao ágil:")

    col_p1, col_p2, col_p3, col_p4 = st.columns(4)

    with col_p1:
        st.markdown("#### 1️⃣ Definir a Dor")
        st.markdown(
            """
            Antes de abrir qualquer IA, responda:
            - Que tarefa chata ou repetitiva isso resolve?
            - O que entra no sistema (arquivos, textos, numeros)?
            - O que a tela deve calcular, prever ou exibir?
            """
        )
        st.caption("Exemplo: 'Preciso consultar 50 PDFs de normas internas e receber respostas instantaneas'.")

    with col_p2:
        st.markdown("#### 2️⃣ O Super Prompt")
        st.markdown(
            """
            Peca para a IA com estrutura profissional:
            - **Papel:** 'Aja como especialista Python e Streamlit'.
            - **Objetivo:** O que o app resolve.
            - **Bibliotecas:** Cite as ferramentas certas (ex: LangChain, Pandas).
            - **Entrega:** 'Codigo completo em arquivo unico app.py'.
            """
        )
        st.caption("Dica: Use a aba 'Gerador de Prompts' deste app!")

    with col_p3:
        st.markdown("#### 3️⃣ Colar e Rodar")
        st.markdown(
            """
            - Crie um arquivo no VS Code (ex: `app.py`).
            - Cole o codigo gerado pela IA.
            - Abra o Terminal (`Ctrl + '`).
            - Digite: `streamlit run app.py`.
            - O navegador abrira automaticamente!
            """
        )
        st.caption("Se aparecer alguma linha vermelha, veja o passo 4.")

    with col_p4:
        st.markdown("#### 4️⃣ Iterar e Atualizar")
        st.markdown(
            """
            O segredo do desenvolvimento com IA e a conversa continua:
            - **Deu erro?** Copie o erro do terminal e envie a IA: *'Deu esse erro, conserte mantendo o resto'*.
            - **Quer novos recursos?** *'Agora adicione um botao para exportar em Excel'*.
            """
        )
        st.caption("Voce vai evoluindo seu aplicativo como um Lego.")

    st.markdown("---")
    st.subheader("💡 A Nova Mentalidade: Programador-Arquiteto (Vibe Coding)")
    st.success(
        "**Mensagem Importante:** Voce nao precisa ser um genio dos algoritmos matematicos. "
        "No mercado de trabalho atual, o profissional mais valorizado e aquele que **identifica problemas reais da empresa** "
        "e usa as IAs gratuitas para construir a solucao em horas em vez de semanas!"
    )

# ==============================================================================
# ABA 2: GERADOR DE SUPER PROMPTS (INTERATIVO & EXPANDIDO)
# ==============================================================================
with aba_gerador:
    st.header("🪄 Gerador Interativo de Prompts para IA")
    st.write("Selecione o tipo de projeto e os recursos que voce deseja. O app vai montar a instrucao perfeita pronta para colar na sua IA:")

    col_g1, col_g2 = st.columns([1, 1])

    with col_g1:
        tipo_app = st.selectbox(
            "1. Qual o tipo de projeto que voce quer construir?",
            [
                "Calculadora ou Simulador de Negocios (Custos, Margem, Financiamentos)",
                "Sistema de Cadastro com Tabela e Exportacao para Excel/CSV (Pandas)",
                "Dashboard de Analise com Graficos e Indicadores (KPIs e Plotly)",
                "Chatbot Inteligente ou Sistema RAG (Consulta a Documentos e PDFs com IA)",
                "Modelo Preditivo de Machine Learning (Previsao de Vendas, Churn ou Fraude)",
                "Robo de Automacao Web (Preenchimento automatico ou Raspagem de dados)",
                "Robo de Automacao Desktop (Manipulacao de Excel, PDFs ou Cliques no Mouse)",
                "Mini Game 2D (Pygame) ou Visao Computacional (OpenCV / Webcam)",
                "Outro Sistema Personalizado"
            ]
        )

        nome_ferramenta = st.text_input(
            "2. De um nome criativo para a sua ferramenta:",
            value="Assistente Inteligente de Produtividade"
        )

        st.markdown("**3. Quais tecnologias e recursos quer incluir no projeto?**")
        c_pandas = st.checkbox("Tabela de dados e operacoes com Pandas", value=True)
        c_graficos = st.checkbox("Graficos visuais interativos (Plotly ou Matplotlib)", value=True)
        c_ia = st.checkbox("Conexao com IA Generativa (Google Gemini ou OpenAI)", value=("RAG" in tipo_app or "Chatbot" in tipo_app))
        c_ml = st.checkbox("Algoritmo de Machine Learning (Scikit-Learn ou XGBoost)", value=("Machine Learning" in tipo_app))
        c_auto = st.checkbox("Recursos de Automacao (Playwright, PyAutoGUI ou PyPDF)", value=("Automacao" in tipo_app))
        c_download = st.checkbox("Botao para baixar relatorios ou arquivos finais", value=True)

    with col_g2:
        campos_regras = st.text_area(
            "4. Descreva em linguagem simples o que a sua ferramenta deve fazer:",
            value="O sistema deve permitir que o usuario insira informacoes basicas e receba uma analise detalhada com calculos precisos, tabela de historico e um grafico visual explicativo.",
            height=180
        )

        # Montando o Super Prompt dinamicamente
        recursos_texto = []
        if c_pandas: recursos_texto.append("- Utilize a biblioteca 'pandas' para gerenciar tabelas e tratar os dados de forma limpa.")
        if c_graficos: recursos_texto.append("- Inclua graficos visuais elegantes e interativos (usando plotly ou componentes nativos do streamlit).")
        if c_ia: recursos_texto.append("- Conecte-se com a API de IA (Google Gemini ou OpenAI) para gerar analises textuais inteligentes e contextuais.")
        if c_ml: recursos_texto.append("- Aplique a biblioteca 'scikit-learn' para treinar um modelo de Machine Learning e realizar previsoes baseadas nos dados fornecidos.")
        if c_auto: recursos_texto.append("- Incorpore funcoes de automacao para agilizar tarefas repetitivas (como geracao de arquivos ou processamento de documentos).")
        if c_download: recursos_texto.append("- Adicione um botao de download para exportar os resultados em formato CSV, Excel ou PDF.")

        prompt_final = f"""Aja como um Engenheiro de Software Python e Especialista em Streamlit e IA.
Crie um aplicativo completo, profissional e pronto para execucao para mim.
Eu sou iniciante na programacao, entao o codigo deve ser super organizado, comentado em portugues e pronto para rodar em um unico arquivo (app.py).

### OBJETIVO DO APLICATIVO:
Criar um(a): {nome_ferramenta} ({tipo_app}).

### FUNCIONAMENTO E REGRAS DE NEGOCIO:
{campos_regras}

### TECNOLOGIAS E REQUISITOS OBRIGATORIOS:
- Interface web construida integralmente em 'streamlit'.
{chr(10).join(recursos_texto)}
- Utilize componentes visuais modernos como st.metric, st.columns, st.tabs, st.info, st.success.
- Mantenha o estado dos dados salvo durante o uso usando st.session_state (se houver listas ou tabelas).
- Forneca o codigo 100% completo, sem partes ocultas ou 'adicione seu codigo aqui'.
- No final da resposta, inclua uma instrucao clara com o comando pip install necessario e como executar com streamlit run.
"""

    st.markdown("---")
    st.subheader("📋 Seu Super Prompt Pronto para Copiar:")
    st.write("Copie o bloco abaixo e envie para o Google Gemini, ChatGPT ou cole no painel do Copilot:")
    st.code(prompt_final, language="markdown")

# ==============================================================================
# ABA 3: ARSENAL DE BIBLIOTECAS PYTHON (FILTRÁVEL)
# ==============================================================================
with aba_bibliotecas:
    st.header("📚 Arsenal de Bibliotecas Python (O Guia de Referencia)")
    st.write("Conheca as principais ferramentas do ecossistema Python. A IA escreve o codigo, mas voce precisa saber qual ferramenta escolher para cada missao:")

    categorias_disponiveis = ["Todas as Categorias"] + sorted(list(set(b["categoria"] for b in BIBLIOTECAS)))
    cat_escolhida = st.selectbox("🔍 Filtrar por Area de Atuacao:", categorias_disponiveis)

    bibliotecas_filtradas = BIBLIOTECAS if cat_escolhida == "Todas as Categorias" else [b for b in BIBLIOTECAS if b["categoria"] == cat_escolhida]

    for item in bibliotecas_filtradas:
        with st.expander(f"📦 {item['nome']}  •  [{item['categoria']}]", expanded=False):
            c_desc, c_code = st.columns([1, 1])

            with c_desc:
                st.markdown(f"**O que e:** {item['descricao']}")
                st.markdown(f"**Quando usar no trabalho:** {item['quando_usar']}")
                st.markdown("**Comando de Instalacao:**")
                st.code(item["instalacao"], language="bash")
                st.markdown("**Prompt Exemplo para pedir a IA:**")
                st.info(f"🗣️ *'{item['prompt_ia']}'*")

            with c_code:
                st.markdown("**Exemplo de Codigo Minimo:**")
                st.code(item["exemplo_codigo"], language="python")

# ==============================================================================
# ABA 4: GUIA DE IAS GRATUITAS & GITHUB COPILOT
# ==============================================================================
with aba_ias_copilot:
    st.header("🤖 Como Usar as IAs Gratuitas & GitHub Copilot")
    st.write("Entenda como tirar o maximo proveito das melhores ferramentas de IA do mercado sem gastar um centavo:")

    col_ia1, col_ia2 = st.columns(2)

    with col_ia1:
        st.subheader("🐙 1. GitHub Copilot Free (Gratuito no VS Code)")
        st.markdown(
            """
            **A grande novidade:** O GitHub liberou o plano **Copilot Free** gratuito oficial para qualquer conta do GitHub!
            
            **Como ativar em 3 minutos:**
            1. Abra o **VS Code**.
            2. Va no menu lateral de Extensoes (`Ctrl + Shift + X`).
            3. Digite **'GitHub Copilot'** e clique em Instalar.
            4. Faca login com sua conta gratuita do GitHub.
            
            **O que a versao gratuita inclui:**
            - **2.000 sugestoes de autocompletar** de codigo por mes (basta apertar `Tab` para aceitar).
            - **50 conversas de Chat** no painel lateral do VS Code todo mes.
            
            **Como usar como Low-Code:**
            - Selecione o trecho do arquivo e aperte **`Ctrl + I`**.
            - Digite: *'Adicione uma coluna calculando o imposto de 15%'*.
            - Ele mostra as alteracoes direto no arquivo e voce so clica em **Accept**!
            """
        )

    with col_ia2:
        st.subheader("🌐 2. IAs Externas Gratuitas (Gemini & ChatGPT)")
        st.markdown(
            """
            As IAs de navegador sao suas melhores parceiras para **gerar o projeto inteiro do zero** sem limites de cota:
            
            **Principais opcoes gratuitas:**
            - **Google Gemini (gemini.google.com):** Janela de contexto gigantesca, excelente para codigos Python e muito rapido.
            - **ChatGPT Free (chatgpt.com):** Ótimo raciocinio logico com o modelo GPT-4o mini.
            - **Claude (claude.ai):** Conhecido pelo capricho no design visual de telas.
            
            **A Estrategia Hibrida dos Campeoes:**
            1. **Do Zero:** Use o **Gemini / ChatGPT** para gerar o primeiro `app.py` completo com o Super Prompt.
            2. **No VS Code:** Cole e rode com `streamlit run app.py`.
            3. **Ajustes Rapidos:** Use o **GitHub Copilot Free** no proprio VS Code (`Ctrl + I`) para pequenas alteracoes.
            4. **Se o Copilot atingir a cota:** Volte ao Gemini/ChatGPT colando o codigo e pedindo as mudancas maiores!
            """
        )

    st.markdown("---")
    st.subheader("🚨 O Prompt de Socorro: O que fazer quando der erro no terminal?")
    st.write("Erros fazem parte do dia a dia de qualquer desenvolvedor. Nao entre em panico! Copie o modelo abaixo e envie para a IA:")

    st.code(
        """Estou rodando meu aplicativo Streamlit e apareceu este erro no terminal:

[COLE AQUI A MENSAGEM VERMELHA DE ERRO DO TERMINAL]

Aqui esta o meu codigo atual do app.py:

[COLE AQUI O SEU CODIGO ATUAL]

Por favor:
1. Explique em linguagem simples e didatica qual foi o motivo do erro.
2. Forneca o codigo corrigido completo para eu apenas substituir no meu arquivo app.py.""",
        language="markdown"
    )

# ==============================================================================
# ABA 5: LABORATÓRIO PRÁTICO (EXEMPLOS VIVOS)
# ==============================================================================
with aba_exemplos:
    st.header("💻 Laboratorio Pratico: Exemplos Reais para a Turma")
    st.write("Veja abaixo 5 ferramentas funcionais que mostram o poder dessas tecnologias na pratica:")

    ex1, ex2, ex3, ex4, ex5 = st.tabs([
        "💰 1. Simulador Financeiro",
        "📋 2. Cadastro & Pandas (Download CSV)",
        "📈 3. Dashboard com Graficos",
        "🧠 4. Machine Learning Interativo",
        "🔍 5. Simulador de RAG & Busca Inteligente"
    ])

    # --------------------------------------------------------------------------
    # EXEMPLO 1: SIMULADOR FINANCEIRO
    # --------------------------------------------------------------------------
    with ex1:
        st.subheader("Calculadora de Precificacao & Margem de Lucro")
        st.caption("Demonstra operacoes matematicas com Streamlit e cards de resultado (st.metric).")

        c1, c2, c3 = st.columns(3)
        with c1:
            custo_produto = st.number_input("Custo de Compra / Producao (R$)", min_value=0.0, value=150.0, step=10.0)
        with c2:
            impostos_pct = st.number_input("Impostos e Taxas (%)", min_value=0.0, max_value=100.0, value=12.0, step=1.0)
        with c3:
            margem_desejada_pct = st.number_input("Margem de Lucro Desejada (%)", min_value=0.0, max_value=100.0, value=25.0, step=1.0)

        fator = 1 - ((impostos_pct + margem_desejada_pct) / 100.0)
        
        if fator <= 0:
            st.error("⚠️ Atencao: A soma de impostos e margem nao pode atingir 100%!")
        else:
            preco_venda = custo_produto / fator
            valor_imposto = preco_venda * (impostos_pct / 100.0)
            lucro_liquido = preco_venda * (margem_desejada_pct / 100.0)

            st.markdown("#### 📊 Resultados Comerciais:")
            m1, m2, m3 = st.columns(3)
            m1.metric("Preco de Venda Sugerido", f"R$ {preco_venda:,.2f}")
            m2.metric("Impostos a Pagar", f"R$ {valor_imposto:,.2f}")
            m3.metric("Lucro Liquido no Bolso", f"R$ {lucro_liquido:,.2f}")

    # --------------------------------------------------------------------------
    # EXEMPLO 2: CADASTRO COM PANDAS E DOWNLOAD
    # --------------------------------------------------------------------------
    with ex2:
        st.subheader("Gerenciador de Oportunidades & Clientes (Pandas)")
        st.caption("Demonstra manipulacao de DataFrames com Pandas e exportacao direta para o Excel.")

        with st.form("form_novo_cliente", clear_on_submit=True):
            f_col1, f_col2 = st.columns(2)
            with f_col1:
                novo_nome = st.text_input("Nome do Cliente / Empresa:")
                novo_email = st.text_input("E-mail de Contato:")
            with f_col2:
                novo_depto = st.selectbox("Departamento:", ["Vendas", "RH", "TI", "Operacoes", "Financeiro"])
                novo_valor = st.number_input("Valor da Oportunidade (R$):", min_value=0.0, value=8500.0, step=500.0)
            
            btn_cadastrar = st.form_submit_button("➕ Inserir na Tabela")

        if btn_cadastrar:
            if not novo_nome.strip() or not novo_email.strip():
                st.warning("Preencha o Nome e o E-mail para continuar.")
            else:
                novo_registro = pd.DataFrame([{
                    "Nome": novo_nome,
                    "Email": novo_email,
                    "Departamento": novo_depto,
                    "Valor_Proposta": float(novo_valor)
                }])
                st.session_state.clientes_db = pd.concat([st.session_state.clientes_db, novo_registro], ignore_index=True)
                st.success(f"Registro de {novo_nome} adicionado com sucesso!")

        st.markdown("#### 📋 Tabela Dinamica com Pandas:")
        st.dataframe(st.session_state.clientes_db, use_container_width=True)

        csv_buffer = io.StringIO()
        st.session_state.clientes_db.to_csv(csv_buffer, index=False)
        csv_bytes = csv_buffer.getvalue().encode('utf-8')

        st.download_button(
            label="📥 Baixar Dados da Tabela em CSV (Abre no Excel)",
            data=csv_bytes,
            file_name="relatorio_clientes.csv",
            mime="text/csv"
        )

    # --------------------------------------------------------------------------
    # EXEMPLO 3: DASHBOARD COM GRAFICO
    # --------------------------------------------------------------------------
    with ex3:
        st.subheader("Dashboard Visual com Agrupamento de Dados")
        st.caption("Usa operacoes do Pandas (.groupby) e renderiza graficos de barra instantaneos.")

        if not st.session_state.clientes_db.empty:
            resumo_depto = st.session_state.clientes_db.groupby("Departamento")["Valor_Proposta"].sum()

            col_met, col_chart = st.columns([1, 2])
            with col_met:
                total_geral = st.session_state.clientes_db["Valor_Proposta"].sum()
                qtd = len(st.session_state.clientes_db)
                ticket = total_geral / qtd if qtd > 0 else 0
                st.metric("Volume Total Negociado", f"R$ {total_geral:,.2f}")
                st.metric("Clientes Cadastrados", f"{qtd}")
                st.metric("Ticket Medio por Proposta", f"R$ {ticket:,.2f}")

            with col_chart:
                st.markdown("**Valores Negociados por Departamento:**")
                st.bar_chart(resumo_depto)
        else:
            st.info("Nenhum cliente cadastrado no momento.")

    # --------------------------------------------------------------------------
    # EXEMPLO 4: SIMULADOR DIDÁTICO DE MACHINE LEARNING (LABS.PY)
    # --------------------------------------------------------------------------
    with ex4:
        render_lab_machine_learning()

    # --------------------------------------------------------------------------
    # EXEMPLO 5: SIMULADOR DIDÁTICO DE RAG & BUSCA SEMÂNTICA (LABS.PY)
    # --------------------------------------------------------------------------
    with ex5:
        render_lab_rag()
