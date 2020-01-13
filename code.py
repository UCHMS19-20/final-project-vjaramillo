print ("Welcome to your closet!")
print ("Are you ready to get your outfit?")
answer = input ("Enter yes or no: ")

while answer not in ["yes", "no"]:
    answer = input("Please answer yes or no ")
if answer == "no":
    print ("Leaving the game")
    exit()
elif answer =="yes":
    gender = input ("Are you a boy or a girl?")
while gender not in ["boy", "girl"]: 
    gender = input("Please answer boy or girl ")
if gender == "boy":
    print("What style are you going for today?")
if gender == "girl": 
    print("What style are you going for today?")
    

clothes = input("sporty, casual, or fancy?")
while clothes not in ["sporty", "casual", "fancy"]:
    clothes = input("Please answer sporty, casual, or fancy")
if clothes == "sporty":
    print("sport")
elif clothes == "casual":
    print("cas")
else:
    print("fanc")