import datetime
def getdate():
    return datetime.datetime.now()

print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome To The Health Management System")
s = set()
while True:
    name = input("Enter your name:\n")
    if name in s:
        print("Hi",name)
        inp = int(input("What do you want to do???\nType:\n1 - To Retrieve the data\n2 - To Store the data\n"))
        if inp==1:
            val = int(input("What do you want to retrieve...\nType: \n1 - Exercise\n2 - Diet\n"))
            if val == 1:
                with open(name+"_exercise.txt", "r") as f:
                    print(f.read())
            elif val == 2:
                with open(name+"diet.txt", "r") as f:
                    print(f.read())
            else:
                print("Invalid Input....")
        else:
            val = int(input("What do you want to store...\nType: \n1 - Exercise\n2 - Diet\n"))
            if val == 1:
                value = input("Enter your exercise here:\n")
                with open(name + "_exercise.txt", "a") as f:
                    f.write(str(getdate()) + " : " + value)
                    print("Added Successfully")
                    break
            elif val == 2:
                value = input("Enter your diet here:\n")
                with open(name + "_diet.txt", "a") as f:
                    f.write(str(getdate()) + " : " + value)
                    print("Added Successfully")
                    break
            else:
                print("Invalid Input....")
    else:
        s.add(name)
        print("Your name is successfully added in our system...")
        continue