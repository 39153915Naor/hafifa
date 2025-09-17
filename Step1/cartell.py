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


def get_vehicle_by_id(vehicle_id):
    vehicle_id = input("insert car number")
    if not vehicle_id.isdigit():
        print("error, must be number")
    else:
        with open(DB_PATH, "r") as f:
            lines = f.readlines() 
            for line in lines:
                if line.startswith(vehicle_id + " "):
                    print(line.strip())
                    return
                
    print("not in list")
        
        
