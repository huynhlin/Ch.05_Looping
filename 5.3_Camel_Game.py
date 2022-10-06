import random
'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
choice = "blank"
fuel = 10
alienmoverate = random.randrange(7, 14)
days = 0
tank = 10
travel = 0
miles = 0


achievement_1 = False
# first ending, dying to the aliens
achievement_2 = False
# second ending, returning safely to earth
achievement_3 = False
# third ending, safely creating a base on another planet to escape the aliens
achievement_4 = False
# fourth ending, joining the aliens
achievement_5 = False
# fifth ending, defeating the aliens
achievement_6 = False
# finding an easter egg, based on a small % chance event
achievement_7 = False
# getting the 6 prior achievements in one run, mastery achievement kind of

print("Welcome to the Spaceship Game!")
print("In this game, you will make a series of choices using multiple choice responses.")
print("These responses will control your spaceship, and ultimately, your fate.")
print("You are running from a group of aliens who wish to take you in for experimentation.")
print("If they catch up to you, you will receive a 'Game Over'.")
print("If you outrun them and return to earth, you will receive a 'Victory'.")
print("These are not the only outcomes however, there are also 3 more secret endings.")
print("You can quit at any time by typing 'quit'.")
print("When you quit the game, you will be able to"
      "see your statistics, including your total amount of interactions, achievements earned, and more.")
print("The game will now commence.")
print()
done = False
aliendistance = -20
playerdistance = 0
distance = 0
stage = 1

while not done:
    print("Your adventure begins now!")
    print("We'll be starting off with a decision.")
    print()
    while stage == 1:
        if playerdistance > 100:
            stage = 2
        else:
            days += 1
            aliendistance += alienmoverate
            interaction = random.randrange(1, 100)
            if interaction > 95:
                print()
                # interaction with 5% chance of happening
            elif interaction > 80:
                print()
                # interaction with 15% chance of happening
            elif interaction > 30:
                print("A) Add fuel to ship.")
                print("B) Ahead moderate speed.")
                print("C) Ahead full speed.")
                print("D) Stop for the night.")
                print("E) Check Status")
                print()
                choice = input("What would you like to do?")
                print()
                if choice.strip().upper() == "A" and fuel > 0:
                    fuel -= 1
                    print("You decided to fuel up your ship. You used one gallon. You have", fuel, "gallons remaining.")
                    print()
                elif choice.strip().upper() == "B" and fuel > 0:
                    tank -= 1
                    print("You decided to keep up a moderate speed for today and tonight. This "
                          "will use one gallon of gas.")
                    travel = random.randrange(10, 20)
                    print("You travelled", travel, "miles today.")
                    miles += travel
                    print()
                elif choice.strip().upper() == "C" and fuel > 1:
                    tank -= 2
                    print("You decided to go full speed for today and tonight. This "
                          "will use two gallons of gas.")
                    travel = random.randrange(10, 20)
                    print("You travelled", travel, "miles today.")
                    miles += travel
                    print()
                elif choice.strip().upper() == "D":
                    print("You decided to stop for the night.")
                    print("Night falls.")
                    days += 1
                elif choice.strip().upper() == "E":
                    print("Total days passed:", days, "days.")
                    print("Miles traveled:", playerdistance, "miles.")
                    print("Fuel remaining:", fuel, "gallons.")
                    print("The aliens are", distance, "miles behind you.")
                else:
                    done = True
                    # gas interaction with 50% chance of happening
            elif interaction > 20:
                print("You stumbled across what seems like another traveller's wreckage, "
                      "there is unused fuel.")
                take = input("Will you take the fuel? Type yes or no.")
                if take.lower().strip() == "yes":
                    fuel += 5
                    print()
                    print("You took the fuel. You now have", fuel, "gallons of fuel.")
                else:
                    print("You decided not to take the fuel. Let's hope this is not a regrettable decision.")
                    # refuel interaction with 10% chance of happening
            elif interaction > 2:
                print()
                # interaction with 18% chance of happening
            else:
                print()
                # interaction with 1% chance of happening
            distance = playerdistance - aliendistance
            if distance > 50:
                print("The aliens are", distance, "miles behind you. Nothing to worry about for the next few days!")
    while stage == 2:
        # in stage 2 the % of rare interactions increase and aliens go faster
        alienmoverate = random.randrage(9, 16)
        print()



