import random

choices = ["ROCK","PAPER","SCISSORS"]


Mychoice = input("What is your choice")
print(f"Computer select:{Mychoice}")

computerChoice = random.choice(choices)
print(f"Computer select:{computerChoice}")

if(computerChoice == Mychoice):
    print("tied")
elif(computerChoice == "ROCK" and Mychoice == "ROCK"):
    print("tied")
elif(computerChoice == "PAPER" and Mychoice == "PAPER"):
    print("tied")
elif(computerChoice == "SCISSORS" and Mychoice == "SCISSORS"):
    print("tied")
elif(computerChoice == "ROCK" and Mychoice == "PAPER"):
    print ("i win")
elif(computerChoice == "PAPER" and Mychoice == "SCISSORS"):
    print ("I win")
elif (computerChoice == "SCISSORS" and Mychoice == "ROCK"):
    print ("I win")
elif(computerChoice == "SCISSORS" and Mychoice == "PAPER"):
    print ("I lose")
elif(computerChoice == "ROCK" and Mychoice == "SCISSORS"):
    print("I lose")
elif(computerChoice == "PAPER" and Mychoice == "ROCK"):
    print("I lose")

else:
    print("Something went wrong")

