from time import sleep
from random import randint

from  main_display import Board 
from positions import position_all

class Lodu():

    def __init__(self,players):
        self.players= players
        self.board = Board(players)   

        self.findout = []
    
    def dice(self) ->int:
        return randint(1,7)
    


    def move(self,player):

        for player_input in self.players:
            if player_input.name ==  player["name"]:
                index = self.players.index(player_input)
                # self.players[index].name = "gaundu"
                print()
                # print(self.players[index].position[player['coin']])
                try:
                    
                    index_chane = position_all.index(self.players[index].position[player['coin']]) + player['dice']
                    # print(position_all[34])

                    try: 
                        self.players[index].position[player['coin']]  = position_all[index_chane]
                        self.findout.append(self.players[index].position[player['coin']])

                    except    IndexError:
                        # print( self.players[index].position[player['coin']] )
                        print("ads")
                        self.players[index].position[player['coin']] = position_all[player['dice']-1]

                except ValueError:
                    print("list len",len(position_all))
                    print("not in list bro",index_chane)   


    
    def player_input(self) ->dict:
        return {
            'name':"Antony",
            'coin':2,
            'dice':1
        }


    def start(self):

        import os
        os.system("cls")
        # self.board.display()
        self.board.mini_display()
        print(self.player_input())
        self.move(self.player_input())
        # sleep(2)
        
        # self.board.display()
        for x in self.findout:
            print(x)
        self.board.mini_display()

        def loop():
            while True:
                self.board.display()
                sleep(3.5)
                self.move()
                self.board.display()


        # loop()

