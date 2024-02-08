from flask import Flask, request, session, redirect, url_for, render_template_string
import hashlib

app = Flask(__name__)
app.secret_key = 'This_cant_be_secure' 

@app.route('/')
def index():
    return '''
        <form action="/login" method="post">
            <input type="password" name="password" placeholder="Password">
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    password = request.form['password']
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if hashed_password == "e16153eb70a8795fa9c845ae7867756111d06334abe900cf0c6f0afe7209cdd9":
        session['admin'] = True
        return redirect(url_for('admin'))
    else:
        session['admin'] = False
        return 'Invalid password', 403

@app.route('/admin')
def admin():
    if session['admin'] and session['admin'] == True:
        with open('flag.txt', 'r') as f:
            flag = f.read()
        return f'Welcome admin, here\'s your flag: {flag}'
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
