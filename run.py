# run.py
from app import app, db

# Safe to remove this after initialization
@app.route('/init-db')
def init_db():
db.create_all()
return "Database initialized."
