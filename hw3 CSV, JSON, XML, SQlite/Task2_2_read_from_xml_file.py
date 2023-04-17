"""Task2
Створіть XML-файл із вкладеними елементами та скористайтеся пошуком XPATH.
Спробуйте здійснити пошук вмісту за створеним документом XML, ускладнюючи
свої запити та додаючи нові елементи, якщо буде потрібно.
"""

from xml.etree import ElementTree as ET

# Parse data from XML-file
tree = ET.parse('data/xml_students.xml')
root = tree.getroot()                       # students

# search values in the root(<students>-> <student>-> <name>, <surname>, <age>)
names = root.findall('./student/name')
surnames = root.findall('./student/surname')
ages = root.findall('./student/age')

# print students data as dicts
for values in zip(names, surnames, ages):
    row = {value.tag: value.text for value in values}
    print(row)
