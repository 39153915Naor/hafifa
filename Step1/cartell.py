import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "CartellDB.txt")

if not os.path.exists(DB_PATH):
    with open(DB_PATH, "w") as f:
        f.write("")
        
def get_vehicles():
  with open(DB_PATH, "r") as f:
    lines = f.readlines() 
    for line in lines:
        print(line.strip())


def get_vehicle_by_id():
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


def add_vihicle():
    car_num = input("add car num")
    company = input("add car company")
    color = input("add car color")
    car_year = input("add car year")
    car_km = input("add car km")

    
    if not car_num.isdigit():
       print("Error: car num must be number")
       return
    elif not company.isalpha():
       print("Error: company must be word")
       return
    elif not color.isalpha():
        print("Error: color must be word")
        return
    elif not car_year.isdigit():
        print("Error: car year must be number")
        return
    elif not car_km.isdigit():
        print("Error: car km must be number")
        return
    with open(DB_PATH, "r") as f:
        lines = f.readlines() 
        for line in lines:
            if line.startswith(car_num + " "):
                print("Error: car in file")
                return
                
    with open(DB_PATH, "a") as f:
         f.write(car_num + " "company + " "color + " "car_year + " "car_km\n)
         print("car added")








        
