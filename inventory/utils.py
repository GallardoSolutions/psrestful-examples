def gen_all_products(all_sellable_products: list) -> list:
    ret = []
    previous_product_id = None
    variants = []
    for product in all_sellable_products:
        if product['productId'] == previous_product_id:
            variants.append(product['partId'])
        else:
            if previous_product_id:
                ret.append({'productId': product['productId'], 'variants': ', '.join(variants)})
            variants = [product['partId']]
            previous_product_id = product['productId']
    return ret
