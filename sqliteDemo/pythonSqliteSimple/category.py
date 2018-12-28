class Category:

    def __init__(self, category_name, description, no_of_item):
        self.category_name = category_name
        self.description = description
        self.no_of_item = no_of_item

    @property
    def category_names(self):
        return '{}.{}'.format(self.category_name, self.description)

    def __repr__(self):
        return "category('{}','{}','{}')".format(self.category_name, self.description)






