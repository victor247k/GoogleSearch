from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/advancedsearch")
def advanced():
    return render_template("advancedsearch.html")

@app.route("/imagesearch")
def image():
    return render_template("imagesearch.html")

if __name__ == "__main__":
    app.run(debug=True)
