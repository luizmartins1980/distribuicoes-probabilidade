import streamlit as st
import seaborn as sns
import numpy as np
import math


#inserindo título do trabalho
st.markdown("# **Distribuições Probabilidade**")

#inserindo descrição trablaho
st.markdown("Escolha ao lado esquerdo e utilize os parâmetros das distribuições.")

#inserindo linha
st.markdown("---")

#incluindo título na barra lateral
st.sidebar.markdown("# **Menu Distribuição**")

#lista com aas distribuições disponíveis
distribuicao = ["1 - Gauss/Normal", "2 - Binomial", "3 - Binomial Negativa" 
               ,"4 - Qui-quadrado", "5 - Gamma", "6 - Exponencial"
               ,"7 - Geométrica", "8 - Beta", "9 - T de Student"
               ,"10 - Poisson", "11 - Log-normal", "12 - Gumbel"
               , "13 - Weibull"]

#select box com as op
selecao_distribuicao = st.sidebar.selectbox("Selecione a distribuição",distribuicao)

#inserindo linha
st.sidebar.markdown("---")

#se distribuição gauss/normal
if selecao_distribuicao[0:2] == "1 ":

    #inserindo texto
    st.sidebar.markdown("Parâmetros Gauss/Normal")

    #tamanho amostra
    tamanho_amostra = st.sidebar.slider("Tamanho da amostra", min_value= 30, max_value= 10000, step= 10)

    #valor média
    media = st.sidebar.slider("Média", min_value= -10, max_value= 10, step= 1, value= 0)

    #valor desvio padrão
    desvio = st.sidebar.slider("Desvio Padrão", min_value= 1, max_value= 10, step= 1, value= 1)

    #distribuição
    data = np.random.normal(loc= media, scale= desvio, size= tamanho_amostra)


#se distribuição binomial
elif selecao_distribuicao[0:2] == "2 ":
    
    #inserindo texto
    st.sidebar.markdown("Parâmetros Binomial")

    #tamanho amostra
    tamanho_amostra = st.sidebar.slider("Tamanho da amostra", min_value= 30, max_value= 10000, step= 10)

    #probabilidade 
    probabilidade = st.sidebar.slider("Probabilidade", min_value= 0.0, max_value= 1.0, step= 0.1, value= 0.5)

    #quantidade testes
    teste = st.sidebar.slider("Teste", min_value= 1000, max_value= 10000, step= 100, value= 5000)

    #distribuicao
    data = np.random.binomial(n= tamanho_amostra, p= probabilidade, size= teste)


#se distribuição binomial negativa
elif selecao_distribuicao[0:2] == "3 ":
    
    #inserindo texto
    st.sidebar.markdown("Parâmetros Binomial Negativa")

    #tamanho amostra
    tamanho_amostra = st.sidebar.slider("Tamanho da amostra", min_value= 30, max_value= 10000, step= 10)

    #probabilidade 
    probabilidade = st.sidebar.slider("Probabilidade", min_value= 0.0, max_value= 1.0, step= 0.1, value= 0.5)

    #quantidade testes
    teste = st.sidebar.slider("Teste", min_value=1000, max_value=10000, step=100, value=5000)

    #distribuicao
    data = np.random.negative_binomial(n= tamanho_amostra, p= probabilidade, size= teste)


#se distribuição qui-quadrado
elif selecao_distribuicao[0:2] == "4 ":
    
    #inserindo texto
    st.sidebar.markdown("Parâmetros Qui-quadrado")

    #tamanho amostra
    tamanho_amostra = st.sidebar.slider("Tamanho da amostra", min_value= 30, max_value= 10000, step= 10)

    #graus liberdade
    graus = st.sidebar.slider("Graus Liberdade", min_value= 1, max_value= 100, step= 1, value= 2)

    #distribuicao
    data = np.random.chisquare(df= graus, size= tamanho_amostra)


#se distribuição Gamma
elif selecao_distribuicao[0:2] == "5 ":
    
    #inserindo texto
    st.sidebar.markdown("Parâmetros Gamma")

    #tamanho amostra
    tamanho_amostra = st.sidebar.slider("Tamanho da amostra", min_value= 30, max_value= 10000, step= 10)

    #forma
    forma = st.sidebar.slider("Forma", min_value= 1, max_value= 10, step= 1, value= 2)

    #escala
    escala = st.sidebar.slider("Escala", min_value= 1, max_value= 10, step= 1, value= 2)

    #distribuicao
    data = np.random.gamma(shape= forma, scale= escala, size= tamanho_amostra)


#se distribuição Exponencial
elif selecao_distribuicao[0:2] == "6 ":
    
    #inserindo texto
    st.sidebar.markdown("Parâmetros Exponencial")

    #tamanho amostra
    tamanho_amostra = st.sidebar.slider("Tamanho da amostra", min_value= 30, max_value= 10000, step= 10)

    #escala
    escala = st.sidebar.slider("Escala", min_value= 1, max_value= 10, step= 1, value= 2)

    #distribuicao
    data = np.random.exponential(scale= escala, size= tamanho_amostra)


