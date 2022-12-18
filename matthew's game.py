import os
import time
import random
import math

# Basic stats
done = False
continueGame = False
breaktest = False
ip = False
cp = False
cap = False
break2 = False
stop = False
camelMiles = 0
nativeMiles = 0
water = 100
energy = 100
canteens = 5
money = 50
speedMult = 1
statusMult = 1
cb = 1
days = 1
lastMove = 1
replenishedDays = 0
waterCost = 30
energyCost = 30
interest = 0

treasureChance = 6
treasureItems = ["Gatorade", "Raygun", "Coupon", "Piece of Trash", "Steroid", "Bag of Money"]
userItems = []

# Upgrade Shop
canteensCost = 20
# each
# horseShoes -- The list means [speed multiplier, price]
horseShoeNames = ["None", "Bronze", "Silver", "Gold", "Platinum", "Rocket"]
horseShoes = {horseShoeNames[0]: [1, 0],
              horseShoeNames[1]: [2, 75],
              horseShoeNames[2]: [4, 200],
              horseShoeNames[3]: [7, 1500],
              horseShoeNames[4]: [20, 5000],
              horseShoeNames[5]: [100, 50000]}
oasisUpgradeCost = 200
treasureUpgradeCost = 300
interestCost = 10000
csbCost = 20000
capCost = 5000
rgSellPrice = 200
potSellPrice = 50

# Upgrade Stats
horseShoeTier = 0
oasisChance = 25


def clear_screen():
    os.system('clear')


def title_screen():
    print("")


'''
def animate():
    time.sleep(0.2)
    clear_screen()
    print("  O    /)_")
    print("__(\__/_'_)")
    print("|  l  |")
    print("|     |")

'''


def move_natives():
    global nativeMiles, camelMiles, days
    if days < 3:
        return

    nativeMiles += round(random.randint(5, 8) * (days / 10 + 1))
    if nativeMiles >= camelMiles:
        print("! The natives have caught you!")
        camel_died()


def camel_rest():
    global energy, days, interest, money
    energy = 100
    if ip:
        interest = math.trunc(money * 0.02)
        money += interest
    print("+ You and your camel have rested well!")
    move_natives()
    days += 1


def camel_drink(amt):
    global water, canteens
    if canteens > 0:
        water += amt
        canteens -= 1
        if water > 100:
            water = 100
        print("+ You drank your canteen! You have {} remaining!\n".format(canteens))

    else:
        print("! Your canteens have ran dry! Wait for an oasis to get more!\n")


def camel_run(speedMult, waterCost, energyCost):
    global camelMiles, water, energy, days, replenishedDays, interest, money, cb
    camelMiles += round(random.randint(6, 14) * speedMult)
    water -= round(waterCost * statusMult)
    energy -= round(energyCost * statusMult)
    check_camel()
    move_natives()
    check_oasis()
    treasure_chest()
    if replenishedDays > 0: replenishedDays -= 1
    days += 1
    if ip:
        interest = money * 0.02
        int(interest)
        money += round(interest)
    if cp:
        cb = 1 + (canteens * 0.01)

# cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "King", "Queen", "Jack", "Ace",
#         "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "King", "Queen", "Jack", "Ace",
#         "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "King", "Queen", "Jack", "Ace",
#         "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "King", "Queen", "Jack", "Ace"]
#
# userCards = []
# pcCards = []
# userScore = 0
# pcScore = 0
# currentCard = ""
# def playerhit():
#     global cards, userCards, currentCard, userScore, x, cards, uturn
#     x = random.choice(cards)
#     currentCard = x
#     userCards.append(currentCard)
#     if currentCard == "1":
#         userScore += 1
#         print("You got a 1, your score is now {}.".format(userScore))
#     elif currentCard == "2":
#         userScore += 2
#         print("You got a 2, your score is now {}.".format(userScore))
#     elif currentCard == "3":
#         userScore += 3
#         print("You got a 3, your score is now {}.".format(userScore))
#     elif currentCard == "4":
#         userScore += 4
#         print("You got a 4, your score is now {}.".format(userScore))
#     elif currentCard == "5":
#         userScore += 5
#         print("You got a 5, your score is now {}.".format(userScore))
#     elif currentCard == "6":
#         userScore += 6
#         print("You got a 6, your score is now {}.".format(userScore))
#     elif currentCard == "7":
#         userScore += 7
#         print("You got a 7, your score is now {}.".format(userScore))
#     elif currentCard == "8":
#         userScore += 8
#         print("You got a 8, your score is now {}.".format(userScore))
#     elif currentCard == "9":
#         userScore += 9
#         print("You got a 9, your score is now {}.".format(userScore))
#     elif currentCard == "10":
#         userScore += 10
#         print("You got a 10, your score is now {}.".format(userScore))
#     elif currentCard == "King" or currentCard == "Queen" or currentCard == "Jack":
#         userScore += 10
#         print("You got a {},".format(currentCard), " your score is now {}.".format(userScore))
#     else:
#         if userScore > 10:
#             userScore += 1
#             print("You got an ace, your score is now {}.".format(userScore))
#         else:
#             userScore += 11
#             print("You got an ace, your score is now {}.".format(userScore))
#     cards.pop(cards.index(currentCard))
#     uturn += 1
#
#
# def pchit():
#     global pcCards, pcScore, x, cards, pcturn
#     x = random.choice(cards)
#     currentCard = x
#     pcCards.append(currentCard)
#     if currentCard == "1":
#         pcScore += 1
#         print("The gambler got a 1, his score is now {}.".format(pcScore))
#     elif currentCard == "2":
#         pcScore += 2
#         print("The gambler got a 2, his score is now {}.".format(pcScore))
#     elif currentCard == "3":
#         pcScore += 3
#         print("The gambler got a 3, his score is now {}.".format(pcScore))
#     elif currentCard == "4":
#         pcScore += 4
#         print("The gambler got a 4, his score is now {}.".format(pcScore))
#     elif currentCard == "5":
#         pcScore += 5
#         print("The gambler got a 5, his score is now {}.".format(pcScore))
#     elif currentCard == "6":
#         pcScore += 6
#         print("The gambler got a 6, his score is now {}.".format(pcScore))
#     elif currentCard == "7":
#         pcScore += 7
#         print("The gambler got a 7, his score is now {}.".format(pcScore))
#     elif currentCard == "8":
#         pcScore += 8
#         print("The gambler got a 8, his score is now {}.".format(pcScore))
#     elif currentCard == "9":
#         pcScore += 9
#         print("The gambler got a 9, his score is now {}.".format(pcScore))
#     elif currentCard == "10":
#         pcScore += 10
#         print("The gambler got a 10, his score is now {}.".format(pcScore))
#     elif currentCard == "King" or currentCard == "Queen" or currentCard == "Jack":
#         pcScore += 10
#         print("The gambler got a {},".format(currentCard), "his score is now {}.".format(pcScore))
#     else:
#         if pcScore > 10:
#             pcScore += 1
#             print("The gambler got an ace, his score is now {}.".format(pcScore))
#         else:
#             pcScore += 11
#             print("The gambler got an ace, his score is now {}.".format(pcScore))
#     pcturn += 1
#     cards.pop(cards.index(currentCard))
#
#
# def wincheck():
#     global bet, j, userScore, pcScore, pcturn, uturn, money, break2, stop
#     if stop:
#         if userScore == pcScore and (uturn + pcturn) > 0:
#             print("You tied! Your money will be returned.")
#             j = False
#             break2 = True
#         if userScore == 21:
#             print("You win!")
#             print("You received {} from the gambler!".format((bet * 2)))
#             money += (bet*2)
#             j = False
#             break2 = True
#         if pcScore == 21:
#             print("You lost!")
#             print("You lost {} to the gambler!".format(bet))
#             money -= bet
#             j = False
#             break2 = True
#         if userScore > 21:
#             print("You lost!")
#             print("You lost {} to the gambler!".format(bet))
#             money -= bet
#             j = False
#             break2 = True
#         if pcScore > 21:
#             print("You win!")
#             print("You received {} from the gambler!".format((bet * 2)))
#             money += (bet * 2)
#             j = False
#             break2 = True
#         if userScore > pcScore:
#             print("You win!")
#             print("You received {} from the gambler!".format((bet * 2)))
#             money += (bet * 2)
#             j = False
#             break2 = True
#         if pcScore > userScore:
#             print("You lost!")
#             print("You lost {} to the gambler!".format(bet))
#             money -= bet
#             j = False
#             break2 = True
#
# def gamble():  # mini-game for money
#     global money, bet, uturn, pcturn, pcAct, stop
#     print("\n" * 10)
#     print("-" * 30)
#     print("You run into a gambler on the side of the road.")
#     g = True
#     while g:
#         b = True
#         j = True
#         print("1] Blackjack")
#         print("2] Coin Flip")
#         print("e] exit\n")
#         print("You have ${} to bet.".format(money))
#         game = input("Which game would you like to play?\n")
#         while b:
#             bet = int(input("How much would you like to bet?\n$"))
#             if bet > money:
#                 print("You don't have that much to bet!")
#             else:
#                 b = False
#                 print()
#         if game == "1":
#             print("\n" * 10)
#             print("-" * 30)
#             instruct = input("Would you like instructions?")
#             if instruct.lower().strip() == "yes" or instruct.lower().strip() == "y":
#                 print("Number Cards = Face Value")
#                 print("Kings, Queens, Jacks = 10")
#                 print("Aces = 11 or 1")
#                 print("If 11 would send you over 21, the ace is worth 1.")
#                 print("The goal is to get a score closest to 21 without going over.")
#                 print("Each round, you can either 'Hit' or 'Stand'.")
#                 print("Picking 'Hit' will deal you a new card to add to your score.")
#                 print("Picking 'Stand' will end your turn and set your final score")
#                 print("If either your opponent gets closer to 21 than you, or your score goes over 21, you will lose.")
#                 print("If you get a score of 21 or get closer to 21 than your opponent, you will win.")
#                 print("\nGood luck!")
#                 print("\n" * 10)
#                 print("-" * 30)
#             d = True
#             uturn = 0
#             pcturn = 0
#             while j:
#                 # maybe create classes for colors for hearts clubs spades and diamonds but thats too complicated rn
#                 wincheck()
#                 # trying to code ai in python lmfao
#                 if d:
#                     print("\nBoth you and the gambler are dealt a card to begin with.\n")
#                     playerhit()
#                     pchit()
#                     uturn += 1
#                     pcturn += 1
#                     d = False
#                 if break2:
#                     break
#                 if userScore == pcScore and (uturn + pcturn) > 0:
#                     action = input("You and the gambler are tied right now, would you like to stand, hit, or quit?")
#                     if action == "h":
#                         playerhit()
#                         uturn+= 1
#                         wincheck()
#                         if break2:
#                             break
#                     else:
#                         if action.lower().strip() == "q" or action == "quit":
#                             stop = True
#                         rng = random.randint(1, 3)
#                         if rng == 1:
#                             pcAct = "h"
#                         else:
#                             pcAct = "s"
#                         pcturn += 1
#                         wincheck()
#                         if break2:
#                             break
#                 if uturn == pcturn:
#                     action = input("Would you like to stand, hit, or quit?")
#                     if action == "h":
#                         playerhit()
#                         uturn += 1
#                     elif action == "s":
#                         print("You decided to stand.")
#                         print("Your score is {}.".format(userScore))
#                         uturn += 1
#                     else:
#                         stop = True
#                 if break2:
#                     break
#                 elif uturn > pcturn:
#                     pcAct = ""
#                     if pcScore > 16:
#                         rng = random.randint(1, 3)
#                         if rng == 1:
#                             pcAct = "h"
#                         else:
#                             pcAct = "s"
#                         pcturn += 1
#                     if pcAct == "h":
#                         pchit()
#                     if pcAct == "s":
#                         print("The gambler decided to stand.")
#                         print("The gambler's score is {}.".format(pcScore))
#                     else:
#                         pchit()
#                 if break2:
#                     break
#                 elif pcturn > uturn:
#                     action = input("Would you like to stand, hit, or quit?")
#                     if action == "h":
#                         playerhit()
#                         uturn += 1
#                     elif action == "s":
#                         print("You decided to stand.")
#                         print("Your score is {}.".format(userScore))
#                         uturn += 1
#                     else:
#                         stop = True
#
#                 # delete cards from deck when dealt
#
#
#                 # end game append to reset cards
#                 cards.append(userCards)
#                 cards.append(pcCards)
#                 # find a way to pick from the list, pop it, then re-append when the game is done
#             # add winning and losing effects here
#         elif game == "2":
#             print("\n" * 10)
#             print("-" * 30)
#             coin = random.randint(1,2)
#             c = input("Heads or Tails?")
#             if c.lower().strip() == "heads":
#                 userCoin = 1
#             else:
#                 userCoin = 2
#
#             if coin == userCoin:
#                 print("\nYou were correct!")
#                 print("\n+${}".format((bet*2)))
#                 money += (bet * 2)
#             else:
#                 print("\nYou were not correct!")
#                 print("Better luck next time!")
#                 print("\n-${}".format(bet))
#                 money -= bet
#         elif game.lower().strip() == "e":
#             g = False
#         else:
#             print("That is not an option!")
#             g = False
#         if g:
#             qgamble = input("Would you like to play again?\n")
#             if qgamble == "y" or qgamble == "yes":
#                 print("The gambler asks for a rematch.")
#             else:
#                 g = False
#                 print("You decided to cut your losses and stop.")


