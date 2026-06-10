import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('filmes.csv')
df['descricao'] = df['descricao'].fillna('')
df['titulo_lower'] = df['titulo'].str.lower()


df['conteudo'] = (
    df['genero'] + ' ' + df['diretor'] + ' ' + df['descricao']
)

vetorizar = TfidfVectorizer(stop_words= None)
matriz_tfidf = vetorizar.fit_transform(df['conteudo'])

similaridade = cosine_similarity(matriz_tfidf, matriz_tfidf)

def recomendar_filmes(titulo, n=5):
    titulo_busca = titulo.lower()

    if titulo_busca not in df['titulo_lower'].values:
        print("Filme não encontrado.")
        return
    
    idx = df[df['titulo_lower'] == titulo_busca].index[0]

    scores = list(enumerate(similaridade[idx]))

    scores = sorted(scores, key=lambda x : x[1], reverse=True)

    scores = scores[1:n+1]

    titulo_original = df.iloc[idx]['titulo']
    print(f"\n Filmes semelhantes a '{titulo_original}': ")
    #print(f"  Gênero: {df.iloc[idx]['genero']}")
    for i, score in scores:
        print(f"- {df.iloc[i]['titulo']} (similaridade: {score:.2f})")
    


print("=== RECOMENDADOR DE FILMES ===")

continuar = "s"

while continuar == "s":
    titulo = input(f"\n Digite o nome de um filme: ")
    recomendar_filmes(titulo)

    continuar = input(f"\n Deseja fazer outra busca? (s/n): ").lower()

    while continuar != "s" and continuar != "n":
        print("Mensagem inválida! Digite apenas 's' ou 'n'.")
        continuar = input(f"\n Deseja fazer outra busca? (s/n): ").lower()


print(f"\n Obrigado por utilzar o recomendador de filmes!")