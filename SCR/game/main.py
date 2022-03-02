import sys
import dice
import menu
    
def main():
    create_menu = menu.Menu()
    create_menu.welcome()
    create_menu.game_menu()

if __name__ == "__main__":
    # Call the main function.
    main()