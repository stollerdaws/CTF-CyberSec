from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name'].replace('{', '').replace('}', '')
        hometown = request.form['hometown'].replace('{', '').replace('}', '')
        favorite_animal = request.form['favorite_animal'].replace('{', '').replace('}', '')
        age = request.form['age'].replace('{', '').replace('}', '')
        favorite_quote = request.form['favorite_quote'] 
        rendered_quote = render_template_string(f'<p>{favorite_quote}</p>')
        return f'''
            <h1>User Profile</h1>
            <p>Name: {name}</p>
            <p>Hometown: {hometown}</p>
            <p>Favorite Animal: {favorite_animal}</p>
            <p>Age: {age}</p>
            <h2>Favorite Quote:</h2>
            {rendered_quote}
        '''
    # Default page with form
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            Hometown: <input type="text" name="hometown"><br>
            Favorite Animal: <input type="text" name="favorite_animal"><br>
            Age: <input type="number" name="age"><br>
            Favorite Quote: <input type="text" name="favorite_quote"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
