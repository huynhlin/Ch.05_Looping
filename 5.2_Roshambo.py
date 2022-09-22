'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits print an end game message and their win/loss/tie record

'''

import random

print("Let's play rock paper scissors. Type 1 for rock, 2 for paper, and 3 for scissors. Enter a 4 at any time if you would like to quit.")

q = False
wincount = 0
losscount = 0
tiecount = 0

while q == False:
    pc = random.randrange(1, 4)
    uc = int(input("What is your choice?"))
    if uc == 1:
        print("Your choice is rock.")
        if pc == 2:
            losscount = losscount+1
            print("The computer chose paper. That means one point for the computer! You now have:",losscount,
                  "losses! Better luck next time.")
            print("Onto the next round!")
        elif pc == 3:
            wincount = wincount+1
            print("The computer chose scissors. According to the rules that nets you one more point! You now have:",wincount,
                  "wins! Congratulations player, you'll be in the big leagues in no time.")
            print("Onto the next round!")
        else:
            tiecount = tiecount+1
            print("The computer chose rock. Jinx! You guys tied! There have been:",tiecount,
                  "ties this session. Try being a little more original.")
            print("Onto the next round!")
    elif uc == 2:
        print("Your choice is paper.")
        if pc == 3:
            losscount = losscount+1
            print("The computer chose scissors. That means one point for the computer! You now have:",losscount,
                  "losses! Better luck next time.")
            print("Onto the next round!")
        elif pc == 2:
            tiecount = tiecount+1
            print("The computer chose paper. Jinx! You guys tied! There have been:",tiecount,
                  "ties this session. Try being a little more original.")
            print("Onto the next round!")
        else:
            wincount = wincount+1
            print("The computer chose rock. According to the rules that nets you one more point! You now have:",wincount,
                  "wins! Congratulations player, you'll be in the big leagues in no time.")
            print("Onto the next round!")

    elif uc == 3:
        print("Your choice is scissors.")
        if pc == 2:
            wincount = wincount + 1
            print("The computer chose paper. According to the rules that nets you one more point! You now have:",
                  wincount, "wins! Congratulations player, you'll be in the big leagues in no time.")
            print("Onto the next round!")
        elif pc == 3:
            tiecount = tiecount + 1
            print("The computer chose scissors. Jinx! You guys tied! There have been:", tiecount,
                  "ties this session. Try being a little more original.")
            print("Onto the next round!")
        else:
            losscount = losscount + 1
            print("The computer chose rock. That means one point for the computer! You now have:", losscount,
                  "losses! Better luck next time.")
            print("Onto the next round!")
    else:
        if wincount == 0 and losscount == 0 and tiecount == 0:
            print("You didn't even play! Try your luck before quitting.")
        else:
            winrate = wincount/(losscount+wincount)
            percent = winrate*100
            print("Thank you for playing. You had a total of:", wincount,"wins,",losscount,"losses, and",tiecount,
                  "ties. That adds up to a winrate of:",percent,"percent. Thanks for playing!")
