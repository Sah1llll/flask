from flask import Flask, render_template, request
from datetime import datetime
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

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/form', methods=["GET",'POST'])
def form():
    if request.method == 'POST':
        from_ = request.form['from']
        to_ = request.form['to']
        people = request.form['people']
        from_date = request.form['fromdate']
        to_date = request.form['todate']
        budget = request.form['budget']
        # Convert string date to datetime object
        from_date = datetime.strptime(from_date, '%Y-%m-%d')
        to_date = datetime.strptime(to_date, '%Y-%m-%d')
        days = (to_date - from_date).days
        print(from_, to_, people, budget, from_date, to_date, days)

        return render_template('form.html',from_ = from_, to_ = to_, people = people, budget = budget, from_date = from_date, to_date = to_date)
    return render_template('form.html')
        

app.run(debug=True, host='0.0.0.0')
