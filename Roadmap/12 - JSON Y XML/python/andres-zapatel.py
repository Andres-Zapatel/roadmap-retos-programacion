import xml.etree.ElementTree as xml
import os
import json

data = {
    "name": "Andres Zapatel",
    "age": 33,
    "birth_date": "21-08-1992",
    "programming_languages": ["Python", "Json", "XML", "JavaScript"]
}

xml_file = "andres.xml"
json_file = "andres.json"

#XML

def save_xml():

    root = xml.Element("data")

    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "Language").text = item
        else:
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(xml_file)

save_xml()

with open(xml_file) as xml_data:
    print(xml_data.read())

os.remove(xml_file)

#JSON

with open(json_file, "w") as json_data:
    json.dump(data, json_data)

with open(json_file, "r") as json_data:
    print(json_data.read())

os.remove(json_file)