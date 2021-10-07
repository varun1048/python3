from termcolor import colored
import os
    
def color(color)->str:
    return colored("#", color)


class Board:

    def __init__(self,players) -> None:
        self.colros = ""
        self.players = players
        
    
    def mini_display(self):
        # os.system('cls')
        print()

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
    
    def print_color(self,d,i,j) -> True:
        for p in self.players:
            if (p.position['x'] == i and p.position['y'] == j) and p.direction == d:
                self.colros= color(p.color )
                return True
        return False




    def display(self):
        print()
        os.system('cls')
        
        # east, west, north, south 

        row = 3
        column = 6

        d = 'N'
        for i in range(1,column+1):
            print()
            print("\t"*7,end="  ")
            for j in range(1,row+1):
                print(" ",end="")
                if self.print_color(d,i,j):                    
                    C =self.colros  
                    print(f"|__{C}__|",end=" ")
                else:
                    print(f"|_{d}-{i}{j}|",end=" ")
                    # print(f"|_|",end=" ")
                    # print()
                    

        print("\n"*2)


        d = ['W','E']
        for i in range(1,4):
            print("\t\t",end="")

            for we in d:
                for j in range(1,7):
                    print("",end=" ")
                    if self.print_color(we,i,j):                    
                        C =self.colros  
                        print(f"|__{C}__|",end=" ")
                    else:
                        print(f"|{we}({i}{j})|",end=" ")
                # print(f"|_____|",end=" ")
                print("\t\t",end="")

            print()

        print()






        d = 'S'
        for i in range(1,column+1):
            print()
            print("\t"*7,end="    ")
            for j in range(1,row+1):
                print(" ",end="")
                if self.print_color(d,i,j):                    
                    C =self.colros  
                    print(f"|__{C}__|",end=" ")
                else:
                    print(f"|_{d}-{i}{j}|",end=" ")
                
                



# # grey
# # red
# # green
# # yellow
# # blue
# # magenta
# # cyan
# # white