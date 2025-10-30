import json
import logging
from datetime import datetime


# Global variables
stock_data = {}
logs = []  # for activity tracking


def addItem(item, qty):
    """Add an item to inventory with proper validation and logging."""
    try:
        if not isinstance(item, str) or not item.strip():
            raise ValueError("Item name must be a non-empty string.")
        qty = int(qty)
        stock_data[item] = stock_data.get(item, 0) + qty
        logs.append(f"{datetime.now()}: Added {qty} of {item}")
        logging.info("Added %d of %s", qty, item)
    except ValueError as e:
        logging.error("Invalid input in addItem: %s", e)


def removeItem(item, qty):
    """Remove an item from inventory with specific exception handling."""
    try:
        qty = int(qty)
        if item not in stock_data:
            logging.warning("Attempted to remove non-existent item: %s", item)
            return
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
        logs.append(f"{datetime.now()}: Removed {qty} of {item}")
        logging.info("Removed %d of %s", qty, item)
    except ValueError as e:
        logging.error("Invalid quantity in removeItem: %s", e)
    except KeyError as e:
        logging.error("KeyError in removeItem: %s", e)


def getQty(item):
    """Return the quantity of a specific item."""
    return stock_data.get(item, 0)


def loadData(file="inventory.json"):
    """Load stock data from a JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        stock_data = {}
    except json.JSONDecodeError as e:
        logging.error("Failed to load data: %s", e)


def saveData(file="inventory.json"):
    """Save stock data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)


def printData():
    """Print all items and their quantities."""
    print("\nItems Report:")
    if not stock_data:
        print("No items in inventory.")
    else:
        for i in stock_data:
            print(f"{i} -> {stock_data[i]}")


def checkLowItems(threshold=5):
    """Return items below a given stock threshold."""
    return [i for i, q in stock_data.items() if q < threshold]


def saveLogs(file="activity.log"):
    """Save activity logs to a text file."""
    with open(file, "a", encoding="utf-8") as f:
        for entry in logs:
            f.write(entry + "\n")
    logs.clear()


def main():
    """Main execution block."""
    logging.basicConfig(
        filename="inventory.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    loadData()
    addItem("apple", 10)
    addItem("banana", 2)
    addItem("orange", "ten")  # invalid quantity handled
    removeItem("apple", 3)
    removeItem("orange", 1)
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    saveData()
    saveLogs()
    printData()


if __name__ == "__main__":
    main()
