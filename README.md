Pig game by: Fredrik Johnsson, Ludvig Jenisch, David Carces
==========================================================

To play our game you simply start it in a terminal, after that you chooses the name you want to have in the game,
after that you can choose to play the game, change your name, if you have played before you can checkout your highscore list where you can view the 5 best rounds, you can choose rules to read how the game is played or you can quit.

When you are playing the game is pretty straight forward by pressing 1 to roll the dice or 0 to hold.
Everytime you roll a 1 your turn is over and your score becomes invalid, if you hold your present score for the round is saved after that it's the computers turn. The first to 100 wins! Good luck.

=============================================================

Computer class. 
In the Computer class we have six methods
We have the init method where we declare and handle all variables.
We have the set difficulty method where we set the difficulty from user input
The play method where we declare and handle all off the game play for the “Ultimate computer” 
We have the set threshold difficulty method where the threshold is set for the computer to relate to.
Computer got 1 method handles when the computer gets the value 1 on the die and prints needed messages
Roll dice handles the difficulty settings from user input with different settings regarding “easy” “hard” and “cheat”

Dice class.
We have the init method where we declare and handle all variables, such as sides on the die.
the method Get rolls made gets all the rolls made
Get sum rolls gets all the value that are generated

High Score class
In the init method we declare the file name
We have the read file method that reads the file declared as file
Then we have the update high score method that updates the file with players and rolls made
We also have “save high score” method that opens the file as “w” and writes into it
Show high score method that sorts and prints the list according to format

Menu class
Welcome method here we print our welcome message with input that proceeds to the main menu
Set name method where we set the player’s name with error handling
 Game menu describes the choices you have as a player in the game, 5 different choices
Rules where we describe the rules of the game 
Main class
Winner winner chicken dinner method handles the winners of the game with different prints regarding winner or loser
Main method takes in what different menu option that has been selected, calls on all the different methods 
Game play handles the game play between player and a computer, decide who’s the winner or loser
Set game difficulty handles the game difficulty with easy hard and cheat, with error handling from bad input
Change player name prints different things and calls on the change name method
Show leaderboard shows the leaderboard and calls on high score methods
Show rules method show the rules of the game and calls on that method

Player class
 init where we declare and handles all the variables.
Change name method where we change the existing player’s name
Input number where we input a number regarding the game menu with error handling.
Play method here we handle all the player game play with different situations and decisions

=====================================================================================

To implement the cheat in pig dice game –
When you have entered your name and are about to start a new game, a menu comes up with two choices 1 or 2.
1 for easy and 2 for hard, here you can press 9 instead for activating the cheat.
The cheat will result in that the computer always will roll a 1, and you will have all the time in the world to win. 
====================================================================================

To run and test our game you must have chocolatey install and make.
https://www.youtube.com/watch?v=5TavcolACQY

First you must be in your git bash terminal to run all our tests.
When you are in the terminal start to type:
"make venv", after the command is done type:
". .venv/scripts/activate", now you are in the virtual enviroment.
To install all the needed packages type, "make install".
Now you have installed all that you need to test our code.
To the test our unittests type, "make test" or "make coverage".
To generate UML diagrams type, "make pyreverse". (You must have graphviz installed for it to work, go into powershell as admin and write choco install graphviz.)
Other things you might want to check is, "make lint", "make flake8" and "make pylint".




