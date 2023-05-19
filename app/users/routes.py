from flask import Blueprint, render_template, request
from app.users.models import User
from werkzeug.security import generate_password_hash, check_password_hash

blueprint = Blueprint('users', __name__)

@blueprint.get('/register')
def get_register():
    return render_template('users/register.html')

@blueprint.post('/register')
def post_register():
    try:
        if request.form.get('password') != request.form.get('password_confirmation'):
            raise Exception('The password confirmation must match the password.')
        elif User.query.filter_by(email=request.form.get('email')).first():
            raise Exception('The email address is already registered.')
    
        user = User(
            email = request.form.get('email'),
            password=generate_password_hash(request.form.get('password'))
        user.save()
        )
        
        return 'User created'
    except Exception as error_message:
        error = error_message or 'An error occured while creating a user. Please make sure to enter valid data.'
        return render_template('users/register.html', error=error)

@blueprint.get('/login')
def get_login():
    return render_template('users/login.html')

@blueprint.post('/login')
def post_login():
    return 'User logged in'

@blueprint.get('/logout')
def logout():
    return 'User logged out'


