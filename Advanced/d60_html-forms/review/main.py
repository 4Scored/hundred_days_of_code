from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def receive_input():    
    if request.method == "POST" and request.form['name_input'] and request.form['password_input']:
        return f"<h1>Name: {request.form['name_input']}, Password: {request.form['password_input']}</h1>"
    return "input received"

if __name__ == "__main__":
    app.run()