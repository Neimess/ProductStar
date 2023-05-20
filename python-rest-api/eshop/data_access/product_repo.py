from typing import List, Optional

from eshop.businsess_logic.product import Product

_products: List[Product] = []


def save(product: Product):
    for i in range(len(_products)):
        existed_product = _products[i]
        if existed_product.id == product.id:
            _products[i] = product
            break
    else:
        _products.append(product)


def delete_by_id(id: str):
    global _products
    _products = [p for p in _products if p.id != id]


def get_by_id(id: str) -> Optional[Product]:
    return next((p for p in _products if p.id == id), None)


def get_many(page: int = 0, limit: int = 10):
    start = page * limit
    end = start + limit
    return _products[start:end]

def save(product: Product):
    for i in range(len(_products)):
        existed_product = _products[i]
        if existed_product.id == product.id:
            _products[i] = product
            break
    else:
        _products.append(product)