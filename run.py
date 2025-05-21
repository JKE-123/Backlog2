# run.py
from app import app, db

# Safe to remove this after initialization
#@app.route('/init-db')
#def init_db():
#  db.create_all()
#  return "Database initialized."

from threading import Thread
from flask import Flask
from app.notion_sync import sync_games  # or wherever sync_games is defined

from notion_sync import sync_games  # import the function correctly

@app.route('/sync-to-notion')
def sync_to_notion():
    try:
        sync_games()
        return "Notion sync successful", 200
    except Exception as e:
        print(f"❌ Error during Notion sync: {e}")
        return "Error syncing to Notion", 500