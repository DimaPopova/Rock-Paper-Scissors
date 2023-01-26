import random

# menu
player_one = input("Enter your name: ")
print(f"Hello {player_one}!")
player_two = "Computer"
choices = ["rock", "paper", "scissors"]

print("Please select game mode.")
game_mode = input("Enter '1' for first to win or enter '2' for first to two wins from three games. ")

# first to win
if game_mode == "1":
    print("First to win.")
    print("Start! Please chose rock,paper or scissors")

    while True:
        player_one_choice = input()
        computer_choice = random.choice(choices)

        if (player_one_choice == "rock" and computer_choice == "scissors") or \
                (player_one_choice == "paper" and computer_choice == "rock") or \
                (player_one_choice == "scissors" and computer_choice == "paper"):

            print(f"The computer chose: {computer_choice}")
            print(f"{player_one} Wins!")

        elif player_one_choice == computer_choice:
            print(f"The computer chose: {computer_choice}")
            print("Draw")

        elif (computer_choice == "rock" and player_one_choice == "scissors") or \
                (computer_choice == "paper" and player_one_choice == "rock") or \
                (computer_choice == "scissors" and player_one_choice == "paper"):

            print(f"The computer chose: {computer_choice}")
            print(f"The {player_two} Wins!")

        else:
            print("Incorrect answer!")
            print("You have to chose rock,paper or scissors!")
            answer = input()

        print(f"Do you want one more game {player_one}?")
        answer = input()

        if answer == "no":
            print("Ok, bye!")
            exit()
        elif answer == "yes":
            print("OK, let's play.")
            print("Start! Please chose rock,paper or scissors")
            continue

        else:
            print("Incorrect answer!")
            print("You have to answer with 'yes' or 'no'.")
            answer = input()

# 2 from 3
elif game_mode == "2":
    print("2 from 3")
    print("Start! Please chose rock,paper or scissors")
    counter_player_one = 0
    counter_player_two = 0

    while counter_player_one < 2 and counter_player_two < 2:
        player_one_choice = input()
        computer_choice = random.choice(choices)

        if (player_one_choice == "rock" and computer_choice == "scissors") or \
                (player_one_choice == "paper" and computer_choice == "rock") or \
                (player_one_choice == "scissors" and computer_choice == "paper"):

            counter_player_one += 1
            print(f"The computer chose: {computer_choice}")
            print(f"Result: {player_one}-{counter_player_one} : {player_two}-{counter_player_two}")

        elif player_one_choice == computer_choice:
            print(f"The computer chose: {computer_choice}")
            print("Draw")

        elif (computer_choice == "rock" and player_one_choice == "scissors") or \
                (computer_choice == "paper" and player_one_choice == "rock") or \
                (computer_choice == "scissors" and player_one_choice == "paper"):

            counter_player_two += 1
            print(f"The computer chose: {computer_choice}")
            print(f"Result: {player_one}-{counter_player_one} : {player_two}-{counter_player_two}")

        else:
            print("Incorrect answer!")
            print("You have to chose rock,paper or scissors!")
            answer = input()

        if counter_player_one == 2 and counter_player_one > counter_player_two:
            print(f"{player_one} Wins!")
            print(f"Do you want one more set {player_one}?")
            new_answer = input()

            if new_answer == "no":
                print("Ok, bye!")
                exit()

            elif new_answer == "yes":
                counter_player_two = 0
                counter_player_one = 0
                print("OK, let's play.")
                print("Start! Please chose rock,paper or scissors")
                continue

        elif counter_player_two == 2 and counter_player_two > counter_player_one:
            print(f"The {player_two} Wins!")
            print(f"Do you want one more set {player_one}?")
            new_answer = input()

            if new_answer == "no":
                print("Ok, bye!")
                exit()

            elif new_answer == "yes":
                counter_player_two = 0
                counter_player_one = 0
                print("OK, let's play.")
                print("Start! Please chose rock,paper or scissors")
                continue
