# Python CRUD Application with MySQL

## Description
This project is an easy Python-based CRUD (Create, Read, Update, Delete) application that interacts with a MySQL database. It allows users to manage customer records stored in the database through a simple console-based interface. The project is designed with modularity and reusability in mind, using classes and methods to encapsulate functionality.

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
- **`initialize_db.py`**: Script to create the required database table (`customer`) automatically.

## Requirements
- Python 3.8 or higher
- MySQL Server
- `mysql-connector-python` library

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/matei84/Python_CRUD.git
   cd Python_CRUD
   ```

2. Install the required Python library:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the database connection in `Connection.py`:
   ```python
   DATABASE = 'ExampleDB'  # Replace with your database name
   USERNAME = 'root'        # Replace with your MySQL username
   PASSWORD = ''            # Replace with your MySQL password
   HOST = 'localhost'
   PORT = '3306'
   ```

4. Create the database (if it doesn't exist):
   - Open your MySQL terminal or use a GUI tool like MySQL Workbench.
   - Run the following command to create the database:
     ```sql
     CREATE DATABASE Example_db;
     ```

5. Run the `initialize_db.py` script to create the `customer` table:
   ```bash
   python initialize_db.py
   ```

   If successful, you should see:
   ```
   Table 'customer' created successfully.
   Connection closed.
   ```

6. Run the application:
   ```bash
   python App.py
   ```

## Usage
1. Follow the on-screen instructions to perform CRUD operations:
   - List all customers
   - Add a new customer
   - Update an existing customer
   - Delete a customer by ID

2. Example:
   - Adding a customer:
     ```
     Customer' name: John
     Customer' surname: Doe
     Customer' membership: 101
     ```
     Output:
     ```
     Cliente agregado a la BD: 1
     Customer John added successfully.
     Connection closed.
     ```

   - Listing customers:
     ```
     (1, 'John', 'Doe', 101)
     Total of customers: 1
     ```

## Error Handling
- **Duplicate Entry**: If you try to add a customer with a duplicate `membership` value, the application will display:
  ```
  Error: Duplicate entry for membership '101'.
  Connection closed.
  ```
- **General Errors**: Any unexpected errors will be caught and displayed in the console.

## Author
LM

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
