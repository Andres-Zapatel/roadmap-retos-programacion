import os

"""
EJERCICIO
"""

file_name = "andres.txt"

with open(file_name, "w") as file:
    file.write("Andres Zapatel\n")
    file.write("36\n")
    file.write("Python\n")


#with open(file_name, "r") as file:
#    print(file.read())

os.remove(file_name)