def camel_died():
    global done, camelMiles
    done = True
    print("You made it {} miles!".format(camelMiles))
    print("Better luck next time!")
    exit()


def check_camel():  # Make sure it hasn't run out of anything
    global water, energy
    if energy <= 0:
        print("Your camel has died of exhaustion!")
        camel_died()
    elif water <= 0:
        print("Your camel has died of dehydration!")
        camel_died()


def camel_status():
    global days, camelMiles, nativeMiles, water, energy, speedMult, money
    print("\n* Days passed: {}".format(days))
    print("* Miles travelled: {}".format(camelMiles))
    print("* % of the way to the moon: {}%".format(round((camelMiles / 238900) * 100, 4)))
    print("* Native miles travelled: {}".format(nativeMiles))
    print("* Water level: {}".format(water))
    print("* Energy level: {}".format(energy))
    print("* Money: {}".format(money))
    print("* Speed multiplier: x{}".format(speedMult))
    print("* Oasis chance per turn: {}%".format(oasisChance))
    print("* Treasure chance per turn: {}%".format(treasureChance))
    print("\n")


def check_oasis():
    global canteens, oasisChance, money, days
    if random.randint(1, 100) <= oasisChance:
        moneyFound = round(random.randint(25, 45) * (days / 10 + 1))
        print("+ You have found an oasis!\n+ You filled +3 canteens!")
        print("+ You also found ${}!\n".format(moneyFound))
        money += moneyFound
        canteens += 3


