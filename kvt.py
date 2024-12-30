from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from flask import jsonify

# Hard code for dev figuring out
KVUri = f"https://kvt-demo-01.vault.azure.net/"
secretName = "SuperSecret"

def get_kvt_secret(KVUri, secretName):
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KVUri, credential=credential)

    print(f"Retrieving secret from key vault...")
    try:
        retrieved_secret = client.get_secret(secretName)
        return jsonify(message=retrieved_secret.value), 200
    except Exception as e:
        #return f"Something suboptimal happened: {e}" 
        return jsonify(message="Something suboptimal happened."), 404

if __name__ == "__main__":
    print(get_kvt_secret(KVUri, secretName)) 