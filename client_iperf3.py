import subprocess
import json
from time import sleep

# IP do ponto remoto
ip_remoto = '172.30.118.72'

# Porta para a conexão
porta = '5001'

# Tempo de execução de cada teste (em minutos)
tempo = 1

# Tempo de espera entre os teste (em minutos)
tempo_espera = 1

# Realiza o teste TCP enviando dados para o servidor
print("Enviando dados TCP...")
saida_tcp_send = subprocess.check_output(f'iperf3 -c {ip_remoto} -p {porta} -t {60*tempo} -i 1 --json', shell=True)

# Converte a saída em um objeto JSON
resultado_tcp_send = json.loads(saida_tcp_send.decode())

# Aguarda um tempo determinado entre um teste e outro
sleep(60*tempo_espera)

# Realiza o teste UDP enviando dados para o servidor
print("Enviando dados UDP...")
saida_udp_send = subprocess.check_output(f'iperf3 -c {ip_remoto} -p {porta} -t {60*tempo} -i 1 -u -b 0 --json', shell=True)

# Converte a saída em um objeto JSON
resultado_udp_send = json.loads(saida_udp_send.decode())

sleep(60*tempo_espera)

# Realiza o teste TCP recebendo dados do servidor
print("Recebendo dados TCP...")
saida_tcp_receive = subprocess.check_output(f'iperf3 -c {ip_remoto} -p {porta} -t {60*tempo} -i 1 --reverse --json', shell=True)

# Converte a saída em um objeto JSON
resultado_tcp_receive = json.loads(saida_tcp_receive.decode())

sleep(60*tempo_espera)

# Aguarda um tempo determinado entre um teste e outro
sleep(10)

# Realiza o teste UDP recebendo dados do servidor
print("Recebendo dados UDP...")
saida_udp_receive = subprocess.check_output(f'iperf3 -c {ip_remoto} -p {porta} -t {60*tempo} -i 1 -u -b 0 --reverse --json', shell=True)

# Converte a saída em um objeto JSON
resultado_udp_receive = json.loads(saida_udp_receive.decode())

# Exporta os resultados em formato JSON
with open('resultados.json', 'w') as arquivo_json:
    json.dump(
        {
            'TCP_SEND': resultado_tcp_send,
            'UDP_SEND': resultado_udp_send,
            'TCP_RECEIVE': resultado_tcp_receive,
            'UDP_RECEIVE': resultado_udp_receive
        }, arquivo_json, indent=4
    )
