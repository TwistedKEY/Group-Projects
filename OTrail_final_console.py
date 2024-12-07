# Adrian Martinez, Connor Crowell, Carlos Ayalay
# Final version of console print out game

# main.py file - Sandbox - Oregon trail project
# Imports
# - random
# - For use of random numbers

import random

class MyTrail:
    def __init__(self):
# Game variables
        self.distance = 2170
        self.maxDays = 0
        self.days = 0
        self.party = []
        self.msIndex = 0

# Player variables - inventory
        self.wallet = random.randrange(700, 1000, 50)
        self.Ox = 0
        self.Food = 0
        self.Wood = 0
        self.Clothes = 0
        self.Parts = 0
        self.Medicine = 0
        self.Rifle = 0
        self.Ammo = 0
        self.Guide = False
        self.Pelts = 0

# Item units
# - For store only
    def itemUnits(self, item):
        if item == "Ox":
            return "cow(s)"

        elif item == "Food":
            return "lb(s)"

        elif item == "Wood":
            return "log(s)"

        elif item == "Clothes":
            return "set(s)"

        elif item == "Parts":
            return "part(s)"

        elif item == "Medicine":
            return "flask(s)"

        elif item == "Rifle":
            return "rifle(s)"

        elif item == "Ammo":
            return "box(s)"

        elif item == "Pelts":
            return "pelt(s)"

        else: pass

# See inventory functions 1, 2, and 3 for different outputs
# - Daily print out
    def showStatus1(self):
        print(f"\nDistance to Oregon: {self.distance} mile(s)")
        if self.Guide: print("- --Guided-- -")
        else: print("- --Unguided-- -")
        print(f"Days to Winter: {self.maxDays - self.days}")
        print(f"Food: {self.Food} lb(s)")
        print(f"Wood: {self.Wood} log(s)")
        print("Party Status: ")

        for member in self.party:
            status = f"Health: {member["Health"]} -- Alive" if member["Health"] > 0 else "Dead"
            print(f"{member["Name"]} -- {status}")

# - View inventory print out
    def showStatus2(self):
        print(f"\nWallet: ${self.wallet:.2f}")
        print(f"Ox: {self.Ox} cow(s)")
        print(f"Food: {self.Food} lb(s)")
        print(f"Wood: {self.Wood} log(s)")
        print(f"Clothes: {self.Clothes} set(s)")
        print(f"Spare parts: {self.Parts} part(s)")
        print(f"Medicine: {self.Medicine} flask(s)")
        print(f"Rifle: {self.Rifle} rifle(s)")
        print(f"Ammo: {self.Ammo} bullet(s)")
        print(f"Pelt: {self.Pelts}")

# After purchase print out
    def showStatus3(self):
        print(f"\nWallet: ${self.wallet:.2f}")
        print(f"Ox: {self.Ox} cow(s)")
        print(f"Food: {self.Food} lb(s)")
        print(f"Wood: {self.Wood} log(s)")
        print(f"Clothes: {self.Clothes} set(s)")
        print(f"Spare parts: {self.Parts} part(s)")
        print(f"Medicine: {self.Medicine} flask(s)")
        print(f"Rifle: {self.Rifle} rifle(s)")
        print(f"Ammo: {self.Ammo} bullet(s)")
        print(f"Guide: {self.Guide}")

# Collects names for party player and party members
    def getParty(self):
        player = input("\nWhat is your name? :")
        self.party.append({"Name": player, "Health": 100, True: "Alive"})
        while True:
            try:
                groupNo = int(input(f"Hello {player}! How many people are you traveling with? :"))
                if groupNo >= 0:
                    for i in range(groupNo):
                        name = input(f"Enter name of member? {i + 2}: ")
                        self.party.append({"Name": name, "Health": 100, True: "Alive"})
                    break

            except ValueError: print("\n**Enter a valid input**")

