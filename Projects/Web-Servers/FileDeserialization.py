import json
import os
from pathlib import Path
from RandomFood import RandomFood

#  Locate and open file
myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'random_food.json')
data = open(myFilePath,)
 
# deserializing the data
data = json.load(data)
food:RandomFood = RandomFood(**data)

# Print data from the object
print(f"ID: {food.id}")
print(f"UID: {food.uid}")
print(f"description: {food.description}")
print(f"ingrdient: {food.ingredient}")
print(f"measurement: {food.measurement}")
