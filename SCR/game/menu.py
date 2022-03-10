class Menu:
    """Menu class"""
    def __init__(self):
        pass

    def welcome(self):
        """Welcome message"""
        print("*" * 50)
        print("""
        Welcome to Pig Dice!
        Press Enter to start game.
        """.center(50))
        print("*" * 50, "\n")

        while True:
            input(">> ")
            return True

    def set_name(self):
        """Set name on player"""
        while True:
            name = input("Enter your name: ").strip()
            if name == "":
                print("Wrong! Please enter a valid name.\n")
            else:
                print(f'Welcome to the game {name}')
                return name

    def game_menu(self):
        """menu"""
        print("*" * 50)
        print("""
        Here are your game menu:
        1. Start new game
        2. Change existing player name
        3. Show highscore
        4. Show rules of the game
        5. Quit game
        """.center(50))
        print("*" * 50)

        while True:
            user = input(">> ")
            if user in ["1", "2", "3", "4", "5"]:
                return user

    def rules(self):
        """rules of the game"""
        print("*" * 100)
        print("""
        * The objective of the game is to be the first one to reach 100 points
        * Each turn, a player will roll a die
        * until either a 1 is rolled or the player decides to hold
        * If the player rolls any other number,
        it is added to their turn total and the player's turn continues
        * If a player chooses to hold, their turn total is added to their score
        * and it becomes the next player's turn
        """.center(50))
        print("*" * 100, "\n")

        while True:
            input("Press enter to return to menu")
            return True
