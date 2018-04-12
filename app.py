from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template("welcome.html", name=username)

if __name__ == '__main__':
    app.run()
