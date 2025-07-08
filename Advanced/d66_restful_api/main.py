import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db' # Connect to Database
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self): # helper function; makes it clear as well
        return {
            "id": self.id,
            "name": self.name,
            "map_url": self.map_url,
            "img_url": self.img_url,
            "location": self.location,
            "seats": self.seats,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "has_sockets": self.has_sockets,
            "can_take_calls": self.can_take_calls,
            "coffee_price": self.coffee_price
        }

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_random_cafe():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    rand_cafe = random.choice(all_cafes)
    return jsonify(rand_cafe.to_dict())

@app.route("/all", methods=["GET"])
def get_all_cafes():
    cafe_jsons = []
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()    
    for cafe in all_cafes:
        cafe_jsons.append(cafe.to_dict())
    return jsonify(cafes=cafe_jsons) # jsonify({"cafes": cafe_jsons}) equivalent

@app.route("/search", methods=["GET"])
def get_searched_cafe():        
    searched_cafe_jsons = []
    search_loc = request.args.get("loc")
    searched_cafes = db.session.execute(db.select(Cafe).where(Cafe.location == search_loc)).scalars().all()    
    for cafe in searched_cafes:
        searched_cafe_jsons.append(cafe.to_dict())
    return jsonify(cafes=searched_cafe_jsons)

# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    cafe_to_add = Cafe(
        name=request.form.get("name"), # form from postman
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(cafe_to_add)
    db.session.commit()
    return jsonify(added_cafe=cafe_to_add.to_dict())

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)



'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''