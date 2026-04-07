# 📊 Dashboard de Análise de Funcionários (Streamlit)

Este projeto é um **dashboard interativo** desenvolvido com a biblioteca **Streamlit**, com foco em análise de dados de funcionários.

Ele demonstra conceitos importantes como:

* Manipulação de dados com **Pandas**
* Limpeza e tratamento de dados
* Feature Engineering
* Criação de dashboards interativos
* Uso de filtros dinâmicos
* Visualização de dados

---

## 🚀 Funcionalidades

✔️ Filtros por cidade
✔️ Filtro por faixa salarial
✔️ KPIs (métricas principais)
✔️ Gráficos interativos
✔️ Tabela dinâmica (pivot table)
✔️ Upload de arquivos CSV
✔️ Visualização de dados em tempo real

---

## 🛠️ Tecnologias utilizadas

* Python 3.x
* Streamlit
* Pandas
* NumPy

---

## 📂 Estrutura do projeto

```
streamlit/
│
├── app.py          # Código principal do dashboard
└── README.md       # Documentação do projeto
```

---

## ⚙️ Como executar o projeto (qualquer máquina)

### 1. Clone ou copie o projeto

```bash
git clone <url-do-repositorio>
cd streamlit
```

ou apenas copie a pasta para outra máquina.

---

### 2. Criar ambiente virtual (RECOMENDADO)

```bash
python -m venv venv
```

Ativar:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

---

### 3. Instalar dependências

```bash
python -m pip install --upgrade pip
python -m pip install streamlit "pandas<3" numpy
```

---

### 4. Rodar o projeto

```bash
python -m streamlit run app.py
```

---

### 5. Acessar no navegador

O Streamlit abrirá automaticamente, ou acesse:

```
http://localhost:8501
```

---

## 📥 Upload de CSV

O sistema permite que o usuário envie arquivos `.csv` diretamente pela interface e visualize os dados.

---

## 📊 Sobre o Dashboard

O dashboard realiza:

* Limpeza automática de dados (valores nulos)
* Cálculo de métricas:

  * Salário médio
  * Total de funcionários
  * Salário máximo
* Agrupamentos por cidade
* Classificação por faixa salarial
* Geração de tabela dinâmica

---

## 🧠 Conceitos aplicados

* Data Cleaning
* Data Analysis
* Data Visualization
* Interatividade com Streamlit
* Estruturação de projetos em Python

---

## ⚠️ Possíveis erros comuns

### ❌ Streamlit não reconhecido

Use:

```bash
python -m streamlit run app.py
```

### ❌ Erro com pandas

Instale versão compatível:

```bash
python -m pip install "pandas<3"
```

### ❌ Pip não reconhecido

Use:

```bash
python -m pip install ...
```

---

