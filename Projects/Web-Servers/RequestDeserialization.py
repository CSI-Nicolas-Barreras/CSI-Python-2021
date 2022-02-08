import json, ssl
import os
from pathlib import Path
import urllib.request
from RandomFood import RandomFood

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
foodsURL = "https://random-data-api.com/api/food/random_food?size=100"

#  Locate and open file
myPath = Path(__file__).parents[0]
myFolderPath = os.path.join(myPath, 'responses')
os.mkdir(myFolderPath)


# Create a list to populate with our data
foods:RandomFood = [] 

# Loop
for x in range(100):

    # Execute HTTP Request
    req = urllib.request.Request(foodsURL)
    requestData = json.loads(urllib.request.urlopen(req).read())

    # Loop over JSON items and Deserialize them into python objects
    for r in requestData:  
        # Deserialize 
        food:RandomFood = RandomFood(**r)
        # Add object to list
        foods.append(food) 
        # Print id
        print(food.uid)
    #Folder to save the 10,000 RandomFood
        outputPathFile = os.path.join(myFolderPath,f"{food.uid}.json")
        with open(outputPathFile,"w") as outfile:
            json.dump (food.__dict__, outfile)