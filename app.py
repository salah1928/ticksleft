from flask import Flask, render_template
from getprods import getprods

app = Flask(__name__)

prods = getprods()

@app.route('/')
def index():
    return render_template('home.html',prods = prods)

if __name__ == '__main__':
    app.run(debug=True)

