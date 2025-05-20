# run.py
from app import app, db

@app.route('/init-db')
def init_db():
    db.create_all()
    return "Database initialized."
