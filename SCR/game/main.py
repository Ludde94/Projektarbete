import sys
import dice
import menu

def main():
    create_menu = menu.Menu()
    die = dice.Dice()
    print(die.roll())
    print(die.get_rolls_made())
    print(die.get_sum_rolls())

if __name__ == "__main__":
    # Call the main function.
    main()
