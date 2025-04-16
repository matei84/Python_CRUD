from CustomerDao import CustomerDao
from Customer import Customer
from mysql.connector.errors import IntegrityError


class App:
    def __init__(self):
        self.CustomerDao = CustomerDao()
        #self.productos = []

    # Método de maquina de snacks
    def maquinaApp(self):
        leaving = False
        print('*** Application ***')
        #self.CustomerDao.get_all_customers()
        while not leaving:
            try:
                option = self.show_menu()
                leaving = self.execute_option(option)
            
            except Exception as e:
                print(f"Error: {e}")
                continue

    # Método de mostrar el menú
    def show_menu(self):
        print(f''' Menu:
            1. Show all customers
            2. Add customer
            3. Update customer
            4. Delete customer
            5. Exit''')
        return int(input("Seleccione una opción: "))

    # Método que ejecura la opción seleccionada
    def execute_option(self, opcion):
        if opcion == 1:
            self.get_all_customers()
        elif opcion == 2:
            self.add_customer()
        elif opcion == 3:
            self.update_customer()
        elif opcion == 4:
            self.delete_customer()
        elif opcion == 5:
            print("Going out of the app...")
            return True
        else:
            print(f"Opción no válida {opcion}.")
        return False

    # Método para mostrar todos los clientes
    def get_all_customers(self):
        customers = self.CustomerDao.get_all_customers()
        for customer in customers:
            print(customer)
        print(f"Total of customers: {len(customers)}")

    # Método para agregar un cliente
    def add_customer(self):
        try:
            name = input("Customer' name: ")
            surname = input("Customer' surname: ")
            membership = int(input("Customer' membership: "))
            customer = Customer(name=name, surname=surname, membership=membership)
            self.CustomerDao.add_customer(customer)
        except Exception as e:
            print(f"Error TESTEO: {e}")
            
    # Método para actualizar un cliente    
    def update_customer(self):
        id = int(input("Customer' id: "))
        name = input("Customer' name: ")
        surname = input("Customer' surname: ")
        membership = int(input("Customer' membership: "))
        customer = Customer(id=id, name=name, surname=surname, membership=membership)
        self.CustomerDao.update_customer(customer)
    
    # Método para eliminar un cliente
    def delete_customer(self):
        id = int(input("Customer' id: "))
        self.CustomerDao.delete_customer(id)

# Programa principal

if __name__ == "__main__":
    application = App()
    application.maquinaApp()