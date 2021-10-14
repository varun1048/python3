from termcolor import colored
import os    

def color(color)->str:
    return colored("#", color)
class Board:

    def __init__(self,players) -> None:
        self.colros = ""
        self.players = players

        self.debug = []
        
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
    def Nums_coins(self,d,i,j) ->str:
        temp = {
            "swith":False,
            "value": "",
            "color":""
        }

        
        output = f"\t\t"
        for player in self.players:

            if (i == 1 and j == 6) and d == 'W':
                if player.staring_direction == "N":
                    coloring = colored("#",player.color)
                    output = f"\t{coloring} {player.coins}\t"

            if (i == 2 and j == 6) and d == 'W':

                if player.staring_direction == "W":
                    temp["swith"] = True
                    temp["value"] =  player.coins
                    temp["color"] =  player.color

            if (i == 2 and j == 6) and d == 'W':
                # self.debug.append(player.staring_direction)
                if player.staring_direction == "E" and  temp["swith"] :
                        coloring = colored("#",player.color)
                        coloring_w = colored("#",temp['color'])
                        return f"    {coloring_w}{temp['value']}     {coloring}{player.coins}\t"

                elif not player.staring_direction == "E" and  temp["swith"] :
                        coloring = colored("#",temp['color'])
                        output =  f"{coloring}{temp['value']}\t\t"
                
                elif player.staring_direction == "E" and not temp["swith"] :
                        coloring = colored("#",player.color)
                        output =  f"\t\t{coloring}{player.coins}"          

            if (i == 3 and j == 6) and d == 'W':
                if player.staring_direction == "S":
                    coloring = colored("#",player.color)
                    output = f"\t{coloring}{player.coins}\t"

        return output 

    
    def print_color(self,direction,i,j) -> True:
        for player in self.players:
            for positions in player.position:
                if (positions['x'] == i and positions['y'] == j) and (positions['direction'] == direction):
                    # self.colros = colored(f"#{ player.position.index(positions)+1}", player.color)  
                    temp = player.position.index(positions)
                    self.colros = colored(f"#{ player.position[temp]['name']}", player.color)  
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
            print("\t"*7,end="")
            for j in range(1,4):
                print(" ",end="")
                if self.print_color(d,j,i):                    
                    C =self.colros  
                    print(f"|__{C}__|",end=" ")
                else:
                    print(f"|_{d}-{j}{i}_|",end=" ")
                    # print(f"|_|",end=" ")
                    # print()
                    

        print("\n"*2)


        d = ['W','E']
        for i in range(1,4):
            print(" ",end="")
            for we in d:
                for j in range(1,7):
                    print("",end=" ")
                    if self.print_color(we,i,j):                    
                        C =self.colros  
                        print(f"|__{C}__|",end=" ")
                    else:
                        print(f"|{we}({i}{j})|",end=" ")
                print(f"\t{self.Nums_coins(we,i,j)} \t",end="")
            print()
        print()






        d = 'S'
        for i in range(1,7):
            print()
            print("\t"*7,end="")
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