from termcolor import colored
import os
    
def color(color)->str:
    return colored("#", color)
    # return "#"


class Board:

    def __init__(self,players) -> None:
        self.colros = ""
        self.players = players
        
    def mini_display(self):
        print()
        # os.system('cls')

        for player in self.players:
            print(f""" {player.name}\t\t   { color(player.color) }  coins:{player.coins}  """,end=" ")
            for positions in player.position:
                print(f"""positions:{positions["direction"]}-{positions["x"]}-{positions["y"]} """,end=" ")
            print()


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
    
    def print_color(self,direction,i,j) -> True:
        for player in self.players:
            for positions in player.position:
                if (positions['x'] == i and positions['y'] == j) and (positions['direction'] == direction):
                    # self.colros= color(player.color)  
                    self.colros= colored(f"#{ player.position.index(positions)+1}", player.color)  
                    return True
        else: 
            return False




    def display(self):
        print()
        os.system('cls')
        self.mini_display()

        d = 'N'
        for i in range(1,7):
            print()
            print("\t"*7,end="  ")
            for j in range(1,4):
                print(" ",end="")
                if self.print_color(d,j,i):                    
                    C =self.colros  
                    print(f"|__{C}__|",end=" ")
                else:
                    print(f"|_{d}-{j}{i}|",end=" ")
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
        for i in range(1,7):
            print()
            print("\t"*7,end="    ")
            for j in range(1,4):
                print(" ",end="")
                if self.print_color(d,j,i):                    
                    C =self.colros  
                    print(f"|__{C}__|",end=" ")
                else:
                    print(f"|_{d}-{j}{i}|",end=" ")

        print()                
                



# # grey
# # red
# # green
# # yellow
# # blue
# # magenta
# # cyan
# # white