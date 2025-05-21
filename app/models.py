# app/models.py
from app import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    #platform = db.Column(db.String(50))
    #platform = db.Column(db.String(50))
    status = db.Column(db.String(50))  # e.g., "Not Started", "Playing", "Completed"
    hours_played = db.Column(db.Integer, nullable=True)  # Optional: For chart grouping
    #steam_id = db.Column(db.String(50), nullable=True)     # Optional: Steam integration
    #rawg_id = db.Column(db.String(50), nullable=True)
    #hltb_id = db.Column(db.String(50), nullable=True)
