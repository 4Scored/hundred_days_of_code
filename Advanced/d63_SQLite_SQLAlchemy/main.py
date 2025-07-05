from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = [] # set of dicts {auth, title, ranking}

@app.route('/')
def home():
    return render_template("index.html", books=all_books, books_len=len(all_books))


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_to_add = {
            "title": request.form["book_title"],
            "author": request.form["book_author"],
            "rating": request.form["book_rating"],
        }
        all_books.append(book_to_add)
        return redirect(url_for("home")) # http redirect instead of page render
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)



'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''