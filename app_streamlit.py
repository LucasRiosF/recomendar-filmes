import streamlit as st
from recomendador import recomendar_filmes

st.title("🎬 Recomendador de Filmes")

st.write("Encontre filmes semelhantes ao seu favorito")

titulo = st.text_input("Digite o nome de um filme")

if st.button("Buscar"):
    resultados = recomendar_filmes(titulo)

    if not resultados:
        st.error("Filme não encontrado.")
    else:
        st.write(f"Filmes semelhantes a '{titulo}': ")

        for titulo, score in resultados:
            st.write(f"- {titulo} (similaridade: {score:.2f})")