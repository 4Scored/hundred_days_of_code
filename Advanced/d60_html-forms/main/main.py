import smtplib
import requests
from flask import Flask, render_template, request

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/5c42df40015e1d608a1c")
posts.raise_for_status()
posts = posts.json()

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    name_data = request.form.get("name")
    email_data = request.form.get("email")
    phone_data = request.form.get("phone")
    message_data = request.form.get("message")
    contact_info_recieved = name_data and email_data and phone_data and message_data
    if request.method == "POST" and contact_info_recieved: # POST
        send_email(name_data, email_data, phone_data, message_data)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False) # GET

def send_email(name, email, phone, message):
    email_content = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone Number: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login("YOUR_EMAIL", "YOUR_PASS")
        conn.sendmail("YOUR_EMAIL", "YOUR_EMAIL", email_content)

if __name__ == "__main__":
    app.run(debug=True)
