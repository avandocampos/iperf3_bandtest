import subprocess
import json
from time import sleep

# IP do ponto remoto
ip_remoto = '172.30.118.72'

# Porta para a conexão
porta = '5001'

# Realiza o teste TCP
print("Realizando teste TCP...")
saida_tcp = subprocess.check_output(f'iperf3 -c {ip_remoto} -p {porta} -t {60*1} -i 1 --json', shell=True)

# Converte a saída em um objeto JSON
resultado_tcp = json.loads(saida_tcp.decode())

# Aguarda um tempo determinado entre um teste e outro
sleep(10)

# Realiza o teste UDP
print("Realizando teste UDP...")
saida_udp = subprocess.check_output(f'iperf3 -c {ip_remoto} -p {porta} -t {60*1} -i 1 -u -b 0 --json', shell=True)

# Converte a saída em um objeto JSON
resultado_udp = json.loads(saida_udp.decode())

# Exporta os resultados em formato JSON
with open('resultados.json', 'w') as arquivo_json:
    json.dump({'TCP': resultado_tcp, 'UDP': resultado_udp}, arquivo_json, indent=4)
