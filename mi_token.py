import requests
import os
from flask import jsonify

def get_env_vars():
    try:
        identityHeader = os.environ["IDENTITY_HEADER"]
        identityEndpoint = os.environ["IDENTITY_ENDPOINT"]
        envVars = {
            "X-IDENTITY-HEADER": identityHeader,
            "X-IDENTITY-ENDPOINT": identityEndpoint
        }
        #return jsonify(message=os.environ["IDENTITY_HEADER"]), 200
        #return jsonify(message=os.environ["IDENTITY_ENDPOINT"]), 200
        return envVars
    except:
        # returnVar = {"message": "No environment variables?"}
        # return returnVar
        return jsonify(message="No environment variables?"), 404
    

def get_mi_token():
    params = {
        "api-version": "2019-08-01",
        "resource": "https://vault.azure.net"
    }

    try:
        # all the os.environ calls need to be within error checking
        url = os.environ["IDENTITY_ENDPOINT"]
        headers = {
        "X-IDENTITY-HEADER": os.environ["IDENTITY_HEADER"]
    }
        # Make the GET request
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad status codes


        # Parse and print the JSON response
        token_response = response.json()
        # print("Access Token:", token_response.get("access_token"))
        return jsonify(message=token_response.get("access_token")), 200

    except:
        return jsonify(message="Something suboptimal happened. Have you configured the Managed Identity?"), 403

if __name__ == "__main__":
    #print(get_mi_token())
    print(get_env_vars())

