import streamlit as st
from streamlit_searchbox import st_searchbox
from recomendador import recomendar_filmes, buscar_filmes

st.title("🎬 Recomendador de Filmes")

st.write("Encontre filmes semelhantes ao seu favorito")

titulo = st_searchbox(
    buscar_filmes,
    key="busca_filmes",
    placeholder="Digite o nome de um filme",
    clear_on_submit=False
)

if st.button("Buscar"):

    if not titulo:
        st.warning("Digite o nome de um filme.")
    else:

        resultados = recomendar_filmes(titulo)

        if not resultados:
            st.error("Filme não encontrado.")
        else:
            st.subheader(f"Filmes semelhantes a '{titulo}': ")

            for titulo_filme, score in resultados:
                st.markdown(
                    f"""
                    <div style="
                        border-radius:10px;
                        padding:15px;
                        margin-bottom:10px;
                        background-color:#A9A9A9;
                    ">
                        <h4>{titulo_filme}</h4>
                        <p> Similaridade: {score*100:.1f}%</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )