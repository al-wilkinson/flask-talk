# Managed Identities - under the hood
### A basic Flask API for an Azure Managed Identity talk

This repo, together with the Terraform AWS EC2 deployment here - https://github.com/al-wilkinson/flask-talk-vm - contain all the code for the demo part of a talk I am presenting a deeper dive into Azure Managed Identies.

### Prerequesites
* An Azure subscription
* The Azure CLI installed and authenticated with an account with at least Contributor privileges to the above subscription.
* I have pre-configured an Azure Key Vault storing a secret.  For the demo, the key vault and secret name are hardcoded in the kvt.py module.
* Though not required to deploy the Azure Web App, Python 3 and Pip are required to run the flask app locally.
* Again though not strictly required, access to a Postman instance makes things easier.

The code will deploy a basic API written using the Python Flask framework to an Azure Web App.  The web app will interact with an Azure Key Vault to retrieve a secret, using a Managed Identity for authentication.  The fake_data.py module creates some fake test data so that our API endpoints return something.

### Walkthrough
Clone the repo locally:<br>
```git clone https://github.com/al-wilkinson/flask-talk.git```

Authenticate an Azure CLI session with ```az login```.  If you have more than one Azure subscription check you have selected the one you wish to deploy into as default with ```az account list --output table```.  Use ```az account set --name "your subscription name"``` if needed.

Make sure that ```flask-talk``` is your current directory, cd into it if not and deploy the Azure Web App with:<br>```az webapp up --runtime PYTHON:3.12 --sku B1 --logs --resource-group rg-webapp-demo --name webapp-demo-e4f51d47f18a4aae8366b7cd56e6756a```<br>
The Web App name must be globally unique.  Note that we have not assigned either a system or user Managed Identity at this point.

When the web app has deployed test a couple of API endpoints.  There are some "dev" ones in the code.

https://webapp-demo-e4f51d47f18a4aae8366b7cd56e6756a.azurewebsites.net/get-all

https://webapp-demo-e4f51d47f18a4aae8366b7cd56e6756a.azurewebsites.net/get-person/x2949994

There are also endpoints that will retrieve the secret from the key vault (a pattern common to a production API, though presenting the secret to a GET request would not really be optimal).

Try these now, before we have assigned a managed identity to the web app.

https://webapp-demo-e4f51d47f18a4aae8366b7cd56e6756a.azurewebsites.net/get-secret

https://webapp-demo-e4f51d47f18a4aae8366b7cd56e6756a.azurewebsites.net/get-mi-token

