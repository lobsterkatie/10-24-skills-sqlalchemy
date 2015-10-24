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

# QUERIES BELOW COMMENTED OUT SO FUNCTIONS WILL RUN. UNCOMMENT OUT TO SEE
# PRETTY COLORS.

# # -------------------------------------------------------------------
# # Start here.

# # PART 1.5: PLAY WITH SQL TO CHANGE COLUMN NAMES
#     # STEP 1: CREATE A NEW TABLE WITH THE NEW COLUMN NAMES
#     CREATE TABLE Models2 (
#     ...> model_id INTEGER PRIMARY KEY,
#     ...> year INT(4) NOT NULL, 
#     ...> brand_name VARCHAR(50) NOT NULL,
#     ...> model_name VARCHAR(50) NOT NULL
#     ...> );

#     # STEP 2: COPY DATA FROM OLD TABLE INTO NEW TABLE
#     INSERT INTO Models2 SELECT * FROM Models;

#     # STEP 3: DROP OLD TABLE
#     DROP TABLE Models;

#     # STEP 4: RENAME NEW TABLE TO OLD NAME
#     ALTER TABLE Models2 RENAME TO Models;

#     # STEP 5: DO IT ALL AGAIN WITH THE OTHER TABLE
#     CREATE TABLE Brands2 (
#     ...> brand_id INTEGER PRIMARY KEY,
#     ...> brand_name VARCHAR(50) NOT NULL UNIQUE,
#     ...> yr_founded INT(4),
#     ...> HQ_location VARCHAR(50),
#     ...> yr_discontinued INT(4)
#     ...> );
#     # THEN
#     INSERT INTO Brands2 SELECT * FROM Brands;
#     # THEN
#     DROP TABLE Brands;
#     # AND FINALLY
#     ALTER TABLE Brands2 RENAME TO Brands;


# # Part 2: Write queries

# # Get the brand with the **id** of 8.
# db.session.query(Brand)
#           .filter(Brand.brand_id == 8)
#           .one()


# # Get all models with the **name** Corvette and the **brand_name** Chevrolet.
# db.session.query(Model)
#           .filter(Model.model_name == "Corvette", 
#                   Model.brand_name == "Chevrolet")
#           .all()


# # Get all models that are older than 1960.
# db.session.query(Model)
#           .filter(Model.year < 1960)
#           .all()
# # it should be noted that ascii vs unicode just ate an hour of my life I'll
# # never get back. *sigh*


# # Get all brands that were founded after 1920.
# db.session.query(Brand)
#           .filter(Brand.yr_founded > 1920)
#           .all()


# # Get all models with names that begin with "Cor".
# db.session.query(Model)
#           .filter(Model.model_name.like("Cor%"))
#           .all()


# # Get all brands with that were founded in 1903 and that are not yet discontinued.
# db.session.query(Brand)
#           .filter(Brand.yr_founded == 1903, 
#                   Brand.yr_discontinued.is_(None))
#           .all()


# # Get all brands with that are either discontinued or founded before 1950.
# db.session.query(Brand)
#           .filter((Brand.yr_discontinued.isnot(None)) | 
#                   (Brand.yr_founded < 1950))
#           .all()
# # This is ambiguously-worded. Above is the D, or F before 1950 reading.
# # Below is the D or F, before 1950 reading.
# db.session.query(Brand)
#           .filter((Brand.yr_discontinued < 1950) | 
#                   (Brand.yr_founded < 1950))
#           .all()


# # Get any model whose brand_name is not Chevrolet.
# db.session.query(Model)
#           .filter(Model.brand_name != "Chevrolet")
#           .all()


# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    """Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query."""

    results = (db.session.query(Model.brand_name,
                               Model.model_name,
                               Brand.HQ_location)
                         .join(Brand)
                         .filter(Model.year == year)
                         .all())

    print "\n\n--------------- {year} ---------------".format(year=year)
    print "(Brand Model, Brand HQ)"

    for result in results:
        brand, model, HQ = result
        result_str = "{brand} {model}, {HQ}"
        print result_str.format(brand=brand.encode("utf-8"),
                                model=model,
                                HQ=HQ)

    print


def get_brands_summary():
    """Prints out each brand name, and each model name for that brand
     using only ONE database query."""

    results = (db.session.query(Model.brand_name, Model.model_name)
                         .group_by(Model.model_name)
                         .order_by(Model.brand_name)
                         .all())

    print "\n\n--------------- Models ---------------"

    for result in results:
        brand, model = result
        result_str = "{brand} {model}"
        print result_str.format(brand=brand.encode("utf-8"),
                                model=model)

    print

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(str):
    """Takes a string and returns (as a list of Brand objects) all brands
    whose name contains the given string"""

    results = (db.session.query(Brand)
                         .filter(Brand.brand_name.like("%" + str + "%"))
                         .all())

    return results

# NOTE THAT THIS IS AMBIGUOUSLY STATED: SHOULD THE RANGE BE INCLUSIVE
# OR EXCLUSIVE? GOING WITH INCLUSIVE
def get_models_between(start_year, end_year):
    """Takes an inclusive range of years and returns all models from
    that range"""

    results = (db.session.query(Model)
                         .filter(Model.year >= start_year,
                                 Model.year <= end_year)
                         .order_by(Model.year, Model.brand_name)
                         .all())

    return results

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of 
# ``Brand.query.filter_by(brand_name='Ford')``?

# As stated, this is just a query, not a result. So you get a 
# flask_sqlalchemy.BaseQuery object. If you were to add .one() to the end
# of the query, you'd get a Brand object.


# 2. In your own words, what is an association table, and what *type* of 
# relationship does an association table manage?

# An association table acts as the midlleman (middleperson?) in a many-to-many
# relationship, because such relatinships do not *actually* work in DB design.
# For example, if you want tables A and B to have an M2M relationship, you'd 
# create a table AB which just had AB pairings in it, along with a constraint 
# that the pairings be unique. Then each of A and B would have a one-to-many 
# relationship to the AB table. If, however, there were actual *information* 
# associated with the pairing (so the AB table would have more than just id, A, 
# and B fields), then the relationsips would work the same way but a) the unique
# constraint likely wouldn't apply, and b) it wouldn't count as an association 
# table.
