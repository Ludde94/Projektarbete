class Player():
    """"creating player object"""
    def __init__(self):
        self.player

    """"creating player with user input"""
    def player(self):
        name = input('Name of player: ')
        return name

    def keep_rolling(self):
        decision= input("Press 1 - Roll again, 2 - Hold?", 1, 2)
        return decision
