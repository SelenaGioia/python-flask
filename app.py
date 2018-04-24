from flask import Flask, render_template, request, redirect, url_for, session
                                            #Per estrarre i dati, uso request, che contiene tutti i dati relativi alla richiesta HTTP 
                                            #che mi è appena arrivata (è un global implicit object e deve essere importato!)
                                            #definisco anche session: in questo modo, flask gestisce e inizializza la sessione
                                            #session è un oggetto globale specifico per utente, un dizionario session ['user'] = user
                                            #che sta in un cookie
import userdb

app = Flask(__name__)                       #istanzio flask

app.secret_key="veryveryverysecrererevf"    #implementing sessions in Flask: it is needed to define a secret key
                                            #funzione che definisce la web page root (tutte le web page che definiamo sono definite così
@app.route('/')                             #indirizzo dal quale posso accedere alla pagina
def hello_world():
    return redirect(url_for('index'))       #quello che ritorno è il contenuto della web page - per semplicità, uso i template
                                            #url_for('index') -> funzione di flask che converte la function name nel nome del file html
                                            #al quale fa riferimento
                                            # return redirect(url_for('index')) -> redirect (flask method)
@app.route('/index')
def index():
    username = session.get('username','')   #prendo lo username dalla sessione (default se non esiste= '')
    if username != '':
        alarms = userdb.all_alarms(session['user_id'])
    else:
        alarms = None
    return render_template("index.html", name=username, alarms=alarms)  #passo al template username

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/logout')                       #by default, the GET method is applied 
def logout():
    del(session['username'])
    return redirect(url_for('index'))

@app.route('/welcome', methods=['POST'])    #so I specify that I need to support a different method (e.s. methods = ['GET','POST']
def welcome():                              #POST -> sends data to the server
    username = request.form['username']     #estraggo i dati da request: request.form è il dictionary che contiene tutti i dati inseriti
                                            #dall'utente - nel caso specifico estraggo username (name del text box nel form di index.html)
    userdata = userdb.check_user(username)
    if(userdata==None):
        return render_template("loginerror.html")
    else:
        session['username'] = userdata[1]
        session['user_id'] = userdata[0]
        session['fullname'] = userdata[3]
        #return render_template("welcome.html", name=username) #in questo modo faccio l'inject di username nella variabile name,
                                            #e poi posso usarlo nella pagina about come {{ name }}
        return redirect(url_for('index'))

if __name__ == '__main__':                              #faccio partire il web server a runtime
    app.run()
