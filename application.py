from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "Nothing here"

@app.route("/table")
def table():
    return render_template("table.html")

@app.route("/printmedia")
def printmedia():
    return render_template("printmedia.html")

@app.route("/viewport")
def viewport():
    return render_template("viewport.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
