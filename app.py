from fake_data import generate_test_data
from kvt import get_kvt_secret
from flask import Flask, jsonify
from mi_token import get_mi_token, get_env_var

app = Flask(__name__)

KVUri = f"https://kvt-demo-01.vault.azure.net/"
secretName = "SuperSecret"

test_data = generate_test_data(10)
for person in test_data:
    print(f"{person} {test_data[person]}") 

@app.route('/get-person/<string:xnumber>', methods=['GET'])
def get_person(xnumber):
    try:
        return test_data[xnumber]
    except:
        print("Person not found")
        return jsonify(message="Person not found."), 404

@app.route('/get-all', methods=['GET'])
def get_all():
    return test_data   

@app.route('/get-secret', methods=['GET']) 
def get_secret():
    return get_kvt_secret(KVUri, secretName)

@app.route('/get-mi-token', methods=['GET'])
def get_token():
    return get_mi_token()

@app.route('/get-env-var', methods=['GET'])
def get_var():
    return get_env_var()
    
if __name__ == '__main__':
    app.run(debug=True)