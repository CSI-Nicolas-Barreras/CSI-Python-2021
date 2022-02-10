import ssl
import urllib, json
from RandomFood import RandomFood
import urllib.request

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

foodsURL = "https://random-data-api.com/api/food/random_food"
    
req = urllib.request.Request(foodsURL)
requestData = json.loads(urllib.request.urlopen(req).read())

food:RandomFood = RandomFood(**requestData)

print (food.ingredient)

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

    