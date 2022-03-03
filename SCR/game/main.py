import sys
import dice
import menu

def main():
    x = False
    while not x:
        create_menu = menu.Menu()
        create_menu.welcome()
        create_menu.game_menu()
        decision = int(input("Choice: "))
        if decision == 5:
            create_menu.rules()
        elif decision == 6:
            x = True

if __name__ == "__main__":
    # Call the main function.
    main()