def treasure_chest():
    global userItems, treasureItems, treasureChance, money
    if random.randint(1, 100) <= treasureChance:
        print("! You found a treasure chest alongside the road!")
        print("Open it?")
        print("Y] Yes")
        print("N] No")
        choiceInput = input("\nChoose your option: ").lower().strip()
        if choiceInput == "y" or choiceInput == "yes":
            chosenItem = treasureItems[random.randint(0, len(treasureItems) - 1)]
            if chosenItem == "Bag of Money":
                loot = random.randint(100, 1000)
                print("You found a bag of money!")
                print("There was ${}".format(loot), "inside!")
                money += loot
                print("-" * 30)
            else:
                userItems.append(chosenItem)
                print("\n+ You found a {}!".format(chosenItem))
                print("-" * 30)


def use_item():
    global userItems, replenishedDays, canteensCost, treasureUpgradeCost, oasisUpgradeCost, horseShoes, rgSellPrice, \
        potSellPrice, waterCost, energyCost, statusMult, interestCost, csbCost, capCost
    print("Type in the number to use the item")
    print("Your items:")
    count = 0
    for i in userItems:
        count += 1
        print("{}] {}".format(count, i))
    print("e] EXIT menu")
    useItemInput = input("\nChoose your option: ").lower().strip()
    if useItemInput == "e": return

    try:
        selectedItem = userItems[int(useItemInput) - 1]

        if selectedItem == "Gatorade":
            print("You drank the Gatorade! Thirst and Energy replenished for +3 turns!")
            replenishedDays += 3
        elif selectedItem == "Steroid":
            print("You gave the steroid to your camel!")
            print("The amount of energy and water used is decreased permanently!")
            print()
            statusMult -= (statusMult * 0.10)
        elif selectedItem == "Raygun":
            if random.randint(1, 10) == 1:
                print("\n" * 10 + "You aimed your raygun at the natives behind you...")
                print("You fire and it incinerates them all!")
                print("You won the raygun ending!")
                win()
            else:
                print("You aimed your raygun at the natives behind you...")
                print("You try to fire it but it doesn't work. You throw it away.")
        elif selectedItem == "Coupon":
            print("You scanned the coupon! 10% discount on upgrades and 10% bonus for sell prices!")
            canteensCost = round(canteensCost * 0.9)
            oasisUpgradeCost = round(oasisUpgradeCost * 0.9)
            treasureUpgradeCost = round(treasureUpgradeCost * 0.9)
            interestCost = round(interestCost * 0.9)
            csbCost = round(csbCost * 0.9)
            capCost = round(capCost * 0.9)
            rgSellPrice = round(rgSellPrice * 1.10)
            potSellPrice = round(potSellPrice * 1.10)
            for item in horseShoes:
                horseShoes[item][1] = round(horseShoes[item][1] * 0.90)
        elif selectedItem == "Piece of Trash":
            print("There's nothing you can do with this...")

        userItems.pop(userItems.index(selectedItem))
    except:
        print("That was not a valid list input! Try again some other time!")


