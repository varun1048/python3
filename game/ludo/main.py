from ludo_layout import Lodu
from player_info import Player

import players

def main():  
    plaryes = []

    plaryes.append(Player(players.varun))
    plaryes.append(Player(players.sarana))
    plaryes.append(Player(players.antony))
    plaryes.append(Player(players.sam))
 
    ludo_game = Lodu(plaryes)
    ludo_game.start()  

if __name__ == '__main__':  
    main()
