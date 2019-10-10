from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
db = client.Contractor
hoodies = db.hoodies

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html')

hoodies = [
    { 'title': 'Original Logo', 'description': 'Original \"Hoody.\" logo' },
    { 'title': 'New Wave', 'description': 'The new classic!' }
]

@app.route('/hoodies')
def hoodies_index():
    """Show all hoodies."""
    return render_template('hoodies_index.html', hoodies=hoodies)

@app.route('/hoodies/<hoodie_id>')
def single_hoodie_view(hoodie_id):
    pass

if __name__ == '__main__':
    app.run(debug=True)