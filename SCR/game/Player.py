class player():
    """"creating player object"""
    def __init__(self):
        self.player = player

    """"creating player with user input"""
    def player(self):
        input('Name of player: ')
        return self
    
    def keep_rolling(self):
        """Decision for keep rolling"""
        print("Press 1 - Roll again, 2 - Hold?")
        decision = int(input(" "))
        return decision
