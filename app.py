from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     """Return homepage."""
#     return render_template('home.html', msg='Hoody.')

hoodies = [
    { 'title': 'Original Logo', 'description': 'Original \"Hoody.\" logo' },
    { 'title': 'New Wave', 'description': 'The new classic!' }
]

@app.route('/')
def hoodies_index():
    """Show all hoodies."""
    return render_template('hoodies_index.html', hoodies=hoodies)

if __name__ == '__main__':
    app.run(debug=True)