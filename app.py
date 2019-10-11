from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Contractor')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
hoodies = db.hoodies
cart = db.cart

hoodies.insert_many([
    {'title': 'Cliff', 'description': 'One of the best!'},
    {'title': 'Delta', 'description': 'One of the best!'},
    {'title': 'Fjord', 'description': 'One of the best!'},
    {'title': 'Gulf', 'description': 'One of the best!'},
    {'title': 'Hill', 'description': 'One of the best!'},
    {'title': 'Lagoon', 'description': 'One of the best!'},
    {'title': 'Island', 'description': 'One of the best!'},
    {'title': 'Mountain', 'description': 'One of the best!'},
    {'title': 'Valley', 'description': 'One of the best!'},
    {'title': 'Butte', 'description': 'One of the best!'}
])


app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html')


# This route loads hoodies index and populates page with items in db.hoodies
@app.route('/hoodies')
def hoodies_index():
    """Show all hoodies."""
    hoody_items = hoodies.find()
    return render_template('hoodies_index.html', hoody_items=hoody_items)

# This route will allow users to view a single hoodie
@app.route('/hoodies/<hoodie_id>')
def single_hoodie_view(hoodie_id):
    hoodie = hoodies.find_one({'_id': ObjectId(hoodie_id)})
    return render_template('hoodie_show.html', hoodie=hoodie)

# This route returns the hoodies cart page
@app.route('/hoodies/cart')
def hoodies_cart():
    """Create a new cart"""
    cart_hoodie = cart.find()
    return render_template('hoodies_cart.html', cart_hoodie=cart_hoodie)


#This route takes you from home and returns the hoodies index page
@app.route('/hoodies', methods=['POST'])
def hoodies_show():
    
    print(request.form.to_dict())
    return redirect(url_for('hoodies_index'))

# Ths route will allow hoodies to be added to the cart database 
@app.route('/hoodies/cart/add', methods=['POST', 'GET'])
def user_cart_add():
    hoody_id = request.form.get('hoodies_id')
    hoody = hoodies.find_one({'_id': ObjectId(hoody_id)})
    new_cart_item = {
        'title': hoody['title'],
        'description': hoody['description'],
        'hoodies_id': ObjectId(hoody_id),
    }
    cart.insert_one(new_cart_item)
    return redirect(url_for('hoodies_index'))

@app.route('/hoodies/cart/delete', methods=['POST'])
def cart_delete(hoodie_id):
    """Delete a hoodie."""
    cart_id = request.form.get('hoodies._id')
    cart.delete_one({'_id': ObjectId(cart_id)})
    return redirect(url_for('hoodies_cart'))


@app.route('/hoodies/<hoodie_id>/edit', methods=['POST', 'GET'])
def hoodie_edit(hoodie_id):
    """Get an edit hoodie."""
    hoodie = hoodies.find_one({'_id': ObjectId(hoodie_id)})
    return render_template('hoodie_update.html', hoodie=hoodie)



@app.route('/hoodies/<hoodie_id>', methods=['POST', 'GET'])
def hoodie_update(hoodie_id):
    update_hoodie_id = request.form.get('hoodie_id')
    updated_hoodie = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
    }
    hoodies.update_one(
        {'_id': ObjectId(update_hoodie_id)},
        {'$set': updated_hoodie})
    return render_template('hoodies_index.html', hoodie=updated_hoodie)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))