#se distribuição Geometrica
elif selecao_distribuicao[0:2] == "7 ":
    
    #inserindo texto
    st.sidebar.markdown("Parâmetros Geométrica")

    #tamanho amostra
    tamanho_amostra = st.sidebar.slider("Tamanho da amostra", min_value= 30, max_value= 10000, step= 10)

    #probabilidade 
    probabilidade = st.sidebar.slider("Probabilidade", min_value= 0.1, max_value= 1.0, step= 0.1, value= 0.1)

    #distribuicao
    data = np.random.geometric(p= probabilidade, size= tamanho_amostra)


#se distribuição Hipergeométrica
elif selecao_distribuicao[0:2] == "8 ":
    
    #inserindo texto
    st.sidebar.markdown("Parâmetros Beta")

    #tamanho amostra
    tamanho_amostra = st.sidebar.slider("Tamanho da amostra", min_value= 30, max_value= 10000, step= 10)

    #alfa
    alfa = st.sidebar.slider("Alfa", min_value= 1, max_value= 100, step= 1, value= 50)

    #beta
    beta = st.sidebar.slider("Beta", min_value= 1, max_value= 100, step= 1, value= 50)

    #distribuicao
    data = np.random.beta(a= alfa, b= beta, size= tamanho_amostra)


#se distribuição T de Student
elif selecao_distribuicao[0:2] == "9 ":
    
    #inserindo texto
    st.sidebar.markdown("Parâmetros T de Student")

    #tamanho amostra
    tamanho_amostra = st.sidebar.slider("Tamanho da amostra", min_value= 30, max_value= 10000, step= 10)

    #graus liberdade
    graus = st.sidebar.slider("Graus Liberdade", min_value= 1, max_value= 100, step= 1, value= 10)

    #distribuicao
    data = np.random.standard_t(df= graus, size= tamanho_amostra)


#se distribuição Poisson
elif selecao_distribuicao[0:2] == "10":
    
    #inserindo texto
    st.sidebar.markdown("Parâmetros Poisson")

    #tamanho amostra
    tamanho_amostra = st.sidebar.slider("Tamanho da amostra", min_value= 30, max_value= 10000, step= 10)

    #esperado
    esperado = st.sidebar.slider("Eventos esperados", min_value= 1, max_value= 1000, step= 10, value= 100)
    
    #distribuicao
    data = np.random.poisson(lam= esperado, size= tamanho_amostra)


#se distribuição log-normal
if selecao_distribuicao[0:2] == "11":

    #inserindo texto
    st.sidebar.markdown("Parâmetros Log-normal")

    #tamanho amostra
    tamanho_amostra = st.sidebar.slider("Tamanho da amostra", min_value= 30, max_value= 10000, step= 10)

    #valor média
    media = st.sidebar.slider("Média", min_value= -10, max_value= 10, step= 1, value= 0)

    #valor desvio padrão
    desvio = st.sidebar.slider("Desvio Padrão", min_value= 1, max_value= 10, step= 1, value= 1)

    #distribuição
    data = np.random.lognormal(mean= media, sigma= desvio, size= tamanho_amostra)


#se distribuição gumbel
if selecao_distribuicao[0:2] == "12":

    #inserindo texto
    st.sidebar.markdown("Parâmetros Gumbel")

    #tamanho amostra
    tamanho_amostra = st.sidebar.slider("Tamanho da amostra", min_value= 30, max_value= 10000, step= 10)

    #valor modo de distirbuição
    media = st.sidebar.slider("Média", min_value= -10, max_value= 10, step= 1, value= 0)

    #valor escala
    beta = st.sidebar.slider("Beta", min_value= 1, max_value= 10, step= 1, value= 1)

    #distribuição
    data = np.random.gumbel(loc= media, scale= beta, size= tamanho_amostra)


#se distribuição Weibull
elif selecao_distribuicao[0:2] == "13":
    
    #inserindo texto
    st.sidebar.markdown("Parâmetros Weibull")

    #tamanho amostra
    tamanho_amostra = st.sidebar.slider("Tamanho da amostra", min_value= 30, max_value= 10000, step= 10)

    #forma
    forma = st.sidebar.slider("Forma", min_value= 1, max_value= 10, step= 1, value= 4)
    
    #distribuicao
    data = np.random.weibull(a= forma, size= tamanho_amostra)


#calculando tamanho bin
bin_size = int(3 + math.log2(tamanho_amostra) * math.log(tamanho_amostra))

#gráfico com a distribuição
grafico = sns.displot(data, bins= bin_size, kde= True)

#plot gráfico
st.pyplot(grafico)
