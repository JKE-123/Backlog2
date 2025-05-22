import logging
from notion_client import Client
import requests
import os
from app.routes import get_games

# Replace with your actual values
NOTION_TOKEN = os.getenv('NOTION_TOKEN', ' ')
DATABASE_ID = os.getenv('NOTION_DATABASE_ID', ' ')

# Initialize client
notion = Client(auth=NOTION_TOKEN)

def push_game_to_notion(game):
    notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties={
            "Title": {
                "title": [
                    {
                        "text": {"content": game["title"]}
                    }
                ]
            },
            "Status": {
                "select": {"name": game.get("status", "Not Started")}
            },
            "Hours Played": {
                "number": game.get("hours", 0)
            }
        }
    )

def sync_games():
    try:
        games = get_games()

        for game in games:
            try:
                push_game_to_notion(game)
            except Exception as e:
                logging.error(f"Failed to push game '{game.get('title', '[unknown]')}': {e}", exc_info=True)

    except Exception as e:
        logging.critical(f"❌ Error during Notion sync: {e}", exc_info=True)

