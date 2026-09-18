# -*- coding: utf-8 -*-
"""
Dicionario de Referencia de Bibliotecas Python
Organizado por areas de atuacao no mercado de tecnologia e IA
"""

BIBLIOTECAS = [
    {
        "nome": "Google GenAI & OpenAI",
        "categoria": "🤖 IAs Generativas, GPTs & RAG",
        "descricao": "Conectam seu codigo diretamente aos cerebros de IA mais inteligentes do planeta (Gemini 2.5 e ChatGPT GPT-4o).",
        "instalacao": "pip install google-genai openai",
        "quando_usar": "Para criar chatbots, assistentes que respondem duvidas sobre sua empresa, resumir documentos, traduzir textos e gerar respostas inteligentes.",
        "exemplo_codigo": '''from google import genai

client = genai.Client() # Le a chave GEMINI_API_KEY do ambiente
resposta = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explique o que e RAG em duas frases simples e didaticas."
)
print(resposta.text)''',
        "prompt_ia": "Crie um aplicativo Streamlit que conecte na API do Google Gemini (usando google-genai) para funcionar como um consultor de negocios que analisa duvidas dos usuarios."
    },
    {
        "nome": "LangChain & LlamaIndex",
        "categoria": "🤖 IAs Generativas, GPTs & RAG",
        "descricao": "Os 'mestres de obras' das aplicacoes com IA. Criam fluxos de RAG (conversar com seus proprios PDFs e planilhas) e orquestram agentes autonomos.",
        "instalacao": "pip install langchain langchain-community llama-index",
        "quando_usar": "Quando voce quer que o ChatGPT ou Gemini responda perguntas consultando a base interna de politicas ou manuais da sua propria empresa sem alucinar.",
        "exemplo_codigo": '''# Fluxo conceitual de RAG:
# 1. Le o PDF da sua empresa (ex: manual_rh.pdf)
# 2. Divide em pedacos menores (chunks)
# 3. Salva os vetores no banco ChromaDB
# 4. Quando o usuario pergunta, a IA busca o trecho exato e responde!''',
        "prompt_ia": "Crie um app no Streamlit usando LangChain ou LlamaIndex onde eu possa fazer upload de um arquivo PDF e conversar com esse documento tirando duvidas com IA."
    },
    {
        "nome": "ChromaDB & FAISS",
        "categoria": "🤖 IAs Generativas, GPTs & RAG",
        "descricao": "Bancos de dados vetoriais de altissima velocidade. Em vez de buscar palavras exatas, buscam pelo contexto e sentido das frases (Embeddings).",
        "instalacao": "pip install chromadb faiss-cpu",
        "quando_usar": "O motor que fica por tras do RAG. Guarda milhares de paginas de manuais e encontra em milissegundos o paragrafo que responde a pergunta do usuario.",
        "exemplo_codigo": '''import chromadb

client = chromadb.Client()
colecao = client.create_collection("base_rh")
colecao.add(
    documents=["O reembolso de viagens e feito ate sexta-feira", "O expediente encerra as 18h"],
    ids=["doc1", "doc2"]
)
# Busca semantica (acha por contexto mesmo sem usar as mesmas palavras!):
resposta = colecao.query(query_texts=["Como recebo o dinheiro que gastei na viagem?"], n_results=1)''',
        "prompt_ia": "Crie um script didatico em Python usando ChromaDB para indexar 4 regras internas de uma empresa e fazer consultas semanticas com base no significado."
    },
    {
        "nome": "Scikit-Learn",
        "categoria": "🧠 Machine Learning & Redes Neurais",
        "descricao": "A biblioteca mais popular e didatica para Machine Learning do mundo. Traz modelos prontos para previsao de numeros, agrupamento e classificacao.",
        "instalacao": "pip install scikit-learn",
        "quando_usar": "Prever faturamento com base em historico, prever se um cliente vai cancelar o contrato (Churn), agrupar clientes por habito de compra ou detectar fraudes.",
        "exemplo_codigo": '''from sklearn.linear_model import LinearRegression
import numpy as np

# Dados: [Horas de estudo] -> Nota na prova
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([25, 45, 65, 80, 98])

modelo = LinearRegression()
modelo.fit(X, y) # A IA aprende o padrao
nota_prevista = modelo.predict([[6]]) # Preve a nota de quem estudar 6h!''',
        "prompt_ia": "Crie um app Streamlit com Scikit-Learn onde o usuario insere dados de historico de vendas e treina um modelo de Machine Learning para prever o proximo mes."
    },
    {
        "nome": "XGBoost & LightGBM",
        "categoria": "🧠 Machine Learning & Redes Neurais",
        "descricao": "Os modelos campeoes mundiais de ciencia de dados para planilhas. Usam arvores de decisao ultra otimizadas (Gradient Boosting).",
        "instalacao": "pip install xgboost lightgbm",
        "quando_usar": "Quando voce precisa da mais alta precisao preditiva do mercado em bancos de dados ou planilhas do Excel com dezenas de colunas.",
        "exemplo_codigo": '''import xgboost as xgb
# Modelo campeao de competicoes de dados corporativos
modelo = xgb.XGBClassifier()
# modelo.fit(X_treino, y_treino)''',
        "prompt_ia": "Crie um script em Python com XGBoost mostrando como prever aprovacao de emprestimo com base em renda, idade e historico de credito."
    },
    {
        "nome": "PyTorch & TensorFlow / Keras",
        "categoria": "🧠 Machine Learning & Redes Neurais",
        "descricao": "Os motores das Redes Neurais Profundas (Deep Learning). Criam modelos que reconhecem imagens, processam voz e aprendem padroes muito complexos.",
        "instalacao": "pip install torch torchvision   # ou: pip install tensorflow",
        "quando_usar": "Para criar ou personalizar modelos de visao computacional, reconhecimento de voz, series temporais complexas ou arquiteturas neurais multicamadas.",
        "exemplo_codigo": '''import torch
import torch.nn as nn

# Mini Rede Neural basica com 1 camada oculta
class MiniRedeNeural(nn.Module):
    def __init__(self):
        super().__init__()
        self.entrada = nn.Linear(3, 10)  # 3 caracteristicas de entrada
        self.ativacao = nn.ReLU()
        self.saida = nn.Linear(10, 1)    # 1 previsao final''',
        "prompt_ia": "Crie uma explicacao para iniciantes em Python mostrando como funciona uma Rede Neural simples usando PyTorch para prever o consumo de energia."
    },
    {
        "nome": "Playwright & Selenium",
        "categoria": "🌐 Automacao Web & Robos (Scraping)",
        "descricao": "Robos inteligentes que abrem o navegador sozinhos, preenchem logins, clicam em botoes, extraem dados e baixam relatorios de portais da internet.",
        "instalacao": "pip install playwright && playwright install   # ou: pip install selenium",
        "quando_usar": "Para eliminar o trabalho chato de entrar todo dia no mesmo site para baixar planilhas, consultar processos, emitir notas fiscais ou preencher formularios.",
        "exemplo_codigo": '''from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False) # Abre a janela visivel
    pagina = navegador.new_page()
    pagina.goto("https://exemplo.com/login")
    pagina.fill("#usuario", "meu_email@empresa.com")
    pagina.fill("#senha", "123456")
    pagina.click("#botao_entrar")
    pagina.screenshot(path="painel.png")
    navegador.close()''',
        "prompt_ia": "Crie um script em Python com Playwright que acesse um site institucional, faca login com seguranca e clique no botao para baixar o relatorio diario em PDF."
    },
    {
        "nome": "Requests & BeautifulSoup4",
        "categoria": "🌐 Automacao Web & Robos (Scraping)",
        "descricao": "A dupla favorita para coletar dados (Web Scraping) de sites na velocidade da luz, sem precisar abrir navegador visual na tela.",
        "instalacao": "pip install requests beautifulsoup4",
        "quando_usar": "Monitorar precos de concorrentes, capturar noticias do seu segmento em portais publicos, raspar tabelas de cotacoes e indicadores economicos.",
        "exemplo_codigo": '''import requests
from bs4 import BeautifulSoup

url = "https://exemplo.com"
resposta = requests.get(url)
sopa = BeautifulSoup(resposta.text, "html.parser")
titulo = sopa.find("h1").text
print("Titulo da pagina:", titulo)''',
        "prompt_ia": "Crie um script em Python com requests e BeautifulSoup que colete as principais manchetes de um portal de noticias e salve em uma tabela do Pandas."
    },
    {
        "nome": "PyAutoGUI",
        "categoria": "🖥️ Automacao de Desktop & Arquivos",
        "descricao": "Assume o controle do mouse e do teclado do seu computador. Clica em botoes, digita textos e automatiza softwares antigos (como SAP, ERPs legados).",
        "instalacao": "pip install pyautogui",
        "quando_usar": "Para automatizar aquele sistema velho da empresa que nao tem API e obriga um ser humano a clicar no mesmo botao 100 vezes por dia.",
        "exemplo_codigo": '''import pyautogui
import time

time.sleep(3) # Tempo para voce mudar para a janela certa
pyautogui.click(x=600, y=400) # Clica no botao da tela
pyautogui.write("Processo automatizado com sucesso!", interval=0.05)
pyautogui.press("enter")''',
        "prompt_ia": "Crie um script em Python com PyAutoGUI que tire print da tela, localize um icone e clique nele automaticamente com trava de seguranca."
    },
    {
        "nome": "OpenPyXL & PyPDF / Python-Docx",
        "categoria": "🖥️ Automacao de Desktop & Arquivos",
        "descricao": "Robos de escritorio para documentos: geram e formatam planilhas Excel (.xlsx), juntam/separam PDFs e criam relatorios no Word automaticamente.",
        "instalacao": "pip install openpyxl pypdf python-docx",
        "quando_usar": "Juntar 40 faturas em PDF em um unico arquivo, gerar contratos preenchidos no Word com nomes de clientes ou formatar planilhas gigantes com formulas.",
        "exemplo_codigo": '''from pypdf import PdfMerger

# Juntar varios PDFs com apenas 4 linhas de codigo:
juntador = PdfMerger()
juntador.append("capa.pdf")
juntador.append("relatorio.pdf")
juntador.write("arquivo_final_completo.pdf")
juntador.close()''',
        "prompt_ia": "Crie um aplicativo em Streamlit onde o usuario faz upload de varios arquivos PDF e eles sao mesclados em um unico PDF pronto para download."
    },
    {
        "nome": "Streamlit & Plotly",
        "categoria": "📊 Visualizacao & Interfaces Modernas",
        "descricao": "A combinacao perfeita para transformar qualquer ideia em dashboards interativos com graficos dinamicos (zoom, filtros e graficos 3D).",
        "instalacao": "pip install streamlit plotly",
        "quando_usar": "Criar ferramentas web internas, simuladores, portais para clientes e dashboards que deixam qualquer reuniao com ar de empresa de tecnologia do Vale do Silicio.",
        "exemplo_codigo": '''import plotly.express as px
import streamlit as st
import pandas as pd

dados = pd.DataFrame({'Mes': ['Jan', 'Fev', 'Mar'], 'Lucro': [20000, 35000, 48000]})
fig = px.bar(dados, x='Mes', y='Lucro', title='Evolucao Mensal', color='Lucro')
st.plotly_chart(fig)''',
        "prompt_ia": "Crie um dashboard elegante no Streamlit usando a biblioteca Plotly com graficos de linha e mapa de calor filtrados por data."
    },
    {
        "nome": "Pygame",
        "categoria": "🎮 Games & Visao Computacional",
        "descricao": "A biblioteca classica do Python para criacao de jogos 2D, animacoes graficas, controle de som, colisao e manipulacao de teclado/mouse.",
        "instalacao": "pip install pygame",
        "quando_usar": "Aprender logica de programacao avancada se divertindo, criar jogos educativos ou simuladores interativos de treinamento.",
        "exemplo_codigo": '''import pygame

pygame.init()
tela = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Meu Game em Python")
# Loop principal onde os quadros (FPS) sao desenhados continuamente''',
        "prompt_ia": "Crie o jogo classico da cobrinha (Snake) completo em Python usando Pygame com placar de pontos e controle pelas setas do teclado."
    },
    {
        "nome": "OpenCV (cv2) & MediaPipe",
        "categoria": "🎮 Games & Visao Computacional",
        "descricao": "Conferem 'visao' aos seus programas: acessam a webcam em tempo real para detectar rostos, maos, gestos corporais e ler codigos de barras/QR Code.",
        "instalacao": "pip install opencv-python mediapipe",
        "quando_usar": "Controle de presenca por reconhecimento de rosto, contagem de produtos em esteira de fabrica ou criacao de filtros estilo Instagram.",
        "exemplo_codigo": '''import cv2

camera = cv2.VideoCapture(0) # Inicia a webcam
ok, frame = camera.read()
if ok:
    cv2.imwrite("foto_capturada.jpg", frame)
camera.release()''',
        "prompt_ia": "Crie um script em Python usando OpenCV que acesse a webcam, identifique rostos na imagem e desenhe uma caixa delimitadora em volta deles."
    }
]