# Gets player character for character attributes - starting inventory
    def getCharacter(self):
        while True:
            print("\nHave any supplies?")
            print("1. Farmer")
            print("2. Carpenter")
            print("3. Doctor")
            choice = input("What is your profession? (1-3): ")
            while True:
                if choice == '1':
                    print("\n- -- Farmer to Start -- -")
                    print("Ox: 3 cow(s)")
                    print("Parts: 3 part(s)")
                    choice = input("Yes or No? (1/0): ")
                    if choice == '1':
                        self.wallet -= random.randrange(50, 150, 50)
                        self.Ox += 3
                        self.Parts += 3
                        return False

                    else: break

                elif choice == '2':
                    print("\n- -- Carpenter to Start -- -")
                    print("Food: 150 lb(s)")
                    print("Wood: 150 log(s)")
                    print("Rifle: 1 rifle(s)")
                    print("Ammo: 100 bullet(s)")
                    choice = input("Yes or No? (1/0): ")
                    if choice == '1':
                        self.Food += 150
                        self.Wood += 150
                        self.Rifle += 1
                        self.Ammo += 100
                        return False

                    else: break

                elif choice == '3':
                    print("\n- -- Doctor to Start -- -")
                    print("Clothes: 5 set(s)")
                    print("Medicine: 5 flask(s)")
                    choice = input("Yes or No? (1/0): ")
                    if choice == '1':
                        self.wallet += random.randrange(100, 300, 50)
                        self.Clothes += 5
                        self.Medicine += 5
                        return False

                    else: break

                else:
                    print("\n**Enter a valid option**")
                    break

# Store
    def store(self):
        while True:
            print("\n ---  - General Store -  ---")
            print(f"You have $ {self.wallet:.2f} to spend")
            print("1. Ox")
            print("2. Food")
            print("3. Wood")
            print("4. Clothes")
            print("5. Parts")
            print("6. Medicine")
            print("7. Rifle")
            print("8. Ammo")
            print("9. Guide")
            print("0. Exit")
            choice = input("What would you like to buy? (1-0): ")
            while True:
                if choice == '1':
                    self.buyItem("Ox", 50)
                    break

                elif choice == '2':
                    self.buyItem("Food", .25)
                    break

                elif choice == '3':
                    self.buyItem("Wood", 2)
                    break

                elif choice == '4':
                    self.buyItem("Clothes", 10)
                    break

                elif choice == '5':
                    self.buyItem("Parts", 15)
                    break

                elif choice == '6':
                    self.buyItem("Medicine", 15)
                    break

                elif choice == '7':
                    self.buyItem("Rifle", 30)
                    break

                elif choice == '8':
                    self.buyItem("Ammo", 5)
                    break

                elif choice == '9':
                    self.buyItem("Guide", 150)
                    break

                elif choice == '0':
                    self.showStatus3()
                    print("Are you sure?")
                    choice = input("Yes or No? (1/0): ")
                    choice = choice.lower()
                    if choice == "1": return False

                    elif choice == "0": break

                    else:
                        print("\n**Enter a valid option**")
                        break

                else:
                    print("\n**Enter a valid option**")
                    break

# Purchase item
# - need values ; item, price
    def buyItem(self, item, price):
        while True:
            if item != "Guide":
                try:
                    print(f"\nYour wallet: ${self.wallet:.2f}")
                    if item != "Ammo":
                        print(f"Price of {item}: ${price:.2f}")
                        if item == "Ox": amount = int(input(f"How many {item} do you want to buy? "))

                        else: amount = int(input(f"How many {self.itemUnits(item).capitalize()} of {item} do you want to buy? "))

                        cost = amount * price
                        print("- -- Purchase -- -")
                        print(f"${price:.2f} \tx{amount} {self.itemUnits(item).capitalize()} -- ${cost:.2f}")

                    else:
                        print(f"Box of Ammo(50) - ")
                        print(f"Price of Box: ${price:.2f}")
                        amount = int(input("How many box's would you like? "))
                        cost = amount * price
                        print("- -- Purchase -- -")
                        print(f"${price:.2f} \tx{amount} {self.itemUnits(item).capitalize()} -- ${cost:.2f}")
                        amount *= 50

                    if self.wallet >= cost:
                        choice = input("Yes or No? (1/0): ")
                        choice = choice.lower()
                        if choice == '1':
                            self.wallet -= cost
                            setattr(self, item, getattr(self, item) + amount)
                            break

                        else:
                            print("Cancelling purchase...")
                            break

                    elif cost > self.wallet:
                        print("You don't have enough for this purchase")
                        print(f"Your wallet: ${self.wallet:.2f}")
                        print(f"Cost of {amount} {self.itemUnits(item)} of {item}: ${cost}")

                except ValueError:
                    print("\n**Enter a valid number**")

            else:
                print("\nWould you like to pay for a guide on your journey?")
                print("Having one may help.")
                print(f"Your wallet: ${self.wallet:.2f}")
                print(f"Price of {item}: ${price:.2f}")
                choice = input("Yes or No? (1/0): ")
                choice = choice.lower()

                if choice == '1':

                    while True:
                        choice = input("Purchase? (1/0): ")
                        choice = choice.lower()

                        if choice == "1" and price <= self.wallet:
                            self.wallet -= price
                            self.Guide = True
                            return False

                        elif choice == "0": return False

                        else: print("\n**Enter a valid option**")

                elif choice == '1': break

                else: print("\n**Enter a valid option**")

    def sellPelts(self):
        while True:
            print("Pelts are a good source of cash on the trail. Would you like to any sell pelts?")
            choice = input("Yes or No? (1/0): ")
            choice = choice.lower()
            if choice == "1":
                cash = self.Pelts * 1
                self.wallet += cash
                print(f"+{cash:.2f}")
                print(f"-{self.Pelts}")
                self.Pelts = 0
                break

            elif choice == "0": break

            else: print("\n**Enter a valid option**")

    def getDeparture(self):
        print("\nDeparture:")
        print("The later you choose to leave, the less time you will have before winter arrives.")
        print("1. February")
        print("2. March")
        print("3. April")
        choice = input("When would you like to leave? (1-3): ")
        while True:
            if choice == '1':
                self.maxDays += 210
                print("\nDays to Winter: 210")
                break

            elif choice == '2':
                self.maxDays += 180
                print("\nDays to Winter: 180")
                break

            elif choice == '3':
                self.maxDays += 150
                print("\nDays to Winter: 150")
                break

            else: print("\n**Enter a valid option**")

    # - in progress
