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

@app.route('/sync-to-notion')
def sync_to_notion():
    def run_sync():
        try:
            sync_games()
        except Exception as e:
            print(f"Sync failed: {e}")

    Thread(target=run_sync).start()
    return "✅ Notion sync started in background."