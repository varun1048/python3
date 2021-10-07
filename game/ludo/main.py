from os import error
from ludo_layout import Lodu
from player_info import Player
import players

def main():  
    plaryes = []
    plaryes.append(Player(players.varun))
    
    ludo_game = Lodu(plaryes)
    ludo_game.start()  




def test():

    varun = Player(players.varun)
    x , y = 3,5
    dice = 1
    varun.position = {'x': x, 'y': y}
    print(varun.position)

    if int(varun.position['y']) > dice  :
        new_y = ( varun.position['y'] + dice ) - 6
        new_x = varun.position['x'] + 1 
        
        if new_y == 0:
            new_y = 1
            print("net set")
        if new_x == 3:
            new_x = 1
            print("net set")



        varun.position ={
            'x': new_y,
            'y':new_y
            }
    else:
        varun.position['y'] = varun.position['y'] + dice

    print(varun.position)





if __name__ == '__main__':
    import os
    os.system('cls')
    # test()
    main()
    print()