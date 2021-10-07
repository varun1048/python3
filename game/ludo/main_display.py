from termcolor import colored
import os
    
def color(color)->str:
    return colored("#", color)


class Board:

    def __init__(self,players) -> None:
        self.colros = ""
        self.players = players
        
    
    def mini_display(self):
        os.system('cls')
        for player in self.players:
            print(f"""{player.name}  {player.color} {player.position}""")

    def top_line(self,top):
        line = ""
        conter = 0
        
        for _ in range(top):
            conter += 1            
            if   conter == 8:
                line +=" "           
                conter = 0
            else:
                line +="_"           
        print(line)
    
    def print_color(self,i,j) -> True:
        for p in self.players:
            if p.position['x'] == i and p.position['y'] == j:
                self.colros= color(p.color )
                return True
        return False

    def display(self,direction)->str:
        
        # east west, 
        # top= 23
        # row = 3
        # column =6
       
        # north, south 
        top= 47
        row = 6
        column = 3
        
        # if direction =="East" or direction =="West":
        #     top= 47
        #     row = 6
        #     column = 3
        

        # self.top_line(top)
        print()
        for i in range(1,column+1):
            for j in range(1,row+1):
                print(" ",end="")
                if self.print_color(i,j):                    
                    C =self.colros  
                    print(f"|__{C}__|",end=" ")
                else:
                    print(f"|__{i}{j}_|",end=" ")
                    # print(f"|_____|",end=" ")
            print()


# grey
# red
# green
# yellow
# blue
# magenta
# cyan
# white