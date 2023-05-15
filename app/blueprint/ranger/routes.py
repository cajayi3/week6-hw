from flask import render_template

from . import bp


@bp.route('/')
def home():
    dog = {
        'sergeants': ('Clay', 'Tracy', 'Daniel'), 
        'soldiers': ['Darell', 'Trey', 'Stacy', 'Mary', 'Greg', 'Namath', 'Harold', 'Christain', 'Chris', 'Jake', 'William', 'Kate', 'Jody', 'Jackson', 'Harrision', 'Blake']
    }
    return render_template('brigadier.jinja', title='Home', sergeants=dog['sergeants'], soldiers=dog['soldiers'])

@bp.route('/colonel')
def colonel():
    return render_template('colonel.jinja')