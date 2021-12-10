import random
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome To The Snake | Water | Gun Game")
lives = 10
user_score, comp_score = 0, 0
i = 0
while i<lives:
    i += 1
    comp_choice = random.choice(["s", "w", "g"])
    user_choice = input(f"Choose one of the value: {['s','w','g']}\n").lower()
    if (user_choice=="s" and comp_choice=="s") or (user_choice=="w" and comp_choice=="w") or (user_choice=="g" and comp_choice=="g"):
        print("It's a tie...\nYou chooses %s and computer chooses %s"%(user_choice,comp_choice))
        print(f"Computer Score : {comp_score}\nUser Score : {user_score}")
    elif (user_choice=="s" and comp_choice=="w") or (user_choice=="w" and comp_choice=="g") or (user_choice=="g" and comp_choice=="s"):
        print("You won this chance...\nYou chooses %s and computer chooses %s" % (user_choice, comp_choice))
        user_score += 1
        print(f"Computer Score : {comp_score}\nUser Score : {user_score}")
    elif (user_choice=="w" and comp_choice=="s") or (user_choice=="g" and comp_choice=="w") or (user_choice=="s" and comp_choice=="g"):
        print("Computer won this chance...\nYou chooses %s and computer chooses %s" % (user_choice, comp_choice))
        comp_score += 1
        print(f"Computer Score : {comp_score}\nUser Score : {user_score}")
if comp_score>user_score:
    print("Computer won this game".center(100, "-"))
elif comp_score<user_score:
    print("User won this game".center(100, "-"))
elif comp_score==user_score:
    print("It's a tie".center(100, "-"))