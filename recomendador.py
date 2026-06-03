import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('filmes.csv')
df['descricao'] = df['descricao'].fillna('')

vetorizar = TfidfVectorizer(stop_words= None)
matriz_tfidf = vetorizar.fit_transform(df['descricao'])

similaridade = cosine_similarity(matriz_tfidf, matriz_tfidf)

def recomendar_filmes(titulo, n=5):
    if titulo not in df['titulo'].values:
        print("Filme não encontrado.")
        return
    
    idx = df[df['titulo'] == titulo].index[0]

    scores = list(enumerate(similaridade[idx]))

    scores = sorted(scores, key=lambda x : x[1], reverse=True)

    scores = scores[1:n+1]

    print(f"\n Filmes semelhantes a '{titulo}': ")
    for i, score in scores:
        print(f"- {df.iloc[i]['titulo']} (similaridade: {score:.2f})")
    

recomendar_filmes("Matrix")