import azure.cosmos.cosmos_client as cosmos_client
from flask import Flask, jsonify





app = Flask(__name__)
@app.route("/")
def get():
        config = {
            'ENDPOINT': 'https://hackny2.documents.azure.com:443/',
            'PRIMARYKEY': 'uDB7OOzZ4QYeDOlVMd4TCRKKyFKM8tc0i53CaVhD4ydDLkrdFcigqwMXNk7POme00MqpBH5sHBStEhv0EgW8Dw==',
            'DATABASE': 'CosmosDatabase',
            'CONTAINER': 'CosmosContainer'
        }

        # Initialize the Cosmos client
        client = cosmos_client.CosmosClient(url_connection=config['ENDPOINT'], auth={
                                            'masterKey': config['PRIMARYKEY']})


        # Create a database

        result_iterable = client.ReadContainers('dbs/hackny2')
        for item in iter(result_iterable):
            return jsonify(item)
        return result_iterable[0]



if __name__ == '__main__':
    app.run(debug=True)
