class Menu():
    """Menu class"""
    def __init__(self):
        pass

    def welcome(self):
        """Welcome message"""
        print("*" * 50)
        print("Welcome to Pig Dice!" .center(50))
        print("Press Enter to start game." .center(50))
        print("*" * 50)
        while True:
            input(">> ")
            return True
        
    def set_name(self):
        """Set name on player"""
        #print("*" * 50)
        while True:
            name = input("Enter your name: ").strip()
            if name == "":
                print("Wrong! Please enter a valid name.")
            else:
                print(f'Welcome to the game {name}')
                return name
                

    def game_menu(self):
        """menu"""
        print("*" * 50)
        print("Here are your game menu: ".center(50))
        print("1. Start new game".center(50))
        print("2. Change existing player name".center(50))
        print("3. Show highscore".center(50))
        print("4. Show rules of the game".center(50))
        print("5.Quit game".center(50))
        print("*" * 50)
        while True:
            user = input(">> ")
            if user in ["1","2","3","4","5"]:
                return user


    def rules(self):
        """rules of the game"""
        print("*" * 100)
        print("* The objective of the game is to be the first one to reach 100 points".center(30))
        print("* Each turn, a player will roll a die".center(30))
        print("* until either a 1 is rolled or the player decides to hold".center(30))
        print("* If the player rolls any other number,".center(30))
        print("it is added to their turn total and the player's turn continues".center(30))
        print("* If a player chooses to hold, their turn total is added to their score".center(30))
        print("* and it becomes the next player's turn".center(30))
        print("*" * 100)
        while True:
            input("Press enter to return to menu")
            return True 
