import random
import requests
import datetime
from flask import Flask, render_template 

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True # for html changes

@app.route("/")
def home():
    rand_num = random.randint(1,10)
    curr_year = datetime.datetime.now().year
    return render_template("index.html", num=rand_num, year=curr_year)

@app.route("/guess/<name>")
def get_guess(name):
    gender_called = requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    age_called = requests.get(f"https://api.agify.io?name={name}").json()["age"]
    return render_template("name_age.html", name=name, gender=gender_called, age=age_called)

@app.route("/blog/<num>")
def get_blog(num):
    blog_response = requests.get("https://www.npoint.io/docs/c790b4d5cab58020d391")
    blog_response.raise_for_status()
    all_posts = blog_response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
