import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "CartellDB.txt")

if not os.path.exits(DB_PATH):
    with open(DB_PATH, "w") as f:
        f.write("")
        
def get_vehicles():
  with open(DB_PATH, "r") as f:
    lines = f.readlines() 
    for line in lines:
        print(line.strip())


def get_vehicle_by_id(<id>):
