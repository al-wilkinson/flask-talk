import requests

def get_mi_token():
    url = "http://169.254.169.254/metadata/identity/oauth2/token"
    headers = {
        "Metadata": "true"
    }
    params = {
        "api-version": "2018-02-01",
        "resource": "https://vault.azure.net"
    }

    try:
        # Make the GET request
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse and print the JSON response
        token_response = response.json()
        #print("Access Token:", token_response.get("access_token"))
        return token_response.get("access_token")

    except requests.exceptions.RequestException as e:
        return(f"Something suboptimal happened: {e}")

if __name__ == "__main__":
    print(get_mi_token())

