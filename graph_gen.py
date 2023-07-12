import json
import matplotlib.pyplot as plt


def plot_graph(results):

    # Extrai as taxas de transferência e os tempos de cada teste
    tcp_send_rates = [float(x['sum']['bits_per_second'])/1e6 for x in results['TCP_SEND']['intervals']]
    tcp_send_times = [x['sum']['start'] for x in results['TCP_SEND']['intervals']]

    udp_send_rates = [float(x['sum']['bits_per_second'])/1e6 for x in results['UDP_SEND']['intervals']]
    udp_send_times = [x['sum']['start'] for x in results['UDP_SEND']['intervals']]

    tcp_receive_rates = [float(x['sum']['bits_per_second'])/1e6 for x in results['TCP_RECEIVE']['intervals']]
    tcp_receive_times = [x['sum']['start'] for x in results['TCP_RECEIVE']['intervals']]

    udp_receive_rates = [float(x['sum']['bits_per_second'])/1e6 for x in results['UDP_RECEIVE']['intervals']]
    udp_receive_times = [x['sum']['start'] for x in results['UDP_RECEIVE']['intervals']]

    # Cria os subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    # Ajusta o espaçamendo entre os gráficos
    fig.subplots_adjust(hspace=0.5)

    # Plota o primeiro gráfico
    ax1.plot(tcp_send_times, tcp_send_rates, label='TCP Send')
    ax1.plot(udp_send_times, udp_send_rates, label='UDP Send')
    ax1.set_title('Taxa de Transferência (MBits por segundo enviados pelo cliente)')
    ax1.set_xlabel('Tempo (s)')
    ax1.set_ylabel('Taxa de Transferência (Mbps)')
    ax1.legend()
    ax1.grid()

    # Plota o segundo gráfico
    ax2.plot(tcp_receive_times, tcp_receive_rates, label='TCP Receive')
    ax2.plot(udp_receive_times, udp_receive_rates, label='UDP Receive')
    ax2.set_title('Taxa de Transferência (MBits por segundo recebidos pelo cliente)')
    ax2.set_xlabel('Tempo (s)')
    ax2.set_ylabel('Taxa de Transferência (Mbps)')
    ax2.legend()
    ax2.grid()

    # Salva o gráfico gerado em formato png
    plt.savefig('graph.png')


if __name__ == '__main__':
    with open('results.json', 'r') as json_file:
        results = json.load(json_file)

        plot_graph(results)
