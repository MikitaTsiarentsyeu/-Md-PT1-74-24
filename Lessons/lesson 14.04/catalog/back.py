repo = [{"name":"test product", "descr":"very interesting product", "price":33}]

attrs = ["name", "descr", "price"]

def show_all():
    if not repo:
        raise RuntimeError("there are no products in catalog right now")
    return '\n'.join([format_product(p) for p in repo])

def add_product(*values):
    if len(attrs) != len(values):
        raise RuntimeError("insufficient number of product attrs")
    product = {}
    for i, attr in enumerate(attrs):
        product[attr] = values[i]
    repo.append(product)

def remove_product(value):
    try:
        p = search_product(value)
        if p:
            del repo[p[0]]
            return "the product was removed"
    except:
        return "something went wrong, please try again later"

def search_product(value):
    for i, p in enumerate(repo):
        if p[attrs[0]] == value:
            return i, p

def search(value):
    p = search_product(value)
    if p:
        return format_product(p[1])
    return "nothing was found"

def format_product(product):
    return ';'.join([f"{k}:{v}" for k, v in product.items()])