# Milestone events through the journey
# - Fort laramie 1200
    def journey(self):
        msDistance = [1800, 1620, 1200, 1085, 785, 535, 0]
        milestones = [
            "Welcome to Fort Kearney!",
            "You are coming upon the Platte River crossing!",
            "Welcome to Fort Laramie!",
            "Welcome to Independence Rock, you are halfway there!",
            "Welcome to Fort Hall!",
            "You are coming upon the Snake River crossing!",
            "You have made it to Oregon City, Congratulations!"
        ]
        milestone = milestones[self.msIndex]
        useClothes = len([m for m in self.party if m["Health"] > 0])
        useRandomClothes = random.randint(1, len(self.party)) * len(self.party)

        while self.msIndex < len(msDistance) and self.distance <= msDistance[self.msIndex]:
            print(milestones[self.msIndex])
            self.msIndex += 1

            if milestone == milestones[0]:
                while True:
                    print("\nNeed to go to the general store?")
                    choice = input("Yes or No? (1/0): ")
                    if choice == '1':
                        self.sellPelts()
                        self.store()

                    elif choice == '0': break

                    else: print("\n**Enter a valid option**")

            elif milestone == milestones[1] or milestone == milestones[5]:

                if self.Guide:
                    if random.randint(1, 6) == 1: self.journeyEvent()

                elif random.randint(1, 3) == 1: self.journeyEvent()

            elif milestone == milestones[2]:
                while True:
                    print("Need to go to the general store?")
                    choice = input("Yes or No? (1/0): ")
                    if choice == '1':
                        self.sellPelts()
                        self.store()

                    elif choice == '0': break

                    else: print("\n**Enter a valid option**")

            elif milestone == milestones[3]:
                addFood = random.randrange(1, 100, 5)
                addWood = random.randrange(1, 100, 5)
                self.Food += addFood
                self.Wood += addWood
                for member in self.party:
                    if member["Health"]:
                        healthGain = random.randint(5, 10)
                        member["Health"] = min(member["Health"] + healthGain, 100)
                        print(f"{member["Name"]} rested and recovered {healthGain} health.")

                print("Items Added:")
                print(f"Food gained: {addFood}")
                print(f"Wood gained: {addWood}")

            elif milestone == milestones[4]:
                while True:
                    print("You will be coming up on the rockies soon.\nYou should change into warmer clothes")
                    print("Need to go to the general store?")
                    print("1. General Store")
                    print("2. Continue Trail")
                    print("3. Settle")
                    choice = input("What would you like to do? (1-3): ")
                    if choice == '1':
                        self.sellPelts()
                        self.store()

                    elif choice == '2':
                        if self.Clothes - useClothes < 0: print("The rockies are harsh. you should buy some clothes.")

                        else:
                            self.Clothes -= useClothes
                            print(f"-{useClothes} clothes")
                            break

                    elif choice == '3': self.settle()

                    else: print("\n**Enter a valid option**")

            elif milestone == milestones[5]:
                print("You Have made it passed the rockies and can change back into cooler clothes.")
                if self.Clothes - useRandomClothes < 0:
                    print("Your party can die from exposure.")

                else:
                    self.Clothes -= useRandomClothes
                    print(f"-{useRandomClothes} clothes")

                if self.Guide:
                    if random.randint(1, 6) == 1: self.journeyEvent()

                elif random.randint(1, 3) == 1: self.journeyEvent()

            else: print(f"{self.distance} miles left")

