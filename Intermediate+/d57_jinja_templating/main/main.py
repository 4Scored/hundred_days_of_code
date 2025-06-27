import requests
from post import Post
from flask import Flask, render_template

posts = requests.get("https://www.npoint.io/docs/c790b4d5cab58020d391")
posts.raise_for_status()
posts = posts.json()
all_posts = []
for post in posts:
    add_post = Post(post["id"], post["title"], post["subtitle"], post["body"])
    all_posts.append(add_post)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_post=all_posts)

@app.route('/post/<int:num_to_show>')
def show_specific_post(num_to_show):
    post_to_show = None
    for post in all_posts:
        if post.id == num_to_show:
            post_to_show = post
    return render_template("post.html", post=post_to_show)

if __name__ == "__main__":
    app.run(debug=True)
