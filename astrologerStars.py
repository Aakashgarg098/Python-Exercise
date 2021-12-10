val = int(input("Enter 1 For printing the pattern in ascending order or 0 for vice-versa:\n"))
a = bool(val)
rows = int(input("Enter the rows you want to print:\n"))
if a:
    for i in range(1, rows+1):
        print(" "*(rows-i),"*"*i)
else:
    for i in range(rows, 0, -1):
        print(" "*(rows-i),"*"*i)