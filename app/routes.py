from flask import render_template
from app import app

@app.route('/')
def home():
    dog = {
        'sergeants': ('Clay', 'Tracy', 'Daniel'), 
        'soldiers': ['Darell', 'Trey', 'Stacy', 'Mary', 'Greg', 'Namath', 'Harold', 'Christain', 'Chris', 'Jake', 'William', 'Kate', 'Jody', 'Jackson', 'Harrision', 'Blake']
    }
    return render_template('brigadier.jinja', title='Home', sergeants=dog['sergeants'], soldiers=dog['soldiers'])

@app.route('/colonel')
def colonel():
    return render_template('colonel.jinja')

@app.route('/sealsix')
def sealsix():
    return render_template('sealsix.jinja')

@app.route('/major')
def major():
    return render_template('major.jinja')