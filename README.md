# Rock_paper_scissors

This code is a Python implementation of the classic game "Rock, Paper, Scissors". The game is played between the user and the computer. The user is prompted to pick either "rock", "paper" or "scissors", and the computer picks a random choice from the same set. Then, the winner is determined according to the game rules: rock beats scissors, scissors beat paper, and paper beats rock. The winner is displayed on the screen, along with the current score. The user is then prompted to play again or quit.


The code defines a Game class that encapsulates the logic of the game. The class has several methods:

**__init__**: Initializes the game by getting the user input and generating the computer's pick.
**get_input**: Prompts the user to enter their choice and validates the input.
select_winner: Determines the winner of the game based on the user and computer picks.
**__str__**: Returns a string representation of the game state, including the user and computer picks, the winner, and the score.
**play_again**: Prompts the user to play again or quit.
The main function creates an instance of the Game class and starts the game loop.

The code uses the emoji library to display emojis representing the game picks, and the sys library to exit the program when the user chooses to quit. The choice function from the random library is used to generate the computer's pick.
