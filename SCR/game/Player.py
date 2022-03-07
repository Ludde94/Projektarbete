class Player():
    """"creating player object"""
    def __init__(self):
        self.player
        self.keep_rolling

    """"creating player with user input"""
    def player(self):
        names = []
        name = input('Name of player: ')
        names.append(name)
        return name, names
    
    
    def keep_rolling(self):
        """Decision for keep rolling"""
        print("Press 1 - Roll again, 2 - Hold?")
        decision = int(input(" "))
        return decision