# Journey(river) events
    def journeyEvent(self):
        events = [
            "You lost a cow to the river",
            "You lost supplies to the river",
            "Your wagon was damaged to the river"
        ]
        event = random.choice(events)
        partsLost = random.randint(1, 3)
        print(f"\nJourney event: {event}")

        if event == events[0]:
            self.Ox -= 1
            print(f"You lost a cow to the river")

        elif event == events[1]:
            self.Parts -= partsLost
            print(f"Parts lost: {partsLost}")

        elif event == events[2]:
            chance = random.randint(1, 20)
            if chance >= 18:
                self.Rifle -= 1
                medicineLost = random.randint(1, 3)
                self.Medicine -= medicineLost
                print(f"You lost: Medicine({medicineLost}), Rifle(1)")

            else:
                foodLost = random.randint(1, 30)
                self.Food -= foodLost
                woodLost = random.randint(1, 30)
                self.Wood -= woodLost
                ammoLost = random.randint(1, 20)
                self.Ammo -= ammoLost
                print(f"You lost: Food({foodLost}), Wood({woodLost}), Ammo({ammoLost})")

# Random events
    def randomEvent(self):
        events = [
            "Sickness strikes one member!",
            "A snake bites one of your party members!",
            "A wheel has broken and needs to be repaired!",
            "Bad weather strikes and slows you down!",
            "Animals stole food in the night!",
            "An ox broke free!",
            "A rifle malfunctioned!",
            "You ran into a travelling merchant"
        ]
        event = random.choice(events)
        medicineUsed = random.randint(1, 3)
        print(f"\nRandom event: {event}")

# Chance of sickness
        if event == events[0]:

            if self.Medicine - medicineUsed >= 0:
                self.Medicine -= medicineUsed
                print(f"Medicine is used({medicineUsed}). Remaining flask(s): {self.Medicine}")

            else:
                member = random.choice([m for m in self.party if m[True]])
                print(f"No medicine available. {member["Name"]}'s health will drop.")
                member["Health"] -= random.randint(8, 20)

                if member["Health"] <= 0:
                    member[True] = "Dead"
                    print(f"{member["Name"]} has died due to sickness!")

# Chance of snake bite
        elif event == events[1]:
            member = random.choice([m for m in self.party if m[True]])

            if self.Medicine - medicineUsed >= 0:
                self.Medicine -= medicineUsed
                print(f"{member['Name']}'s has been healed.")
                print(f"Medicine is used({medicineUsed}). Remaining medicine: {self.Medicine} flask(s).")

            else:
                print(f"No medicine available. {member["Name"]}'s health will drop.")
                member["Health"] -= random.randint(10, 20)

                if member["Health"] <= 0:
                    member[True] = "Dead"
                    print(f"{member["Name"]} has died from a snake bite!")

# Chance of wheel breaking
        elif event == events[2]:
            partUsed = random.randint(1, 3)

            if self.Parts - partUsed >= 0:
                self.Parts -= partUsed
                print(f"Spare parts are used({partUsed}). Remaining spare parts: {self.Parts}.")

            else: print("No spare parts available. You are stuck.")
            # look into an event here
            # remove cows and give the meat

# Chance of bad weather
        elif event == events[3]:
            self.distance += random.randint(2, 6)
            print(f"Your traveling speed is slowed. {self.distance} mile(s) remaining.")

# Chance of wildlife
        elif event == events[4]:
            foodLost = random.randint(2, 10)
            self.Food = max(self.Food - foodLost, 0)
            print(f"You lost {foodLost} lb(s) of food. {self.Food} lb(s) remaining.")

# Chance of an ox breaking free
        elif event == events[5]:
            loseOx = random.randint(1, 4)

            if loseOx == 1:
                print("You you have lost an ox!")
                self.Ox = max(self.Ox - 1, 0)

            else: print("You recovered your ox!")

            print(f"You have {self.Ox} ox(en) remaining.")

