import random
done = False
score = 0
guess = 100
num = 0
tries = 0
totaltries = 0
print("Guess a number between one and one hundred.")
while not done:
    num = random.randrange(1,100)
    tries = 0
    while guess != num:
        guess = int(input("What's your guess?"))
        if guess > num:
            print("The number is a little lower.")
            tries += 1
        elif guess < num:
            print("The number is a little higher.")
            tries +=1
        else:
            print("Correct!")
            print("That took",tries,"tries!")
            score +=1
            totaltries += tries
            state = input("Would you like to play again? Type yes or no.")
            if state.lower().strip() == "no":
                done = True
print("The game is over. Your score was:", score, ". Your total number of tries was:", totaltries)
rate = totaltries/score
format_rate = "{:.2f}".format(rate)
print("The average amount of guesses per win was:", format_rate,)