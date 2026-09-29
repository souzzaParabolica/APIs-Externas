import os
from dotenv import load_dotenv
load_dotenv()
import requests
import matplotlib.pyplot as plt
api_key_weather = os.getenv("OPENWEATHER_API_KEY")
cidades = ['Viana', 'Osasco', 'Itaquera', 'Santos']
temperaturas = []
umidades = []

print('=== DASHBOARD DE CLIMA ===')

for cidade in cidades:
    url_clima = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key_weather}&units=metric&lang=pt_br"
    response_clima = requests.get(url_clima)

    if response_clima.status_code == 200:
        dados_clima = response_clima.json()
        climas_desc = dados_clima['weather'][0]['description']
        temp = dados_clima['main']['temp']
        umidade = dados_clima['main']['humidity']
        pressao = dados_clima['main']['pressure']

        temperaturas.append(temp)
        umidades.append(umidade)

        print(f'\n {cidade.upper()}:')
        print(f'Condição: {climas_desc.capitalize()}')
        print(f'Temperatura: {temp}ºC')
        print(f'Umidade: {umidade}%')
        print(f'Pressão: {pressao} hPa')

        if 'rain' in dados_clima:
            chuva_1h = dados_clima['rain'].get('1h', 0)
            print(f'Precipitação (última 1h): {chuva_1h} mm')

    else:
        print(f'\nErro ao obter dados para {cidade}')
        temperaturas.append(0)
        umidade.append(0)


plt.figure(figsize=(10,5))

plt.bar(cidades, temperaturas, color='skyblue', edgecolor='black')

plt.title('Comparação de Temperatura Atual', fontsize=14)
plt.xlabel('Cidades', fontsize=12)
plt.ylabel('Temperatura (Cº)', fontsize=12)

for i in range(len(cidades)):
    plt.text(i, temperaturas[i] + 0.5, f'{temperaturas[i]}ºC', ha='center')

plt.show()