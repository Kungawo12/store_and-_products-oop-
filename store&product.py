class Store():
    def __init__(self,name):
        self.name = name
        self.product_list = []

    def add_products(self,new_product):
        self.product_list.append(new_product)
        return self
    
    def sell_product(self,id):
        sold_product =self.product_list.pop(id)
        sold_product.print_info()
        return self
    
    def print_info(self):
        print(f"name of the store: {self.name}")
        for product in self.product_list:
            product.print_info()
    
    def inflation(self, percent_increase):
        for product in self.product_list:
            product.update_price(percent_increase, is_increased = True)
        return self
    def set_clearance(self,category,percent_discount):
        for product in self.product_list:
            product.category == category
            product.update_price(percent_discount, is_increased = False)
        return self
class Product():
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += (self.price * percent_change/ 100)
        else:
            self.price -= (self.price * percent_change/ 100)
        return self
    
    def print_info(self):
        print(f"name of the product: {self.name}, \ncategory: {self.category}, \nprice: {self.price}")
        return self
Universal = Store("Asian")
Universal.add_products(Product("shoes", 100,"footwear"))
Universal.add_products(Product("jeans", 70,"clothes"))
Universal.add_products(Product("shirts", 40,"front wear"))
Universal.print_info()
Universal.sell_product(0)
Universal.inflation(10)  # Increase prices by 10%
Universal.set_clearance("clothes", 20)  # Reduce prices of Apparel by 20%

Universal.print_info()
# Universal.print_info()
