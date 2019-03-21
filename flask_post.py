import flask
from flask import *
app = flask.Flask(__name__)

@app.route('/login', methods=["GEt", "POST"])
def login():

    error = ''
    try:
	
        if request.method == "POST":
		
            attempted_username = request.form['username']
            attempted_password = request.form['password']

            #flash(attempted_username)
            #flash(attempted_password)

            if attempted_username == "admin" and attempted_password == "password":
                return redirect(url_for('dashboard'))
				
            else:
                error = "Invalid credentials. Try Again."

        return render_template("login.html")

    except Exception as e:
        #flash(e)
        return render_template("login.html")   	
app.run()
