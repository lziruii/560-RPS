import random  

def generate_user_choice():
    user_choice = input("Choose (r, p, or s): ").lower()
    return user_choice

def generate_computer_choice():
    return random.choice(["r", "p", "s"])

def det_win(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "U tied!"
    elif (user_choice == "r" and computer_choice == "s") or \
         (user_choice == "p" and computer_choice == "r") or \
         (user_choice == "s" and computer_choice == "p"):
        return "U win!"
    else:
        return "U lose!"

def play_game():
    print("Let's play r, p, s!")

    while True:
        user_choice = generate_user_choice()  
        computer_choice = generate_computer_choice()  

        print(f"U chose {user_choice}.")
        print(f"C chose {computer_choice}.")

        result = det_win(user_choice, computer_choice)  
        print(result)

        play_again = input("Play again? (y/n): ").lower()  
        if play_again != 'y':
            print("Thanks. Bye!")
            break

if __name__ == "__main__":
    play_game()
