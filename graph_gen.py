import json
import matplotlib.pyplot as plt

# Lê o arquivo de resultados em formato JSON
with open('resultados.json', 'r') as arquivo_json:
    resultados = json.load(arquivo_json)

# Extrai as informações de tempo e taxa de transferência dos testes TCP e UDP
tempo_tcp = []
taxa_tcp = []
for item in resultados['TCP']['intervals']:
    tempo_tcp.append(item['sum']['start'])
    taxa_tcp.append(item['sum']['bits_per_second'] / 1e9)

tempo_udp = []
taxa_udp = []
for item in resultados['UDP']['intervals']:
    tempo_udp.append(item['sum']['start'])
    taxa_udp.append(item['sum']['bits_per_second'] / 1e9)

# Gera o gráfico de linha com os resultados
plt.plot(tempo_tcp, taxa_tcp, label='TCP')
plt.plot(tempo_udp, taxa_udp, label='UDP')
plt.ylabel('Taxa de transferência (Gbps)')
plt.xlabel('Tempo decorrido (s)')
plt.title('Teste de velocidade de banda')
plt.legend()
plt.show()
