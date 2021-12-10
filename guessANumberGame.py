import random
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome To The Guess A Number Game")
comp_val = random.randint(1, 50)
lives = 10
initial = 0
while True:
    initial += 1
    user_val = int(input("Enter your guess number:\n"))
    if user_val>comp_val:
        print("Your guess number is high...")
        print("Total lives left",lives-initial)
    elif user_val<comp_val:
        print("Your guess number is low...")
        print("Total lives left", lives - initial)
    else:
        print(f"You won the game in {initial} guesses...")
        print("Total lives left", lives - initial)
        print("Thanks For Playing...".center(100, "-"))
        break