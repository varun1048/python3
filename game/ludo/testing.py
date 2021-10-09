class Test_cases:
    def __init__(self,direction,position,dice,output) -> None:
        self.direction = direction
        self.position =position
        self.dice =dice
        self.output =output
        self.yourout = {}
        def __repr__(self):
            return f"""Player object Name:{self.name} Color:{self.color}"""

        def __str__(self):
            return self.__repr__()
def test():
    test1 = Test_cases()
    
    print("varun")