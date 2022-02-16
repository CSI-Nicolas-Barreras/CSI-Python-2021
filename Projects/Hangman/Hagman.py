import ssl
import urllib, json
from RandomFood import RandomFood
import urllib.request

def get_food():
    # This is discouraged but it will avoid certificate validation (prevents error)
    ssl._create_default_https_context = ssl._create_unverified_context

    foodsURL = "https://random-data-api.com/api/food/random_food"
        
    req = urllib.request.Request(foodsURL)
    requestData = json.loads(urllib.request.urlopen(req).read())

    food:RandomFood = RandomFood(**requestData)

    return (food.ingredient)

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
for step in Steps:
    print (step)


def getInput():
    invalid_characters= ("1","2","3","4","5","6","7","8","9","10",",","'","/","?","<",":",";",">",".","[","]","{","}","|","=","+","_","-",")","0","(","*","&","^","%","$","#","@","!","`","~")
   
    while(True):   
        letter = input("Choose letter")

        if(len(letter)!= 1):
            print("error")
            continue

        if(letter in invalid_characters):
            print("error")
            continue

        return letter

print(getInput())