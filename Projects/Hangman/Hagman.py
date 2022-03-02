
import ssl
import urllib, json
from RandomFood import RandomFood
import urllib.request

# used characters list
used=[]

# Giving a function to this code
def get_food():

# This is discouraged but it will avoid certificate validation (prevents error)
    ssl._create_default_https_context = ssl._create_unverified_context

# This is my URL from the Api provider
    foodsURL = "https://random-data-api.com/api/food/random_food"

# Request from URL to choose word    
    req = urllib.request.Request(foodsURL)
    requestData = json.loads(urllib.request.urlopen(req).read())
    food:RandomFood = RandomFood(**requestData)

    return food.ingredient.upper()

#Create variable to store the value of get_food()
myFood= get_food()

WrongLetters = []

print(len(myFood) * "_")

# Steps for Hangman
Steps= ["""
        /---------|
        |         |
        |
        |
        |
        |
    -------------------
""",
"""
        /---------|
        |         |
        |         O
        |
        |
        |
    -------------------


""",
"""
        /---------|
        |         |
        |         O
        |         |
        |
        |
    -------------------
""",
"""
        /---------|
        |         |
        |         O
        |        -|
        |
        |
    -------------------
""",
"""
        /---------|
        |         |
        |         O
        |        -|-
        |
        |
    ------------------- 
""",
"""
        /---------|
        |         |
        |         O
        |        -|-
        |        ( 
        |
    ------------------- 
""",
"""
        /---------|
        |         |
        |         O
        |        -|-
        |        ( )
        |
    ------------------- 
""",
"""
        /---------|
        |         |
        |         0
        |        -|-
        |        ( )
        |
    ------------------- 
""",
]


def getInput():
    invalid_characters= ("1","2","3","4","5","6","7","8","9","10",",","'","/","?","<",":",";",">",".","[","]","{","}","|","=","+","_","-",")","0","(","*","&","^","%","$","#","@","!","`","~")
   
    while(True):   
        letter = input("Choose letter=").upper()

        if(len(letter)!= 1):
            print("error")
            continue

        if(letter in invalid_characters):
            print("error")
            continue

        if letter in WrongLetters:
            print("Already guessed letter")

        used.append(letter)

        return letter



def printWord():
    temp:str=""

    for letter in myFood:
        if letter in used:
            temp= temp + letter
        else: 
            temp= temp + "_"
        


    print(temp)

    

def printStep():
    
    counter= 0
    for letter in used:
        if letter not in myFood:
            counter= counter + 1

    print(Steps[counter])


    
    
while True:
     printStep()
     getInput()
     printWord()

        
    
    

  

