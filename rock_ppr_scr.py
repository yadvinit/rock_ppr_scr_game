import random

print(" Game Rock Paper Scissors") 

game = ["rock","paper","scissors"]

play = input("want to play Yes or No").lower()
if play == "yes":

    choice = int(input("enter your choice rock paper scissore 1 2 3"))

    if choice > 3 or choice <1:
        print("wrong input")
    else:
        
        choice2 = random.randint(1,3)

        a = game[choice -1]
        print("you choose ",a)

        b=game[choice2-1]
        print("computer choose ",b)

        if a==b:
            print("draw")
        elif a == "rock" and b =="paper":
            print("computer won")
        elif a == "paper" and b == "scissors":
            print("computer won")
        elif a == "scissors" and b =="rock":
            print("computer won")
        else:
            print("you won")
else:
    print("see you soon")

