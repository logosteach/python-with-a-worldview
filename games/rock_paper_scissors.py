import random

print("=" * 50)
print("   ROCK  •  PAPER  •  SCISSORS")
print("=" * 50)
print("1 = Rock")
print("2 = Paper")
print("3 = Scissors")
print("4 = Quit")
print("5 = Take over the world")
print()

# Ask how many times the player wants to play
times_input = input("How many times would you like to play? (enter a number or 'infinity'): ").strip().lower()

unlimited = False
max_games = 0

if times_input == "infinity":
    unlimited = True
    print("\nYou chose infinity mode!")
    print("At any time you can type 'quit', 'exit', or 4 to end the game.")
else:
    # Try to convert the input into a whole number
    try:
        max_games = int(times_input)
        if max_games <= 0:
            print("That number is too small. We will play 1 game instead.")
            max_games = 1
    except ValueError:
        print("I didn't understand that. We will play 1 game.")
        max_games = 1

print()
games_played = 0

# Main game loop
while unlimited or games_played < max_games:

    user_input = input("Enter your choice:\n\t1 = Rock\n\t2 = Paper\n\t3 = Scissors\n\t4 = Quit\n\t5 = Take over the world!\n\t(1-5, or quit/exit): ").strip().lower()

    # --- Quit options ---
    if user_input == "4" or user_input == "quit" or user_input == "exit":
        print("\nThanks for playing! Goodbye.")
        break

    # --- Special option 5 ---
    if user_input == "5":
        print("\n🌍  You attempt to TAKE OVER THE WORLD...")
        print("The computer laughs in binary and continues the game.")
        print("(That choice doesn't count as a real round.)\n")
        continue

    # --- Check for a valid number 1, 2, or 3 ---
    try:
        user_choice = int(user_input)
    except ValueError:
        print("Please enter a number 1-5, or type quit/exit.\n")
        continue

    if user_choice < 1 or user_choice > 3:
        print("Only 1, 2, or 3 are valid moves. Try again.\n")
        continue

    # Computer picks randomly
    computer_choice = random.randint(1, 3)

    # Convert numbers into words so the output looks nice
    names = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f"\nYou chose:      {names[user_choice]}")
    print(f"Computer chose: {names[computer_choice]}")

    # Decide the winner using if / elif / else and comparison operators
    if user_choice == computer_choice:
        print("Result: It's a tie!")
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        print("Result: You win! 🎉")
    else:
        print("Result: Computer wins.")

    games_played += 1
    print(f"(Games played so far: {games_played})\n")

# Final message when the loop ends normally (finite games)
if not unlimited and games_played >= max_games:
    print(f"You finished all {max_games} games. Thanks for playing!")
    
# Copyright 2026 LogosTeach - All Rights Reserved
