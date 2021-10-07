from  main_display import Board 
from time import sleep
from random import randint

class Lodu():
    def __init__(self,plaryes):
        self.plaryes= plaryes
        self.board = Board(plaryes)
    
    def dice(self) ->int:
        return randint(1,7)
    
    def moveing(self):
        
        dice = self.dice()
        # dice = 2

        if int(self.plaryes[0].position['y']) > dice  :
            new_y = ( self.plaryes[0].position['y'] + dice ) - 6
            new_x = self.plaryes[0].position['x'] + 1 
            
            if new_y == 0:
                new_y = 1
                print("net set")
            if new_x == 3:
                new_x = 1
                print("net set")



            self.plaryes[0].position ={
                'x': new_y,
                'y':new_y
                }
        else:
            self.plaryes[0].position['y'] = self.plaryes[0].position['y'] + dice




    def start(self):


        while True:
            self.board.mini_display()
            self.board.display('north')
            # while True:
            sleep(2)
            self.moveing()
            self.board.mini_display()
            self.board.display('north')
        
