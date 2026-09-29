import os
from dotenv import load_dotenv
load_dotenv()
import requests
import matplotlib.pyplot as plt

API_KEY = os.getenv("TMDB_API_KEY")

generos = {
    '1':('Ação', 28),
    '2':('Aventura', 12),
    '3':('Comédia', 35),
    '4':('Drama', 18),
    '5':('Terror', 27),
    '6':('Ficção Científica', 878),
    '7':('Romance', 10749),
    '8':('Animação', 16)
}

print("Escolha um gênero:")
for numero, genero in generos.items():
    print(numero, '-', genero[0])

escolha = input('Digite o numero do gênero: ')

nome_genero = generos[escolha][0]
id_genero = generos[escolha][1]

url = 'https://api.themoviedb.org/3/discover/movie'

parametros = {
    'api_key': API_KEY,
    'language': 'pt-BR',
    'with_genres': id_genero,
    'sort_by': 'vote_average.desc',
    'vote_count.gte': 1000
}

resposta = requests.get(url, params=parametros)
dados = resposta.json()

filmes = dados['results'][:5]

print('\nTop 5 filmes de', nome_genero)
print('-' * 40)

nomes = []
notas = []

for filme in filmes:
    titulo = filme["title"]
    nota = filme['vote_average']
    id_filme = filme['id']

    nomes.append(titulo)
    notas.append(nota)

    print('\nFilme:', titulo)
    print('Nota:', nota)
    print('Lançamento:', filme['release_date'])

    url_creditos = f'https://api.themoviedb.org/3/movie/{id_filme}/credits'

    resposta_creditos = requests.get(
        url_creditos,
        params={
            'api_key': API_KEY,
            'language': 'pt-BR'
        }
    )

    creditos = resposta_creditos.json()

    elenco = creditos['cast'][:5]

    print('Elenco:')
    for ator in elenco:
        print('-', ator['name'])

plt.bar(nomes, notas)

plt.title('Filmes mais bem avaliados - ' + nome_genero)
plt.xlabel('Filmes')
plt.ylabel('Nota')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()