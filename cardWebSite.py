from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def card_info():
    return render_template("web1.html")


if __name__=="__main__":
    app.run(debug=True)