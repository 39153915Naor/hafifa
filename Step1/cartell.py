import os
import json

from datetime import date

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "CartellDB.json")

if not os.path.exists(DB_PATH):
    with open(DB_PATH, "w") as f:
        json.dump({}, f, indent=4)
    
def get_vehicles():
  with open(DB_PATH, "r") as f:
    data = json.load(f)
    if not data:
        print("List is empty")
        return
    for key,value in data.items():
        print(key, ":", value)

def get_vehicle_by_id():
    vehicle_id = input("Insert car number\n")
    if not vehicle_id.isdigit():
        print("Error, must be number")
    else:
        with open(DB_PATH, "r") as f:
            lines = f.readlines() 
            for line in lines:
                if line.startswith(vehicle_id + " "):
                    print(line.strip())
                    return
            print("Not in list")
          
def add_vihicle():
    while True:
        car_num = input("Add car number\n")
        if not car_num.isdigit():
            print("Error: car num must be number")
            return  

        
        with open(DB_PATH, "r") as f:
            lines = f.readlines()
            if any(line.startswith(car_num + " ") for line in lines):
                print("Error: car in file")
                return  

        company = input("Add car company\n")
        if not company.isalpha():
            print("Error: company must be word")
            return

        color = input("Add car color\n")
        if not color.isalpha():
            print("Error: color must be word")
            return

        car_year = input("Add car year\n")
        if not car_year.isdigit():
            print("Error: car year must be number")
            return

        car_km = input("Add car km\n")
        if not car_km.isdigit():
            print("Error: car km must be number")
            return

        
        with open(DB_PATH, "a") as f:
            f.write(car_num + " " + company + " " + color + " " + car_year + " " + car_km + "\n")
            print("Car added")

       
        add_again = input("Do you want to add another car? (yes/no)\n").strip().lower()
        if add_again != "yes":
            break


def main():
    tries = 0
    
    while True:
        options = input("Choose your choice\n 1: Show all vehicles.\n 2: Get vehicle by number.\n 3: Add a new vehicle.\n Type exit to quit\n")
        if options == "1":
            get_vehicles()
        elif options == "2":
            get_vehicle_by_id(vehicle_id)
        elif options == "3":
            add_vihicle()
        elif options.lower() == "exit":
            print("Exiting the system, goodbye")
            break
        else:
            print("Not avaidble, try again")
            tries +=1
        if tries >= 5:
            print("Too many invalid attempts. System terminating due to security concerns.")
            break
if __name__ == "__main__":
    main()




        
