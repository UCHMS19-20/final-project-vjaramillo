import random
print ("Welcome to your closet!")
print ("Are you ready to get your outfit? ")
answer = input ("Enter yes or no: ")
boy_sportybottom = ["blue basketball shorts", "red basketball shorts", "white basketball shorts"]
boy_sportytop = ["blue t-shirt", "red t-shirt", "black t-shirt"]
boy_sportyshoes = ["red sneakers", "black sneakers", "white sneakers"]
casual_top = ["brown shirt", "black shirt", "white shirt"]
casual_bottom = ["grey sweatpants", "blue jeans", "black jeans", "black sweatpants"]
casual_shoes =["gucci slides", "black air forces", "white air forces"]
boy_fancysuit = ["black suit", "navy blue suit", "grey suit"]
boy_fancyshoes = ["black dress shoes", "brown dress shoes"]
girl_sportybottom = ["blue leggings", "black leggings", "gray leggings"]
girl_sportytop = ["blue t-shirt", "red t-shirt", "pink t-shirt"]
girl_sportyshoes = ["blue sneakers", "black sneakers", "white sneakers"]
girl_fancydress = ["white dress", "red dress", "purple dress"]
girl_fancyheels = ["white heels", "black heels"]

def boy_accessorys ():
    accesory = input("Would you like an acccesory? ")
    while accesory not in ["yes", "no"]:
        accesory = input("Would you like an acccesory? ")
    if accessory == "yes":
        print ("You should wear an ADIDAS hoodie. Have fun")
    else:
        exit()
 
def boy_clothes():
    clothes = input("sporty, casual, or fancy?")
    while clothes not in ["sporty", "casual", "fancy"]:
        clothes = input("Please answer sporty, casual, or fancy ")
    if clothes == "sporty":
        print(f"Your shorts are {random.choice(boy_sportybottom)} and your shirt is a {random.choice(boy_sportytop)}")
        print(f"Your sneakers are {random.choice(boy_sportyshoes)}")
        boy_accessorys()
    elif clothes == "casual":
        print(f"You're gonna be wearing {random.choice(casual_bottom)} and your shirt is a {random.choice(casual_top)}")
        print(f"Your shoes are {random.choice(casual_shoes)}")
    else:
        print(f"Look at you! Your swaggy {random.choice(boy_fancysuit)} and {random.choice(boy_fancyshoes)}")

def girl_clothes():
    clothes = input("sporty, casual, or fancy? ")
    while clothes not in ["sporty", "casual", "fancy"]:
        clothes = input("Please answer sporty, casual, or fancy ")
    if clothes == "sporty":
        print(f"You're gonna be wearing {random.choice(girl_sportybottom)} and your shirt is a {random.choice(girl_sportytop)}")
        print(f"You're shoes to work out are {random.choice(boy_sportyshoes)}")
    elif clothes == "casual":
        print(f"You're gonna be wearing {random.choice(casual_bottom)} and your shirt is a {random.choice(casual_top)}")
        print(f"Your shoes are {random.choice(casual_shoes)}")
    else:
        print(f"Wow you're gonna look great! Your dress is a {random.choice(girl_fancydress)} and your heels are {random.choice(girl_fancyheels)}")

while answer not in ["yes", "no"]:
    answer = input("Please answer yes or no ")
if answer == "no":
    print ("Leaving the game")
    exit()
elif answer =="yes":
    gender = input ("Are you a boy or a girl? ")
while gender not in ["boy", "girl"]: 
    gender = input("Please answer boy or girl ")
if gender == "boy":
    print("What style are you going for today? ")
    boy_clothes()
if gender == "girl": 
    print("What style are you going for today? ")
    girl_clothes()