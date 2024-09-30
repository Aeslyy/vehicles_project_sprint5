import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo o arquivo CSV
car_data = pd.read_csv('vehicles.csv')

# Caixas de seleção para selecionar o gráfico a ser criado
build_histogram = st.checkbox('Criar um histograma')
build_scatter = st.checkbox('Criar um gráfico de dispersão')

# Criando histograma se a caixa de seleção for marcada
if build_histogram:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Criando gráfico de dispersão se a caixa de seleção for marcada
if build_scatter:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Dispersão: Odometer vs Preço")
    st.plotly_chart(fig_scatter, use_container_width=True)
