  #Sign your name: Lindy Huynh

'''
 1. Make the following program work.
   '''  
# print("This program takes three numbers and returns the sum.")
# total = 0
#
# for i in range(3):
#     x = float(input("Enter a number: "))
#     total = total + x
# print("The total is:", total)



'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
# for i in range(101):
#     if i % 2 == 0:
#         print(i)
#remember theres a step feature too
#format is (begin#,end#,step)
#step# = how much it counts down by

'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
# i = 11
# while i > 0:
#     i = i-1
#     print(i)
# print("Blast off!")

# i completely forgot how to do the i+- stuff


# '''
#   4. Write a program that prints a random integer from 1 to 10 (inclusive).
# '''
# import random
#
# b = random.randrange(1,11)
# print("Your random number is:",b)

#i highly doubt this was the intended solution but it works lol

'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''

poscount = 0
negcount = 0
zerocount = 0
q = int(input("First number?"))
w = int(input("Second number?"))
e = int(input("Third number?"))
r = int(input("Four number?"))
t = int(input("Fifth number?"))
y = int(input("Sixth number?"))
u = int(input("Seventh number?"))
uservars = [q, w, e, r, t, y, u]
print("The sum of your numbers is;",sum(uservars))

for x in uservars:
    if x > 0:
        poscount = poscount + 1
    elif x < 0:
        negcount = negcount + 1
    else:
        zerocount = zerocount + 1
print("You had",poscount,"positive entries.")
print("You had",negcount,"negative entries.")
print("You had",zerocount,"entries that were 0.")