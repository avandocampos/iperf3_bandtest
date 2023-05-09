def to_html(results):

    style = """
        <style>
            .table-container {
                display: flex;
                flex-direction: row;
                width: 100%;
                margin-top: 20px;
            }

            .table-container div {
                flex: 1;
            }

            table {
                border-collapse: collapse;
                margin: 0 10px;
            }

            th, td {
                padding: 8px;
                text-align: left;
                border: 1px solid #ddd;
            }

            th {
                background-color: #f2f2f2;
                color: #555;
            }
        </style>
    """

    email_body = f""" <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Gráficos</title>

        {style}

    </head>
    <body>
        <div class="table-container">
            <table id="tcp-send">
                <thead>
                    <tr>
                        <th colspan="4">ENVIO DE DADOS TCP</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th>Bytes enviados</th>
                        <th>Tempo total (s)</th>
                        <th>Bits por segundo (média)</th>
                        <th>Reenvios</th>
                    </tr>
                    <tr>
                        <td>{results['TCP_SEND']['end']['streams'][0]['sender']['bytes']}</td>
                        <td>{results['TCP_SEND']['end']['streams'][0]['sender']['seconds']}</td>
                        <td>{results['TCP_SEND']['end']['streams'][0]['sender']['bits_per_second']}</td>
                        <td>{results['TCP_SEND']['end']['streams'][0]['sender']['retransmits']}</td>
                    </tr>
                </tbody>
            </table>

            <table id="tcp-receive">
                <thead>
                    <tr>
                        <th colspan="4">RECEBIMENTO DE DADOS TCP</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th>Bytes Recebidos</th>
                        <th>Tempo total (s)</th>
                        <th>Bits por segundo (média)</th>
                        <th>Reenvios</th>
                    </tr>
                    <tr>
                        <td>{results['TCP_RECEIVE']['end']['streams'][0]['sender']['bytes']}</td>
                        <td>{results['TCP_RECEIVE']['end']['streams'][0]['sender']['seconds']}</td>
                        <td>{results['TCP_RECEIVE']['end']['streams'][0]['sender']['bits_per_second']}</td>
                        <td>{results['TCP_RECEIVE']['end']['streams'][0]['sender']['retransmits']}</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="table-container">
            <table id="udp-send">
                <thead>
                    <tr>
                        <th colspan="7">ENVIO DE DADOS UDP</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th>Bytes Enviados</th>
                        <th>Tempo total (s)</th>
                        <th>Bits por segundo (média)</th>
                        <th>Jitter (ms)</th>
                        <th>Lost packets</th>
                        <th>Packets</th>
                        <th>Lost percent</th>
                    </tr>
                    <tr>
                        <td>{results['UDP_SEND']['end']['sum']['bytes']}</td>
                        <td>{results['UDP_SEND']['end']['sum']['seconds']}</td>
                        <td>{results['UDP_SEND']['end']['sum']['bits_per_second']}</td>
                        <td>{results['UDP_SEND']['end']['sum']['jitter_ms']}</td>
                        <td>{results['UDP_SEND']['end']['sum']['lost_packets']}</td>
                        <td>{results['UDP_SEND']['end']['sum']['packets']}</td>
                        <td>{results['UDP_SEND']['end']['sum']['lost_percent']}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        
        <div class="table-container">
            <table id="udp-receive">
                <thead>
                    <tr>
                        <th colspan="7">RECEBIMENTO DE DADOS UDP</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th>Bytes Recebidos</th>
                        <th>Tempo total (s)</th>
                        <th>Bits por segundo (média)</th>
                        <th>Jitter (ms)</th>
                        <th>Lost packets</th>
                        <th>Packets</th>
                        <th>Lost percent</th>
                    </tr>
                    <tr>
                        <td>{results['UDP_RECEIVE']['end']['sum']['bytes']}</td>
                        <td>{results['UDP_RECEIVE']['end']['sum']['seconds']}</td>
                        <td>{results['UDP_RECEIVE']['end']['sum']['bits_per_second']}</td>
                        <td>{results['UDP_RECEIVE']['end']['sum']['jitter_ms']}</td>
                        <td>{results['UDP_RECEIVE']['end']['sum']['lost_packets']}</td>
                        <td>{results['UDP_RECEIVE']['end']['sum']['packets']}</td>
                        <td>{results['UDP_RECEIVE']['end']['sum']['lost_percent']}</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <img src="cid:graph" width="1200">

    </body>
    </html> """

    return email_body


if __name__ == '__main__':
    import json

    with open('results.json', 'r') as json_file:
        results = json.load(json_file)

    print(to_html(results))
