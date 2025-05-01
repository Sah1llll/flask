from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', name = "travel with harsh")

@app.route('/login')
def login():
    return render_template('login.html')

app.run(debug=True, host='0.0.0.0')
