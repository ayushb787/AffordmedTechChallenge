import requests
import uuid
from src.services.auth_service import get_auth_token

PRODUCTS_API_URL = "http://20.244.56.144/test/companies/{companyname}/categories/{categoryname}/products"

def fetch_products(categoryname, n, minPrice, maxPrice, company, page, sort_by, order):
    access_token = get_auth_token()
    headers = {"authorization": f"Bearer {access_token}"}

    url = PRODUCTS_API_URL.format(companyname=company, categoryname=categoryname)

    params = {
        "top": n,
        "minPrice": minPrice,
        "maxPrice": maxPrice
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception("Failed to retrieve products")

    products = response.json()

    # Transform the response to match the schema
    transformed_products = []
    for product in products:
        transformed_product = {
            "productName": product.get("productName"),
            "company": company,
            "price": product.get("price"),
            "rating": product.get("rating"),
            "discount": product.get("discount"),
            "availability": product.get("availability"),
        }
        transformed_products.append(transformed_product)

    # Sorting logic
    if sort_by:
        reverse = True if order == "desc" else False
        transformed_products.sort(key=lambda x: x[sort_by], reverse=reverse)

    # Pagination logic
    start_idx = (page - 1) * n
    end_idx = start_idx + n
    paginated_products = transformed_products[start_idx:end_idx]

    return paginated_products

def fetch_product_details(categoryname, productid, company):
    access_token = get_auth_token()
    headers = {"Authorization": f"Bearer {access_token}"}

    url = PRODUCTS_API_URL.format(companyname=company, categoryname=categoryname)

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to retrieve product details")

    products = response.json()

    product = next((p for p in products if p.get("id") == productid), None)
    if not product:
        raise Exception("Product not found")

    return product
