import json


def transform_product(data):
    def capitalize(text: str):
        return text.lower().capitalize()

    transformed_data = {
        "name": capitalize(data["product_name"]),
        "category": data["product_category"],
        "images": [list(image.keys())[0] for image in json.loads(data["product_images"])],
        "price": data["Price_usd"],
        "description": data["details"],
        "text": f"**Name** {capitalize(data['product_name'])}, \n**Description** {data['details']}, \n**Category** {data['product_category']}, \n**Price** {data['Price_usd']}"
    }
    return transformed_data


def transform_products(products, product_ids):
    texts = []
    metadatas = []
    id_map = {product['name']: product['id'] for product in product_ids}

    for product in products:
        transformed_product = transform_product(product)
        name = transformed_product['name']
        if name in id_map:
            transformed_product['id'] = id_map[name]
        text = transformed_product.pop("text")
        texts.append(text)
        metadatas.append(transformed_product)

    return texts, metadatas
