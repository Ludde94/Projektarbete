from menu import Menu
from computer import Computer
from dice import Dice

def main():
   start_game = Menu()
   start_game.welcome()
   die = Dice()

if __name__ == "__main__":
    # Call the main function.
    main()
