import logging
from notion_client import Client
import requests
import os

# Replace with your actual values
NOTION_TOKEN = "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"
DATABASE_ID = "1efd679009c180629c65ecaeaf9ca550"

# Initialize logging
logging.basicConfig(
    level=logging.DEBUG,  # DEBUG level to see everything
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

# Initialize client
notion = Client(auth=NOTION_TOKEN)

def push_game_to_notion(game):
    logging.debug(f"Preparing to push game to Notion: {game.get('title', '[no title]')}")
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
    logging.info(f"Pushed game to Notion: {game.get('title', '[no title]')}")

def sync_games():
    try:
        logging.info("Starting sync_games")
        response = requests.get("https://backlog-m02j.onrender.com/games")
        response.raise_for_status()
        games = response.json()
        logging.info(f"Fetched {len(games)} games")

        for game in games:
            try:
                push_game_to_notion(game)
            except Exception as e:
                logging.error(f"Failed to push game '{game.get('title', '[unknown]')}': {e}", exc_info=True)

        logging.info("Finished syncing all games")

    except Exception as e:
        logging.critical(f"❌ Error during Notion sync: {e}", exc_info=True)
