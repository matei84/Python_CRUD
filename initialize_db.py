from Connection import Connection

def create_table():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS customer1 (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(50),
        surname VARCHAR(50),
        membership INT UNIQUE,
        PRIMARY KEY (id)
    );
    """
    try:
        connection = Connection.get_connection()
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        print("Table 'customer' created successfully.")
        cursor.close()
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        if connection.is_connected():
            connection.close()
        print("Connection closed.")

if __name__ == "__main__":
    create_table()