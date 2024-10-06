import json

print('...............python object to json string.................')
py_person = {
    'name': 'Hasan',
    'age': 23,
    'city': 'Khulna',
    'language': ['Bangla', 'Arabic', 'English']
}

jsonObj = json.dumps(py_person, indent = 4)  # indent=4 for formate json data
print(jsonObj)
print(py_person['name'])

print('...............json string to python object.................')
jsonPerson = '''{
    "name": "Hasan",
    "age": 23,
    "city": "Khulna",
    "language": ["Bangla", "Arabic", "English"]
}'''

pythonObj = json.loads(jsonPerson)
print(pythonObj)
print(pythonObj['language'])


