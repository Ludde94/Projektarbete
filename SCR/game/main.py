from sys import exit
from menu import Menu
from player import Player
from computer import Computer
from high_score import High_score


def winner_winner_chicken_dinner(winner, who, high_score):
    """define who is the winner of the game"""
    if who == "player":
        print(f"Congratulations, you won {winner.name}")
        entry = {"name": winner.name, "rolls": winner.current_rolls}
        filename = high_score.filename
        data = high_score.read_file(filename)
        data = high_score.update_high_score(data, entry)
        high_score.save_high_score(filename, data)
        return data
    elif who == "computer":
        print(f"You losed against the {winner.name}.")


def main():
    """main function"""
    winning_number = 100  # how many points to win the game
    high_score = High_score()  # instance of the High_score class
    menu = Menu()  # instance of the Menu class
    choice = menu.welcome()  # returned value after showing the welcome screen
    if choice:
        # set a variable to their input of chosen name from welcome
        player_name = menu.set_name()
    player = Player(player_name, winning_number)  # create player
    game_menu_choice = menu.game_menu()  # show menu and capture a choice

    while True:
        if game_menu_choice == "5":
            # Quit the game
            exit()

        elif game_menu_choice == "4":
            # Show the game rules for the player
            game_menu_choice = show_game_rules(game_menu_choice, menu)

        elif game_menu_choice == "3":
            # Show current leaderboard. if leaderboard is empty, let them know
            game_menu_choice = show_game_leaderboard(
                data, game_menu_choice, high_score, menu)

        elif game_menu_choice == "2":
            # Let player change their name or keep their current one
            game_menu_choice = change_player_name(
                game_menu_choice, menu, player)

        elif game_menu_choice == "1":
            # create instance of Computer class
            comp = Computer(winning_number)
            turn = "player"  # set default starting player to "player" or "computer"

            # player has to choose between Easy or Hard difficulty on the computer
            set_game_difficulty(comp)

            # Start game and switch turns until a player or computer has won
            data, game_menu_choice, player = game_play(comp, game_menu_choice, high_score, menu,
                                                       player, player_name, turn, winning_number)


def game_play(comp, game_menu_choice, high_score, menu, player, player_name, turn, winning_number):
    while True:
        if turn == "player":
            return_value = player.play()
            if return_value == "computer":
                turn = return_value
            elif return_value == "winner":
                data = winner_winner_chicken_dinner(
                    player, "player", high_score)
                print("Would you like to return to menu or quit?")
                user_input = input(
                    "press 1 for menu, press anything else for quit the game: ")
                if user_input == "1":
                    game_menu_choice = menu.game_menu()
                    break
                else:
                    exit()
        elif turn == "computer":
            return_value = comp.play()
            if return_value == "player":
                turn = return_value
            elif return_value == "winner":
                winner_winner_chicken_dinner(comp, "computer", high_score)
                print("Would you like to return to menu or quit?")
                user_input = input(
                    "press 1 for menu, press anything else for quit the game: ")
                if user_input == "1":
                    player = Player(player_name, winning_number)
                    comp = Computer(winning_number)
                    game_menu_choice = menu.game_menu()
                    break
                else:
                    exit()
    return data, game_menu_choice, player


def set_game_difficulty(comp):
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


def change_player_name(game_menu_choice, menu, player):
    print("Select a new name\n\nTo keep your name press enter without any text.\n")
    name = input("Enter your new name: ").strip()
    if name == "":
        print(f'\nWe keep your name {player.name}')
        game_menu_choice = menu.game_menu()
    else:
        player.changename(name)
        print(f'\nWe have changed your name to: {player.name}')
        game_menu_choice = menu.game_menu()
    return game_menu_choice


def show_game_leaderboard(data, game_menu_choice, high_score, menu):
    data_ = high_score.read_file(high_score.filename)
    if data_ != []:
        high_score.show_high_score(data)
        input("Press enter to return to menu")
        game_menu_choice = menu.game_menu()
    else:
        print("High-score is currently empty")
        input("Press enter to continue")
        game_menu_choice = menu.game_menu()
    return game_menu_choice


def show_game_rules(game_menu_choice, menu):
    if menu.rules():
        game_menu_choice = menu.game_menu()
    return game_menu_choice


if __name__ == "__main__":
    # Call the main function.
    main()
