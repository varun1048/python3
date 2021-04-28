s
p1 = input("Ener Player 1 \t:")
p1 = str(p1)

p2 = random.randint(0,2)


if( p2 == 0):
    p2 = 'r'
elif( p2 == 1):
    p2 = 's'
else:
    p2 = 'P'


print('computer \t:'+p2)
if p1:
    if p1 == p2 :
        print("tie..")    

    else:
        if( ( p1 == "s") and ( p2 == "p")) or (( p1 == "p") and ( p2 == "r")) or (( p1 == "r") and ( p2 == "s")):
            winner = "p1"

        else:
            winner = "computer wins hahaha"
        print("...... \t" + winner)  
else:
    print("plese enter value p1")

