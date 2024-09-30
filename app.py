'''import pandas as pd
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
'''
import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo o arquivo CSV
car_data = pd.read_csv('vehicles.csv')

# Caixas de seleção para selecionar o gráfico a ser criado
build_histogram = st.checkbox('Criar um histograma de quilometragem (odometer)')
build_scatter = st.checkbox('Criar um gráfico de dispersão (odometer vs price)')
build_price_hist = st.checkbox('Criar um histograma de preço (price)')
build_model_bar = st.checkbox('Criar gráfico de barras para contagem de modelos')
build_box_plot = st.checkbox('Criar box plot de preço por tipo de combustível')

# Criando histograma se a caixa de seleção for marcada
if build_histogram:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros (quilometragem)')
    fig_hist = px.histogram(car_data, x="odometer", title="Distribuição de Quilometragem (Odometer)")
    st.plotly_chart(fig_hist, use_container_width=True)

# Criando gráfico de dispersão se a caixa de seleção for marcada
if build_scatter:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros (odometer vs price)')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Dispersão: Odometer vs Preço")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Criando histograma de preço
if build_price_hist:
    st.write('Criando um histograma para o preço dos veículos')
    fig_price_hist = px.histogram(car_data, x="price", title="Distribuição de Preços")
    st.plotly_chart(fig_price_hist, use_container_width=True)

# Gráfico de barras para contagem de modelos
if build_model_bar:
    st.write('Criando um gráfico de barras para mostrar a contagem de modelos de veículos')
    fig_model_bar = px.bar(car_data['model'].value_counts().reset_index(),
                           x='index', y='model', title="Contagem de Modelos de Veículos",
                           labels={'index': 'Modelo', 'model': 'Contagem'})
    st.plotly_chart(fig_model_bar, use_container_width=True)

# Criando box plot de preço por tipo de combustível
if build_box_plot:
    st.write('Criando um box plot para comparar preço por tipo de combustível')
    fig_box = px.box(car_data, x="fuel", y="price", title="Preço por Tipo de Combustível",
                     labels={'fuel': 'Tipo de Combustível', 'price': 'Preço'})
    st.plotly_chart(fig_box, use_container_width=True)
