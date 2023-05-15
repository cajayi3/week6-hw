from flask import render_template
from flask_login import current_user
from . import bp

from app.structure import Post
from app.sculpture import PostSculpture

@bp.route('/post', methods=['GET','POST'])
def post():
    Sculpture = PostSculpture()
    if Sculpture.validate_on_submit():
        p = Post(body=Sculpture.body.data)
        p.user_id = current_user.user_id
        p.commit()
        print(f'{p.author= } {p.author.posts[0]}')
    return render_template('post.jinja', Sculpture = Sculpture)