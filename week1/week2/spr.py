class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product_name, price, rating, discount):
        self.products.append({
            "product_name": product_name,
            "price": price,
            "rating": rating,
            "discount": discount
        })


class TotalValue:
    def calculate_total_value(self, cart):
        total = 0
        for item in cart.products:
            price = item["price"]
            discount = item["discount"]
            final_price = price - (price * discount / 100)
            total += final_price
        return total


class DiscountCalculator:
    def apply_item_discount(self, cart):
        discounted_items = []

        for item in cart.products:
            price = item["price"]
            discount = item["discount"]

            final_price = price - (price * discount / 100)

            discounted_items.append({
                "product_name": item["product_name"],
                "final_price": final_price
            })

        return discounted_items

class generate_invoice:
    def show_invoice(self,discount_calc,calc,cart):
        total_price_after_discount=discount_calc.apply_item_discount(cart)
        total=calc.calculate_total_value(cart)
        return total_price_after_discount,total
        

cart = ShoppingCart()
cart.add_product("shampoo", 23, 2.5, 10)
cart.add_product("towel", 67, 8.9, 5)
cart.add_product("soap", 63, 1.5, 20)

print("Cart:", cart.products)

calc = TotalValue()
print("Total after discount:", calc.calculate_total_value(cart))

discount_calc = DiscountCalculator()
print("Discounted items:", discount_calc.apply_item_discount(cart))

invoice=generate_invoice()
bill=invoice.show_invoice(discount_calc,calc,cart)
print(bill)
# --------