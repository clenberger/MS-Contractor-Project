from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

client = MongoClient()
db = client.Contractor
hoodies = db.hoodies
cart = db.cart

hoodies.insert_many([
    {'title': 'y', 'description': 'y'},
    {'title': 'n', 'description': 'y'},
    {'title': 'd', 'description': 'y'},
    {'title': 'g', 'description': 'y'},
    {'title': 'e', 'description': 'y'},
    {'title': 't', 'description': 'y'},
    {'title': 'f', 'description': 'y'},
    {'title': 'm', 'description': 'y'},
    {'title': 'n', 'description': 'y'},
    {'title': 'b', 'description': 'y'}
])

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html')

# hoodies = [
#     { 'title': 'Original Logo', 'description': 'Original \"Hoody.\" logo' },
#     { 'title': 'New Wave', 'description': 'The new classic!' }
# ]

# This route loads hoodies index and populates page with items in db.hoodies
@app.route('/hoodies')
def hoodies_index():
    """Show all hoodies."""
    return render_template('hoodies_index.html', hoodies=hoodies.find())

# This route will allow users to view a single hoodie
@app.route('/hoodies/<hoodie_id>')
def single_hoodie_view(hoodie_id):
    pass

# This route returns the hoodies cart page
@app.route('/hoodies/cart')
def hoddies_cart():
    """Create a new cart"""
    return render_template('hoodies_cart.html')


#This route takes you from home and returns the hoodies index page
@app.route('/hoodies', methods=['POST'])
def hoodies_show():
    """Submit a new playlist."""
    print(request.form.to_dict())
    return redirect(url_for('hoodies_index'))

# Ths route will allow hoodies to be added to the cart database 
@app.route('hoodies/cart/add', methods=['POST', 'GET'])
def user_cart_add():
    pass
if __name__ == '__main__':
    app.run(debug=True)