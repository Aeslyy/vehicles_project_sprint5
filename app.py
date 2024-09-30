# Versão Inicial
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
# Versão melhorada
import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo o arquivo CSV
car_data = pd.read_csv('vehicles.csv')

# Configurações gerais do aplicativo
st.set_page_config(page_title="Análise de Veículos", layout="wide")

# Cabeçalho principal
st.title('Análise Exploratória de Veículos Usados')

# Subcabeçalho
st.header('Visualização de Dados de Veículos')

# Exibindo uma breve descrição
st.write("""
    Este aplicativo web permite a visualização e análise exploratória de um conjunto de dados de veículos usados.
    Você pode selecionar gráficos para visualizar a distribuição da quilometragem, do preço, e outros atributos dos veículos.
""")

# Seções para os gráficos
st.subheader('Escolha as visualizações de gráficos')

# Organizando as opções de gráficos em colunas para melhor layout
col1, col2, col3 = st.columns(3)

with col1:
    # Botão para criar o histograma da quilometragem (odometer)
    if st.button('Criar Histograma de Quilometragem'):
        st.write('Distribuição da quilometragem dos veículos')
        fig_odometer_hist = px.histogram(car_data, x='odometer', color_discrete_sequence=['#1f77b4'],
                                         title='Distribuição da Quilometragem (Odometer)')
        st.plotly_chart(fig_odometer_hist, use_container_width=True)

with col2:
    # Botão para criar o gráfico de dispersão entre quilometragem (odometer) e preço (price)
    if st.button('Criar Gráfico de Dispersão (Odometer vs Price)'):
        st.write('Dispersão: Relação entre Quilometragem e Preço')
        fig_scatter = px.scatter(car_data, x='odometer', y='price', color='condition',
                                 title='Dispersão: Odometer vs Preço', 
                                 color_discrete_sequence=px.colors.qualitative.Vivid)
        st.plotly_chart(fig_scatter, use_container_width=True)

with col3:
    # Botão para criar o histograma de preço
    if st.button('Criar Histograma de Preço'):
        st.write('Distribuição dos Preços dos Veículos')
        fig_price_hist = px.histogram(car_data, x='price', color_discrete_sequence=['#ff7f0e'],
                                      title='Distribuição de Preços dos Veículos')
        st.plotly_chart(fig_price_hist, use_container_width=True)

# Organizando mais gráficos em outra seção
st.subheader('Análises Detalhadas')

# Exibição de gráficos mais detalhados
col4, col5 = st.columns(2)

with col4:
    # Gráfico de barras para contagem de modelos de veículos
    if st.checkbox('Mostrar Gráfico de Barras para Contagem de Modelos'):
        st.write('Contagem de Modelos de Veículos no Conjunto de Dados')
        fig_model_bar = px.bar(car_data['model'].value_counts().reset_index(),
                               x='index', y='model', title="Contagem de Modelos de Veículos",
                               labels={'index': 'Modelo', 'model': 'Contagem'},
                               color_discrete_sequence=['#2ca02c'])
        st.plotly_chart(fig_model_bar, use_container_width=True)

with col5:
    # Box plot para comparar preços por tipo de combustível
    if st.checkbox('Mostrar Box Plot de Preço por Tipo de Combustível'):
        st.write('Comparação de Preços por Tipo de Combustível')
        fig_box = px.box(car_data, x="fuel", y="price", color='fuel',
                         title="Preço por Tipo de Combustível",
                         labels={'fuel': 'Tipo de Combustível', 'price': 'Preço'},
                         color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig_box, use_container_width=True)

# Finalização com um rodapé ou mensagem adicional
st.write("---")
st.write("Aplicativo desenvolvido para análise exploratória de veículos usados.")

# Função adicional para organizar o layout e melhorar a experiência do usuário
def load_data(file_path):
    """
    Função para carregar os dados de veículos do arquivo CSV.
    """
    return pd.read_csv(file_path)
