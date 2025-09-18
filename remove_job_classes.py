import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "main.db")

with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM job_classes")
    conn.commit()

print("All job_classes have been removed.")
