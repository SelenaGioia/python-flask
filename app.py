from flask import Flask, render_template, request, redirect, url_for, session
import userdb

app = Flask(__name__)

app.secret_key="veryveryverysecrererevf"

@app.route('/')
def hello_world():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    username = session.get('username','')
    if username != '':
        alarms = userdb.all_alarms(session['user_id'])
    else:
        alarms = None
    return render_template("index.html", name=username, alarms=alarms)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/logout')
def logout():
    del(session['username'])
    return redirect(url_for('index'))

@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form['username']
    userdata = userdb.check_user(username)
    if(userdata==None):
        return render_template("loginerror.html")
    else:
        session['username'] = userdata[1]
        session['user_id'] = userdata[0]
        session['fullname'] = userdata[3]
        #return render_template("welcome.html", name=username)
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
