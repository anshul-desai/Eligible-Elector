age = int(input("How old are you? "))
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    # creating a variable for the number of years they have until turning 18 and making it a string so it can be printed
    diff = str(18-age)
    print("Oops! You’re not eligible yet. But hey, only " + diff + " more years to go!")
