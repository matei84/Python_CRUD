from Customer import Customer
from Connection import Connection
from mysql.connector.errors import IntegrityError


class CustomerDao:

    GET_ALL_CUSTOMERS = "SELECT * FROM customer order By id"
    INSERT_CUSTOMER = "INSERT INTO customer (name, surname, membership) VALUES (%s, %s, %s)"
    UPDATE_CUSTOMER = "UPDATE customer SET name=%s, surname=%s, membership=%s WHERE id=%s"
    DELETE_CUSTOMER = "DELETE FROM customer WHERE id=%s"

    def __init__(self):
        pass

    #Metodo para obtener todos los clientes
    @classmethod
    def get_all_customers(cls):
        try:
            connection = Connection.get_connection()
            cursor = connection.cursor()
            cursor.execute(cls.GET_ALL_CUSTOMERS)
            rows = cursor.fetchall()
            cursor.close()
            customers = []
            for row in rows:
                customers.append(Customer(row[0], row[1], row[2], row[3]))
            return customers
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
                connection.close()
            print("Connection closed.")

    #Metodo para obtener todos los clientes
    @classmethod
    def add_customer(cls, customer):
        try:
            connection = Connection.get_connection()
            cursor = connection.cursor()
            VALUES =  (customer.name, customer.surname, customer.membership)
            cursor.execute(cls.INSERT_CUSTOMER, VALUES)   
            connection.commit()
            print(f"Clientes agregado a la BD: {cursor.rowcount}")
            print(f"Customer {customer.name} added successfully.")
            cursor.close()
        except IntegrityError as e:
            print(f"Error: Duplicate entry for membership '{customer.membership}'.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
               connection.close()
            print("Connection closed.")

    #Metodo para actualizar un cliente
    @classmethod
    def update_customer(cls, customer):
        try:
            connection = Connection.get_connection()
            cursor = connection.cursor()
            VALUES =  (customer.name, customer.surname, customer.membership, customer.id)
            cursor.execute(cls.UPDATE_CUSTOMER, VALUES)   
            connection.commit()
            print(f"Clientes actualizados a la BD: {cursor.rowcount}")
            print(f"Updated Customer: {customer.name} successfully.")
            cursor.close()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
               connection.close()
            print("Connection closed.")

    #Metodo para actualizar un cliente
    @classmethod
    def delete_customer(cls, id):
        try:
            connection = Connection.get_connection()
            cursor = connection.cursor()
            cursor.execute(cls.DELETE_CUSTOMER, [id])   
            connection.commit()
            print(f"Customer deleted.")
            cursor.close()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
               connection.close()
            print("Connection closed.")   