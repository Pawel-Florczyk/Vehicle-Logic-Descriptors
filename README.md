# Vehicle Logic Descriptors

A professional Python-based management system for various types of vehicles (Cars, Motorcycles, Cross-Bikes). The project demonstrates advanced Object-Oriented Programming (OOP) concepts, custom data validation using descriptors, and defensive programming techniques.

## Key Features

* **Advanced Data Validation:** Uses custom Python Descriptors to manage fuel levels and mileage, ensuring data integrity (e.g., preventing odometer rollback).
* **Dynamic Constraints:** Fuel tank capacity is dynamically validated based on the specific vehicle model using the `type(self)` protocol.
* **Defensive Logic:** Smart methods for `ride`, `training`, and `tanking` that prevent invalid operations (like riding without fuel or overfilling the tank).
* **Clean Architecture:** Clear separation of concerns with dedicated modules for descriptors, vehicle types, and error handling.

## Tech Stack

* **Language:** Python 3.9+
* **Linting:** Flake8 (PEP 8 compliance)
* **Concepts:** Descriptors, Inheritance, Encapsulation, Custom Exceptions.

## Project Structure

```text
├── descriptors.py      # Custom descriptors (Counter, Tank)
├── vehicle_types.py    # Vehicle class hierarchy
├── errors.py           # Custom exception classes
├── main.py             # Application entry point & simulation
├── requirements.txt    # Project dependencies
└── .flake8             # Linter configuration
```

## Running program via Docker Compose
```bash
docker compose up --build
```

## Running program via Docker (Alternative):

1. Building an image
```bash
docker build -t vehicle-logic-descriptors .
```

2. Running program (container)
```bash
docker run -v .:/app vehicle-logic-descriptors
```
