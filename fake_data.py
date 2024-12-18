#!/usr/bin/env python3

from faker import Faker
import random
import string

fake = Faker()

#def generate_xnumber():
#    return f"X{random.randint(2949990, 2950000)}"

xnumbers = (
    "x2949990",
    "x2949991",
    "x2949992",
    "x2949993",
    "x2949994",
    "x2949995",
    "x2949996",
    "x2949997",
    "x2949998",
    "x2950000",
    "x2950001",
)

def generate_test_data(num_records):
    data = {}
    for _ in range(num_records):
        firstName = fake.first_name()
        lastName = fake.last_name()
        tfn = ''.join(random.choices(string.digits, k=9))
        xnumber = xnumbers[_]
        data[xnumber] = {"firstname": firstName,  "lastname": lastName, "tfn": tfn}
    return data

def find_person(xnumber):
    return test_data[xnumber]

if __name__ == "__main__":
    test_data = generate_test_data(10)
    for person in test_data:
        print(f"{person} {test_data[person]}")

    print(find_person("x2949995"))