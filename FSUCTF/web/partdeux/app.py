from flask import Flask, request, session, redirect, url_for, render_template_string
import hashlib
import urllib.parse
import os

app = Flask(__name__)

app.config.from_pyfile('ignoreMe/config.py')

base_directory = 'freebies'
default_file = 'hamster'

@app.route('/login', methods=['POST'])
def login():
    password = request.form['password']
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if hashed_password == "e16153eb70a8795fa9c845ae7867756111d06334abe900cf0c6f0afe7209cdd9":
        session['admin'] = True
        return redirect(url_for('admin'))
    else:
        session['admin'] = False
        return redirect(url_for('index'))

@app.route('/admin')
def admin():
    if session.get('admin') and session['admin'] == True:
        with open('ignoreMe/flag.txt', 'r') as f:
            flag = f.read()
        return f'Welcome admin, here\'s your flag: {flag}'
    else:
        return redirect(url_for('index'))

def ignore_it(file_param):
    if file_param != 'hamster':
        yoooo = file_param.replace('.', '').replace('/', '').replace('l', '').replace('a', '').replace('t', '').replace('x', '')
        if yoooo != file_param:
            return "Illegal characters detected in file parameter!"
        return yoooo
    return file_param

def another_useless_function(file_param):
    return urllib.parse.unquote(file_param)

def url_encode_path(file_param):
    return urllib.parse.quote(file_param, safe='')

def useless(file_param):
    file_param1 = ignore_it(file_param)
    file_param2 = another_useless_function(file_param1)
    file_param3 = ignore_it(file_param2)
    file_param4 = another_useless_function(file_param3)
    file_param5 = another_useless_function(file_param4)
    return file_param5

@app.route('/')
def index():
    return '''
        <form action="/read" method="get">
            <input type="text" name="filename" placeholder="Enter filename">
            <input type="submit" value="Read File">
        </form>
    '''

@app.route('/read')
def read_file():
    filename = request.args.get('filename')
    if not filename:
        filename = default_file
    sanitized_filename = useless(filename)
    sanitized_filename = os.path.join(base_directory, sanitized_filename)
    if "Illegal characters detected in file parameter!" in sanitized_filename:
        return sanitized_filename

    # Prevent reading the flag.txt file
    if 'flag.txt' in sanitized_filename:
        return 'Access to flag.txt is not allowed', 403

    try:
        with open(sanitized_filename, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return 'File not found', 404


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
