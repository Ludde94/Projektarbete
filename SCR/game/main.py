from sys import exit
from menu import Menu
from player import Player
from computer import Computer
from highscore import Highscore


def winner_winner_chicken_dinner(winner, who, highscore):
   """define who is the winner of the game"""
   if who == "player":
         print(f"Congratulations, you won {winner.name}")
         entry = {"name": winner.name, "rolls": winner.current_rolls}
         filename = highscore.filename
         data = highscore.read_file(filename)
         data = highscore.update_highscore(data, entry)
         highscore.save_highscore(filename, data)
         return data
         
         
         
   elif who == "computer":
         print(f"You losed against the {winner.name}.")
         

def main():
   """main function"""
   winning_number = 10
   highscore = Highscore()
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
         highscore.show_highscore(data)
         input("Press enter to return to menu")
         game_menu_choice = menu.game_menu()
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
               return_value = player.play()
               if return_value == "computer":
                  turn = return_value
               elif return_value == "winner":
                  data = winner_winner_chicken_dinner(player, "player", highscore)
                  print("Would you like to return to menu or quit?")
                  user_input= input("press 1 for menu, press anything else for quit the game: ")
                  if user_input == "1":
                     game_menu_choice = menu.game_menu()
                     break
                  else:
                     exit()
            elif turn == "computer":
               return_value= comp.play()
               if return_value == "player":
                  turn = return_value
               elif return_value == "winner":
                  winner_winner_chicken_dinner(comp, "computer", highscore)
                  print("Would you like to return to menu or quit?")
                  user_input= input("press 1 for menu, press anything else for quit the game: ")
                  if user_input == "1":
                     player = Player(player_name, winning_number)
                     comp = Computer(winning_number)
                     game_menu_choice = menu.game_menu()
                     break
                  else:
                     exit()


if __name__ == "__main__":
    # Call the main function.
    main()
