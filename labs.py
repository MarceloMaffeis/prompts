# -*- coding: utf-8 -*-
"""
Modulos de Laboratorio Interativo:
1. Simulador de Machine Learning (Regressao Linear e Previsao) usando Altair interativo
2. Simulador de RAG (Busca Semantica em Base de Documentos)
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def render_lab_machine_learning():
    st.subheader("🧠 Como Funciona o Machine Learning na Pratica?")
    st.caption("Simulador interativo de Regressao Linear (previsao continua baseada em historico real).")

    st.markdown(
        """
        No **Machine Learning classico (usando Scikit-Learn ou XGBoost)**, em vez de criarmos regras 'se isso entao aquilo' na mao,
        nos entregamos os **dados do passado** para o algoritmo. Ele calcula a melhor linha matematica e **aprende a prever o futuro**!
        """
    )

    col_cfg, col_view = st.columns([1, 1.3])

    with col_cfg:
        st.markdown("##### 1. Ajustar o Historico da Empresa:")
        qtd_meses = st.slider("Meses de historico de vendas:", min_value=6, max_value=36, value=14)
        retorno_mkt = st.slider("Eficiencia do Marketing (Retorno por R$ investido):", min_value=1.5, max_value=6.0, value=3.4, step=0.1)

        np.random.seed(42)
        investimento = np.linspace(1000, 15000, qtd_meses)
        ruido = np.random.normal(0, 2000, qtd_meses)
        faturamento_historico = (investimento * retorno_mkt) + 8000 + ruido

        df_treino = pd.DataFrame({
            "Investimento_Marketing": investimento,
            "Faturamento_Real": faturamento_historico
        })

        st.markdown("##### 2. Fazer uma Nova Previsao:")
        investimento_futuro = st.number_input(
            "Se investirmos este valor no proximo mes (R$):",
            min_value=500.0,
            max_value=50000.0,
            value=12000.0,
            step=1000.0
        )

        # Calculo de regressao linear (equivalente a LinearRegression().fit do Scikit-Learn)
        coefs = np.polyfit(df_treino["Investimento_Marketing"], df_treino["Faturamento_Real"], 1)
        faturamento_estimado = np.polyval(coefs, investimento_futuro)

        st.success(f"📈 **Faturamento Previsto pela IA:** R$ {faturamento_estimado:,.2f}")
        st.caption(f"Formula aprendida: Faturamento = ({coefs[0]:.2f} x Investimento) + {coefs[1]:,.2f}")

    with col_view:
        st.markdown("##### 📊 Grafico Interativo: A IA Encontrando o Padrao nos Dados")
        
        # 1. Pontos do Historico Real (Scatter)
        scatter = alt.Chart(df_treino).mark_circle(size=90, color="#1f77b4").encode(
            x=alt.X("Investimento_Marketing:Q", title="Investimento em Marketing (R$)", axis=alt.Axis(format="$,.0f")),
            y=alt.Y("Faturamento_Real:Q", title="Faturamento Real (R$)", axis=alt.Axis(format="$,.0f")),
            tooltip=[
                alt.Tooltip("Investimento_Marketing:Q", format="$,.2f", title="Investimento"),
                alt.Tooltip("Faturamento_Real:Q", format="$,.2f", title="Faturamento Real")
            ]
        )

        # 2. Linha de Tendencia Aprendida pela IA (Line)
        x_vals = np.linspace(500, 18000, 80)
        y_vals = np.polyval(coefs, x_vals)
        df_linha = pd.DataFrame({"x": x_vals, "y": y_vals})
        line = alt.Chart(df_linha).mark_line(color="#ff7f0e", strokeDash=[6, 4], strokeWidth=3).encode(
            x="x:Q",
            y="y:Q"
        )

        # 3. Ponto Previsto pelo Usuario (Destaque em Vermelho)
        df_ponto = pd.DataFrame({
            "x": [investimento_futuro],
            "y": [faturamento_estimado]
        })
        ponto = alt.Chart(df_ponto).mark_circle(size=220, color="red").encode(
            x="x:Q",
            y="y:Q",
            tooltip=[
                alt.Tooltip("x:Q", format="$,.2f", title="Investimento Planejado"),
                alt.Tooltip("y:Q", format="$,.2f", title="Faturamento Previsto pela IA")
            ]
        )

        grafico_final = (scatter + line + ponto).properties(
            height=380
        ).interactive()

        st.altair_chart(grafico_final, use_container_width=True)
        st.caption("💡 **Dica Interativa:** Passe o mouse sobre os pontos para ver os valores exatos e use a roda do mouse para dar zoom!")


def render_lab_rag():
    st.subheader("🔍 O que e RAG (Retrieval-Augmented Generation)?")
    st.caption("Simulador visual de como o ChatGPT ou Gemini consultam arquivos e politicas da empresa sem inventar dados.")

    st.markdown(
        """
        **RAG** e a tecnologia mais requisitada do mercado corporativo atualmente. 
        Ela funciona em 2 etapas:
        1. **Retrieval (Recuperacao):** O sistema busca em um banco de vetores (ChromaDB) o paragrafo exato do manual interno.
        2. **Generation (Geracao):** O modelo de linguagem (GPT/Gemini) le aquele paragrafo e formula uma resposta clara e educada.
        """
    )

    base_rh = [
        {
            "titulo": "Politica de Ferias e Recessos",
            "conteudo": "As solicitacoes de ferias devem ser submetidas com no minimo 30 dias de antecedencia. Podem ser fracionadas em ate 3 periodos, sendo que um nao pode ter menos de 14 dias corridos.",
            "palavras": ["ferias", "folga", "recesso", "descanso", "antecedencia", "dias", "periodo", "rh"]
        },
        {
            "titulo": "Reembolso de Viagens e Combustivel",
            "conteudo": "Despesas com deslocamento, quilometragem e hospedagem corporativa exigem comprovante fiscal emitido em nome da empresa. O deposito do reembolso ocorre na folha do dia 15.",
            "palavras": ["reembolso", "viagem", "combustivel", "gasolina", "km", "nota", "fiscal", "despesa", "hotel"]
        },
        {
            "titulo": "Regime de Home Office e Escala Hibrida",
            "conteudo": "Colaboradores com contratos hibridos tem direito a 2 dias de home office semanais (padrao: tercas e quintas). O horario de trabalho oficial e das 09h as 18h.",
            "palavras": ["home", "office", "remoto", "casa", "hibrido", "terca", "quinta", "horario", "expediente", "escala"]
        },
        {
            "titulo": "Suporte de TI e Troca de Maquinas",
            "conteudo": "Problemas de hardware ou pedidos de troca de notebook devem ser registrados via chamado interno (ti@empresa.com). O SLA padrao de atendimento e de ate 48h uteis.",
            "palavras": ["computador", "notebook", "ti", "suporte", "defeito", "teclado", "mouse", "chamado", "tela"]
        }
    ]

    pergunta = st.text_input(
        "Faca uma pergunta simulada para testar a busca interna da IA:",
        value="Como recebo de volta o valor que gastei com combustivel na viagem a trabalho?"
    )

    if pergunta:
        termos = pergunta.lower().split()
        melhor_doc = None
        maior_match = -1

        for doc in base_rh:
            match_score = sum(1 for t in termos if any(t in p for p in doc["palavras"]))
            if match_score > maior_match:
                maior_match = match_score
                melhor_doc = doc

        col_busca, col_resp = st.columns(2)

        with col_busca:
            st.markdown("##### 1. Trecho Recuperado no Banco Interno (Retrieval):")
            if melhor_doc and maior_match > 0:
                st.info(f"📄 **Documento Localizado:** {melhor_doc['titulo']}\n\n*\"{melhor_doc['conteudo']}\"*")
            else:
                st.warning("Nenhum trecho correspondente encontrado na base de dados.")

        with col_resp:
            st.markdown("##### 2. Resposta Sintetizada pela IA (Generation):")
            if melhor_doc and maior_match > 0:
                st.success(
                    f"🤖 **Resposta do Assistente Corporativo:**\n\n"
                    f"De acordo com a nossa **{melhor_doc['titulo']}**, para receber o reembolso de combustivel voce deve "
                    f"apresentar o comprovante fiscal com o CNPJ da empresa. O valor correspondente sera creditado na folha do **dia 15**!"
                )
            else:
                st.write("A IA respondeu: *'Desculpe, nao encontrei essa informacao nos documentos oficiais da empresa.'*")
