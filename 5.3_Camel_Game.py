import random

choice = "blank"
fuel = 10
alienmr = random.randrange(8, 16)
days = 0
tank = 10
travel = 0
miles = 0
dialogue = True
dialogue2 = True
radar = True
ae = False
raygun = False
done = False
breakv = False
aliendistance = -20
playerdistance = 0
distance = playerdistance - aliendistance
stage = 1
events = 0
heat = 0
totalm = 0
totald = 0


def leave():
    global done
    global again
    global breakv
    again = input("Would you like to play again?")
    print()
    if again.lower().strip() == "no":
        done = True
        breakv = True
    else:
        print("The game will now continue.")
        print()
        reassign()


def checkstatus():
    print("Total days passed:", days, "days.")
    print("Miles traveled:", playerdistance, "miles.")
    print("Spare fuel:", fuel, "gallons.")
    print("Your heat level is:", heat, )
    print("The aliens are", distance, "miles behind you.")
    print()


def reassign():
    global totalm
    global totald
    global choice
    global fuel
    global alienmr
    global days
    global tank
    global travel
    global miles
    global dialogue
    global dialogue2
    global radar
    global ae
    global raygun
    global done
    global breakv
    global aliendistance
    global playerdistance
    global distance
    global stage
    global events
    global heat
    totalm += miles
    totald += days
    choice = "blank"
    fuel = 10
    alienmr = random.randrange(8, 16)
    days = 0
    tank = 10
    travel = 0
    miles = 0
    dialogue = True
    dialogue2 = True
    radar = True
    ae = False
    raygun = False
    done = False
    breakv = False
    aliendistance = -20
    playerdistance = 0
    distance = playerdistance - aliendistance
    stage = 1
    events = 0
    heat = 0
    # this one took me forever to figure out that I needed to global all vars, but it saved like 200 lines of code :D


def rgending():
    print("You hate to do this, but there's no other options.")
    print("You open the hatch on your spaceship, exiting while holding the raygun.")
    print("You have to move quick, if you hesitate the aliens will see and bring you to your"
          "demise before you can bring them to theirs.")
    print("After a deep breath, you kill all your hesitation.")
    print("Aiming as quickly as you can, you pull the trigger.")
    print("...")
    print("Everything is bright for a moment.")
    print("After the explosion clears, their aircraft is nothing more than debris.")
    print("Congratulations! You are safe.")
    print()
    # saving a few lines of code to repeat dialogue


def aending():
    print("With your hands up, you exit your spaceship.")
    print("You can't tell if the aliens are friendly or not, but this is the only chance you have.")
    print("An alien exits the enemy aircraft.")
    print("You'd be sweating if it wasn't cold in outer space. With your hands shaking,"
          "you hand them the alien manuscript.")
    print("The alien looks at it for a second. Then back to you.")
    print("Remembering the graphic found inside it, you hold out your hand for a handshake.")
    print("...")
    print("The alien shakes your hand.")
    print()
    print("Congratulations! You have made peace with the aliens. Who knows"
          "what kind of adventures await you now.")
    print()
    # saving a few lines of code to repeat dialogue


def inventory():
    print()
    print("You can inspect items by typing a number corresponding to the order of which your items are displayed in")
    print()
    # just a function to save code time and make it cleaner


def rg():
    print("The raygun feels heavy and looks dangerous. If I were you, I'd only use it as a last resort.")
    # just another function to save code time and make it cleaner


def a():
    print("Opening the alien manifest, much of it is in impossible to decipher.")
    print("However, looking at picture within the book, you can see a graphic of "
          "a human and an alien shaking hands.")
    print("Would could it mean?")
    # just another function to save code time and make it cleaner


def options():
    print("A) Add fuel to ship.")
    print("B) Ahead moderate speed.")
    print("C) Ahead full speed.")
    print("D) Stop for the night.")
    print("E) Check Status")
    print()
    # same as other functions


achievement_1 = False
# first ending, dying to the aliens
achievement_2 = False
# second ending, returning safely to earth
achievement_3 = False
# third ending, safely creating a base on another planet to escape the aliens
achievement_4 = False
# either fail achievement 3 or get really unlucky and explode while refueling
achievement_5 = False
# fifth ending, joining the aliens
achievement_6 = False
# sixth ending, defeating the aliens
achievement_7 = False
# seventh ending, spaceship overheat ending
achievement_8 = False
# getting the 7 prior achievements in one run, mastery achievement kind of
acs = 0

