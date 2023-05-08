import subprocess
import json
from decouple import config
from time import sleep

# IP do ponto remoto
remote_host = config('REMOTE_HOST', default='10.41.110.122')

# Porta para a conexão
port = config('PORT', default=5001, cast=int)

# Tempo de execução de cada teste (em minutos)
time = config('TIME', default=60, cast=int)

# Tempo de espera entre os teste (em minutos)
time_wait = config('TIME_WAIT', default=60, cast=int)

# Realiza o teste TCP enviando dados para o servidor
print("Enviando dados TCP...")
tcp_send_output = subprocess.check_output(f'iperf3 -c {remote_host} -p {port} -t {time} -i 1 --json', shell=True)

# Converte a saída em um objeto JSON
tcp_send_result = json.loads(tcp_send_output.decode())

# Aguarda um tempo determinado entre um teste e outro
sleep(time_wait)

# Realiza o teste UDP enviando dados para o servidor
print("Enviando dados UDP...")
udp_send_output = subprocess.check_output(f'iperf3 -c {remote_host} -p {port} -t {time} -i 1 -u -b 0 --json', shell=True)

# Converte a saída em um objeto JSON
udp_send_result = json.loads(udp_send_output.decode())

sleep(time_wait)

# Realiza o teste TCP recebendo dados do servidor
print("Recebendo dados TCP...")
tcp_receive_output = subprocess.check_output(f'iperf3 -c {remote_host} -p {port} -t {time} -i 1 --reverse --json', shell=True)

# Converte a saída em um objeto JSON
tcp_receive_result = json.loads(tcp_receive_output.decode())

sleep(time_wait)

# Realiza o teste UDP recebendo dados do servidor
print("Recebendo dados UDP...")
udp_receive_output = subprocess.check_output(f'iperf3 -c {remote_host} -p {port} -t {time} -i 1 -u -b 0 --reverse --json', shell=True)

# Converte a saída em um objeto JSON
udp_receive_result = json.loads(udp_receive_output.decode())

# Exporta os resultados em formato JSON
with open('results.json', 'w') as json_file:
    json.dump(
        {
            'TCP_SEND': tcp_send_result,
            'UDP_SEND': udp_send_result,
            'TCP_RECEIVE': tcp_receive_result,
            'UDP_RECEIVE': udp_receive_result
        }, json_file, indent=4
    )
