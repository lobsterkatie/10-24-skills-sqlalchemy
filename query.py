"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.

# PART 1.5: PLAY WITH SQL TO CHANGE COLUMN NAMES
    # STEP 1: CREATE A NEW TABLE WITH THE NEW COLUMN NAMES
    CREATE TABLE Models2 (
    ...> model_id INTEGER PRIMARY KEY,
    ...> year INT(4) NOT NULL, 
    ...> brand_name VARCHAR(50) NOT NULL,
    ...> model_name VARCHAR(50) NOT NULL
    ...> );

    # STEP 2: COPY DATA FROM OLD TABLE INTO NEW TABLE
    INSERT INTO Models2 SELECT * FROM Models;

    # STEP 3: DROP OLD TABLE
    DROP TABLE Models;

    # STEP 4: RENAME NEW TABLE TO OLD NAME
    ALTER TABLE Models2 RENAME TO Models;

    # STEP 5: DO IT ALL AGAIN WITH THE OTHER TABLE
    CREATE TABLE Brands2 (
    ...> brand_id INTEGER PRIMARY KEY,
    ...> brand_name VARCHAR(50) NOT NULL UNIQUE,
    ...> yr_founded INT(4),
    ...> HQ_location VARCHAR(50),
    ...> yr_discontinued INT(4)
    ...> );
    # THEN
    INSERT INTO Brands2 SELECT * FROM Brands;
    # THEN
    DROP TABLE Brands;
    # AND FINALLY
    ALTER TABLE Brands2 RENAME TO Brands;


# Part 2: Write queries

# Get the brand with the **id** of 8.
db.session.query(Brand)
          .filter(Brand.brand_id == 8)
          .one()


# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
db.session.query(Model)
          .filter(Model.model_name == "Corvette", 
                  Model.brand_name == "Chevrolet")
          .all()


# Get all models that are older than 1960.
db.session.query(Model).filter(Model.year < 1960).all()
# it should be noted that ascii vs unicode just ate an hour of my life I'll
# never get back. *sigh*


# Get all brands that were founded after 1920.
db.session.query(Brand).filter(Brand.yr_founded > 1920).all()


# Get all models with names that begin with "Cor".

# Get all brands with that were founded in 1903 and that are not yet discontinued.

# Get all brands with that are either discontinued or founded before 1950.

# Get any model whose brand_name is not Chevrolet.

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    pass

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    pass

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
