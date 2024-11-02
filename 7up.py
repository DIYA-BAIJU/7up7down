import random
def roll():
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    return die1+die2
print("welcome to 7 up 7 down game!!!!")
while True:
    guess=input("Guess the sum (7 Up, 7 Down, or 7): ").strip().lower()
    if guess not in ["7 up","7 down", "7"]:
        print("Invalid input ! \n Please choose '7 Up', '7 Down', or '7'.")
        continue
    sum=roll()
    print("the sum is : ",sum)
    if (sum > 7 and guess == "7 up") or (sum < 7 and guess == "7 down") or (sum == 7 and guess == "7"):
            print("Congratulations, you guessed correctly!")
    else:
        print("Sorry, your guess was wrong.")
    flag=input("play again? [y/n] : ")
    if flag=='n' or flag=='N':
        print("Goodbye !")
        break        