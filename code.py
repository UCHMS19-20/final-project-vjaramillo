print ("Welcome to your closet!")
print ("Are you ready to get your outfit?")
answer = input ("Enter yes or no: ")
while answer not in ["yes", "no"]:
    answer = input("Please answer yes or no ")
if answer == "no":
    print ("Leaving the game")
    exit()
elif answer =="yes":
    print("Are you a boy or a girl?")
    answer = input ("Enter boy or girl:")

while answer not in ["boy", "girl"]: 
        answer = input("Please answer boy or girl ")
    if answer == "boy":
        print("What style are you going for today?")
        clothes = input ("Enter sporty, casual, or fancy:")
        while clothes not in ["sporty", "casual", "fancy"]:
            clothes = input("Please answer sporty, casual, or fancy")
        if clothes == "sporty": 
            print("okay")
        elif clothes == "casual":
            print("boomer")
        else clothes == "fancy":
            print("okay boomer")
    elif answer == "girl": 
       print("boomer")