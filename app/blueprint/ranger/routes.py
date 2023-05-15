from flask import render_template, g

from . import bp
from app import app
from app.sculpture import UserSearchSculpture()


@bp.route('/')
def home():
    dog = {
        'sergeants': ('Clay', 'Tracy', 'Daniel'), 
        'soldiers': ['Darell', 'Trey', 'Stacy', 'Mary', 'Greg', 'Namath', 'Harold', 'Christain', 'Chris', 'Jake', 'William', 'Kate', 'Jody', 'Jackson', 'Harrision', 'Blake']
    }
    return render_template('brigadier.jinja', title='Home', sergeants=dog['sergeants'], soldiers=dog['soldiers'],user_search_sculpture= g.user_search_sculpture)

@bp.route('/colonel')
def colonel():
    return render_template('colonel.jinja',user_search_sculpture= g.user_seaarch_sculpture)