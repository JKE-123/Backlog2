# run.py
from app import app, db

# Safe to remove this after initialization
#@app.route('/init-db')
#def init_db():
#  db.create_all()
#  return "Database initialized."

from flask import Flask
from app.notion_sync import sync_games

@app.route('/sync-to-notion')
def sync_to_notion():
    try:
        sync_games()
        return "Sync to Notion completed successfully."
    except Exception as e:
        return f"Sync failed: {str(e)}", 500
