import random

CHOICES = ["rock", "paper", "scissors"]


def get_player_move():
    """Ask until the player types a legal move or quit."""
    while True:
        move = input("Your move: ").strip().lower()
        if move == "quit" or move in CHOICES:
            return move
        print("That is not a legal move. Type rock, paper, scissors, or quit.")


def pick_computer():
    """Return one random legal move."""
    return random.choice(CHOICES)


def decide_winner(player, computer):
    """Return 'player', 'computer', or 'tie'."""
    if player == computer:
        return "tie"
    if player == "rock" and computer == "scissors":
        return "player"
    if player == "paper" and computer == "rock":
        return "player"
    if player == "scissors" and computer == "paper":
        return "player"
    return "computer"


def main():
    player_score = 0
    computer_score = 0

    print("Rock, Paper, Scissors")
    print("Type rock, paper, or scissors. Type quit to stop.")

    while True:
        player = get_player_move()
        if player == "quit":
            break

        computer = pick_computer()
        print("Computer chose", computer)

        winner = decide_winner(player, computer)
        if winner == "tie":
            print("Tie.")
        elif winner == "player":
            print("You win this round.")
            player_score = player_score + 1
        else:
            print("Computer wins this round.")
            computer_score = computer_score + 1

        print("Score  You:", player_score, " Computer:", computer_score)

    print("Final score  You:", player_score, " Computer:", computer_score)
    print("Thanks for playing.")


if __name__ == "__main__":
    main()
