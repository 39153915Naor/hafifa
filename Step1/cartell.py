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
        vehicles = json.load(f)  
        if not vehicles:
            print("List is empty")
            return
        for vehicle in vehicles:
            print(json.dumps(vehicle, indent=4))

def get_vehicle_by_id():
    vehicle_id = input("Insert car number\n")
    if not vehicle_id.isdigit():
        print("Error, must be number")
        return

    vehicle_id = int(vehicle_id)

  
    with open(DB_PATH, "r") as f:
            vehicles = json.load(f)  
  
    for vehicle in vehicles:
        if vehicle.get("id") == vehicle_id:
            print(json.dumps(vehicle, indent=4)) 
            return

    print("Not in list")

def add_vihicle():
    while True:
        car_num = input("Add car id\n")
        if not car_num.isdigit():
            print("Error: id must be number")
            return  

        
    with open(DB_PATH, "r") as f:
        vehicles = json.load(f)  
  
    for vehicle in vehicles:
        if vehicle.get("id") == vehicle_id:
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

        car_year = input("Add car year of manufacture\n")
        if not car_year.isdigit():
            print("Error: car year must be number")
            return
            
        car_country = input("Add car country of manufacture\n")
        if not car_country.isalpha():
            print("Error: car country must be word")
            return

        car_km = input("Add car km\n")
        if not car_km.isdigit():
            print("Error: car km must be number")
            return

        isFirstHand = input("is the car first hand?\n")
        if not isFirstHand.isalpha():
            print("Error: answer must be number")
            return
        if isFirstHand.lower() == no:
            car_owner = inpur("please enter previous owners\n")
            if not car_owner.isalpha():
                print("Error: answer must be number")
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
            get_vehicle_by_id()
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




        
