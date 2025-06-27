from flask import Flask
import random

app = Flask(__name__)
random_num = random.randint(0,9)

@app.route("/")
def home():
    return "<h1 style='text-align:center'>Guess a number between 0 and 9</h1>" \
           "<p style='text-align:center'>You'll be in for a giphy suprise!</p>" \
           "<div style='text-align:center'>" \
                "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>" \
            "</div>"

@app.route("/<int:guess_num>")
def make_guess(guess_num):
    if guess_num == random_num:
        return "<h1 style='text-align:center'>CORRECT NUMBER!</h1>" \
                "<div style='text-align:center'>" \
                    "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGhrdzQ2cHcxcWVtb3FmdTNkaWM2M2tjNmR1dndtc2VxOHY0ZHdkZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/WvR1t4ZAOiE9B50ipa/giphy.gif'>" \
                "</div>"
    else:
        return "<h1 style='text-align:center'>Wrong number, pick again.</h1>" \
                "<div style='text-align:center'>" \
                    "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGFpMmw5ZW1hemRha2JteXo0MjBwMG0xczF1NHFkOWQwbmF6anppZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qACPNbQDJS3WE/giphy.gif'>" \
                "</div>"

if __name__ == "__main__":
    app.run(debug=True)
