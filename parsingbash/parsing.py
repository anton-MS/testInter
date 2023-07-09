import json
import csv

# JSON-код
json_data = '''
[
    {
        "ofbgazrwsq": [
            -572848284.1157659,
            "Llsv4AiIP2eT"
        ]
    },
    {
        "onkjwbuzsiiy": 128102243.05547054,
        "nkoxe": "CjJn",
        "zfuvj": true
    }
]
'''

# Разбір JSON
data = json.loads(json_data)

# Створення CSV-файла та запис даних 
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Запис заголовків
    headers = data[0].keys()
    writer.writerow(headers)
    
    # Запис значень
    for item in data:
        row = [str(item.get(header, '')) for header in headers]
        writer.writerow(row)

print("Файл збереженний як 'output.csv'.")
