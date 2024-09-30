# vehicles_project_sprint5
Projeto - Sprint 5 - TripleTen (DA-15)

# Análise de Dados de Veículos - Streamlit App

Este é um aplicativo web interativo de visualização de dados, desenvolvido com **Streamlit** e **Plotly**, que permite explorar um conjunto de dados de vendas de veículos. O objetivo do aplicativo é fornecer aos usuários uma maneira intuitiva de visualizar e analisar a quilometragem (`odometer`) e o preço (`price`) dos veículos através de gráficos dinâmicos.

## Funcionalidades

- **Histograma**: Permite ao usuário visualizar a distribuição da quilometragem dos veículos através de um histograma.
  
- **Gráfico de Dispersão**: Exibe a relação entre a quilometragem (`odometer`) e o preço (`price`) dos veículos.

- **Seleção Interativa**: O usuário pode selecionar quais gráficos deseja visualizar utilizando caixas de seleção:
  - Ao marcar **Criar um histograma**, o histograma é gerado.
  - Ao marcar **Criar um gráfico de dispersão**, o gráfico de dispersão é gerado.
  - Ambas as caixas de seleção podem ser ativadas simultaneamente para exibir os dois gráficos.

## Como Usar

1. **Instalar as Dependências**: Para instalar as dependências necessárias, execute o comando abaixo em seu terminal:

   ```bash
   pip install -r requirements.txt
   ```

2. **Executar o Aplicativo**: Após instalar as dependências, inicie o aplicativo com o comando:

   ```bash
   streamlit run app.py
   ```

3. **Interagir com o Aplicativo**: Ao abrir o aplicativo, você verá caixas de seleção:
   - Selecione a opção "Criar um histograma" para visualizar o histograma da coluna `odometer`.
   - Selecione a opção "Criar um gráfico de dispersão" para visualizar a relação entre `odometer` e `price`.
   - Marque ambas as caixas de seleção para ver os dois gráficos simultaneamente.

## Estrutura do Projeto

- **app.py**: Arquivo principal que contém o código do aplicativo Streamlit.
- **vehicles.csv**: Conjunto de dados contendo informações sobre veículos.
- **requirements.txt**: Lista de bibliotecas necessárias para rodar o projeto.

## Exemplo de Uso

Uma vez que o aplicativo esteja rodando, você pode interagir com ele e visualizar os dados de quilometragem e preço dos veículos:

- O **histograma** será exibido ao selecionar a opção "Criar um histograma".
- O **gráfico de dispersão** será exibido ao selecionar a opção "Criar um gráfico de dispersão".
- Você pode gerar ambos os gráficos simultaneamente selecionando ambas as caixas de seleção.

## Requisitos

- Python 3.7 ou superior
- Streamlit
- Pandas
- Plotly

## Conjunto de Dados

O conjunto de dados utilizado no projeto está no arquivo `vehicles.csv`, que contém informações sobre quilometragem (`odometer`), preço (`price`), e outras características de veículos listados para venda.