class Player():
    def __init__(self,info):
        self.name = info['name']
        self.color = info['color']
        self.points= info['points']
        self.coins= info['coins']

    def info(self):
            return f"""
    Name    :{self.name}
    Color   :{self.color}
    Points  :{self.points}
    Ciubs   :{self.coins} 
        """

