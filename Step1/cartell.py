import os
import json
import re
from datetime import date

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "CartellDB.json")


if not os.path.exists(DB_PATH):
    with open(DB_PATH, "w") as f:
        json.dump([], f, indent=4)



def get_vehicles():
    with open(DB_PATH, "r") as f:
        vehicles = json.load(f)
    if not vehicles:
        print("Vehicle list is empty")
        return
    for vehicle in vehicles:
        print(json.dumps(vehicle, indent=4))

def get_vehicle_by_id():
    vehicle_id = input("Enter car ID:\n")
    if not vehicle_id.isdigit():
        print("Error: must be a number")
        return
    vehicle_id = int(vehicle_id)

    with open(DB_PATH, "r") as f:
        vehicles = json.load(f)

    for vehicle in vehicles:
        if vehicle.get("id") == vehicle_id:
            print(json.dumps(vehicle, indent=4))
            return
    print("Vehicle not found")

def add_vehicle(username):
    while True:
        car_id = input("Enter car ID:\n")
        if not car_id.isdigit():
            print("Error: ID must be a number")
            continue
        car_id = int(car_id)

        with open(DB_PATH, "r") as f:
            vehicles = json.load(f)

        if any(vehicle.get("id") == car_id for vehicle in vehicles):
            print("Error: car already exists")
            continue

        color = input("Enter car color:\n")
        company = input("Enter car company:\n")
        car_year = input("Enter car year of manufacture:\n")
        if not car_year.isdigit():
            print("Error: year must be a number")
            continue
        car_year = int(car_year)

        car_country = input("Enter car country of manufacture:\n")
        is_first_hand = input("Is the car first hand? (yes/no):\n").lower()
        if is_first_hand not in ["yes", "no"]:
            print("Error: answer must be 'yes' or 'no'")
            continue

        owners = []
        if is_first_hand == "no":
            owners_input = input("Enter previous owners separated by commas:\n")
            owners = [o.strip() for o in owners_input.split(",") if o.strip()]

        new_vehicle = {
            "id": car_id,
            "color": color,
            "company": company,
            "Manufacture": {
                "year": car_year,
                "country": car_country
            },
            "isFirstHand": is_first_hand == "yes",
            "date": date.today().strftime("%d/%m/%Y"),
            "user": username
        }

        if owners:
            new_vehicle["owners"] = owners

        vehicles.append(new_vehicle)

        with open(DB_PATH, "w") as f:
            json.dump(vehicles, f, indent=4)

        print("Vehicle added successfully!")

        add_again = input("Do you want to add another car? (yes/no)\n").strip().lower()
        if add_again != "yes":
            break



def main():
    tries = 0

  
    while True:
        username = input("Enter your username (Firstname_l):\n")
        if re.match(r"^[A-Z][a-z]+_[a-z]$", username):
            break
        else:
            print("Invalid format. Please use Firstname_l (e.g., Ilai_d)")

    while True:
        options = input(
            "Choose an option:\n"
            "1: Show all vehicles\n"
            "2: Get vehicle by ID\n"
            "3: Add a new vehicle\n"
            "Type 'exit' to quit\n"
        ).strip()

        if options == "1":
            get_vehicles()
        elif options == "2":
            get_vehicle_by_id()
        elif options == "3":
            add_vehicle(username)
        elif options.lower() == "exit":
            print("Exiting the system, goodbye")
            break
        else:
            print("Invalid option, try again")
            tries += 1

        if tries >= 5:
            print("Too many invalid attempts. System terminating for security reasons.")
            break

if __name__ == "__main__":
    main()
