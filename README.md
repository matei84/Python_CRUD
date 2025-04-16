# Python CRUD Application with MySQL

## Description
This project is a Python-based CRUD (Create, Read, Update, Delete) application that interacts with a MySQL database. It allows users to manage customer records stored in the database through a simple console-based interface. The project is designed with modularity and reusability in mind, using classes and methods to encapsulate functionality.

## Features
1. **List All Customers**: Retrieve and display all customer records from the database.
2. **Add a Customer**: Insert a new customer into the database.
3. **Update a Customer**: Modify the details of an existing customer.
4. **Delete a Customer**: Remove a customer from the database by their ID.
5. **Error Handling**: Gracefully handles database errors, such as duplicate entries or connection issues.

## Project Structure
- **`App.py`**: The main entry point of the application. It handles user input and calls the appropriate methods for CRUD operations.
- **`CustomerDao.py`**: Contains the database interaction logic, including SQL queries and exception handling.
- **`Connection.py`**: Manages the connection pool to the MySQL database.
- **`Customer.py`**: Defines the `Customer` class, which represents a customer entity.

## Requirements
- Python 3.8 or higher
- MySQL Server
- `mysql-connector-python` library

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/matei84/Python_CRUD.git
   cd your-repository-name
