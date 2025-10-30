from flask import Flask, render_template, request, session, redirect 

app = Flask(__name__) 
app.secret_key = 'softwareapplicationssecret'

@app.route('/') 
def index(): 
    return render_template('index.html') 
 
@app.route('/slides') 
def slides(): 
    user = session['user'] 
    topics = ["Introdução", "O que é Software?"] 
    return render_template('slides.html', user=user, slides=topics) 

@app.route('/login', methods=['POST']) 
def login(): 
    user = request.form['user'] 
    session['user'] = user 
    return render_template('welcome.html', user=user) 

@app.route('/logout') 
def logout(): 
    del session['user'] 
    return redirect('/') 

if __name__ == '__main__': 
 app.run(debug=True)