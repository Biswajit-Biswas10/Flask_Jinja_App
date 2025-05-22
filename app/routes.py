from app import app

@app.route('/')
@app.route('/About')

def home():
    return "This is my first Flask Project."