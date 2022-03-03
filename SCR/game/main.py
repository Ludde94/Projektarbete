import sys
import dice
import menu

def main():
<<<<<<< HEAD
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
=======
    #create_menu = menu.Menu()
    #create_menu.welcome()
    #create_menu.game_menu()
    
    x= dice.Dice()
    x.roll
    x.get_value
    print(x.sum_rolls)#testar
    
>>>>>>> 17c33c298d00ba559fd53c1ca6d52cba40ea40bc


    
    
if __name__ == "__main__":
    # Call the main function.
    main()