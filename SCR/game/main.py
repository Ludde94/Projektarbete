from menu import Menu
from player import Player
from sys import exit
#from dice import Dice

def main():
   menu = Menu()
   choice = menu.welcome()
   if choice:
      player_name = menu.set_name()
   player = Player(player_name)
   game_menu_choice = menu.game_menu()
   while True:
      if game_menu_choice == "5":
         exit()
      elif game_menu_choice == "4":
         if menu.rules():
            game_menu_choice = menu.game_menu()
      elif game_menu_choice == "3":
         pass
      elif game_menu_choice == "2":
         print("Select a new name\n\nTo keep your name press enter without any text.\n")
         name = input("Enter your new name: ").strip()
         if name == "":
            print(f'\nWe keep your name {player.name}')
            game_menu_choice = menu.game_menu()
         else:
            player.changename(name)
            print(f'\nWe have changed your name to: {player.name}')
            game_menu_choice = menu.game_menu()
      elif game_menu_choice == "1"  
         pass
   
      
   
      
      
   
   

if __name__ == "__main__":
    # Call the main function.
    main()
