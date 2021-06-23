from math import tan
import random 
import os
table  = 3
limit = 60

numbers = [x for x in range(0,(table*limit)+table,table)][1:]
os.system("cls")
while True:
    num  = random.choice( numbers )
    inner = input(str( int(num/table) )+" x "+ str(table) +" = ")
    if num != int(inner):
        print("------"+str(num))
    else:
        os.system("cls")
    