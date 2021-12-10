while True:
       dic = {"string":"it's a set of characters and is immutable in Python.",
       "tuple":"it's similar to the list, but unlike list, it's immutable in Python and it's also hashable.",
       "hashable":"any python's object is hashable if it's value doesn't change during the lifetime."}
       print(dic.keys())
       val = input("Enter the value from the list to get the desired meaning:\n").lower()
       if val in dic.keys():
              print(val,dic[val],sep = " : ")

       inp = input("Enter c to continue or q to quit:\n")
       if inp == "c":
              continue
       elif inp == "q":
              quit()