import random 
num = random.randint(0,11)

while True:
    innner = input("Guess a number between 1 and 10 :")
    if( int(innner) == num):
        print("................You guessed it ypu won")
        p = input("do want to play (y,n) :")    
        if(p == 'n'):
            print("Thanks for playing . Bye :)")
            break
        else:
            num = random.randint(0,11)            
    else:
        if(num<num):
            print("Too high ,try again")
        else:
            print("Too low ,try again")
        
