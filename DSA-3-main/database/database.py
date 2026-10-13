import sqlite3


def create_database():
    connection = sqlite3.connect("database/patents.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patents (
            patent_id TEXT PRIMARY KEY,
            title TEXT,
            abstract TEXT,
            claims TEXT,
            technology TEXT,
            year INTEGER
        )
    """)

    connection.commit()
    connection.close()

    print("Database created successfully!")


if __name__ == "__main__":
    create_database()
