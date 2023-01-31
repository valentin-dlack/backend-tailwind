from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    page = 'index'
    
    return render_template('hello.html', page=page)

@app.route('/login')
def login():
    return "Login TODO"

@app.route('/register')
def register():
    return "Register TODO"

@app.route('/profile')
def profile():
    return "Profile TODO"