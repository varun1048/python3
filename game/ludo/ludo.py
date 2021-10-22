from time import sleep
from random import randint
from termcolor import colored

from  main_display import Board 
from positions import position_all

class Lodu():

    def __init__(self,players):
        self.players= players
        self.board = Board(players)   

        self.findout_error = []
        self.current_player = ""



    def dice(self) ->int:
        return randint(1,6)
    
    def error(self):
        for x in self.findout_error:
            print(x)



    def player_input(self) ->dict:

        dice  = self.dice()
        # dice  = 1
        print("\n"*2)
        print(f"\t\t\t\t\t|\tyour dice number:",dice)
        print("\t\t\t\t\t|\t"+colored(f"{self.current_player.name}",self.current_player.color),end="'s coins are")
        print("\n",end="\t\t\t\t\t|\t")

        for coin in self.current_player.position:
            print(f'{coin["name"]}',end="\t")

        coins = []   
        for x in self.current_player.position:
            coins.append(x["name"]) 

        while True:
            self.error()
            coin = input("\n\t\t\t\t\t"+"-"*32+">")
            if coin in coins:
                break
            print("\n\t\t\t\t\t invalide input ! ")

        return {
            'coin':coin,   
            'dice':dice
        }



    def brain(self):
        data = self.player_input()
        index = 0

        for position in self.current_player.position:             
            if data['coin'] == position['name']:
                
                temp = dict(position)
                temp.pop('name')

                index_change = int(position_all.index(temp) + data['dice'])
                try:        
                    set_position =dict(position_all[index_change])
                except:
                    index_change = index_change - 52
                    set_position = dict(position_all[index_change])                
                    # sleep(20)
                temp = set_position
                temp.update({"name":data['coin']})
                self.current_player.position[index] = temp

                return None

            index += 1

        

    


    def start(self):
        def loop():
            while True:
                for player in self.players:
                    self.current_player = player
                    self.board.display()    
                    self.brain()
        loop()  


