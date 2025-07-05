from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"

class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)    

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    selected_books = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = selected_books.scalars().all()    
    return render_template("index.html", books=all_books, books_len=len(all_books))

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":        
        book_to_add = Book(title=request.form["book_title"], author=request.form["book_author"], rating=request.form["book_rating"])
        db.session.add(book_to_add)
        db.session.commit()        
        return redirect(url_for("home")) 
    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST": # POST      
        book_to_update = db.get_or_404(Book, request.form["book_id"]) # proper get
        book_to_update.rating = request.form["new_book_rating"]
        db.session.commit()
        return redirect(url_for("home"))    
    book_selected = db.get_or_404(Book, request.args.get("id")) # GET
    return render_template("rating_edit.html", book=book_selected)

@app.route("/delete")
def delete():
    book_to_delete = db.get_or_404(Book, request.args.get("id"))
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

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