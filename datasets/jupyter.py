# import requests
# from bs4 import BeautifulSoup


# url = "https://www.therabody.com/"
# response = requests.get(url)


# soup = BeautifulSoup(response.text, "html.parser")

# products = []

# for product_elem in soup.find_all("div", class_="product"):
#     product_name = product_elem.find("h2", class_="name-link").text
#     product_price = product_elem.find("span", class_="price-sales").text
#     product_image = product_elem.find("img")["src"]
#     product_description = product_elem.find("p", class_="content-asset").text

#     products.append({
#         "name": product_name,
#         "price": product_price,
#         "image": product_image,
#         "description": product_description
#     })