def upgrade_menu():
    global horseShoeTier, horseShoes, money, speedMult, canteens, canteensCost, oasisChance, oasisUpgradeCost, \
        treasureUpgradeCost, treasureChance, rgSellPrice, ip, interestCost, cp, csbCost, cap, capCost

    if horseShoeTier < 5:
        nextShoeName = horseShoeNames[horseShoeTier + 1]
        nextShoeMult = horseShoes[horseShoeNames[horseShoeTier + 1]][0]
        nextShoeCost = horseShoes[horseShoeNames[horseShoeTier + 1]][1]

    print("Welcome to the upgrade shop!")
    print("You have: ${}".format(money))
    if horseShoeTier < 5:
        print("1] Upgrade to {} horseshoes ... ${}".format(nextShoeName, nextShoeCost))
    else:
        print("1] Out of stock!")
    print("2] Buy canteens ................... ${}x".format(canteensCost))
    print("3] +3% Chance of oasis ............ ${}".format(oasisUpgradeCost))
    print("4] +5% Chance of treasure ......... ${}".format(treasureUpgradeCost))
    if not ip:
        print("5] Interest upgrade ............... ${}".format(interestCost))
    else:
        print("5] Out of stock!")
    if not cp:
        print("6] Canteen speed boost ............ ${}".format(csbCost))
    else:
        print("6] Out of stock!")
    if not cap:
        print("7] Canteen capacity upgrade ....... ${}".format(capCost))
    else:
        print("7] Out of stock!")
    print("8] Sell item ...................... +$")
    print("e] EXIT menu")
    userUpgradeInput = input("\nChoose your option: ").lower().strip()

    if userUpgradeInput == "1":
        if horseShoeTier == 5:
            print("You can't buy another upgrade of this kind!")
        if money < nextShoeCost:
            print("You can't afford that!")
        else:
            money -= nextShoeCost
            speedMult = nextShoeMult
            horseShoeTier += 1
            print("Purchased successfully! Your speed multiplier is now x{}!".format(nextShoeMult))
    elif userUpgradeInput == "2":
        bought = int(input("How many canteens would you like to buy? (0 to cancel)"))
        if money >= (bought * canteensCost):
            canteens += bought
            money -= (bought * canteensCost)
            if bought == 0:
                print("Come back another time!")
            else:
                print("You bought {} canteens!".format(bought))
                print("Purchased successfully! You now have {} canteens!".format(canteens))
                canteensCost += 5
        else:
            print("You can't afford that!")
    elif userUpgradeInput == "3":
        if money < oasisUpgradeCost:
            print("You can't afford that!")
        else:
            money -= oasisUpgradeCost
            oasisChance += 3
            print("Purchased successfully! Oasis chance upgraded {}% -> {}%!".format(oasisChance - 3, oasisChance))
            oasisUpgradeCost *= 2
    elif userUpgradeInput == "4":
        if money < treasureUpgradeCost:
            print("You can't afford that!")
        else:
            money -= treasureUpgradeCost
            treasureChance += 5
            print("Purchased successfully! Treasure chance upgraded {}% -> {}%!".format(treasureChance - 5,
                                                                                        treasureChance))
            treasureUpgradeCost *= 2
    elif userUpgradeInput == "8":
        if userItems:
            print("Your items to sell:")
        count = 0
        for i in userItems:
            count += 1
            print("{}] {}".format(count, i))
        print("e] EXIT menu")
        useItemInput = input("\nChoose your option: ").lower().strip()

        if useItemInput == "e": return
        selectedItem = userItems[int(useItemInput) - 1]
        if selectedItem == "Raygun":
            money += rgSellPrice
            print("You sold the raygun to a merchant and got ${}!".format(rgSellPrice))
            print()
            userItems.pop(userItems.index(selectedItem))
        elif selectedItem == "Piece of Trash":
            money += potSellPrice
            print("You sold the piece of trash to a merchant and got ${}!".format(potSellPrice))
            print()
            userItems.pop(userItems.index(selectedItem))
        elif selectedItem == "Coupon" or selectedItem == "Gatorade":
            print("You cannot sell that!")
        else:
            print("You do not have anything to sell!")
    elif userUpgradeInput == "5":
        if not ip:
            if money > interestCost:
                print("You purchased the interest upgrade! "
                      "\nYou will now gain a small amount of income per round based on your total money!")
                ip = True
                money -= interestCost
            else:
                print("You can't afford that!")
    elif userUpgradeInput == "6":
        if not cp:
            if money > csbCost:
                print("You purchased the canteen speed boost! "
                      "\nYou will now gain a small speed multiplier based on how many canteens you have!")
                cp = True
                money -= csbCost
            else:
                print("You can't afford that!")
        else:
            print("You can't buy another upgrade of this kind!")
    elif userUpgradeInput == "7":
        if not cap:
            if money < capCost:
                print("You can't afford that!")
            else:
                cap = True
                print("Your canteen now holds more water for your camel! \nLess canteens will be used.")
        else:
            print("You can't buy another upgrade of this kind!")



    elif userUpgradeInput == "e" or userUpgradeInput == "exit":
        print("Come back another time!")
    else:
        print("That is not an available item! Come back another time!")
    print("-" * 30 + "\n")


