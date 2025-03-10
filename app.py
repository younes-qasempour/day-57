from flask import Flask, render_template
import random
import datetime
import requests


app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.datetime.now().year
    return render_template("index.html",
                           num=random_number,
                           year=year)


@app.route('/guess/<name>')
def guess(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    age = response.json()["age"]
    response = requests.get(f"https://api.genderize.io?name={name}")
    gender = response.json()["gender"]
    return render_template("guess.html", age=age, name=name, gender=gender)


@app.route('/blog')
def blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)






if __name__ == '__main__':
    app.run()