# Chance of a rifle malfunctioning
        elif event == events[6]:
            loseRifle = random.randint(1, 4)

            if loseRifle == 1:
                print("You have lost a rifle!")
                self.Rifle = max(self.Rifle - 1, 0)

            else: print("Your rifle is still usable!")

            print(f"You have {self.Rifle} rifle(s) remaining.")

# Chance of Travelling merchant
        elif event == events[7]:
            while True:
                print("Hello Traveller! Need any supplies?")
                choice = input("Yes or No? (1/0): ")
                if choice == '1':
                    self.sellPelts()
                    self.store()

                elif choice == '0':
                    break

                else:
                    print("\n**Enter a valid option**")

# Travel option
    def travel(self):
        if self.Ox > 2:
            travelDistance = random.randint(12, 20)

        elif 0 < self.Ox <= 2:
            travelDistance = random.randint(10, 16)

        else:
            travelDistance = random.randint(6, 12)

        foodConsumed = random.randint(1, 5) * len([m for m in self.party if m["Health"] > 0])
        if self.Food - foodConsumed < 0:
            print("You don't have enough food. You and your members will starve.")

            for member in self.party:

                if member["Health"]:
                    member["Health"] -= random.randint(5, 15)

                    if member["Health"] <= 0:
                        member[True] = "Deceased"
                        print(f"{member["Name"]} has died from starvation.")

        else:
            self.Food -= foodConsumed
            self.distance -= travelDistance
            print(f"\nYou traveled {travelDistance} miles. Food consumed: {foodConsumed} lbs.")

# Trigger random event
        if self.Guide:

            if random.randint(1, 8) == 1:
                self.randomEvent()

        elif random.randint(1, 6) == 1:
            self.randomEvent()

# Hunting option
    def hunt(self):
        woodGathered = random.randint(1, 4) * len([m for m in self.party if m["Health"] > 0])
        if self.Rifle == 1 and self.Ammo > 0:
            foodGained = random.randint(5, 35)
            ammoUsed = random.randint(1, 3)

            if ammoUsed > self.Ammo: pass

            else:
                self.Ammo -= ammoUsed
                self.Food += foodGained
                print(f"Ammo used from hunting: {ammoUsed} bullet(s)")

        elif self.Rifle >= 2 and self.Ammo > 0:
            foodGained = random.randint(15, 60)
            ammoUsed = random.randint(2, 8)

            if ammoUsed > self.Ammo: pass

            else:
                self.Ammo -= ammoUsed
                self.Food += foodGained
                print(f"Ammo used from hunting: {ammoUsed} bullet(s)")

        else:
            foodGained = random.randint(0, 20)
            self.Food += foodGained

        if foodGained > 10:
            peltsGained = random.randint(1, 5)
            self.Pelts += peltsGained
            print(f"Pelts gained from hunting: {peltsGained}")

        self.Wood += woodGathered
        print(f"Food gained from hunting: {foodGained} lb(s)")
        print(f"Wood gathered: {woodGathered} log(s)")

# Resting option
    def rest(self):
        foodConsumed = random.randint(1, 5) * len([m for m in self.party if m["Health"] > 0])
        woodConsumed = random.randint(2, 5) * len([m for m in self.party if m["Health"] > 0])

        if self.Food - foodConsumed < 0 or self.Wood - woodConsumed < 0:
            print("You do not have enough resources to rest. You and your members will starve.")

        else:
            self.Wood -= woodConsumed
            self.Food -= foodConsumed
            for member in self.party:
                if member["Health"]:
                    healthGain = random.randint(5, 10)
                    member["Health"] = min(member["Health"] + healthGain, 100)
                    print(f"{member["Name"]} rested and recovered {healthGain} health.")

# Settle option
    def settle(self):
        print("Are your sure you want to settle?")
        choice = input("This will end the game. (1/0): ")
        choice = choice.lower()

        if choice == "1":
            self.__init__()
            playGame()

        else:
            print("Back to the trail.")
            self.chooseAction()

    def hints(self):
        hints = ["Having more than three ox can increase your movement speed",
                 "Having more rifles can increase your odds of more meat per hunt",
                 "More rifles use more ammo",
                 "Resting requires wood AND food",
                 "Having a guide can better your odds of something bad happening",
                 "Hunting and resting still uses a day",
                 "A broken wheel uses spare parts, see how bad it is",
                 "Rifles can malfunction, check if they work",
                 "An ox can break free but you can still recover it",
                 "The more ox and members in your party, the more food is consumed"
                 ]
        hint = random.choice(hints)
        print(f"Hint: {hint}")