def win():
    global done, camelMiles, days, money, statusMult, speedMult, cb
    done = True
    print("--- Final Stats ---")
    print("\n* Days passed: {}".format(days))
    print("* Miles travelled: {}".format(camelMiles))
    print("* Money: {}".format(money))
    percent = 1 - statusMult
    print("* Resources saved due to steroids: {:.2f}%".format(percent))
    print("* Speed multiplier: {}x".format(speedMult))
    print("* Canteen multiplier: {}x".format(cb))
    print("\nYou win!")
    print("\nThank you for playing!")
    print("\n(Coded by Matthew Avis for CSP, 2022)")
    exit()


def ufo():
    global done, camelMiles
    done = True
    print("You and your camel begin lifting into the sky")
    print("You got abducted by a UFO")
    print("L bozo")


print("Would you like instructions?")
userInput = input().lower().strip()
if userInput == "y" or userInput == "yes":
    print("Welcome to Camel 2!")
    print("The natives are after your camel!")
    print("You need to cross 100 miles to win!")
    print("But you are given the choice to continue after you win")
    print("You can continue up to 238,900 miles (the moon)")
    print("This is only possible if you buy upgrades to make your camel faster")
    print("Remember to maintain your camel's water, energy, and other stats")
    print("Water canteens can be found in an oasis or bought")
    print("There are also other hidden features too! Good luck!")
    print("By Matthew A. for CSP")

