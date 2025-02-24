import json
import re

def load_json():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data

def write_json(data, file):
    with open(f'{file}.json', 'w') as f:
        json.dump(data, f, indent=4)


#returns the data, status, and index of the product
def find_product(product, products):
    counter = 0
    try:
        for prod in products["Data"]:
            if prod["Product"] == product:
                resp_dict = {"data": prod, "status": True, "index": counter}
                return resp_dict
            counter+=1
    except:
        print("Error")

    return {"data": {}, "status": False, "index": -1}


def get_price(product_name, date_to_search):
    products = load_json()
    found = find_product(product_name, products)

    counter = 0
    for date in found["data"]["Dates"]:
        if date == date_to_search:
            return found["data"]["Prices"][counter]
        counter+=1
    return 0

#returns the list of searched product
def search_product(product):
    list = []
    products = load_json()
    for prod in products["Data"]:
        match_product = re.search(product.lower(), prod.get("Product").lower())
        if match_product:
            list.append(prod)

    return list


def add_new_product(product_name, website, date, price):
    products = load_json()

    found = find_product(product_name, products)

    if not found["status"]:
        new_product = {'Product': product_name, 'Website': website, 'Dates': [date], 'Prices': [price]}
        products["Data"].append(new_product)
        write_json(products, "data")
        return True
    return False

def update_price_history(product_name, new_price):
    products = load_json()
    found = find_product(product_name, products)
    index = found["index"]

    if found["status"]:
        products["Data"][index]["Prices"].append(new_price)
        write_json(products, "data")
        return True
    return False


def update_date_history(product_name, new_date):
    products = load_json()
    found = find_product(product_name, products)
    index = found["index"]

    if found["status"]:
        products["Data"][index]["Dates"].append(new_date)
        write_json(products, "data")
        return True
    return False


def update_date_price(product_name, new_date, new_price):
    products = load_json()
    found = find_product(product_name, products)
    index = found["index"]

    if found["status"]:
        products["Data"][index]["Dates"].append(new_date)
        products["Data"][index]["Prices"].append(new_price)
        write_json(products, "data")
        return True
    return False

def edit_product_name(product_name, new_name):
    products = load_json()
    found = find_product(product_name, products)
    index = found["index"]

    if found["status"]:
        products["Data"][index]["Product"] = new_name
        write_json(products, "data")
        return True
    return False


def delete_product(product_name):
    products = load_json()
    found = find_product(product_name, products)
    index = found["index"]

    if found["status"]:
        products["Data"].pop(index)
        write_json(products, "data")
        return True
    return False

edit_product_name("Laptop", "Asus rog")