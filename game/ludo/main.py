from ludo_layout import Lodu
from player_info import Player

import players

def main():  
    plaryes = []

    plaryes.append(Player(players.varun))
    plaryes.append(Player(players.antony))
    
    ludo_game = Lodu(plaryes)
    ludo_game.start()  




def test():
    pass


if __name__ == '__main__':
    import os
    os.system('cls')
    
    main()