while not done:
    if random.randint(1, 10000) == 1:
        ufo()
        breaktest = True
    if breaktest:
        break
    if camelMiles >= 100 and not continueGame:
        print("\n" * 10 + "You have crossed 100 miles!")
        print("You have won the game! Congrats!")
        print("Do you want to continue to the moon?")
        print("Y] Yes")
        print("N] No")
        yesNoInput = input().strip().lower()
        if yesNoInput == "n" or yesNoInput == "no":
            print("Thanks for playing!")
            win()
        else:
            print("\n" * 10 + "-" * 30 + "\nThis will take a while but good luck i guess\n" + "-" * 30)
            continueGame = True

    if camelMiles >= 238900:
        print("\n" * 10 + "After 238900 miles...")
        print("You have won the moon ending!")
        win()

    print("\n" * 10)
    print("-" * 30)

    if replenishedDays > 0:
        print("** Gatorade power-up active for {} more turns!".format(replenishedDays))
        water, energy = 100, 100
    if days >= 15 and horseShoeTier == 0: print("// WARNING // Buy an upgrade soon!")
    if water < 32: print("// WARNING // Low water!")
    if energy < 32: print("// WARNING // Low energy!")
    print("* Day {}".format(days))
    print("* You have travelled {} miles".format(camelMiles))
    if days > 2: print("* The natives are {} miles behind you".format(camelMiles - nativeMiles))
    if ip:
        print("* You gained ${}".format(math.trunc(interest)), "from interest!")
    if cp:
        print("* Your canteen speed boost today was {:.2f}%".format(cb))
    print("* ${}".format(money))
    print("1] DRINK from your canteen")
    print("2] Ahead MODERATE SPEED")
    print("3] Ahead FULL SPEED")
#    print("4] Risky GAMBLE")
    print("5] STOP for the night")
    print("6] INVENTORY")
    print("7] UPGRADE menu")
    print("8] STATUS check")
    print("9] QUIT")
    userInput = input("\nChoose your option: ").lower().strip()

    print("\n" * 8)
    print("-" * 30)

    if userInput == "1" or userInput.lower().strip() == "drink":
        if not cap:
            camel_drink(40)
        else:
            camel_drink(60)
    elif userInput == "2" or userInput.lower().strip() == "moderatespeed":
        camel_run(1 * speedMult * cb, 20, 15)
    elif userInput == "3" or userInput.lower().strip() == "fullspeed":
        camel_run(2 * speedMult * cb, 30, 30)
#    elif userInput == "4" or userInput.lower().strip() == "gamble":
#        gamble()
    elif userInput == "5" or userInput.lower().strip() == "stop":
        camel_rest()
    elif userInput == "6" or userInput.lower().strip() == "inventory":
        use_item()
    elif userInput == "7" or userInput.lower().strip() == "upgrade":
        upgrade_menu()
    elif userInput == "8" or userInput.lower().strip() == "status":
        camel_status()
    elif userInput == "9" or userInput.lower().strip() == "quit":
        print("You travelled {} miles that game!\nThanks for playing!".format(camelMiles))
        done = True
