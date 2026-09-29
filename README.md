🌐 APIs Externas com Python

Bem-vindo ao repositório APIs-Externas! 🚀

Este projeto é uma coleção de três aplicações práticas desenvolvidas em Python com o objetivo de aprender e aplicar o consumo de APIs externas. Através destes desafios, exploramos requisições web, tratamento de dados (JSON) e visualização de informações através de gráficos e tabelas.

💻 Desafios Realizados

1️⃣ Dashboard de Previsão do Tempo ⛅

Uma aplicação para monitorar e visualizar dados climáticos atuais e previsões.

API Utilizada: OpenWeatherMap (gratuita)

Objetivo: Consumir dados climáticos como temperatura, umidade e previsão para os próximos dias.

Bibliotecas: requests, json, matplotlib

Conceitos Aplicados: Requisições GET, tratamento básico de JSON e geração de gráficos simples.

Desafios Extras Concluídos:

✅ Adição de previsão para várias cidades e comparação utilizando um gráfico de barras.

✅ Exibição de parâmetros avançados (pressão atmosférica, precipitação, etc.).

2️⃣ Ranking de Filmes e Séries 🎬

Um sistema para buscar e listar as produções cinematográficas mais populares e bem avaliadas.

API Utilizada: The Movie Database (TMDb)

Objetivo: Buscar filmes mais bem avaliados ou populares do momento.

Bibliotecas: requests, pandas, matplotlib

Conceitos Aplicados: Extração de listas em JSON, ordenação de dados via DataFrames e gráficos de barras.

Desafios Extras Concluídos:

✅ Filtro interativo permitindo que o usuário escolha o gênero do filme.

✅ Exibição de detalhes aprofundados dos filmes (elenco principal, filmografias, sinopses).

3️⃣ Sistema de Notícias com Análise de Tendências 📰

Uma ferramenta para coletar manchetes, analisar tendências e gerar insights visuais sobre as notícias do momento.

API Utilizada: NewsAPI / GNews

Objetivo: Coletar as principais manchetes sobre um tema, contar a frequência de palavras-chave e criar nuvens de palavras (Wordclouds).

Bibliotecas: requests, collections, nltk, matplotlib, wordcloud

Conceitos Aplicados: Processamento de Linguagem Natural (NLP) básico, contagem de palavras e geração de wordclouds.

Desafios Extras Concluídos:

✅ Criação de um ranking das palavras mais frequentes estruturado em formato de tabela.

✅ Sistema de filtragem para mostrar notícias separadas por tema, região e data.

🛠️ Como executar o projeto na sua máquina

Se você quiser testar os scripts localmente, siga os passos abaixo:

Clone o repositório:

git clone https://github.com/souzzaParabolica/APIs-Externas.git
cd APIs-Externas


Crie um ambiente virtual (Opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  # No Linux/Mac
venv\Scripts\activate     # No Windows


Instale as dependências:

pip install requests pandas matplotlib nltk wordcloud


(Nota: Caso utilize bibliotecas adicionais, instale-as conforme a necessidade de cada script).

Configure as Chaves de API (API Keys):

Para que os projetos funcionem, você precisará criar contas gratuitas nas plataformas (OpenWeatherMap, TMDb e NewsAPI) e inserir suas API Keys nos respectivos arquivos Python.

👨‍💻 Autor

Desenvolvido por souzzaParabolica. Sinta-se à vontade para fazer um fork, abrir issues ou enviar pull requests!
