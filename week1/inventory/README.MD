markdown
# Inventory Management Package

A production-ready, structured Python package designed to read, validate, and manage product inventory data from CSV files. This project implements core Object-Oriented Programming (OOP) principles and modern software design patterns.

## 🚀 Key Features
- **Data Validation:** Uses **Pydantic** (`BaseModel`) to strictly validate data types and catch input errors.
- **Robust Error Handling:** Features a **Singleton Logger** to capture and log validation failures without crashing the application.
- **Encapsulation:** Protects core inventory data structures using Python private variables.
- **Clean Architecture:** Organized cleanly into reusable modules and packages.

## 🛠️ Tech Stack & Tools
- **Language:** Python 3
- **Validation:** Pydantic
- **Formatting:** Black
- **Linting:** Ruff

## 📂 Project Structure
```text
inventory_project/
│
├── inventory/                  # Core Package
│   ├── __init__.py             # Exposes package interface
│   ├── models.py               # Pydantic validation models
│   ├── logger.py               # Singleton logger module
│   └── manager.py              # Inventory core logic
│
├── data/
│   └── inventory.csv           # Raw inventory input data
│
└── main.py                     # Main execution script
```

## ⚙️ How to Run
Run the main script from your terminal:
```bash
python3 week1/main.py
