
from inventory.manager import InventoryManager

def main():
    manager = InventoryManager()
    print("Loading Inventory Data")
    manager.load_from_csv("week1/data/inventory.csv")
    for item in manager.get_all_items():
        print(f"Product: {item.item_name} | Price: {item.price} | Qty: {item.quantity}")

if __name__ == "__main__":
    main()
