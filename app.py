
print("Welcome to the simple calculator, please select from the following options:")
print("1: Addition \n2: Subtraction \n3: Multiplication\n4: Division")

tryAgain = True
num_tries = 10

# Test if user input is a valid input between 1 and 4. Also checks for errors such as invalid keyboard entries
while True:
    try:
        for tryAgain in range(0, num_tries):
            usr_selection = int(input("Please enter selection: "))
            if(0 < usr_selection <= 4):
                break
            else:
                continue
        break
    except Exception:
        if tryAgain:
            print("Error. Please enter a valid entry")
            continue

tryAgainNum = True
while True:
    try:
        selection_1 = int(input("Please enter first number: "))
        selection_2 = int(input("Please enter second number: "))
    except NameError:
        if tryAgainNum:
            print("Error. Please enter a valid entry")
            continue
    except ValueError:
        if tryAgainNum:
            print("Error. Please enter a valid entry")
            continue

    print("Are you satisfied with your numbers ", selection_1," and ", selection_2)
    continue_select = input("yes/no (y/n): ")
    if(continue_select == "y"):
        break
    elif(continue_select == "n"):
        continue
    else:
        print("Invalid entry. Please enter 'y' or 'n'")

if(usr_selection == 1):
    import addition
    print("Solution: ", addition.add_numbers(selection_1,selection_2))
elif(usr_selection == 2):
    import subtraction
    print("Solution: ", subtraction.subtract_numbers(selection_1,selection_2))
elif(usr_selection == 3):
    import multiplication
    print("Solution: ", multiplication.multiply_numbers(selection_1,selection_2))
elif(usr_selection == 4):
    import division
    print("Solution: ", division.divide_numbers(selection_1,selection_2))




