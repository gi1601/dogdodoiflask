from flask import Flask, render_template

app = Flask(__name__)

@app.route('/header')
def header():
    return render_template("header.html", titulo="header")

@app.route('/dog')
def dog():
    return render_template("dog.html", titulo="dog")

@app.route('/index')
def index():
    return render_template("index.html", titulo="index")



if __name__ == '__main__':
    app.run()
