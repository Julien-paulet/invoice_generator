import json

def read_json():
    with open("./sources/json/facture_data.json", 'r', encoding='utf-8') as file:
        return json.load(file)