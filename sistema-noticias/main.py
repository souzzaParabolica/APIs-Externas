import os
import re
import requests
import nltk
import matplotlib.pyplot as plt

from collections import Counter
from wordcloud import WordCloud
from dotenv import load_dotenv


# =========================
# CONFIGURAÇÃO
# =========================

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

URL = "https://newsapi.org/v2/everything"


# Palavras que não ajudam na análise
STOPWORDS = {
    "a", "o", "e", "de", "do", "da", "dos", "das",
    "em", "no", "na", "nos", "nas", "um", "uma",
    "uns", "umas", "para", "por", "com", "sem",
    "que", "se", "os", "as", "ao", "aos", "à", "às",
    "é", "foi", "ser", "são", "como", "mais", "menos",
    "já", "também", "sobre", "entre", "após", "até",
    "tem", "ter", "têm", "seu", "sua", "seus", "suas",
    "ou", "mas", "não", "sim", "nos", "nas"
}


# =========================
# ESCOLHA DO TEMA
# =========================

tema = input("Digite o tema das notícias: ")

print("\nBuscando notícias...\n")


# =========================
# BUSCAR NOTÍCIAS
# =========================

parametros = {
    "q": tema,
    "language": "pt",
    "sortBy": "publishedAt",
    "pageSize": 20
}

resposta = requests.get(
    URL,
    params=parametros,
    headers={"X-Api-Key": API_KEY}
)

dados = resposta.json()


# Verificar erro da API
if dados.get("status") != "ok":
    print("Erro ao buscar notícias.")
    print(dados.get("message", "Erro desconhecido."))
    exit()


noticias = dados.get("articles", [])


if not noticias:
    print("Nenhuma notícia encontrada.")
    exit()


# =========================
# MOSTRAR NOTÍCIAS
# =========================

print("=" * 60)
print(f"NOTÍCIAS SOBRE: {tema.upper()}")
print("=" * 60)

for i, noticia in enumerate(noticias, start=1):

    titulo = noticia.get("title", "Sem título")
    fonte = noticia.get("source", {}).get("name", "Fonte desconhecida")
    data = noticia.get("publishedAt", "Data desconhecida")
    descricao = noticia.get("description") or "Sem descrição."

    print(f"\n{i}. {titulo}")
    print(f"Fonte: {fonte}")
    print(f"Data: {data[:10]}")
    print(f"Descrição: {descricao}")


# =========================
# SEPARAÇÃO POR REGIÃO
# =========================

print("\n")
print("=" * 60)
print("NOTÍCIAS POR REGIÃO / FONTE")
print("=" * 60)

regioes = {}

for noticia in noticias:

    fonte = noticia.get("source", {}).get("name", "Desconhecida")

    if fonte not in regioes:
        regioes[fonte] = []

    regioes[fonte].append(noticia)


for fonte, lista in regioes.items():

    print(f"\n--- {fonte} ---")

    for noticia in lista:
        print("-", noticia.get("title", "Sem título"))


# =========================
# SEPARAÇÃO POR DATA
# =========================

print("\n")
print("=" * 60)
print("NOTÍCIAS POR DATA")
print("=" * 60)

datas = {}

for noticia in noticias:

    data = noticia.get("publishedAt", "Desconhecida")[:10]

    if data not in datas:
        datas[data] = []

    datas[data].append(noticia)


for data, lista in sorted(datas.items(), reverse=True):

    print(f"\n--- {data} ---")

    for noticia in lista:
        print("-", noticia.get("title", "Sem título"))


# =========================
# ANÁLISE DAS PALAVRAS
# =========================

texto = ""

for noticia in noticias:

    titulo = noticia.get("title") or ""
    descricao = noticia.get("description") or ""

    texto += " " + titulo + " " + descricao


# Transformar tudo em letras minúsculas
texto = texto.lower()

# Remover números e símbolos
palavras = re.findall(r"\b[a-záàâãéêíóôõúç]+\b", texto)

# Remover palavras comuns
palavras_filtradas = [
    palavra
    for palavra in palavras
    if palavra not in STOPWORDS and len(palavra) > 2
]


# =========================
# RANKING
# =========================

contagem = Counter(palavras_filtradas)

print("\n")
print("=" * 60)
print("RANKING DAS PALAVRAS MAIS FREQUENTES")
print("=" * 60)

print("\nPalavra                  Frequência")
print("-" * 40)

for palavra, quantidade in contagem.most_common(15):

    print(f"{palavra:<25} {quantidade}")


# =========================
# GRÁFICO
# =========================

top_palavras = contagem.most_common(10)

nomes = [item[0] for item in top_palavras]
quantidades = [item[1] for item in top_palavras]

plt.figure(figsize=(10, 5))

plt.bar(nomes, quantidades)

plt.title("10 palavras mais frequentes")
plt.xlabel("Palavras")
plt.ylabel("Frequência")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# =========================
# WORDCLOUD
# =========================

wordcloud = WordCloud(
    width=1000,
    height=500,
    background_color="white",
    stopwords=STOPWORDS,
    collocations=False
).generate(" ".join(palavras_filtradas))


plt.figure(figsize=(12, 6))

plt.imshow(wordcloud, interpolation="bilinear")

plt.axis("off")

plt.title(f"Nuvem de palavras - {tema}")

plt.show()


# =========================
# FINAL
# =========================

print("\n")
print("=" * 60)
print("ANÁLISE CONCLUÍDA!")
print("=" * 60)