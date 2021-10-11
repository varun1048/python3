class Player():
    def __init__(self,info):
        self.name = info['name']
        self.color = info['color']

        # self.direction = info["direction"]
        self.position= info['position']
        self.coins=  len(info['position'])
        self.points= info['points']
        self.staring_direction = info["staring_direction"]


    def info(self):
        return f"""
    Name    :{self.name}
    Color   :{self.color}
    Points  :{self.points}
    Coins   :{self.coins} 
            """

    def __repr__(self):
        return f"""Player object Name:{self.name} Color:{self.color}"""

    def __str__(self):
        return self.__repr__()