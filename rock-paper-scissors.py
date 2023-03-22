from random import choice
from emoji import emojize
from sys import exit


class Game:
    emojies = {
        "rock": emojize(":brick:"),
        "paper": emojize(":page_facing_up:"),
        "scissors": emojize(":scissors:"),
    }
    player_score, computer_score = 0, 0

    def __init__(self):
        self.player_pick = self.get_input()
        self.computer_pick = choice(["rock", "paper", "scissors"])

    def get_input(self):
        while True:
            player_pick = input("Pick: ").strip().lower()
            if player_pick in ["rock", "paper", "scissors"]:
                return player_pick
            else:
                print(f"'{player_pick}' isn't a valid input")

    def select_winner(self):
        if (
            (self.player_pick == "rock" and self.computer_pick == "scissors")
            or (self.player_pick == "paper" and self.computer_pick == "rock")
            or (self.player_pick == "scissors" and self.computer_pick == "paper")
        ):
            Game.player_score += 1
            return "Player win!!!"
        elif self.player_pick == self.computer_pick:
            return "It's a draw!!!"
        else:
            Game.computer_score += 1
            return "Computer win!!!"

    def __str__(self):
        return (
            f"[ Your pick: {Game.emojies[self.player_pick]} ]  x  [ Computer pick: {Game.emojies[self.computer_pick]} ]\n"
            f"[ Winner: {self.select_winner()} ]\n"
            f"[ Your score: {Game.player_score} ]  x  [ Computer score: {Game.computer_score} ]"
        )

    def play_again(self):
        while True:
            player_choice = input("Play again?\nYes or no? ").strip().lower()
            if player_choice == "yes":
                self.__init__()
                print(self.__str__(), end="\n\n")
            elif player_choice == "no":
                exit("Thanks for playing ^_^\n")
            else:
                print(f"'{player_choice}' isn't an available option")


def main():
    game = Game()
    print(game, end="\n\n")
    game.play_again()


if __name__ == "__main__":
    main()
