from flask import Flask, render_template, redirect, url_for, flash, session
from models import db, User
from forms import RegisterForm, LoginForm, EditProfileForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Регистрация прошла успешно. Пожалуйста, войдите в систему.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            session['user_id'] = user.id
            flash('Вход выполнен успешно.')
            return redirect(url_for('profile'))
        flash('Неправильный email или пароль.')
    return render_template('login.html', form=form)

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        flash('Пожалуйста, войдите в систему для доступа к этой странице.')
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    form = EditProfileForm()
    if form.validate_on_submit():
        if form.name.data:
            user.name = form.name.data
        if form.email.data:
            user.email = form.email.data
        if form.password.data:
            user.set_password(form.password.data)
        db.session.commit()
        flash('Профиль успешно обновлен.')
        return redirect(url_for('profile'))
    return render_template('profile.html', form=form, user=user)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Вы вышли из системы.')
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.run(debug=True)


