from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI(title="Patent Prior Art Analytics Engine")

DATABASE = "database/patents.db"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def get_connection():
    return sqlite3.connect(DATABASE)

@app.get("/")
def home():
    return {"message": "Patent Analytics API is running"}

@app.get("/api/test")
def test():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM patents")
    count = cursor.fetchone()[0]
    connection.close()

    return {
        "status": "success",
        "message": "Database connection working",
        "total_patents": count
    }

@app.get("/api/search")
def search_patents(keyword: str):
    connection = get_connection()
    cursor = connection.cursor()

    search = f"%{keyword.lower()}%"

    cursor.execute("""
        SELECT patent_id, title, abstract, claims, technology, year
        FROM patents
        WHERE LOWER(title) LIKE ?
           OR LOWER(abstract) LIKE ?
           OR LOWER(claims) LIKE ?
           OR LOWER(technology) LIKE ?
    """, (search, search, search, search))

    rows = cursor.fetchall()
    connection.close()

    patents = []

    for row in rows:
        patents.append({
            "patent_id": row[0],
            "title": row[1],
            "abstract": row[2],
            "claims": row[3],
            "technology": row[4],
            "year": row[5]
        })

    return {
        "keyword": keyword,
        "count": len(patents),
        "results": patents
    }
@app.get("/api/stats")
def stats():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM patents")
    total_patents = cursor.fetchone()[0]

    cursor.execute("SELECT technology, COUNT(*) FROM patents GROUP BY technology")
    technologies = cursor.fetchall()

    cursor.execute("SELECT MIN(year), MAX(year) FROM patents")
    years = cursor.fetchone()

    connection.close()

    return {
        "total_patents": total_patents,
        "technologies": [
            {"technology": row[0], "count": row[1]}
            for row in technologies
        ],
        "year_range": {
            "from": years[0],
            "to": years[1]
        }
    }
