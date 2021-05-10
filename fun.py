from csv import DictReader
from random import choice
with open("data.csv") as file:
    csv_reader  = DictReader(file)
    data = list(csv_reader) 
player = 1
while player:
    out = choice(data)
    name = out["author"]
    print(name)
    inner = input("Find out author name :")
    if inner == name:
        break 
    inner = input(f"author name start with {name[0]}:")

    
