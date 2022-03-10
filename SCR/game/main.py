"""module docstring"""
import sys
from menu import Menu
from player import Player
from computer import Computer
from high_score import HighScore


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
        print(f"\nYou lost against [the {winner.name}].\n")


def main():
    """main function"""
    winning_number = 10

    high_score = HighScore()
    menu = Menu()

    menu.welcome()
    player_name = menu.set_name()
    player = Player(player_name, winning_number)
    game_menu_choice = menu.game_menu()

    while True:
        if game_menu_choice == "5":
            # Quit the game
            sys.exit()

        elif game_menu_choice == "4":
            # Show the game rules for the player
            game_menu_choice = show_game_rules(menu)

        elif game_menu_choice == "3":
            # Show current leaderboard. if leaderboard is empty, let them know
            data = high_score.read_file(high_score.filename)
            game_menu_choice = show_game_leaderboard(data, high_score, menu)

        elif game_menu_choice == "2":
            # Let player change their name or keep their current one
            game_menu_choice = change_player_name(menu, player)

        elif game_menu_choice == "1":
            comp = Computer(winning_number)
            turn = "player"

            # player has to choose between Easy / Hard difficulty on computer
            set_game_difficulty(comp)
            print(("~" * 15), "THE GAME HAS BEGUN", ("~" * 15))

            # Start game and switch turns until a player or computer has won
            data, game_menu_choice, player, comp = game_play(comp, high_score, menu, player,
                                                             player_name, turn, winning_number)


def game_play(comp, high_score, menu, player, player_name, turn, winning_number):
    """game play function"""
    while True:
        if turn == "player":
            return_value = player.play()
            if return_value == "computer":
                turn = return_value
            elif return_value == "winner":
                data = winner_winner_chicken_dinner(player, "player", high_score)
                user_input = input("Press 1 for menu, press anything else for quit the game: ")
                if user_input == "1":
                    game_menu_choice = menu.game_menu()
                    break
                else:
                    sys.exit()
        elif turn == "computer":
            return_value = comp.play()
            if return_value == "player":
                turn = return_value
            elif return_value == "winner":
                data = []
                winner_winner_chicken_dinner(comp, "computer", high_score)
                user_input = input("Press 1 for menu, press anything else for quit the game: ")
                if user_input == "1":
                    player = Player(player_name, winning_number)
                    comp = Computer(winning_number)
                    game_menu_choice = menu.game_menu()
                    break
                else:
                    sys.exit()
    return data, game_menu_choice, player, comp


def set_game_difficulty(comp):
    """Set the difficulty"""
    while True:
        try:
            set_difficulty = int(input("Press 1 for easy or 2 for hard: "))
            if set_difficulty == 1:
                comp.set_difficulty("Easy")
                print()
                break
            elif set_difficulty == 2:
                comp.set_difficulty("Hard")
                print()
                break
            else:
                print('This was not an valid option, please enter 1 or 2\n')
        except ValueError:
            print("This is not an number please enter 1 or 2\n")


def change_player_name(menu, player):
    """"Change player name"""
    print("Select a new name\n\nTo keep your name press enter without any text.\n")
    name = input("Enter your new name: ").strip()
    if name == "":
        print(f'\nWe keep your name {player.name}')
        game_menu_choice = menu.game_menu()
    else:
        player.changename(name)
        print(f'\nWe have changed your name to: {player.name}')
        input("Press enter to continue...")
        game_menu_choice = menu.game_menu()
    return game_menu_choice


def show_game_leaderboard(data, high_score, menu):
    """Show the game leaderboard"""
    if data == []:
        print("High-score is currently empty")
        input("Press enter to continue")
        game_menu_choice = menu.game_menu()
    else:
        high_score.show_high_score(data)
        input("Press enter to return to menu")
        game_menu_choice = menu.game_menu()
    return game_menu_choice


def show_game_rules(menu):
    """Show the game rules"""
    if menu.rules():
        game_menu_choice = menu.game_menu()
    return game_menu_choice


if __name__ == "__main__":
    # Call the main function.
    main()
