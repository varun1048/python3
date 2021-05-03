import  requests
from random import choice

url = "https://icanhazdadjoke.com/search"
geted = requests.get(url,
    headers={"Accept":"application/json"},
    params={"term":input("Enter a world :")}
).json()
results = geted["results"]
def number_jok(num):
    if num >1:
        print("\nThere are maney joke." )
        return choice(results)['joke']
    elif num == 1:
        print("Ther  one joke only.") 
        return results["joke"]
    return  "There  are no joke."

print(number_jok(geted["total_jokes"]))