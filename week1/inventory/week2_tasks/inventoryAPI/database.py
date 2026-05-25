from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, id: int, name: str, base_price: float):
        self.id = id
        self.name = name
        self.base_price = base_price

    @abstractmethod
    def calculate_total_price(self) -> float:
        pass

class PhysicalProduct(Product):
    def calculate_total_price(self) -> float:
        return self.base_price + 5.0

class DigitalProduct(Product):
    def calculate_total_price(self) -> float:
        return self.base_price * 1.18

class InventoryManager:
    def __init__(self):
        # Using sample mock data so your advance routes aren't empty on launch
        self._products = {
            1: PhysicalProduct(1, "Laptop Stand", 45.0),
            2: DigitalProduct(2, "Antivirus License", 20.0)
        }

    def add_product(self, product: Product):
        self._products[product.id] = product

    # 1.  Get a single product by ID
    def get_product_by_id(self, product_id: int):
        return self._products.get(product_id)

    # 2. New Logic: Get all products with a Query Parameter filter
    def get_all_products(self, max_price: float = None):
        results = []
        for p in self._products.values():
            total = p.calculate_total_price()
            # If max_price query is provided, filter out expensive items
            if max_price is not None and total > max_price:
                continue
            
            # Determine type dynamically for presentation
            p_type = "physical" if isinstance(p, PhysicalProduct) else "digital"
            
            results.append({
                "id": p.id,
                "name": p.name,
                "base_price": p.base_price,
                "total_price": total,
                "product_type": p_type
            })
        return results

    # 3. New Logic: Delete product
    def delete_product(self, product_id: int) -> bool:
        if product_id in self._products:
            del self._products[product_id]
            return True
        return False

fake_db = InventoryManager()
