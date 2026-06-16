import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('filmes.csv')
df['genero'] = df['genero'].fillna('')
df['subgenero'] = df['subgenero'].fillna('')
df['diretor'] = df['diretor'].fillna('')
df['descricao'] = df['descricao'].fillna('')
df['titulo_lower'] = df['titulo'].str.lower()


df['conteudo'] = (
    df['genero'] + ' ' + df['subgenero'] + ' ' + df['diretor'] + ' ' + df['descricao']
)

vetorizar = TfidfVectorizer(stop_words= None)
matriz_tfidf = vetorizar.fit_transform(df['conteudo'])

similaridade = cosine_similarity(matriz_tfidf, matriz_tfidf)

def recomendar_filmes(titulo, n=5):
    titulo_busca = titulo.lower()

    if titulo_busca not in df['titulo_lower'].values:
        return []
    
    idx = df[df['titulo_lower'] == titulo_busca].index[0]

    scores = list(enumerate(similaridade[idx]))

    scores = sorted(scores, key=lambda x : x[1], reverse=True)

    scores = scores[1:n+1]

    resultados = []

    for i, score in scores:

        titulo_filme = df.iloc[i]['titulo']

        resultados.append((titulo_filme, score))


    return resultados



lista_titulos = df['titulo'].fillna('').astype(str).tolist()

def buscar_filmes(termo_digitado: str):
    if not termo_digitado:
        return []
    
    return [filme for filme in lista_titulos if termo_digitado.lower() in filme.lower()]