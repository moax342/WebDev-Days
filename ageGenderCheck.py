from flask import Flask,render_template
import datetime as dt
import requests
import random

app= Flask(__name__)

@app.route("/<name>")
def main_page(name):
    res=requests.get(f"https://api.genderize.io?name={name}")
    res2=requests.get(f"https://api.agify.io?name={name}")
    gender=res.json()["gender"]
    year=dt.datetime.now().year
    age=res2.json()["age"]
    return render_template("blogPost.html",year=year,gender=gender,age=age,name=name)


if __name__=="__main__":
    app.run(debug=True)