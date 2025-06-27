from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

@app.route("/")
def hello_world():
    return "<h1 style='text-align:center'>Hello, World!</h1>" \
           "<p>This is a paragraph</p>" \
           "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGtrd3M2cnhocGxzb3p2eXowcnF1YWR2NjRvNDRqZmQ3cDkzbmE0NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jgCVVyXRC8pP2/giphy.gif'>"

@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return "Bye Bye!"

@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)
