# Classificação de Desastres Naturais com Machine Learning

## Descrição

Este projeto tem como objetivo classificar tipos de desastres naturais (como ciclones, terremotos, enchentes e incêndios florestais) usando um dataset real da base EM-DAT (Emergency Events Database). Foi desenvolvido um modelo de machine learning clássico utilizando algoritmos como KNN, Árvore de Decisão, Naive Bayes e SVM.

O projeto inclui:

- Notebook Python no Google Colab para pré-processamento, treinamento, avaliação e exportação do modelo;
- Aplicação full stack simples para realizar predições usando o modelo treinado;
- Testes automatizados para garantir a qualidade do modelo.

---

## Estrutura do Repositório

- `/notebook/` — Contém o notebook Jupyter (`.ipynb`) com todo o pipeline de machine learning;
- `/backend/` — Código do backend para carregar o modelo e servir a API de predição;
- `/frontend/` — Código frontend para interface do usuário;
- `requirements.txt` - Dependencias para o projeto
- `README.md` — Este arquivo.

---

## Tecnologias Utilizadas

- Python 3.11+
- Pandas, NumPy
- Scikit-learn (ML)
- Flask (backend)
- HTML, CSS, JavaScript (frontend)
- PyTest (testes automatizados)
- Google Colab (execução do notebook)

---

## Passo a passo para executar o projeto

### 1. Rodar o notebook no Google Colab

- Abra o notebook [[link para o notebook no GitHub](https://colab.research.google.com/drive/1lwvgVuD6Zp4CvwohaElaOqa4E3n0x9Xr?usp=sharing)] no Google Colab.
- Execute todas as células para:
  - Importar os dados reais via URL;
  - Realizar o pré-processamento dos dados;
  - Treinar e avaliar os modelos clássicos de ML;
  - Exportar o modelo final (`modelo_disaster_real.pkl`).

### 2. Configurar backend

- Acesse a pasta `/backend/`
- Instale as dependências:
  ```bash
  pip install -r requirements.txt
- Execute a aplicação Flask:
  ```bash
  python app.py
- O backend estará disponível em http://127.0.0.1:5000.
  
### 3. Configurar frontend
- Acesse a pasta `/frontend/`
- Abra o arquivo index.html no navegador.
- Insira os dados de entrada e faça a predição que será consultada no backend.

### 4. Executar testes automatizados
- Acesse a pasta `/backend/`
- Execute:
  ```bash
  pytest test_model.py
- O teste irá validar se o modelo atende aos requisitos mínimos de desempenho.
  
---

## Métricas e Avaliação
- Foram testados quatro algoritmos clássicos: KNN, Árvore de Decisão, Naive Bayes e SVM.
- Utilizou-se Stratified Train-Test Split e pipeline com padronização dos dados.
- O modelo com melhor acurácia no conjunto de teste foi escolhido e exportado.
- Métricas detalhadas de precisão, recall e f1-score são exibidas no notebook.
