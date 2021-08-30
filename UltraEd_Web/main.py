from flask import Flask, redirect, url_for, render_template

app = Flask("app")

@app.route('/')
def blank():
	return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/join")
def join():
    return render_template("join.html")

@app.route("/classes")  
def classes():
    return render_template("classes.html")
    
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/ourteam")
def ourteam():
    return render_template("ourteam.html")

if __name__ == "__main__":
    app.run()