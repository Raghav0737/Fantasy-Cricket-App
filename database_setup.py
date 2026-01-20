import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("fantasy.db")
cursor = conn.cursor()

# ---------------- PLAYERS TABLE ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    name TEXT PRIMARY KEY,
    role TEXT,
    value INTEGER
)
""")

# ---------------- TEAMS TABLE ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS teams (
    team_name TEXT PRIMARY KEY,
    players TEXT,
    points INTEGER
)
""")

# ---------------- MATCH STATS TABLE ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS match_stats (
    match_id INTEGER,
    player TEXT,
    runs INTEGER,
    balls INTEGER,
    fours INTEGER,
    sixes INTEGER,
    wickets INTEGER,
    overs REAL,
    runs_given INTEGER,
    catches INTEGER,
    stumpings INTEGER,
    runouts INTEGER
)
""")


# ---------------- INSERT SAMPLE PLAYERS ----------------
players_data = [
    ("Virat Kohli", "BAT", 120),
    ("Rohit Sharma", "BAT", 110),
    ("Shikhar Dhawan", "BAT", 100),
    ("Jasprit Bumrah", "BOW", 120),
    ("Mohammed Shami", "BOW", 110),
    ("Yuzvendra Chahal", "BOW", 100),
    ("Ravindra Jadeja", "AR", 110),
    ("Hardik Pandya", "AR", 105),
    ("MS Dhoni", "WK", 100),
    ("Rishabh Pant", "WK", 105),
    ("Ruturaj", "BAT", 115),
    ("Ishan Kishan", "WK", 100),
    ("Dinesh Karthik", "WK", 95),
    ("Heinrich Klaasen", "WK", 105),
    ("Suryakumar Yadav", "BAT", 120),
    ("Tilak Varma", "BAT", 100),
    ("Devon Conway", "BAT", 110),
    ("Rajat Patidar", "BAT", 95),
    ("Shreyas Iyer", "BAT", 105),
    ("Rinku Singh", "BAT", 100),
    ("Kane Williamson", "BAT", 110),
    ("Rahul Tripathi", "BAT", 95),
    ("Abhishek Sharma", "BAT", 100),
    ("Kieron Pollard", "AR", 105),
    ("Ravindra Jadeja", "AR", 115),
    ("Shivam Dube", "AR", 95),
    ("Glenn Maxwell", "AR", 115),
    ("Washington Sundar", "AR", 100),
    ("Sunil Narine", "AR", 110),
    ("Rahul Chahar", "BOW", 95),
    ("Jasprit Bumrah", "BOW", 120),
    ("Trent Boult", "BOW", 115),
    ("Piyush Chawla", "BOW", 90),
    ("Deepak Chahar", "BOW", 105),
    ("Matheesha Pathirana", "BOW", 110),
    ("Josh Hazlewood", "BOW", 110),
    ("Harshal Patel", "BOW", 100),
    ("Varun Chakravarthy", "BOW", 105),
    ("Harshit Rana", "BOW", 95),
    ("Bhuvneshwar Kumar", "BOW", 110),
    ("Umran Malik", "BOW", 95)
]


cursor.executemany(
    "INSERT OR IGNORE INTO players VALUES (?, ?, ?)",
    players_data
)

# ---------------- INSERT MATCH STATS ----------------
match_data = [
    (1, "Virat Kohli", 85, 60, 8, 2, 0, 0.0, 0, 1, 0, 0),
    (1, "Rohit Sharma", 45, 35, 5, 1, 0, 0.0, 0, 0, 0, 0),
    (1, "Shikhar Dhawan", 30, 25, 4, 0, 0, 0.0, 0, 0, 0, 0),
    (1, "Jasprit Bumrah", 5, 10, 0, 0, 3, 4.0, 18, 0, 0, 0),
    (1, "Mohammed Shami", 10, 8, 1, 0, 2, 4.0, 22, 0, 0, 0),
    (1, "Yuzvendra Chahal", 8, 6, 1, 0, 2, 4.0, 20, 0, 0, 0),
    (1, "Ravindra Jadeja", 35, 28, 3, 1, 1, 4.0, 24, 1, 0, 0),
    (1, "Hardik Pandya", 28, 20, 2, 1, 1, 3.0, 18, 0, 0, 0),
    (1, "MS Dhoni", 40, 30, 3, 1, 0, 0.0, 0, 2, 1, 0),
    (1, "Rishabh Pant", 50, 32, 4, 2, 0, 0.0, 0, 1, 0, 0),
    (1, "Ishan Kishan", 48, 32, 6, 2, 0, 0, 0, 1, 0, 0),
    (1, "Suryakumar Yadav", 72, 40, 8, 4, 0, 0, 0, 1, 0, 0),
    (1, "Tilak Varma", 38, 28, 3, 1, 0, 0, 0, 0, 0, 0),
    (1, "Kieron Pollard", 25, 16, 2, 2, 1, 2, 18, 0, 0, 0),
    (1, "Ruturaj Gaikwad", 64, 45, 7, 2, 0, 0, 0, 1, 0, 0),
    (1, "Devon Conway", 55, 42, 6, 1, 0, 0, 0, 0, 0, 0),
    (1, "Shivam Dube", 42, 25, 2, 3, 0, 0, 0, 0, 0, 0),
    (1, "Ravindra Jadeja", 32, 22, 2, 1, 2, 4, 24, 1, 0, 0),
    (1, "Deepak Chahar", 5, 6, 0, 0, 2, 4, 26, 0, 0, 0),
    (1, "Matheesha Pathirana", 2, 4, 0, 0, 3, 4, 20, 0, 0, 0),
    (1, "Virat Kohli", 68, 50, 6, 2, 0, 0, 0, 1, 0, 0),
    (1, "Rajat Patidar", 40, 30, 4, 1, 0, 0, 0, 0, 0, 0),
    (1, "Glenn Maxwell", 30, 18, 2, 2, 1, 2, 15, 1, 0, 0),
    (1, "Dinesh Karthik", 28, 12, 2, 2, 0, 0, 0, 1, 0, 0),
    (1, "Harshal Patel", 6, 8, 0, 0, 2, 4, 28, 0, 0, 0),
    (1, "Josh Hazlewood", 4, 6, 0, 0, 2, 4, 22, 0, 0, 0),
    (1, "Shreyas Iyer", 52, 38, 5, 1, 0, 0, 0, 1, 0, 0),
    (1, "Rinku Singh", 34, 16, 2, 3, 0, 0, 0, 0, 0, 0),
    (1, "Sunil Narine", 22, 14, 2, 1, 2, 4, 23, 1, 0, 0),
    (1, "Varun Chakravarthy", 3, 5, 0, 0, 2, 4, 21, 0, 0, 0),
    (1, "Harshit Rana", 1, 3, 0, 0, 1, 3, 18, 0, 0, 0),
    (1, "Abhishek Sharma", 46, 28, 4, 3, 0, 0, 0, 0, 0, 0),
    (1, "Kane Williamson", 44, 36, 4, 1, 0, 0, 0, 1, 0, 0),
    (1, "Rahul Tripathi", 35, 24, 3, 1, 0, 0, 0, 0, 0, 0),
    (1, "Washington Sundar", 18, 14, 1, 1, 1, 3, 20, 1, 0, 0),
    (1, "Bhuvneshwar Kumar", 2, 5, 0, 0, 2, 4, 24, 0, 0, 0),
    (1, "Rahul Chahar", 4, 6, 0, 0, 2, 4, 25, 0, 0, 0),
    (1, "Jasprit Bumrah", 6, 8, 0, 0, 3, 4, 18, 0, 0, 0),
    (1, "Trent Boult", 3, 4, 0, 0, 2, 4, 20, 0, 0, 0),
    (1, "Piyush Chawla", 5, 7, 0, 0, 1, 4, 28, 0, 0, 0),
    (1, "Heinrich Klaasen", 58, 34, 5, 3, 0, 0, 0, 1, 0, 0),
    (1, "Umran Malik", 2, 5, 0, 0, 1, 4, 30, 0, 0, 0),
]


cursor.executemany("""
INSERT INTO match_stats VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", match_data)


conn.commit()
conn.close()

print("Database created and sample data inserted successfully.")
