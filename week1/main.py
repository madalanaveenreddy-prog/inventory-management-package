from inventory.manager import InventoryManager

def main():
    manager = InventoryManager()
    
    print("--- Loading Inventory Data ---")
    manager.load_from_csv("week1/data/inventory.csv")
    
    print("\n--- Current Valid Inventory ---")
    for item in manager.get_all_items():
        print(f"Product: {item.item_name} | Price: {item.price} | Qty: {item.quantity}")

    for item in manager.get_low_stock_report(threshold=12):
        print(f": {item.item_name} is running low! Qty left: {item.quantity}")

if __name__ == "__main__":
    main()