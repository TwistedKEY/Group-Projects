# Adrian Martinez, Connor Crowell, Carlos Ayalay
# main.py file - Oregon trail project 1.1
#Oregon Trail game! non-GUI version. Still has some kinks to work out. Works very much like the GUI version.

# Imports
import random
# - random
# - For use of random numbers

class OregonTrailGame:
    def __init__(self):
        self.money = 400.00
        self.food = 0
        self.medicine = 0
        self.spare_parts = 0
        self.pelts = 0
        self.distance = 2000
        self.days = 0
        self.max_days = 150
        self.survivors = []

    def main_menu(self):
        print("\n--- Main Menu ---")
        print("1. Play")
        print("2. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.start_game()
        elif choice == "2":
            print("Goodbye!")
        else:
            print("Invalid choice. Try again.")
            self.main_menu()

    def start_game(self):
        print("\n--- Starting a new game! ---")
        self.get_survivor_names()
        self.shop_for_supplies()
        self.game_loop()

    def get_survivor_names(self):
        leader_name = input("Enter your name (leader of the group): ")
        self.survivors.append({"name": leader_name, "health": 100, "alive": True})
        for i in range(4):
            name = input(f"Enter the name of family member {i + 1}: ")
            self.survivors.append({"name": name, "health": 100, "alive": True})

    def shop_for_supplies(self):
        print("\n--- Shopping for supplies ---")
        print(f"Starting money: ${self.money:.2f}")
        self.buy_item("food", 1)
        self.buy_item("medicine", 10)
        self.buy_item("spare_parts", 20)

    def buy_item(self, item, price_per_unit):
        while True:
            try:
                amount = int(input(f"How many units of {item} would you like to buy? (${price_per_unit:.2f} each): "))
                cost = amount * price_per_unit
                if cost > self.money:
                    print(f"Not enough money. You only have ${self.money:.2f}")
                else:
                    self.money -= cost
                    setattr(self, item, getattr(self, item) + amount)
                    print(f"Bought {amount} {item}. Remaining money: ${self.money:.2f}")
                    break
            except ValueError:
                print("Invalid input. Enter a valid number.")

    def game_loop(self):
        while self.distance > 0 and self.days < self.max_days:
            print(f"\n--- Day {self.days + 1} ---")
            self.show_status()
            self.choose_action()
            if all(not survivor["alive"] for survivor in self.survivors):
                print("All family members have died. Game over.")
                break
            self.days += 1
        else:
            if self.distance <= 0 and any(survivor["alive"] for survivor in self.survivors):
                print("Congratulations! You reached Oregon with surviving family members!")
            else:
                print("You failed to reach Oregon in time. Game over.")
        self.main_menu()

    def show_status(self):
        print(f"Distance to Oregon: {self.distance} miles")
        print(f"Food: {self.food} lbs, Medicine: {self.medicine}, Spare Parts: {self.spare_parts}")
        print(f"Days left: {self.max_days - self.days}")
        print("Survivor status:")
        for survivor in self.survivors:
            status = "Alive" if survivor["alive"] else "Deceased"
            print(f"{survivor['name']}: {survivor['health']} health, {status}")

    def choose_action(self):
        print("\nChoose an action:")
        print("1. Travel")
        print("2. Hunt")
        print("3. Rest")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.travel()
        elif choice == "2":
            self.hunt()
        elif choice == "3":
            self.rest()
        else:
            print("Invalid choice. Try again.")
            self.choose_action()

    def travel(self):
        travel_distance = random.randint(10, 20)
        food_consumed = random.randint(1, 5) * len([s for s in self.survivors if s["alive"]])

        if self.food - food_consumed < 0:
            print("You don't have enough food. Survivors will starve.")
            for survivor in self.survivors:
                if survivor["alive"]:
                    survivor["health"] -= random.randint(10, 20)
                    if survivor["health"] <= 0:
                        survivor["alive"] = False
                        print(f"{survivor['name']} has died from starvation.")
        else:
            self.food -= food_consumed
            self.distance -= travel_distance
            print(f"You traveled {travel_distance} miles. Food consumed: {food_consumed} lbs.")

        if random.randint(1, 5) == 1:  # 1 in 5 chance for a random event
            self.trigger_random_event()

    def hunt(self):
        food_gained = random.randint(5, 20)
        self.food += food_gained
        print(f"You hunted and gained {food_gained} lbs of food.")

        if random.randint(1, 5) == 1:  # 1 in 5 chance to get pelts
            pelts_gained = random.randint(1, 5)
            self.pelts += pelts_gained
            print(f"You also gained {pelts_gained} pelts.")

    def rest(self):
        food_consumed = random.randint(1, 5) * len([s for s in self.survivors if s["alive"]])
        if self.food - food_consumed < 0:
            print("You don't have enough food to rest properly.")
        else:
            self.food -= food_consumed
            for survivor in self.survivors:
                if survivor["alive"]:
                    health_gain = random.randint(5, 10)
                    survivor["health"] = min(survivor["health"] + health_gain, 100)
                    print(f"{survivor['name']} recovered {health_gain} health.")

    def trigger_random_event(self):
        events = [
            "Sickness strikes one survivor!",
            "A snake bite causes injury!",
            "A wheel breaks and needs repair!",
            "Bad weather slows you down!",
            "Rodents steal some food!"
        ]
        event = random.choice(events)
        print(f"\nRandom Event: {event}")

        if event == "Sickness strikes one survivor!":
            if self.medicine > 0:
                self.medicine -= random.randint(1, 3)
                print(f"Medicine used. Remaining medicine: {self.medicine}")
            else:
                print("No medicine left! Survivors' health will drop.")
                survivor = random.choice([s for s in self.survivors if s["alive"]])
                survivor["health"] -= random.randint(10, 20)
                if survivor["health"] <= 0:
                    survivor["alive"] = False
                    print(f"{survivor['name']} has died due to sickness.")
        elif event == "A snake bite causes injury!":
            if self.medicine > 0:
                self.medicine -= random.randint(1, 3)
                print(f"Medicine used. Remaining medicine: {self.medicine}")
            else:
                print("No medicine left! Survivors' health will drop.")
                survivor = random.choice([s for s in self.survivors if s["alive"]])
                survivor["health"] -= random.randint(10, 20)
                if survivor["health"] <= 0:
                    survivor["alive"] = False
                    print(f"{survivor['name']} has died from a snake bite.")
        elif event == "A wheel breaks and needs repair!":
            if self.spare_parts > 0:
                self.spare_parts -= random.randint(1, 2)
                print(f"Spare parts used. Remaining spare parts: {self.spare_parts}")
            else:
                print("No spare parts left! You lose travel progress.")
                self.distance += random.randint(5, 15)
        elif event == "Rodents steal some food!":
            food_lost = random.randint(5, 10)
            self.food = max(self.food - food_lost, 0)
            print(f"Rodents stole {food_lost} lbs of food.")

game = OregonTrailGame()
game.main_menu()

# ---------------------------------------------------------------------------------------------------------------- #
#
#                                       ----  - NOTES -  ----
#
# ---------------------------------------------------------------------------------------------------------------- #
# - Oregon Trail game! non-GUI version. Still has some kinks to work out. Works very much like the GUI version.
