BG_COLOR = "#0b3d2e"      # Dark cricket green
CARD_COLOR = "#145a32"    # Panel green
ACCENT = "#f4d03f"        # Gold
TEXT_COLOR = "white"
FONT_TITLE = ("Segoe UI", 18, "bold")
FONT_LABEL = ("Segoe UI", 11)
FONT_BUTTON = ("Segoe UI", 10, "bold")

import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

class FantasyCricketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fantasy Cricket League")
        self.root.geometry("900x550")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)


        self.team_name = None
        self.selected_players = []
        self.points_available = 1000
        self.points_used = 0

        self.create_menu()
        self.create_header()      
        self.create_widgets()
        self.conn = sqlite3.connect("fantasy.db")
        self.cursor = self.conn.cursor()



    def create_menu(self):
        menubar = tk.Menu(self.root)
        team_menu = tk.Menu(menubar, tearoff=0)

        team_menu.add_command(label="New Team", command=self.new_team)
        team_menu.add_command(label="Save Team", command=self.save_team)
        team_menu.add_command(label="Evaluate Team", command=self.evaluate_team)

        menubar.add_cascade(label="Manage Teams", menu=team_menu)
        self.root.config(menu=menubar , bg = BG_COLOR)


    def create_header(self):
         header = tk.Frame(self.root, bg=ACCENT, height=60)
         header.pack(fill="x")

         title = tk.Label(
    header,
        text="Fantasy Cricket League",
        bg=ACCENT,
        fg="black",
        font=FONT_TITLE
    )
         title.pack(pady=10)

    
    def create_widgets(self):

      info_frame = tk.Frame(self.root, bg=BG_COLOR)
      info_frame.pack(pady=10)

      self.team_label = tk.Label(
        info_frame,
        text="Team: Not Created",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=FONT_LABEL
    )
      self.team_label.grid(row=0, column=0, padx=20)

      self.points_label = tk.Label(
        info_frame,
        text="Points Available: 1000 | Used: 0",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=FONT_LABEL
    )
      self.points_label.grid(row=0, column=1, padx=20)

      main_frame = tk.Frame(self.root, bg=BG_COLOR)
      main_frame.pack(pady=15)

    # CATEGORY PANEL
      cat_frame = tk.LabelFrame(
        main_frame,
        text=" Player Categories ",
        bg=CARD_COLOR,
        fg=ACCENT,
        font=FONT_BUTTON,
        padx=15,
        pady=15
    )
      cat_frame.grid(row=0, column=0, padx=15)

      self.category = tk.StringVar()
      for cat in ["BAT", "BOW", "AR", "WK"]:
        tk.Radiobutton(
            cat_frame,
            text=cat,
            value=cat,
            variable=self.category,
            command=self.load_players,
            bg=CARD_COLOR,
            fg=TEXT_COLOR,
            selectcolor=CARD_COLOR,
            font=FONT_LABEL
        ).pack(anchor="w")

    # AVAILABLE PLAYERS
      left_frame = tk.LabelFrame(
        main_frame,
        text=" Available Players ",
        bg=CARD_COLOR,
        fg=ACCENT,
        font=FONT_BUTTON,
        padx=10,
        pady=10
    )
      left_frame.grid(row=0, column=1, padx=15)

      self.available_list = tk.Listbox(
        left_frame,
        width=30,
        height=15,
        font=FONT_LABEL
    )
      self.available_list.pack()
      self.available_list.bind("<Double-Button-1>", self.add_player)

    # SELECTED PLAYERS
      right_frame = tk.LabelFrame(
        main_frame,
        text=" Selected Team ",
        bg=CARD_COLOR,
        fg=ACCENT,
        font=FONT_BUTTON,
        padx=10,
        pady=10
    )
      right_frame.grid(row=0, column=2, padx=15)

      self.selected_list = tk.Listbox(
        right_frame,
        width=30,
        height=15,
        font=FONT_LABEL
    )
      self.selected_list.pack()
      self.selected_list.bind("<Double-Button-1>", self.remove_player)

    
    def new_team(self):
        name = simpledialog.askstring("New Team", "Enter Team Name:")
        if not name:
            return

        self.team_name = name
        self.team_label.config(text=f"Team Name: {name}")
        self.selected_players.clear()
        self.available_list.delete(0, tk.END)
        self.selected_list.delete(0, tk.END)
        self.points_available = 1000
        self.points_used = 0
        self.update_points()
    
    
    def load_players(self):
     if not self.team_name:
        messagebox.showerror("Error", "Create a team first")
        return

     self.available_list.delete(0, tk.END)

     category = self.category.get()

     self.cursor.execute(
        "SELECT name FROM players WHERE role = ?",
        (category,)
    )

     players = self.cursor.fetchall()

     for player in players:
        self.available_list.insert(tk.END, player[0])


    
    def add_player(self, event):
     if len(self.selected_players) >= 11:
        messagebox.showerror("Error", "Only 11 players allowed")
        return

     player = self.available_list.get(tk.ACTIVE)
     if not player or player in self.selected_players:
        return

    # Fetch player value from database
     self.cursor.execute(
        "SELECT value FROM players WHERE name = ?",
        (player,)
    )
     result = self.cursor.fetchone()

     if not result:
        messagebox.showerror("Error", "Player value not found")
        return

     player_value = result[0]

    # Check remaining points
     if self.points_used + player_value > 1000:
        messagebox.showerror("Error", "Not enough points available")
        return

    # Add player
     self.selected_players.append(player)
     self.selected_list.insert(tk.END, f"{player} ({player_value})")

     self.points_used += player_value
     self.update_points()


    def remove_player(self, event):
     selection = self.selected_list.curselection()
     if not selection:
        return

     index = selection[0]
     entry = self.selected_list.get(index)

    # Extract player name (before '(')
     player = entry.split(" (")[0]

    # Fetch player value
     self.cursor.execute(
        "SELECT value FROM players WHERE name = ?",
        (player,)
    )
     result = self.cursor.fetchone()
     if not result:
        return

     player_value = result[0]

     self.selected_list.delete(index)
     self.selected_players.remove(player)

     self.points_used -= player_value
     self.update_points()

    
    def update_points(self):
     remaining = 1000 - self.points_used
     self.points_label.config(
        text=f"Points Available: {remaining} | Used: {self.points_used}"
    )

    
    def evaluate_team(self):
     if len(self.selected_players) != 11:
        messagebox.showerror("Error", "Team must have exactly 11 players")
        return

    # Popup window
     eval_window = tk.Toplevel(self.root)
     eval_window.title("Match Evaluation")
     eval_window.geometry("500x450")
     eval_window.configure(bg=BG_COLOR)
     eval_window.resizable(False, False)

    # Title
     tk.Label(
        eval_window,
        text="Fantasy Team Score",
        bg=BG_COLOR,
        fg=ACCENT,
        font=FONT_TITLE
    ).pack(pady=10)

    # Score list frame
     list_frame = tk.Frame(eval_window, bg=CARD_COLOR, padx=10, pady=10)
     list_frame.pack(pady=10)

     score_list = tk.Listbox(
        list_frame,
        width=45,
        height=12,
        font=FONT_LABEL
    )
     score_list.pack()
     
     total_score = 0
     
     for player in self.selected_players:
         # Fetch match stats from database
         self.cursor.execute("""
                             SELECT runs, balls, fours, sixes, wickets, overs,
                             runs_given, catches, stumpings, runouts
                             FROM match_stats
                             WHERE player = ?
                             """, (player,))
         
         stats = self.cursor.fetchone()
         
         if stats:
            player_score = self.calculate_player_score(stats)
            total_score += player_score
            score_list.insert(tk.END, f"{player:<20} {player_score} pts")
         else:
            score_list.insert(tk.END, f"{player:<20} 0 pts")     


    # Total score display
     tk.Label(
        eval_window,
        text=f"Total Score : {total_score}",
        bg=BG_COLOR,
        fg=ACCENT,
        font=("Segoe UI", 14, "bold")
    ).pack(pady=15)
     
     
    def calculate_player_score(self, stats):
         runs, balls, fours, sixes, wickets, overs, runs_given, catches, stumpings, runouts = stats
         score = 0
         
         # Batting
         score += runs // 2
         if runs >= 50:
          score += 5
         if runs >= 100:
          score += 10
          
          if balls > 0:
           strike_rate = (runs / balls) * 100
           if 80 <= strike_rate <= 100:
            score += 2
           elif strike_rate > 100:
            score += 4
            
            score += fours * 1
            score += sixes * 2
            
            # Bowling
            score += wickets * 10
            if wickets >= 3:
             score += 5
            if wickets >= 5:
             score += 10
             
             if overs > 0:
              economy = runs_given / overs
             if economy < 2:
              score += 10
             elif 2 <= economy < 3.5:
              score += 7
             elif 3.5 <= economy <= 4.5:
              score += 4
             
             # Fielding
             score += (catches + stumpings + runouts) * 10

         return score


    
    def save_team(self):
     if not self.team_name:
        messagebox.showerror("Error", "No team to save")
        return

     if len(self.selected_players) != 11:
        messagebox.showerror("Error", "Team must have 11 players")
        return

     players_str = ",".join(self.selected_players)

     self.cursor.execute(
        "INSERT OR REPLACE INTO teams VALUES (?, ?, ?)",
        (self.team_name, players_str, self.points_used)
    )
     self.conn.commit()

    messagebox.showinfo("Success", "Team saved successfully")
    
    
    def open_team(self, team_name):
     self.cursor.execute(
        "SELECT players FROM teams WHERE team_name = ?",
        (team_name,)
    )
     data = self.cursor.fetchone()

     if data:
        self.selected_players = data[0].split(",")
        
        
        
        



if __name__ == "__main__":
    root = tk.Tk()
    app = FantasyCricketApp(root)
    root.mainloop()
