from recomendador import recomendar_filmes

print("=== RECOMENDADOR DE FILMES ===")

continuar = "s"

while continuar == "s":
    titulo = input(f"\n Digite o nome de um filme: ")

    resultados = recomendar_filmes(titulo)

    if not resultados:
        print(" Filme não encontrado")
    else:
        print(f"\n Filmes semelhantes a '{titulo}': ")


    for titulo, score in resultados:

        print(f"- {titulo} (similaridade: {score:.2f})")



    continuar = input(f"\n Deseja fazer outra busca? (s/n): ").lower()

    while continuar != "s" and continuar != "n":
        print("Mensagem inválida! Digite apenas 's' ou 'n'.")
        continuar = input(f"\n Deseja fazer outra busca? (s/n): ").lower()


print(f"\n Obrigado por utilzar o recomendador de filmes!")