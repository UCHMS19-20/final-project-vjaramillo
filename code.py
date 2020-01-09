print ("Welcome to your closet!")
print ("Are you ready to get your outfit?")
answer = input ("Enter yes or no: ")
if answer != "yes" or "no":
    if answer == "no":
        print ("Leaving the game")
        exit()
    elif answer =="yes":
        print("Are you a boy or a girl?")
    else:
        print("Please enter yes or no")