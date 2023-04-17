"""Task2
Створіть XML-файл із вкладеними елементами та скористайтеся пошуком XPATH.
Спробуйте здійснити пошук вмісту за створеним документом XML, ускладнюючи
свої запити та додаючи нові елементи, якщо буде потрібно.
"""

from xml.etree import ElementTree as ET

# Students data
data = [
    {'name': "Tonny", 'surname': 'Peterson', 'age': 27},
    {'name': "Jordan", 'surname': 'Lee', 'age': 29},
    {'name': "Leslie", 'surname': 'Cheung', 'age': 37},
]

# Create xml structure with students
root = ET.Element('students')

for person in data:
    student = ET.SubElement(root, 'student')
    for key, value in person.items():
        e = ET.SubElement(student, key)
        e.text = str(value)

tree = ET.ElementTree(root)

# Write xml file with students
tree.write('data/xml_students.xml', encoding='utf-8')
