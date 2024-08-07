import json

json_data = '{"name": "Zophie", "isCat": true, "mmiceCaught": "0", "felineIQ": null}'
print(json_data)

python_dict = json.loads(json_data)

print(f"Name: {python_dict}")