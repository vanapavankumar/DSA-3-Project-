import sqlite3
import csv

DB_PATH = "database/patents.db"
CSV_PATH = "patent_dataset_10000.csv"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

with open(CSV_PATH, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    inserted = 0
    skipped = 0

    for row in reader:
        try:
            cursor.execute("""
                INSERT INTO patents
                (patent_id, title, abstract, claims, technology, year)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                row["patent_id"],
                row["title"],
                row["abstract"],
                row["claims"],
                row["technology"],
                int(row["year"])
            ))

            inserted += 1

        except sqlite3.IntegrityError:
            skipped += 1

connection.commit()
connection.close()

print("Import completed!")
print("Inserted:", inserted)
print("Skipped:", skipped)