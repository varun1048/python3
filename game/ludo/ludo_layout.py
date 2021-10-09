from time import sleep
from random import randint

from  main_display import Board 
from positions import position_all

class Lodu():
    def __init__(self,plaryes):
        self.plaryes= plaryes
        self.board = Board(plaryes)
        
    
    
    def dice(self) ->int:
        return randint(1,7)
        return 6

    def moveing(self,dice):
        for test in self.plaryes:
            try:
                index = position_all.index(test.position) +dice
                try: 
                    test.yourout = position_all[index]
                except    IndexError:
                    test.yourout = position_all[dice-1]
            except ValueError:
                print("not in list bro")
    


    def start(self):
        # self.board.display()
        # self.board.mini_display()
        self.board.display()
        self.moveing(2)#
        sleep(2.5)  
        self.board.display()

        # self.board.mini_display()


        def loop():
            while True:
                print(self.test_case)
                self.board.display()
                self.board.mini_display()
                sleep(3.5)
                self.moveing()
                self.board.mini_display()
            # self.board.display('north')
        # loop()













    
    # def moveing(self):
        
    #     dice = self.dice()
    #     direction = ['w','N','E','S']
    #     dice = 1

    #     if int(self.plaryes[0].position['y']) < dice  :
    #         # print(self.plaryes[0].position['y'] )
    #         new_y = ( self.plaryes[0].position['y'] + dice ) - 6
    #         new_x = self.plaryes[0].position['x'] + 1 

    #         self.test_case.append(f"dice={dice}   x={new_x}   y={new_y}")
    #         # self.test_case.append(f"af")
    #         if new_y == 0:
    #             new_y = 1
    #             print("net set")
    #         if new_x == 3:
    #             new_x = 1
    #             print("net set")



    #         self.plaryes[0].position ={
    #             'x': new_y,
    #             'y':new_y
    #             }
    #     else:
    #         self.plaryes[0].position['y'] = self.plaryes[0].position['y'] + dice


