import json

# Reading JSON with the loads() function
string_of_json_data = '{"name": "Zophie", "isCat": true,' \
    ' "miceCaught": 0, "felineIQ": null}'
json_data_as_python_value = json.loads(string_of_json_data)
print(json_data_as_python_value)

# Writing JSON with the dumps() function
python_value = {
    'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
string_of_json_data = json.dumps(python_value)
print(string_of_json_data)
