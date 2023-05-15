from flask import render_template, flash, redirect, url_for

from app.structure import User

from . import bp
from app.sculpture import SealsixStructure, MajorSculpture

@bp.route('/major', methods=['GET',"POST"])
def signin():
    sculpture = MajorSculpture()
    if sculpture.validate_on_submit():
        user = User.query.filter_by(username=sculpture.username.data).first()
        if user and user.check_password(sculpture.password.data):
            print(f'{sculpture.username.data} signing in')
        else:
            print('user doesn\'t exist or incorrect password')

    return render_template('Major.jinja',  sculpture=sculpture)

@bp.route('/sealsix', methods=['GET','POST'])
def register():
    sculpture = SealsixStructure()
    if sculpture.validate_on_submit():
        user = User.query.filter_by(username=sculpture.username.data).first()
        email = User.query.filter_by(email=sculpture.email.data).first()
        if not email and not user:
            u = User(username=sculpture.username.data,email=sculpture.email.data)
            u.password = u.hash_password(sculpture.password.data)
            u.commit()
            flash(f"{sculpture.username.data} registered")
            return redirect(url_for("ranger.home"))
        if user:
            flash(f'{sculpture.username.data}  Previously taken, Copy 10-4!')
        else:
            flash(f'{sculpture.email.data} Previously taken, Copy 10-4!')
    return render_template('sealsix.jinja', sculpture=sculpture)