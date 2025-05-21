from notion_client import Client
import requests
# Replace with your actual values
NOTION_TOKEN = "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"
DATABASE_ID = "1efd679009c180629c65ecaeaf9ca550"

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
    # Adjust the URL to match your own Flask API route
    response = requests.get("https://backlog-m02j.onrender.com/games")
    response.raise_for_status()
    games = response.json()  # ✅ Parsed JSON list of games

    try:
        print(f"Fetched {len(games)} games")

        # ✅ Loop over the actual list of game dicts
        for game in games:
            try:
                push_game_to_notion(game)
                print(f"✅ Pushed: {game['title']}")
            except Exception as e:
                print(f"⚠️ Failed to push {game.get('title', '[unknown]')}: {e}")


    except Exception as e:
        print(f"❌ Error during Notion sync: {e}")



sync_games()

