from flask import Flask
from flask_migrate import Migrate
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
# Get Relative Imports with Updated System Traversal
from model import db, Waveseries
import requests
from bs4 import BeautifulSoup
from app import app 

# app.config["SQLALCHEMY_DATABASE_URI"] = "your_database_uri_here"



with app.app_context():
    Waveseries.query.delete()
    BASE_URL_PATH = "https://www.therabody.com/"
    url = "https://www.therabody.com/us/en-us/products/?prefn1=productTypeMasterPLP&prefv1=waveseries"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    product_list = []
    url_list = []
    print("Before loop")



    for product_elem in soup.find_all(class_="product-info"):
        product_name = product_elem.find("div", class_="product-name").text
        product_price = product_elem.find("div", class_="product-pricing").text
        # product_classification = product_elem.find("div", class_="product-classification")
        
        # if product_classification is not None:
        #     product_classification = product_classification.text
        # else:
        #     product_classification = "N/A"

        for a_tag in product_elem.find_all("a", class_="name-link", href=True):
            product_href = f"{BASE_URL_PATH}/{a_tag['href']}"
            url_list.append(product_href)

            try:
                response = requests.get(product_href)
                soup = BeautifulSoup(response.text, 'html.parser')
                image_url = None  

                img_tag = soup.find("img", class_="pdp-media-slider__img zoom")
                if img_tag is not None:
                    image_url = img_tag.get("src")
                    print("Image URL:", image_url)
                else:
                    img_tag = soup.find("img", class_="pdp-media-slide__img")
                    if img_tag is not None:
                        image_url = img_tag.get("src")
                        print("Image URL:", image_url)

                if image_url is not None:
                    print("no")
                else:
                    print("Image URL not found")
            
                
                product_description = soup.find('div', class_='content-tab-content')

                if product_description:
                    
                    print(product_description.text)
                else:

                    product_description = soup.find('div', class_='pdp-short-description')

                    if product_description:
                        print(product_description.text)
                    else:
                        print("Description not found")

                
                p = product_description.find('p')
                if product_description is not None:
                    description = product_description.get_text()
                else:
                    product_description = "Description not found"

                
     

                product_list.append({
                    "name": product_name,
                    "price": product_price,
                    "href": product_href,
                    "description": product_description.text,
                    "image":image_url,
                    "category":"Waveseries",  
                    "brand":"Therabody" 
                    
                })

                waveseriesProduct = Waveseries(name=product_name, price=product_price, href=product_href, description=product_description.text, image=image_url,category="Waveseries",  
                    brand="Therabody" )
                db.session.add(waveseriesProduct)
                db.session.commit()
                print(waveseriesProduct)
            except Exception as e:
                print(f"Error scraping {product_href}: {str(e)}")

   

    print("Exit")

