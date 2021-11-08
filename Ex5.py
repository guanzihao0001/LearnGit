import random
print("welcome to the Guessing Game")
print("")
again="y"
while(again=="y"):
    print("l'm thinking of a number between 1 and 100,try to guess it!")
    num = random.randint(1, 100)
    guess = -1
    sum = 0
    while (guess != num):
        sum = sum + 1
        print("your guess:", end="")
        guess = int(input())
        if guess > num:
            print("too high")
        elif guess < num:
            print("too low")
        else:
            break
    print("Congratulation,you guessed it in",sum,"guess(es)")
    print("Do you want to play again(enter 'y' or 'n'):",end="")
    again=input()
