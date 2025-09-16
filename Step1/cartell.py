import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "CartellDB.txt")

if not os.path.exists(DB_PATH):
    with open(DB_PATH, "w") as f:
        f.write("")
