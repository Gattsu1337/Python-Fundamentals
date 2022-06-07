class Catalogue:
    products = []

    def __init__(self, name: str):
        self.name = name

    def add_product(self, product_name: str):
        Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        new_list = [item for item in Catalogue.products if list(item)[0] == first_letter]
        return new_list

    def __repr__(self):
        result = ''
        Catalogue.products.sort()
        result += f"Items in the {self.name} catalogue:\n"
        result += '\n'.join(Catalogue.products)
        return result
