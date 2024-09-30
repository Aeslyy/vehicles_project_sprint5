# **Projeto Veículos - Sprint 5 - TripleTen (DA-15)**

## 🚗 **Análise de Dados de Veículos - Streamlit App** 🚗

Este é um aplicativo web interativo de visualização de dados, desenvolvido com **Streamlit** e **Plotly**, que permite explorar um conjunto de dados de vendas de veículos. O objetivo do aplicativo é fornecer uma maneira **intuitiva** e **dinâmica** para os usuários visualizarem e analisarem a **quilometragem** (`odometer`) e o **preço** (`price`) dos veículos por meio de gráficos interativos.

---

### **⚙️ Funcionalidades**

- **Histograma**: Visualiza a **distribuição da quilometragem** dos veículos.
  
- **Gráfico de Dispersão**: Exibe a **relação** entre **quilometragem** (`odometer`) e **preço** (`price`) dos veículos.

- **Seleção Interativa**: O usuário pode selecionar quais gráficos deseja visualizar usando caixas de seleção:
  - 🔳 **Criar um histograma**: Gera o histograma da coluna `odometer`.
  - 🔳 **Criar um gráfico de dispersão**: Exibe o gráfico de dispersão mostrando a relação entre `odometer` e `price`.
  - **Ambas as opções podem ser selecionadas ao mesmo tempo** para visualizar os dois gráficos simultaneamente.

---

### **📝 Como Usar**

1. **Instalar Dependências**: Para instalar as bibliotecas necessárias, execute o seguinte comando no terminal:
   ```bash
   pip install -r requirements.txt
   ```

2. **Executar o Aplicativo**: Após a instalação das dependências, inicie o aplicativo com o comando:
   ```bash
   streamlit run app.py
   ```

3. **Interagir com o Aplicativo**: No aplicativo, você verá opções de seleção:
   - **Histograma**: Marque "Criar um histograma" para visualizar a distribuição da coluna `odometer`.
   - **Gráfico de Dispersão**: Marque "Criar um gráfico de dispersão" para visualizar a relação entre **quilometragem** e **preço**.
   - **Ambas as opções**: Marque ambas as opções para visualizar os dois gráficos simultaneamente.

---

### **📁 Estrutura do Projeto**

- **`app.py`**: Arquivo principal que contém o código do aplicativo Streamlit.
- **`vehicles.csv`**: Conjunto de dados com informações sobre veículos.
- **`requirements.txt`**: Arquivo com as dependências necessárias para rodar o projeto.

---

### **🔍 Exemplo de Uso**

- O **histograma** será exibido ao marcar a opção **Criar um histograma**.
- O **gráfico de dispersão** será gerado ao selecionar **Criar um gráfico de dispersão**.
- Marcar ambas as opções permitirá visualizar os dois gráficos ao mesmo tempo para uma análise mais completa.

---

### **📋 Requisitos**

- **Python 3.7** ou superior
- **Streamlit**
- **Pandas**
- **Plotly**

---

### **📊 Conjunto de Dados**

O conjunto de dados utilizado está no arquivo **`vehicles.csv`**, contendo informações como **quilometragem** (`odometer`), **preço** (`price`), e outras características de veículos à venda.

---

### **🌐 Visualização do Aplicativo**

A visualização interativa do aplicativo está disponível online. **Acesse através deste link** para ver o projeto em ação:

🔗 **Visualizar Aplicativo no Render: [https://vehicles-project-sprint5.onrender.com](https://vehicles-project-sprint5.onrender.com)**
