import csv
import re
from collections import defaultdict

DATA = [
    ["03-06-2025", "Total Lunch", "0 - Thin", 1,1,1,1,1,1],
    ["03-06-2025", "Total Dinner", "6 - Soft and Bite-sized", 0,0,0,0,0,0],
    ["03-06-2025", "Total Dinner", "4 - Extremely thick", 0,0,0,0,0,0],
    ["03-06-2025", "Total Dinner", "5 - Minced and Moist", 0,0,0,0,0,0],
    ["03-06-2025", "Total Dinner", "7 - Easy to Chew", 0,0,0,0,0,0],
    ["03-06-2025", "Total Lunch", "7 - Regular", 0,0,0,0,0,0],
    ["03-06-2025", "Total Lunch", "4 - Pureed", 0,0,0,0,0,0],
    ["03-06-2025", "Total Lunch", "2 - Mildly thick", 0,0,0,0,0,0],
    ["03-06-2025", "Total Dinner", "0 - Thin", 0,0,0,0,0,0],
    ["03-06-2025", "Total Dinner", "1 - Slightly thick", 2,2,2,2,2,2],
]

def diet_number(text):
    m = re.match(r"(\d+)", text)
    return int(m.group(1)) if m else 0

# Sort by date, then unit, then numeric part of diet_texture
sorted_rows = sorted(DATA, key=lambda r: (r[0], r[1], diet_number(r[2])))

# Group by date and unit for display
grouped = defaultdict(list)
for row in sorted_rows:
    grouped[(row[0], row[1])].append(row)

if __name__ == "__main__":
    for (date, unit), rows in grouped.items():
        print(f"{date}\t{unit}")
        for r in rows:
            print("\t" + "\t".join(str(x) for x in r[2:]))

