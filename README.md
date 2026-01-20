# Fantasy-Cricket-App

🏏 Fantasy Cricket Game – Python Project
📌 Project Description

The Fantasy Cricket Game is a Python-based desktop application developed using Tkinter for the graphical user interface and SQLite for persistent data storage. The application allows users to create a fantasy cricket team within a fixed points limit and evaluate team performance based on real cricket match statistics.

The project simulates the core working of real fantasy cricket platforms such as Dream11 by enforcing player selection rules, point limits, and performance-based scoring.

🎯 Objectives of the Project :-

1) To design a database-driven fantasy sports application
2) To apply Python programming concepts in a real-world scenario
3) To integrate GUI, database, and business logic
4) To calculate fantasy points using batting, bowling, and fielding performance
5) To enforce team constraints and points limits

🛠 Technologies Used :-

Programming Language: Python 3
GUI Framework: Tkinter
Database: SQLite
IDE: Visual Studio Code

📂 Project Structure :-

│
├── main.py               # Main application file (GUI + logic)
├── database_setup.py     # Database creation and data insertion
├── fantasy.db            # SQLite database file
└── README.md             # Project documentation

🗄 Database Design :-

The project uses SQLite with the following tables:

1️⃣ Players Table :
Stores player details and fantasy value.
players(name, role, value)

2️⃣ Teams Table :
Stores user-created fantasy teams.
teams(team_name, players, points)

3️⃣ Match Stats Table
Stores match-wise performance data used for scoring.
match_stats(match_id, player, runs, balls, fours, sixes,
            wickets, overs, runs_given, catches, stumpings, runouts)

⚙ Application Features :-

1) Create a fantasy cricket team
2) Select players category-wise (BAT / BOW / AR / WK)
3) Enforce a 1000 points budget
4) Assign different fantasy values to players
5) Prevent team creation beyond budget
6) Calculate fantasy points based on:
    Batting performance
    Bowling performance
    Fielding contributions
7) Display player-wise and total team score
8) Store teams and match data persistently using SQLite

🧮 Fantasy Scoring Logic :-

Fantasy points are calculated using predefined rules:

Batting :-
  1 point per 2 runs
  Bonus for half-century and century
  Strike rate bonus
  Boundary bonus (fours and sixes)

Bowling :-
  Points per wicket
  Bonus for 3+ and 5+ wickets
  Economy rate bonus

Fielding :-
  Points for catches, stumpings, and run-outs

▶ How to Run the Project :-

1) Install Python 3.x
2) Open the project folder in terminal or VS Code
3) Run database setup
4) Run the application
 
📘 Learning Outcomes :-

1) Understanding of Python GUI development
2) Practical experience with SQLite databases
3) Implementation of real-world business logic
4) Debugging and error handling in Python
5) Designing scalable application architecture

✅ Conclusion

This project demonstrates the integration of Python programming, database management, and graphical user interfaces to build a realistic fantasy cricket application. The system closely follows real fantasy sports platforms by enforcing budget constraints and performance-based scoring, making it a complete and practical academic project.
