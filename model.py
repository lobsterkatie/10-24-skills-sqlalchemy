"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the SQLite database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Model(db.Model):

    __tablename__ = "Models"

    model_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, nullable=False)
    brand_name = db.Column(db.String(50), db.ForeignKey("Brand.brand_name"),
                           nullable=True) #QUESTION FOR MEGGIE: NULL? DEFAULT?
    model_name = db.Column(db.String(50), nullable=False)

    brand = db.relationship("Brand",
                            backref=db.backref("Models", order_by=brand_name))


    def __repr__(self):
        """Make printing the object useful"""

        repr_string = ("<Model model_id: {id}, year: {year}, " +
                       "brand_name: {brand}, model_name: {model}>")
        print repr_string.format(id=self.model_id, year=self.year,
                                 brand=self.brand_name, model=self.model_name)


class Brand(db.Model):

    __tablename__ = "Brands"

    brand_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand_name = db.Column(db.String(50), nullable=False, unique=True)
    yr_founded = db.Column(db.Integer, nullable=True)
    HQ_location = db.Column(db.String(50), nullable=True)
    #QUESTION FOR MEGGIE: STYLE-WISE, OKAY TO USE CAPS IN VAR NAMES IF IT'S CLEAR
    #THEY'RE NOT CONSTANTS, JUST BECAUSE OF ACRONYMS?
    yr_discontinued = db.Column(db.Integer, nullable=True)


    def __repr__(self):
        """Make printing the object useful"""

        repr_string = ("Brand brand_id: {id}, brand_name: {name}, " +
                       "yr_founded: {founded}, HQ_location: {HQ}, " +
                       "yr_discontinued: {ended}")
        print repr_string.format(id=self.brand_id, name=self.brand_name,
                                 founded=self.yr_founded, HQ=self.HQ_location,
                                 ended=self.yr_discontinued)


# End Part 1
##############################################################################
# Helper functions


def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auto.db'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
