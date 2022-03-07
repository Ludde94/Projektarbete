class Player():
    """"creating player object"""
    def __init__(self):
        self.player

    """"creating player with user input"""
    def player(self):
        name = input('Name of player: ')
        return name

    def keep_rolling(self):
        """Decision for keep rolling"""
        print("Press 1 - Roll again, 2 - Hold?")
        decision = int(input(" "))
        return decision
