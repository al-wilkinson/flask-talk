#!/usr/bin/env python3

from fake_data import generate_test_data
from flask import Flask

app = Flask(__name__)

def find_person(xnumber):
    return test_data[xnumber]

test_data = generate_test_data(10)
for person in test_data:
    print(f"{person} {test_data[person]}")

print(find_person("x2950000"))    

@app.route('/get-all', methods=['GET'])
def get_all():
    return test_data    
    
if __name__ == '__main__':
    app.run(debug=True)