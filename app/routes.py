# app/routes.py
from flask import request, jsonify
from app import app, db
from app.models import Game

@app.route("/games", methods=["GET"])
def get_games():
    games = Game.query.all()

    return[{
        "id": game.id,
        "title": game.title,
        #"platform": game.platform,
        #"platform": game.platform,
        "status": game.status,
        "hours_played": game.hours_played
    } for game in games]

@app.route("/games", methods=["POST"])
def add_game():
    data = request.get_json()
    new_game = Game(
        title=data.get("title"),
        #platform=data.get("platform"),
        status=data.get("status"),
        hours_played=data.get("hours_played")
    )
    db.session.add(new_game)
    db.session.commit()
    return jsonify({"message": "Game added", "id": new_game.id}), 201

@app.route("/games/<int:game_id>", methods=["PUT"])
def update_game(game_id):
    game = Game.query.get_or_404(game_id)
    data = request.get_json()
    game.title = data.get("title", game.title)
    #game.platform = data.get("platform", game.platform)
    game.status = data.get("status", game.status)
    game.hours_played = data.get("hours_played", game.hours_played)
    db.session.commit()
    return jsonify({"message": "Game updated"})

@app.route("/games/<int:game_id>", methods=["DELETE"])
def delete_game(game_id):
    game = Game.query.get_or_404(game_id)
    db.session.delete(game)
    db.session.commit()
    return jsonify({"message": "Game deleted"})
