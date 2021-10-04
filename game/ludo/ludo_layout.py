from  player_info import Player as Player_info 

class Lodu(Player_info):
    def __init__(self,player):
        Player_info .__init__(self,player)

    def player_points(self):
        return Player_info.info(self)
    
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
    
    def Main_display(self,direction,boolean,x,y)->str:
        # east west, north, south 
        top= 23
        row = 3
        column =6
        if direction =="East" or direction =="West":
            top= 47
            row = 6
            column = 3
        self.top_line(top)

        for i in range(1,column+1):
            for j in range(1,row+1):
                if x == i and y == j:
                    print("|__#__|",end=" ")
                else:
                    print("|_____|",end=" ")
            print()

    def logic(self) ->None:

        self.Main_display('North',False,2,2)
        self.Main_display('East',False,3,1)
