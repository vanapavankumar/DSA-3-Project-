import sqlite3
import json


connection = sqlite3.connect("database/patents.db")
cursor = connection.cursor()

with open("data/patents.json", "r", encoding="utf-8") as file:
    patents = json.load(file)

for patent in patents:
    cursor.execute("""
        INSERT OR REPLACE INTO patents
        (patent_id, title, abstract, claims, technology, year)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        patent["patent_id"],
        patent["title"],
        patent["abstract"],
        patent["claims"],
        patent["technology"],
        patent["year"]
    ))

connection.commit()

cursor.execute("SELECT COUNT(*) FROM patents")
count = cursor.fetchone()[0]

connection.close()

print("Patents inserted successfully!")
print("Total patents:", count)