if dialogue:
    print("Welcome to the Spaceship Game!")
    print("You are an astronaut who's on a mission gone wrong, can you find your way out of this mess?")
    print("You are running from a group of aliens who wish to take you in for experimentation.")
    print("You must manage your fuel, heat, and items to find an escape.")
    print("If they catch up to you, you will receive a 'Game Over'.")
    print("If you survive, you will receive a 'Victory'.")
    print("There are also a number of secret endings.")
    print("During multiple choice events you can quit the game by typing 'quit' "
          "or check your inventory by typing 'i'.")
    print("When you quit the game, you will be able to"
          "see your statistics, including total miles traveled, total days played, and achievements earned.")
    print("The game will now commence.")
    print()

while not done:
    while stage == 1:
        distance = playerdistance - aliendistance
        if playerdistance > 100:
            stage = 2
            events = 0
        if events == 3:
            days += 1
            aliendistance += alienmr
            events = 0
            if heat > 0:
                heat -= 1
            print("It's been a long day so you take a rest to get some shut-eye.")
            print("The aliens are", distance, "miles behind. It worries you slightly but being"
                                              " well rested is important.")
            print()
        if choice.lower().strip() == "quit":
            break
        if heat > 4:
            print("Gave over!")
            print("Your spaceship overheated and exploded! Maybe you should be more patient next time.")
            if not achievement_7:
                print("Achievement 'Haste Makes Waste' has been unlocked!")
                achievement_7 = True
            leave()
            if breakv:
                break
        if distance < 1:
            print("Game over!")
            print("The aliens caught up to you. Was it just bad luck or could you have played better?")
            if not achievement_1:
                print("Achievement 'Inferior Species' has been unlocked!")
                achievement_1 = True
            leave()
            if breakv:
                break
        interaction = random.randrange(1, 100)
        if interaction > 95:
            if heat > 0:
                heat -= 1
            print("While looking out into the abyss, you noticed a small floating box. Loot may be contained inside.")
            box = input("Will you go out and investigate? Type yes or no.")
            print()
            if box.lower().strip() == "yes" and not ae:
                if heat > 0:
                    heat -= 1
                print("Inside you found a gallon of fuel and what looks like some kind of foreign book!")
                print("After investigating the book more, it appears to be an alien manifest.")
                print("Good find! It might prove useful in the future.")
                print()
                fuel += 1
                ae = True
            elif box.lower().strip() == "no":
                print("You decided not to investigate, hopefully that was nothing important")
                print()
            elif box.lower().strip() == "yes" and ae:
                print("Inside you find two gallons of gas.")
                print("Lucky!")
                print()
                fuel += 2
            else:
                done = True
                break
            events += 1
            # manuscript interaction with 5% chance of happening
            # unlocks the join alien ending in the future
        elif interaction > 85:
            if radar:
                print("Using the ship's built in radar, you see that the aliens are", distance, "miles behind you.")
                print()
                events += 1
                radar = False
            else:
                radar = True
        elif interaction > 20:
            print("You feel like your velocity needs some tinkering with so you stop for a moment to "
                  "change something.")
            options()
            choice = input("What would you like to do?")
            print()
            if choice.strip().upper() == "A" and fuel > 0:
                tank += fuel
                if heat > 0:
                    heat -= 1
                fuel = 0
                print("You decided to add all fuel to your ship's tank. You have", tank,
                      "gallons in your tank now.")
                events += 1
                print()
            elif choice.strip().upper() == "A" and fuel == 0:
                print("You do not have any fuel to use!")
                print()
            elif choice.strip().upper() == "B" and tank > 0:
                tank -= 1
                if heat > 0:
                    heat += 1
                print("You decided to keep up a moderate speed for today and tonight. This "
                      "will use one gallon of gas.")
                print("Your spaceship has a heat level of:", heat,)
                print("If this level reaches 5, your ship will spontaneously combust. Be careful.")
                travel = random.randrange(8, 16)
                print("You travelled", travel, "miles today.")
                miles += travel
                events += 1
                playerdistance += travel
                print()
            elif choice.strip().upper() == "C" and tank > 1:
                tank -= 2
                heat += 2
                print("You decided to go full speed for today and tonight. This "
                      "will use two gallons of gas.")
                print("Your spaceship has a heat level of:", heat, )
                print("If this level reaches 5, your ship will spontaneously combust. Be careful.")
                travel = random.randrange(10, 20)
                print("You travelled", travel, "miles today.")
                events += 1
                miles += travel
                playerdistance += travel
                print()
            elif choice.strip().upper() == "C" or choice.strip().upper() == "B" and tank == 0:
                print("You have no fuel in your tank!")
            elif choice.strip().upper() == "D":
                print("You decided to stop for the night.")
                print("Night falls.")
                print()
                days += 1
                aliendistance += alienmr
                events = 0
            elif choice.strip().upper() == "E":
                checkstatus()
            elif choice.strip().upper() == "I":
                if raygun and ae:
                    print("You have a raygun and the alien manifest.")
                    inventory()
                    check = int(input("Type a number from 1-9 or 0 to exit the inventory."))
                    if check == 1:
                        rg()
                    elif check == 2:
                        a()
                    elif check == 0:
                        print()
                    else:
                        print("You do not have enough items for that!")
                        print()
                elif raygun:
                    print("You have a raygun.")
                    inventory()
                    check = int(input("Type a number from 1-9 or 0 to exit the inventory."))
                    if check == 1:
                        rg()
                    elif check == 0:
                        print()
                    else:
                        print("You do not have enough items for that!")
                elif ae:
                    print("You have the alien manifest.")
                    inventory()
                    check = int(input("Type a number from 1-9 or 0 to exit the inventory."))
                    print()
                    if check == 1:
                        a()
                        print()
                    elif check == 0:
                        print()
                    else:
                        print("You do not have enough items for that!")
                        print()
                else:
                    print("You don't have any items in your inventory currently.")
                    print()
            else:
                if choice.lower().strip() == "quit":
                    totalm += miles
                    totald += days
                    done = True
                    break
                # gas interaction with 60% chance of happening
        elif interaction > 10:
            if heat > 0:
                heat -= 1
            print("You stumbled across what seems like another traveller's wreckage, "
                  "there is spare fuel.")
            take = input("Will you take the fuel? Type yes or no.")
            print()
            if take.lower().strip() == "yes":
                rng = random.randrange(1, 100)
                if rng != 1:
                    fuel += 5
                    print("You took the fuel. You now have", fuel, "gallons of fuel.")
                    print()
                else:
                    print("While trying to take the fuel, you accidentally drop a lighter and cause an explosion!")
                    print("You died!")
                    if not achievement_4:
                        print("Achievement 'Die Trying' has been unlocked!")
                        achievement_4 = True

            elif take.lower().strip() == "no":
                print("You decided not to take the fuel. Let's hope this is not a regrettable decision.")
                print()
                # refuel interaction with 10% chance of happening
            else:
                done = True
                stage = 100
        elif interaction > 2:
            if heat > 0:
                heat -= 1
            print("Curiously, you gaze out into the empty space.")
            sight = random.randrange(1, 8)
            if sight == 8 and not ae:
                print("A small box a moderate distance away piques your interest. "
                      "Perhaps you'll reach it one of these days.")
            elif sight == 7:
                print("You see your home planet, Earth, very far and out of your reach. "
                      "It does feel like you're getting closer.")
            elif sight == 6:
                print("You see the sun, however it's really bright and your parents told "
                      "you never to look at the sun, so you stop.")
            elif sight == 5:
                print("You see a belt of floating rocks... you didn't pay attention "
                      "in science class so your best guess is that they're comets.")
            elif sight == 4:
                print("You see a satellite. It's probably powering someone's cable television.")
            elif sight == 3:
                print("You see the moon. It's effortless beauty is always something "
                      "to marvel at.")
            elif sight == 2:
                print("You see another planet very far away, not completely impossible "
                      "to reach but you would need a miracle for that.")
            else:
                print("Nothing but stars and darkness.")
            events += 1
            print()
            # sight interaction with 8% chance of happening
        else:
            if not raygun:
                if heat > 0:
                    heat -= 1
                print("You decided to examine the exterior of your ship on a whim.")
                print("You found a ray-gun taped to the bottom of your ship!")
                print("This may prove useful in the future.")
                print()
                raygun = True
                # raygun interaction with 1% chance of happening
    while stage == 2:
        alienmr = random.randrange(10, 25)
        distance = playerdistance - aliendistance
        if events == 3:
            days += 1
            aliendistance += alienmr
            events = 0
            if heat > 0:
                heat -= 1
            print("It's been a long day so you take a rest to get some shut-eye.")
            print("The aliens are", distance, "miles behind. It worries you slightly but being"
                                              " well rested is important.")
            print()
        if choice.lower().strip() == "quit":
            totalm += miles
            totald += days
            break
        if heat > 4:
            print("Gave over!")
            print("Your spaceship overheated and exploded! Maybe you should be more patient next time.")
            if not achievement_7:
                print("Achievement 'Haste Makes Waste' has been unlocked!")
                achievement_7 = True
            leave()
            if breakv:
                break
        if distance < 1:
            print("Game over!")
            print("The aliens caught up to you. Was it just bad luck or could you have played better?")
            if not achievement_1:
                print("Achievement 'Inferior Species' has been unlocked!")
                achievement_1 = True
            leave()
            if breakv:
                break
        alienmr = random.randrange(10, 20)
        if dialogue2:
            print("It's been over a hundred miles now. Earth looks larger and larger as you approach it.")
            print("However, the aliens seem to be getting closer, and quicker, as the days pass.")
            print()
            dialogue2 = False
        if playerdistance > 200 > aliendistance:
            # ending 2
            print("Congratulations you have made it back safely!")
            if not achievement_2:
                print("Achievement 'Home Safe' has been unlocked!")
                achievement_2 = True
            leave()
            if breakv:
                break
        if distance < 20 and ae or raygun:
            print("The aliens will catch up in no time, you're running out of options!")
            print()
            if ae and raygun:
                print("You have read the alien's manuscript and you have the raygun...")
                print("Seems like you'll have to forge your own adventure now!")
                end = input("Do you want to eliminate them or join their ranks? "
                            "Type 1 for elimination and 2 for an alliance.")
                print()
                if end == 1:
                    rgending()
                    if not achievement_6:
                        print("Achievement 'Locked and Loaded' unlocked!")
                        achievement_6 = True
                    print()
                    leave()
                    if breakv:
                        break
                else:
                    aending()
                    if not achievement_5:
                        print("Achievement 'Misunderstood' unlocked!")
                        achievement_5 = True
                    leave()
                    if breakv:
                        break
            elif ae:
                aending()
                if not achievement_5:
                    print("Achievement 'Misunderstood' unlocked!")
                    achievement_5 = True
                leave()
                if breakv:
                    break
            else:
                rgending()
                if not achievement_6:
                    print("Achievement 'Locked and Loaded' unlocked!")
                    achievement_6 = True
                print()
                print("Your statistics have been saved.")
                again = input("Would you like to play again?")
                if again.lower().strip() == "yes":
                    reassign()
                    print("The game will continue.")
                    print()
                else:
                    done = True
        elif distance < 20:
            print("The aliens are closing in, and you have no choice but to try to improvise something!")
            print("You see a few planets out in the distance, maybe you have enough fuel to make "
                  "it to one of them if you put the ship in overdrive.")
            bet = input("Do you want to make an attempt for it? Type yes or no.")
            if bet.lower().strip() == "yes":
                print("Buckling your seatbelt even tighter, you put the spaceship into overdrive.")
                print("The quick acceleration almost sends you flying, but you hang on tight.")
                print()
                # rng ending lmao
                if fuel + tank > 25:
                    chance = random.randrange(1, 25)
                elif fuel + tank > 10:
                    chance = random.randrange(1, 50)
                else:
                    chance = random.randrange(1, 100)
                if chance == 1:
                    print("Hoping and praying all the way, somehow you enter one of the planet's atmospheres!")
                    print("Looking around, there's enough resources to make something with.")
                    print("Looking into the sky, you can see the alien aircraft getting further away.")
                    print("It seems they gave up on you.")
                    print("This is the start of a new future!")
                    print()
                    print("Congratulations! You got lucky and found somewhere new to call home.")
                    if not achievement_3:
                        print("Achievement 'Die Hard' unlocked!")
                        achievement_3 = True
                    print()
                    print("Your statistics have been saved.")
                    again = input("Would you like to play again?")
                    if again.lower().strip() == "yes":
                        reassign()
                        print("The game will continue.")
                        print()
                else:
                    print("As you approach the planet, it becomes mercilessly clear that you "
                          "won't be able to reach it.")
                    print("You close your eyes and let fate reign.")
                    print()
                    print("You died!")
                    totald += days
                    totalm += miles
                    if not achievement_4:
                        print("Achievement 'Die Trying' unlocked!")
                        achievement_4 = True
                    done = True
                    break
            else:
                print("You chose not to take a risk.")
                print()
        interaction = random.randrange(1, 100)
        if interaction > 95 and not ae:
            if heat > 0:
                heat -= 1
            print("While looking out into the abyss, you noticed a small floating box. Loot may be contained inside.")
            box = input("Will you go out and investigate? Type yes or no.")
            if box.lower().strip() == "yes":
                print("Inside you found a gallon of fuel and what looks like some kind of foreign book!")
                print("After investigating the book more, it appears to be an alien manifest.")
                fuel += 1
                ae = True
            elif box.lower().strip() == "yes" and ae:
                fuel += 2
                print("Inside you find two gallons of fuel.")
                print("Lucky!")
                print()
            else:
                print("You decided not to investigate, hopefully that was nothing important")
            events += 1
            # manuscript interaction with 5% chance of happening
            # unlocks the join alien ending in the future
        elif interaction > 90:
            if radar:
                print("Using the ship's built in radar, you see that the aliens are", distance, "miles behind you.")
                print()
                events += 1
                radar = False
            else:
                radar = True
            # random check interaction with 5% chance of occuring
        elif interaction > 40:
            print("You feel like your velocity needs some tinkering with so you stop for a moment to "
                  "change something.")
            options()
            choice = input("What would you like to do?")
            print()
            if choice.strip().upper() == "A" and fuel > 0:
                tank += fuel
                if heat > 0:
                    heat -= 1
                fuel = 0
                print("You decided to add all fuel to your ship's tank. You have", tank, "gallons in your "
                      "tank now.")
                events += 1
                print()
            elif choice.strip().upper() == "A" and fuel == 0:
                print("You do not have any fuel to use!")
                print()
            elif choice.strip().upper() == "B" and fuel > 0:
                tank -= 1
                heat += 1
                print("You decided to keep up a moderate speed for today and tonight. This "
                      "will use one gallon of gas.")
                print("Your spaceship has a heat level of:", heat, )
                print("If this level reaches 5, your ship will spontaneously combust. Be careful.")
                travel = random.randrange(8, 16)
                print("You travelled", travel, "miles today.")
                miles += travel
                events += 1
                print()
            elif choice.strip().upper() == "C" and fuel > 1:
                tank -= 2
                heat += 2
                print("You decided to go full speed for today and tonight. This "
                      "will use two gallons of gas.")
                print("Your spaceship has a heat level of:", heat, )
                print("If this level reaches 5, your ship will spontaneously combust. Be careful.")
                travel = random.randrange(10, 20)
                print("You travelled", travel, "miles today.")
                events += 1
                miles += travel
                print()
            elif choice.strip().upper() == "C" or choice.strip().upper() == "B" and tank == 0:
                print("You have no fuel in your tank!")
            elif choice.strip().upper() == "D":
                print("You decided to stop for the night.")
                print("Night falls.")
                print()
                if heat > 0:
                    heat -= 1
                days += 1
                aliendistance += alienmr
                events = 0
            elif choice.strip().upper() == "E":
                checkstatus()
            elif choice.strip().upper() == "I":
                if raygun and ae:
                    print("You have a raygun and the alien manifest.")
                    inventory()
                    check = int(input("Type a number from 1-9 or 0 to exit the inventory."))
                    if check == 1:
                        rg()
                    elif check == 2:
                        a()
                    elif check == 0:
                        print()
                    else:
                        print("You do not have enough items for that!")
                elif raygun:
                    print("You have a raygun.")
                    inventory()
                    check = int(input("Type a number from 1-9 or 0 to exit the inventory."))
                    if check == 1:
                        rg()
                    elif check == 0:
                        print()
                    else:
                        print("You do not have enough items for that!")
                elif ae:
                    print("You have the alien manifest.")
                    inventory()
                    check = int(input("Type a number from 1-9 or 0 to exit the inventory."))
                    if check == 1:
                        a()
                        print()
                    elif check == 0:
                        print()
                    else:
                        print("You do not have enough items for that!")
                        print()
                else:
                    print("You don't have any items in your inventory currently.")
                    print()
            else:
                if choice.lower().strip() == "quit":
                    done = True
                    stage = 100
                # gas interaction with 50% chance of happening
        elif interaction > 22:
            if heat > 0:
                heat -= 1
            print("You stumbled across what seems like another traveller's wreckage, "
                  "there is spare fuel.")
            take = input("Will you take the fuel? Type yes or no.")
            if take.lower().strip() == "yes":
                fuel += 5
                print()
                print("You took the fuel. You now have", fuel, "gallons of fuel.")
            elif take.lower().strip() == "no":
                print("You decided not to take the fuel. Let's hope this is not a regrettable decision.")
                # refuel interaction with 12% chance of happening
            else:
                done = True
                stage = 100
        elif interaction > 12:
            if heat > 0:
                heat -= 1
            print("Curiously, you gaze out into the empty space.")
            sight = random.randrange(1, 8)
            if sight == 8 and not ae:
                print("A small box a moderate distance away piques your interest. "
                      "Perhaps you'll reach it one of these days.")
            elif sight == 7:
                print("You see your home planet, Earth, very far and out of your reach. "
                      "It does feel like you're getting closer.")
            elif sight == 6:
                print("You see the sun, however it's really bright and your parents told "
                      "you never to look at the sun, so you stop.")
            elif sight == 5:
                print("You see a belt of floating rocks... you didn't pay attention "
                      "in science class so your best guess is that they're comets.")
            elif sight == 4:
                print("You see a satellite. It's probably powering someone's cable television.")
            elif sight == 3:
                print("You see the moon. It's effortless beauty is always something "
                      "to marvel at.")
            elif sight == 2:
                print("You see another planet very far away, not completely impossible "
                      "to reach but you would need a miracle for that.")
            else:
                print("Nothing but stars and darkness.")
            events += 1
            print()
            # sight interaction with 21% chance of happening
        else:
            if not raygun:
                if heat > 0:
                    heat -= 1
                print("You decided to examine the exterior of your ship on a whim.")
                print("You found a ray-gun taped to the bottom of your ship!")
                print("This may prove useful in the future.")
                print()
                raygun = True
                # raygun interaction with 5% chance of happening
        distance = playerdistance - aliendistance

# in stage 2 the % of rare interactions increase and aliens go faster
# secret endings are unlocked if player has the required items and if the aliens are <20 miles behind the player


print("Thank you for playing! Your statistics will now be listed below")
print("Total days played:", totald)
print("Total miles travelled:", totalm)
print("Achievements Collected:")
if achievement_1:
    print("Achievement 1: Inferior Species")
    acs += 1
if achievement_2:
    print("Achievement 2: Home Safe")
    acs += 1
if achievement_3:
    print("Achievement 3: Die Hard")
    acs += 1
if achievement_4:
    print("Achievement 4: Die Trying")
    acs += 1
if achievement_5:
    print("Achievement 5: Misunderstood")
    acs += 1
if achievement_6:
    print("Achievement 6: Locked and Loaded")
    acs += 1
if achievement_7:
    print("Achievement 7: Haste Makes Waste")
    acs += 1
if acs == 7:
    acs += 1
    print("Achievement 8: SG Mastery")
comprate = acs/8
fcomprate = "{:.2f}".format(comprate)
print("You completed", acs, "achievements out of 8!")
print("That gives you a completion rate of", fcomprate, "percent.")
