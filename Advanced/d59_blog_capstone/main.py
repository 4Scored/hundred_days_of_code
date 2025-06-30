import requests
from flask import Flask, render_template

NPOINT_BLOG_URL = "https://api.npoint.io/5c42df40015e1d608a1c"
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

posts = requests.get(NPOINT_BLOG_URL)
posts.raise_for_status()
posts_data = posts.json()

@app.route('/')
def home():
    return render_template("index.html", all_posts=posts_data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:post_idx>')
def get_post(post_idx):    
    for post in posts_data:
        if post["id"] == post_idx:
            return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
