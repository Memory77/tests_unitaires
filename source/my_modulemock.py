import random
import requests

def f1():
    return random.randint(1,100)

def f2():
    result = f1()
    return result * 10



def fetch_product_price(product_id):
    response = requests.get(f"<https://api.example.com/products/{product_id}>")
    return response.json()['price']

def calculate_tax(product_id):
    price = fetch_product_price(product_id)
    tax_rate = 0.20  # 20% Tax
    return price * tax_rate