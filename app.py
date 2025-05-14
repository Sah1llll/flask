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

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/form', methods=["GET",'POST'])
def form():
    if request.method == 'POST':
        from_ = request.form['from']
        to_ = request.form['to']
        people = request.form['people']

        days = request.form['days']
        budget = request.form['budget']
        print(from_, to_, people, days, budget)

        return render_template('form.html',from_ = from_, to_ = to_, people = people, days = days, budget = budget)
    return render_template('form.html')
        

app.run(debug=True, host='0.0.0.0')