# Choose actions menu
    def chooseAction(self):
        print(f"\nWhat would you like to do?")
        print("1. Travel")
        print("2. Hunt")
        print("3. Rest")
        print("4. Check Status")
        print("5. Hints")
        print("6. Settle")
        while True:
            choice = input("Choose an option (1-6): \n")
            if choice == '1':
                self.travel()
                break

            elif choice == '2':
                self.hunt()
                break

            elif choice == '3':
                self.rest()
                break

            elif choice == '4':
                self.days -= 1
                self.showStatus2()
                break

            elif choice == '5':
                self.hints()
                break

            elif choice == '6':
                self.days -= 1
                self.settle()
                break

            else:
                print("**Enter a valid option**")

# Start game function
    def startGame(self):
        print("\nWelcome to Independence, Missouri!\n**This is the start of the trail**")
        self.getParty()
        self.getCharacter()
        print(f"\nYou will need some supplies before you start your journey.")
        self.store()
        self.getDeparture()
        self.gameLoop()

# Game loop to function
    def gameLoop(self):
        while self.distance > 0 and self.days < self.maxDays:
            print(f"\n\t---Day {self.days}---")
            self.showStatus1()
            self.chooseAction()
            self.journey()
            input("\nEnter to Continue: ")

            if all(not members["Health"] for members in self.party):
                print("All members have died.\n\t-- Game over! --")
                break
            self.days += 1

        else:
            if self.distance <= 0 and any(members["Health"] for members in self.party):
                print("Congratulations! You've reached Oregon city.")

            else:
                print("You failed to reach Oregon in time.\n\n\t--- - Game over - ---")
                playGame()

# ----------------------------------------------------------------------------------------------------------------- #
#
#                                          ----  - Play Game -  ----
#
# ----------------------------------------------------------------------------------------------------------------- #
def playGame():
    myTrail =  MyTrail()

    while True:

        print("\n\t---  - Oregon Trail -  ---\n")
        print("Would you like to travel the Oregon Trail?\n")
        print("1. Prepare for journey")
        print("2. Quit")
        choice = input("Choose an option (1-2): ")

        if choice == "1":
            myTrail.startGame()

        elif choice == "2":
            print("This will close the game")
            choice = input("Are you sure? (1/0): ")
            choice = choice.lower()

            if choice == "1":
                print("Good Bye!")
                exit()

            elif choice == "0":
                break

            else:
                print("\n**Enter a valid option**")

        else:
            print("\n**Enter a valid option**")

playGame()


# ---------------------------------------------------------------------------------------------------------------- #
#
#                                            ----  - NOTES -  ----
#
# ---------------------------------------------------------------------------------------------------------------- #
# Health reduction functions only reduce once
# - If health is reduced to member, the health reduces once but does not reduce for any further turns

# - Can continue to move after you run out of parts or don't have enough and get stuck

# Ghost bug -> Casper = Enter --- Fixed
# - Bug that causes random select option and empty line
# -- Possibly the events/milestones, travel, or gameLoop
# -- The bug can evolve to where instead of "Enter to continue:", "Choose an option (1-6):" prints out
# - Can become a bigger issue
# -- Print out also feeds to the options menu when the print-out is given
# -- can evolve further into not display the daily print-out loop
# --- Bug likely occurs in the gameLoop -- correction; occurs when hit ENTER

# - Journey milestones events do not get read --- Fixed

# ----------------------------------------- --- To Do List --- -------------------------------------------------- #

# - See about adding more variation to more rifles or ox --- meh

# - 'Pop' the member of the party once the health drops to 0 and keep a tally of dead members

# Look into adding a ghost in the game
# - possibly a random event

# ----------------------------------------- --- COMPLETED --- -------------------------------------------------- #

# Look into adding an option for hint notes --- half completed
# - Create a start info function to give a description of benefits of items; Guide, Ox

# - Ask if they need the store for events and milestones --- completed

# - change buy ox print out --- completed

# - Journey milestones events do not get read --- completed

# Use clothes for something --- completed; maybe
# - or get rid of clothes/add different item
# rocky mountains milestone subtract 1 clothes per player
# between fort hall and platte river

# Maybe more random events --- completed; maybe
# - Add random traveler shop event/Look into using pelts in game
# - Add function so pelts is only collect if foodCollected in hunting != 0 --- check
# - any leftover pelts at end game will be sold and added to wallet as "final point" - cash for new home
# sell pelt function; likely sell item
# - sell pelts for extra money to buy items, add it in traveling merchant and milestones with store
