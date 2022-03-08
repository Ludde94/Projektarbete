class Player():
    """"creating player object"""
    def __init__(self, name):
        self.name = name
        

    """"creating player with user input"""
    def player(self):
        name = input('Name of player: ')
        return name
    
    def changename(self, newname):
        self.name = newname
    
    def keep_rolling(self):
        """Decision for keep rolling"""
        print("Press 1 - Roll again, 2 - Hold?")
        decision = int(input(" "))
        return decision
