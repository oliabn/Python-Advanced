"""Task1
Створіть прості словники та конвертуйте їх у JSON.
Збережіть JSON у файлі та спробуйте завантажити
дані з файлу.
"""

import json

persons = [{'name': "Kate", 'surname': 'Blackwood', 'age': 35},
        {'name': "Sergij", 'surname': 'Petrenko', 'age': 33},
        {'name': "Sato", 'surname': 'Akada', 'age': 30}]

with open('data/task1.json', 'w') as file:
    for person in persons:
        json.dump(person, file)
        file.write('\n')

with open('data/task1.json', 'r') as file:
    data = [json.loads(line) for line in file]
    print(data)
