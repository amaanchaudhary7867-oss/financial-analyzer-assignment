import sqlite3

# Connect to SQLite database file
conn = sqlite3.connect("analysis.db", check_same_thread=False)

cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS analysis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    query TEXT,
    result TEXT
)
""")

conn.commit()


# Save analysis result
def save_result(filename, query, result):

    cursor.execute(
        "INSERT INTO analysis (filename, query, result) VALUES (?, ?, ?)",
        (filename, query, result)
    )

    conn.commit()


# Retrieve analysis result
def get_result(result_id):

    cursor.execute(
        "SELECT * FROM analysis WHERE id=?",
        (result_id,)
    )

    return cursor.fetchone()