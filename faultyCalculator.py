def add(num1, num2):
    if num1 == 1 and num2 == 10:
        print("Lol")
    else:
        print(sum(num1,num2))

def sub(num1, num2):
    if num1 == 1 and num2 == 10:
        print("Lol")
    else:
        print(sub(num1,num2))

def mul(num1, num2):
    if num1 == 1 and num2 == 10:
        print("Lol")
    else:
        print(num1*num2)


def div(num1, num2):
    if num1 == 1 and num2 == 10:
        print("Lol")
    else:
        print(divmod(num1,num2))

while True:
    n1 = int(input("Enter the number1:\n"))
    n2 = int(input("Enter the number2:\n"))
    op = input("Enter the operator you want to perform\nType:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
    if int(op)==1:
        add(n1, n2)
    elif int(op)==2:
        sub(n1, n2)
    elif int(op)==3:
        mul(n1, n2)
    elif int(op)==4:
        div(n1, n2)
    else:
        print("Invalid Input!!!")

    inp = input("Enter c to continue or q to quit:\n")
    if inp == "c":
        continue
    elif inp == "q":
        quit()