import csv
from .models import ItemModel
from .logger import logger

class InventoryManager:
    def __init__(self):
        self.__items = []  # Encapsulated list

    def load_from_csv(self, file_path: str):
        try:
            with open(file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        # Pydantic validition
                        validated_item = ItemModel(**row)
                        self.__items.append(validated_item)
                        logger.info(f"Successfully loaded: {validated_item.item_name}")
                    except Exception as e:
                        logger.error(f"Validation Failed for row {row}: {e}")
        except FileNotFoundError:
            logger.error(f"File not found at: {file_path}")
        
    # added logic of getting low stock quantity
    def get_low_stock_report(self, threshold: int = 5):
        low_stock_list = []
        for item in self.get_all_items():
            if item.quantity < threshold:
                low_stock_list.append(item)
        return low_stock_list

    def get_all_items(self):
        return self.__items
