from fake_data import generate_test_data
from kvt import get_kvt_secret
from flask import Flask
from flask_smorest import abort
from mi_token import get_mi_token, get_env_var

app = Flask(__name__)

KVUri = f"https://kvt-demo-01.vault.azure.net/"
secretName = "SuperSecret"

def find_person(xnumber):
    return test_data[xnumber]

test_data = generate_test_data(10)
for person in test_data:
    print(f"{person} {test_data[person]}")

print(find_person("x2950000"))  

@app.route('/get-person/<string:xnumber>', methods=['GET'])
def get_person(xnumber):
    try:
        return test_data[xnumber]
    except:
        print("Person not found")
        abort(404, message="Person not found")

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