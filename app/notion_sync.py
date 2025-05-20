from notion_client import Client
import requests
import os

notion = Client(auth=os.environ.get("NOTION_TOKEN"))
database_id = os.environ.get("NOTION_DATABASE_ID")

def push_game_to_notion(game):
    notion.pages.create(
        parent={"database_id": database_id},
        properties={
            "Title": {
                "title": [
                    {
                        "text": {
                            "content": game["name"]
                        }
                    }
                ]
            },
            "Status": {
                "select": {"name": game["status"]}
            },
            "Hours Played": {
                "number": game.get("hours", 0)
            }
        }
    )

def sync_games():
    # Adjust the URL to match your own Flask API route
    response = requests.get("https://backlog-m02j.onrender.com/games")
    response.raise_for_status()
    games = response.json()

    for game in games:
        push_game_to_notion(game)
