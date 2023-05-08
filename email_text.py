import json


with open('results.json', 'r') as json_file:
    results = json.load(json_file)

html_format = f""" <!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gráficos</title>
</head>
<body>
    <table border="1px solid" cellspacing="0.1" border-collapse="collapse">
        <thead>
            <tr>
                <th colspan="3">ENVIO DE DADOS TCP</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th>Bytes enviados</th>
                <th>Tempo total (s)</th>
                <th>Bits por segundo (média)</th>
            </tr>
            <tr>
                <td>{results['TCP_SEND']['end']['streams'][0]['sender']['bytes']}</td>
                <td>{results['TCP_SEND']['end']['streams'][0]['sender']['seconds']}</td>
                <td>{results['TCP_SEND']['end']['streams'][0]['sender']['bits_per_second']}</td>
            </tr>
        </tbody>
</table>

    <img src="cid:graph" width="1000">
</body>
</html> """
