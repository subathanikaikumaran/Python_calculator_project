class Product:

    def __init__(self, product_name, category, product_price):
        self.product_name = product_name
        self.category = category
        self.product_price = product_price

    @property
    def product_names(self):
        return '{}.{}'.format(self.product_name, self.category)

    def __repr__(self):
        return "Product('{}','{}','{}')".format(self.product_name, self.category)






