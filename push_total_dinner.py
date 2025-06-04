import requests

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzSchUSKUoMqfVJvjvu91_gyEdP7kZVyVZA4jY10HE62f4ANgVhcTs-WBJZ1U8ogbySQg/exec"

# Data for Total Dinner
DATA = [
    ["03-06-2025", "0 - Thin", 0, 0, 0, 0, 0, 0],
    ["03-06-2025", "1 - Slightly thick", 2, 2, 2, 2, 2, 2],
    ["03-06-2025", "2 - Mildly thick", 0, 0, 0, 0, 0, 0],
    ["03-06-2025", "3 - Moderately thick", 0, 0, 0, 0, 0, 0],
    ["03-06-2025", "4 - Extremely thick", 0, 0, 0, 0, 0, 0],
    ["03-06-2025", "4 - Pureed", 0, 0, 0, 0, 0, 0],
    ["03-06-2025", "5 - Minced and Moist", 0, 0, 0, 0, 0, 0],
    ["03-06-2025", "6 - Soft and Bite-sized", 0, 0, 0, 0, 0, 0],
    ["03-06-2025", "7 - Easy to Chew", 0, 0, 0, 0, 0, 0],
    ["03-06-2025", "7 - Regular", 0, 0, 0, 0, 0, 0],
]

for row in DATA:
    form = {
        "date": row[0],
        "unit": "Total Dinner",
        "diet_texture": row[1],
        "soup": row[2],
        "meal1": row[3],
        "meal2": row[4],
        "vegetarian": row[5],
        "sideveg": row[6],
        "dessert": row[7],
    }
    resp = requests.post(GOOGLE_SCRIPT_URL, data=form)
    resp.raise_for_status()
    print(f"Sent {row[1]}: {resp.status_code}")
