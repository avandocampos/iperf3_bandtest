import json
import matplotlib.pyplot as plt

# Lê os dados do arquivo gerado pelo código anterior
with open('resultados.json', 'r') as arquivo_json:
    resultados = json.load(arquivo_json)

# Extrai as taxas de transferência e os tempos de cada teste
taxas_tcp_send = [float(x['sum']['bits_per_second'])/1e9 for x in resultados['TCP_SEND']['intervals']]
tempos_tcp_send = [x['sum']['start'] for x in resultados['TCP_SEND']['intervals']]

taxas_udp_send = [float(x['sum']['bits_per_second'])/1e9 for x in resultados['UDP_SEND']['intervals']]
tempos_udp_send = [x['sum']['start'] for x in resultados['UDP_SEND']['intervals']]

taxas_tcp_receive = [float(x['sum']['bits_per_second'])/1e9 for x in resultados['TCP_RECEIVE']['intervals']]
tempos_tcp_receive = [x['sum']['start'] for x in resultados['TCP_RECEIVE']['intervals']]

taxas_udp_receive = [float(x['sum']['bits_per_second'])/1e9 for x in resultados['UDP_RECEIVE']['intervals']]
tempos_udp_receive = [x['sum']['start'] for x in resultados['UDP_RECEIVE']['intervals']]

# Cria os subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# Ajusta o espaçamendo entre os gráficos
fig.subplots_adjust(hspace=0.5)

# Plota o primeiro gráfico
ax1.plot(tempos_tcp_send, taxas_tcp_send, label='TCP Send')
ax1.plot(tempos_udp_send, taxas_udp_send, label='UDP Send')
ax1.set_title('Taxa de Transferência (Envio)')
ax1.set_xlabel('Tempo (s)')
ax1.set_ylabel('Taxa de Transferência (Gbps)')
ax1.legend()
ax1.grid()

# Plota o segundo gráfico
ax2.plot(tempos_tcp_receive, taxas_tcp_receive, label='TCP Receive')
ax2.plot(tempos_udp_receive, taxas_udp_receive, label='UDP Receive')
ax2.set_title('Taxa de Transferência (Recebimento)')
ax2.set_xlabel('Tempo (s)')
ax2.set_ylabel('Taxa de Transferência (Gbps)')
ax2.legend()
ax2.grid()

# Exibe os gráficos
# plt.show()

# Salva o gráfico gerado em formato png
plt.savefig('graph.png')