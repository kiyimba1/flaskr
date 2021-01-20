from datetime import datetime

from flask import session, redirect, url_for, render_template

from app.main.forms import NameForm
from app.models import User
from .. import db
from . import main



@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False

        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name'), known=session.get('known', False))
