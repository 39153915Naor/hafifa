import os
import json
import re
import sys
import logging
from datetime import date

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "CartellDB.json")
LOG_PATH = os.path.join(BASE_DIR, "cartellogs.txt")


if not os.path.exists(DB_PATH):
    with open(DB_PATH, "w") as f:
        json.dump([], f, indent=4)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format='%(asctime)s  %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)


def get_vehicles(username):
    try:
        with open(DB_PATH, "r") as f:
            vehicles = json.load(f)
        if not vehicles:
            print("Vehicle list is empty")
            logging.info(f"{username} user viewed all vehicles (empty list)")
            return
        for vehicle in vehicles:
            print(json.dumps(vehicle, indent=4))
        logging.info(f"{username} user viewed all {len(vehicles)} vehicles")
    except Exception as e:
        logging.error(f"{username} failed to view vehicles - {e}")
        print("Error reading vehicles")


def get_vehicle_by_id(username):
    try:
        vehicle_id = input("Enter car ID:\n").strip()
        if not vehicle_id.isdigit():
            print("Error: must be a number")
            logging.warning(f"{username} searched with invalid ID - {vehicle_id}")
            return
        vehicle_id = int(vehicle_id)

        with open(DB_PATH, "r") as f:
            vehicles = json.load(f)

        for vehicle in vehicles:
            if vehicle.get("id") == vehicle_id:
                print(json.dumps(vehicle, indent=4))
                logging.info(f"{username} searched car - {vehicle_id}")
                return

        print("Vehicle not found")
        logging.info(f"{username} searched car - {vehicle_id} (not found)")
    except Exception as e:
        logging.error(f"{username} failed to search vehicle - {e}")
        print("Error reading vehicles")


def add_vehicle(username):
    try:
        car_id = input("Enter car ID:\n").strip()
        if not car_id.isdigit():
            print("Error: ID must be a number")
            logging.warning(f"{username} entered invalid car ID - {car_id}")
            return
        car_id = int(car_id)

        with open(DB_PATH, "r") as f:
            vehicles = json.load(f)

        if any(vehicle.get("id") == car_id for vehicle in vehicles):
            print("Error: car already exists")
            logging.warning(f"{username} tried to add existing car ID - {car_id}")
            return

        color = input("Enter car color:\n").strip()
        company = input("Enter car company:\n").strip()
        car_year = input("Enter car year of manufacture:\n").strip()
        if not car_year.isdigit():
            print("Error: year must be a number")
            logging.warning(f"{username} entered invalid year - {car_year}")
            return
        car_year = int(car_year)

        car_country = input("Enter car country of manufacture:\n").strip()
        is_first_hand = input("Is the car first hand? (yes/no):\n").strip().lower()
        if is_first_hand not in ["yes", "no"]:
            print("Error: must answer 'yes' or 'no'")
            logging.warning(f"{username} entered invalid first-hand input - {is_first_hand}")
            return

        owners = []
        if is_first_hand == "no":
            owners_input = input("Enter previous owners separated by commas:\n").strip()
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
        logging.info(f"{username} user added car to collection - {car_id}")

    except Exception as e:
        logging.error(f"{username} failed to add vehicle - {e}")
        print("Error adding vehicle")


def main():
    tries = 0

    while tries < 5:
        username = input("Enter your username (Firstname_l):\n").strip()
        if re.match(r"^[A-Z][a-z]+_[a-z]$", username):
            logging.info(f"{username} user logged on")
            break
        else:
            print("Invalid format. Please use Firstname_l (e.g., Ilai_d)")
            logging.warning("UNKNOWN_USER user failed to logon - invalid username")
            tries += 1
    else:
        logging.error("System terminated after 5 invalid login attempts")
        print("Too many invalid attempts. System terminating.")
        sys.exit()

   
    while True:
        option = input(
            "\nChoose an option:\n"
            "1: Show all vehicles\n"
            "2: Get vehicle by ID\n"
            "3: Add a new vehicle\n"
            "Type 'exit' to quit\n"
        ).strip()
        if option == "1":
            get_vehicles(username)
        elif option == "2":
            get_vehicle_by_id(username)
        elif option == "3":
            add_vehicle(username)
        elif option.lower() == "exit":
            logging.info(f"{username} user logged off")
            print("Exiting the system, goodbye")
            break
        else:
            print("Invalid option, try again")
            logging.warning(f"{username} entered invalid menu option - {option}")


if __name__ == "__main__":
    main()
