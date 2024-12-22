from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

# Hard code for dev figuring out
KVUri = f"https://kvt-demo-01.vault.azure.net/"
secretName = "SuperSecret"

def get_kvt_secret(KVUri, secretName):
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KVUri, credential=credential)

    print(f"Retrieving secret from key vault...")
    try:
        retrieved_secret = client.get_secret(secretName)
        # print(f"The secret is {retrieved_secret.value}")
        return retrieved_secret.value
    except Exception as e:
        print(f"Something suboptimal happened: {e}")   

if __name__ == "__main__":
    print(get_kvt_secret(KVUri, secretName)) 