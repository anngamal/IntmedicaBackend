from flask import Flask
from flask_migrate import Migrate
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
# Get Relative Imports with Updated System Traversal
from model import db, PortableElectrotherapy
import requests
from bs4 import BeautifulSoup
from app import app 

# app.config["SQLALCHEMY_DATABASE_URI"] = "your_database_uri_here"

with app.app_context():
    
    BASE_URL_PATH = ""
    
    # First URL
    url = "https://www.chattanoogarehab.com/us/portable-electrotherapy"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    migrate = Migrate(app, db) 
    PortableElectrotherapy.query.delete() 

    for product_elem in soup.find_all(class_="product details product-item-details"):
        product_name = product_elem.find("strong", class_="product name product-item-name").text
        product_price_elem = product_elem.find("span", class_="price")

        if product_price_elem is not None:
            product_price = product_price_elem.text
        else:
            product_price = "Price not found"

        a_tag = product_elem.find("a", attrs={"class": "product-item-link", "href": True})

        if a_tag is not None:
            product_href = BASE_URL_PATH + a_tag['href']

            response = requests.get(product_href)
            product_soup = BeautifulSoup(response.text, 'html.parser')
            product_description = product_soup.find('div', class_='value', itemprop="description")
            if product_description is not None:
                description_text = product_description.get_text()
            else:
                description_text = "Description not found"

            img_tag = product_soup.find("img", class_="product-image-photo")
            if img_tag is not None:
                image_url = img_tag.get("src")
            else:
                image_url = "Image not found"

            portableelectrotherapyProduct = PortableElectrotherapy(name=product_name, price=product_price, href=product_href, image=image_url, description=description_text)
            db.session.add(portableelectrotherapyProduct)
            db.session.commit()
            print(portableelectrotherapyProduct)

    print("DONE - First URL")
