'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
import random

headcount = 0
tailcount = 0

for i in range(50):
    a = random.randrange(0, 2)
    if a == 0:
        print("This flip's result was... heads!")
        headcount = headcount + 1
    else:
        print("This flip's result was... tails!")
        tailcount = tailcount + 1
print("The total amount of heads was:", headcount)
print("The total amount of tails was:", tailcount)





