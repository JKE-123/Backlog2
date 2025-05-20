from app import create_app, db

app = create_app()

@app.route('/init-db')
def init_db():
    db.create_all()
    return "✅ Database initialized."

if __name__ == '__main__':
    app.run(debug=True)
