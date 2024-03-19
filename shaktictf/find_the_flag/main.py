import os

from flask import Flask, request, render_template

app = Flask(__name__)

@app.get('/')
def index():
    test = request.args.get('test', None)
    if test is None:
        return render_template('index.html')

    command = f"find {test}"

    try:
        output = os.popen(command).read()

    except Exception as e:
        output = f"Error: {str(e)}"

    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
