from  main_board import Board 
from time import sleep

class Lodu():
    def __init__(self,plaryes):
        self.plaryes= plaryes
        self.board = Board(plaryes)
    
    def start(self):

        for x in range(1,6):
            for y in range(1,4):
                # sleep(0.50)
                self.plaryes[0].position = {"x":x,"y":y} 
                self.board.mini_display()
                self.board.display('east')
        
