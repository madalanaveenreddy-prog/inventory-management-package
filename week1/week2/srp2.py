# solid princile designs

class shopping_cart:
    def __init__(self):
        self.products=[]
    def add_product(self,product_name,price):
        self.products.append({
            "name":product_name,
            "price":price

        })
        
class total_product_value:
    def get_total(self,cart):
        total=0
        for i in cart.products:
            total+=i["price"]
        return total
        
class InvoicePrinter:
    def print_invoice(self,cart,calculation):

        for product in cart.products:
            print(f"{product['name']} : ₹{product['price']}")

        
        print(f"Total Bill : ₹{calculation.get_total(cart)}")

class database:
    def store_in_database(self):
        return "data stored in database"


cart=shopping_cart()
cart.add_product("laptop",1235)
cart.add_product("keyboard",896)
cart.add_product("mouse",453)



calculation=total_product_value()
invoice=InvoicePrinter()
invoice.print_invoice(cart,calculation)

DataBase=database()
print(DataBase.store_in_database())
