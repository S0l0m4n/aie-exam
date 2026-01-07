#!/bin/python3
# Fetch the CSV data and return the array of names sorted alphabetically
#
# ATTENTION: The code is written in Python as I don't know PHP and it was not
# mentioned that we should study it in the exam study kit.

import requests

URL = "https://coderbyte.com/api/challenges/logs/user-info-csv"

response = requests.get(URL)

# 0. data is a list in the form:
#   'Name,Email,Phone\n(first person))\n(second person)\n...'
csv_data = response.text

# 1. split the data based on '\n'
L = csv_data.split('\n')

# 2. first entry is the keys (Name,Email,Phone), remaining entry is the data
N, E, P = L[0].split(',')
values_list = L[1:]

# 3. each value is in the form 'Harry Potter,harrypotter@gmail.com,123-4567'
# we need to split on the comma and build the dictionary of JSON objects
json_data = []
for entry in values_list:
    name, email, phone = entry.split(',')
    json_data.append({N: name, E: email, P: phone})

# 4. sort the data
json_data.sort(key=lambda x: x['Name'])

# 5. get the names only
names = [ x['Name'] for x in json_data ]

# 6. print result
print(names)
