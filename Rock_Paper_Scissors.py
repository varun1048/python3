import random 

pl  = 0
c  = 0
print("\t\t\t 3 points to win")
while True:
    print(F"\t\t\tplayer :{pl} computer :{c} ")
    p1 = input("Ener Player \t:")
    p1 = str(p1)

    if p1=='r' or p1 == 's' or p1 == 'p':
        p2 = random.randint(0,2)        
        if( p2 == 0):
            p2 = 'r'
        elif( p2 == 1):
            p2 = 's'
        else:
            p2 = 'P'
        print('computer \t:'+p2)
    
        if p1 == p2 :
            print(".................tie")

        else:
            if( ( p1 == "s") and ( p2 == "p")) or (( p1 == "p") and ( p2 == "r")) or (( p1 == "r") and ( p2 == "s")):
                winner = "player wins"
                pl +=1
                print("\t........" + winner)  


            else:
                winner = "computer wins "
                c +=1
                print("\t........" + winner)  


        if (pl == 3) or (c == 3):
 
            print("\t\t\tGame Over")
            print(f"\t\t  player :{pl} computer :{c}")
            print(f" ........................{winner} hahahaha"  )  
            pl = 0
            c =3
            p = input("do want to play (y,n) :")    
            if(p == 'n'):
                print("Thanks for playing . Bye :)")
                break
 
        

    else:
        print("plese enter value s r p ")


 