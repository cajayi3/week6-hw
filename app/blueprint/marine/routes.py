from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from app.structure import User
from flask_login import current_user

from . import bp
from app.structure import SealsixStructure, MajorStructure

@bp.route('/major', methods=['GET',"POST"])
def major():
     sculpture = MajorStructure()
     if sculpture.validate_on_submit():
        user = User.query.filter_by(username=sculpture.username.data).first()
        if user and user.check_password(sculpture.password.data):
            flash(f'{sculpture.username.data} signed in','success')
            login_user(user)
            return redirect(url_for('ranger.home'))
        else:
            flash(f'{sculpture.username.data} doesn\'t exist or incorrect password','warning')
     return render_template('Major.jinja', sculpture=sculpture)

@bp.route('/sealsix', methods=['GET','POST'])
def sealsix():
    sculpture = SealsixStructure()
    if sculpture.validate_on_submit():
        user = User.query.filter_by(username=sculpture.username.data).first()
        email = User.query.filter_by(email=sculpture.email.data).first()
        if not email and not user:
            u = User(username=sculpture.username.data,email=sculpture.email.data)
            u.commit()
            flash(f"{sculpture.username.data} registered")
            return redirect(url_for("ranger.home"))
        if user:
            flash(f'{sculpture.username.data}  Previously taken, Copy 10-4!')
        else:
            flash(f'{sculpture.email.data} Previously taken, Copy 10-4!')
    return render_template('sealsix.jinja', sculpture=sculpture)