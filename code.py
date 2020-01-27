import random
print ("Welcome to your closet!")
print ("Are you ready to get your outfit?")
answer = input ("Enter yes or no: ")
boy_sportybottom = ["blue basketball shorts", "red basketball shorts", "white basketball shorts"]
#dictionary of boy sporty bottom options to be randomly generated
boy_sportytop = ["blue t-shirt", "red t-shirt", "black t-shirt"]
#dictionary of boy sporty top optons to be randomly generated
boy_sportyshoes = ["red sneakers", "black sneakers", "white sneakers"]
#dictionary of boy sporty shoe options to be randomly generated
casual_top = ["brown shirt", "black shirt", "white shirt"]
#dictionary of casual top options for boys or girls to be randomly generated
casual_bottom = ["grey sweatpants", "blue jeans", "black jeans", "black sweatpants"]
#dictionary of casual bottom options for boys and girls to be randomly generated
casual_shoes =["gucci slides", "black air forces", "white air forces"]
#dictionary of casual shoe options for boys or girls to be randomly generated
boy_fancysuit = ["black suit", "navy blue suit", "grey suit"]
#dictionary of boy fancy suit options to be randomly generated
boy_fancyshoes = ["black dress shoes", "brown dress shoes"]
#dictionary of boy fancy shoe options to be randomly generated
girl_sportybottom = ["blue leggings", "black leggings", "gray leggings"]
#dictionary of girls sporty bottom options to be randomly generated
girl_sportytop = ["blue t-shirt", "red t-shirt", "pink t-shirt"]
#dictionary of girls sporty top options to be randomly generated
girl_sportyshoes = ["blue sneakers", "black sneakers", "white sneakers"]
#dictionary of girls sporty shoe options to be randomly generated
girl_fancydress = ["white dress", "red dress", "purple dress"]
#dictionary of girls fancy dress options to be randomly generated
girl_fancyheels = ["white heels", "black heels"]
#dictionary of girls fancy heel options to be randomly generated
 
def boy_accessorys ():
    accesory = input("Would you like an acccesory? ")
    while accesory not in ["yes", "no"]:
        accesory = input("Would you like an acccesory? ")
    if accesory == "yes":
        print ("You should wear an ADIDAS hoodie. Have fun")
        pygame.image.load(src/img/downloadadidashoodie.jpg)
    else:
        exit()

def boy_clothes():
    #function that generates a random outfit for boys after choosing a mood
    clothes = input("sporty, casual, or fancy?")
    #options of moods to randomly generate clothes
    while clothes not in ["sporty", "casual", "fancy"]:
        clothes = input("Please answer sporty, casual, or fancy")
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
   #function that randomly generates an outfit for girls after choosing a mood 
    clothes = input("sporty, casual, or fancy? ")
    #options of moods to randomly generate clothes
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
    gender = input ("Are you a boy or a girl?")
while gender not in ["boy", "girl"]: 
    gender = input("Please answer boy or girl ")
if gender == "boy":
    print("What style are you going for today?")
    boy_clothes()
if gender == "girl": 
    print("What style are you going for today?")
    girl_clothes()