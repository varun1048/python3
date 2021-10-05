from ludo_layout import Lodu
from player_info import Player
import players

def main():
    varun = Player(players.varun)
    saravana = Player(players.saravana)
    
    plaryes = [varun,saravana]
    
    ludo_game = Lodu(plaryes)
    ludo_game.start()  

if __name__ == '__main__':
    import os
    os.system('cls')

    main()
    print()