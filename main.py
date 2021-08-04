from flask import Flask, redirect, url_for, render_template
app = Flask('app')

@app.route('/')
def home():
	return render_template("home.html")
@app.route('/')
def classes():
  return render_template("classes.html")


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080)
