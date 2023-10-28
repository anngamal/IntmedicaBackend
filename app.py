from flask import Flask, make_response,jsonify
from flask_migrate import Migrate
from model import db, Product
import pandas
import sqlite3


# PATH_TO_SPARE_PARTS_DATA = "./datasets/spare-parts-2023.xlsx"
# df_spare_parts = pandas.read_excel(PATH_TO_SPARE_PARTS_DATA)
# print(f"\nFirst ten rows of my dataframe:\n{df_spare_parts.head(10)}\n")

app=Flask(__name__)

if __name__ == "__main__":
    app.run(port=3000, debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate()
migrate.init_app(app, db)

@app.route('/')
def root():
    print("hello")
    return make_response(jsonify({}), 200)