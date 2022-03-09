from menu import Menu
from player import Player
from sys import exit
from computer import Computer
#from dice import Dice

def winner_winner_chicken_dinner(winner, who):

      if who == "player":
         print(f"Congratulations, you won {winner.name}")
      elif who == "computer":
         print(f"You losed against the {winner.name}.")


def main():
   winning_number = 10
   menu = Menu()
   choice = menu.welcome()
   if choice:
      player_name = menu.set_name()
   player = Player(player_name, winning_number)
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
      elif game_menu_choice == "1":
         comp = Computer(winning_number)
         turn = "player"
         while True:
            try:
               
               set_difficulty = int(input("Press 1 for easy or 2 for hard: "))
               if set_difficulty == 1:
                  comp.set_difficulty("Easy")
                  break
               elif set_difficulty == 2:
                  comp.set_difficulty("Hard")
                  break
               else:
                  print('This was not an valid option, please enter 1 or 2')
            except ValueError:
               print("This is not an number please enter 1 or 2")

         
         while True:
            if turn == "player":
               _ = player.play()
               if _ == "computer":
                  turn = _
               elif _ == "winner":
                  winner_winner_chicken_dinner(player, "player")
               else:
                  break
            elif turn == "computer":
               _ = comp.play()
               if _ == "player":
                  turn = _
               elif _ == "winner":
                  winner_winner_chicken_dinner(comp, "computer")


if __name__ == "__main__":
    # Call the main function.
    main()
