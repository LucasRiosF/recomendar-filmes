# 🎬 Sistema de Recomendação de Filmes

Um sistema simples de recomendação de filmes desenvolvido em Python utilizando técnicas de Processamento de Linguagem Natural (NLP) e Machine Learning.
O projeto utiliza **TF-IDF** e **Similaridade do Cosseno** para encontrar filmes com descrições, gêneros e diretores parecidos e recomendar títulos semelhantes ao usuário.

---

## 📌 Objetivo do Projeto

O objetivo deste projeto é estudar e aplicar conceitos importantes de:

* Python
* Manipulação de dados
* Processamento de texto
* Machine Learning
* Sistemas de recomendação
* NLP (Natural Language Processing)

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* Scikit-learn
* Streamlit

---

## 📄 Dataset

O arquivo `filmes.csv` contém:

* Título do filme
* Gênero do filme
* Diretor do filme
* Descrição/resumo do filme

Exemplo:

```csv
titulo,genero,diretor,descricao
Matrix,Ficção Científica,Wachowski,"Um hacker descobre a verdade sobre sua realidade..."
```

---

## ⚙️ Como o Sistema Funciona

O sistema segue as seguintes etapas:

### 1. Leitura dos dados

O arquivo CSV é carregado usando Pandas:

```python
df = pd.read_csv('filmes.csv')
```

---

### 2. Tratamento de valores nulos

Descrições vazias são substituídas por texto vazio:

```python
df['descricao'] = df['descricao'].fillna('')
```

---

### 3. Vetorização TF-IDF

As informações dos filmes são transformadas em números usando o algoritmo **TF-IDF**.

```python
df['conteudo'] = (
    df['genero'] + ' ' + df['diretor'] + ' ' + df['descricao']
)

vetorizar = TfidfVectorizer(stop_words=None)
matriz_tfidf = vetorizar.fit_transform(df['conteudo'])
```

### O que é TF-IDF?

TF-IDF significa:

* **TF (Term Frequency)** → frequência da palavra no texto
* **IDF (Inverse Document Frequency)** → importância da palavra entre todos os textos

Ele ajuda o sistema a identificar palavras importantes nas descrições dos filmes.

Exemplo:

* palavras como "o", "de", "a" têm pouca importância
* palavras como "máquinas", "guerra", "anel" possuem mais relevância

---

## 📐 Similaridade do Cosseno

Após transformar os textos em vetores numéricos, o sistema utiliza a **Similaridade do Cosseno** para medir o quanto dois filmes são parecidos.

```python
similaridade = cosine_similarity(matriz_tfidf, matriz_tfidf)
```


A Similaridade do Cosseno mede o ângulo entre dois vetores.

* Quanto menor o ângulo:

  * mais semelhantes os filmes são
* Quanto maior o ângulo:

  * menos semelhantes eles são

O valor varia entre:

| Valor | Significado        |
| ----- | ------------------ |
| 1     | Muito semelhantes  |
| 0     | Sem relação        |
| -1    | Totalmente opostos |

---

<img width="246" height="205" alt="images" src="https://github.com/user-attachments/assets/e6030ddc-2855-49c4-857d-99b42fd05535" />

---

## 🔎 Como a recomendação é feita

Quando o usuário informa um filme:

o sistema:

1. encontra o índice do filme
2. calcula os filmes mais parecidos
3. ordena pela maior similaridade
4. exibe os melhores resultados

Exemplo de saída:

```bash
Filmes semelhantes a 'Matrix': 
- Senhor dos Anéis (similaridade: 0.11)
- Matrix Revolutions (similaridade: 0.09)
```

---

## ▶️ Como executar o projeto

### 1. Instale as dependências

```bash
pip install pandas scikit-learn
```

---

### 2. Execute o arquivo

```bash
python recomendador.py
```

---

## 💡Conceitos Aprendidos

Este projeto utiliza conceitos importantes de Ciência de Dados e Machine Learning:

* Vetorização de texto
* TF-IDF
* Similaridade do Cosseno
* NLP básico
* Manipulação de DataFrames
* Algoritmos de recomendação

---

## Possíveis Melhorias Futuras

* Melhorar o dataset com mais filmes
* Utilizar banco de dados
* Permitir recomendação por gênero
* Sistema de usuários e avaliações
* Recomendação híbrida
