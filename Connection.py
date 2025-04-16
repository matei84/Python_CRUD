import mysql.connector

class Connection:
    DATABASE = 'ExampleDB'
    USERNAME = 'root'
    PASSWORD = ''
    HOST = 'localhost'
    PORT = '3306'
    POOL_SIZE = 5
    POOL_NAME = 'default'
    pool = None

    @classmethod
    def get_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = mysql.connector.pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.PORT,
                    user=cls.USERNAME,
                    password=cls.PASSWORD,
                    database=cls.DATABASE
                )
                return cls.pool
            except ImportError:
                raise ImportError("mysql.connector is not installed. Please install it to use the connection pool.")
            except mysql.connector.Error as err:
                raise Exception(f"Error connecting to the database: {err}")
        else:
            return cls.pool

    @classmethod
    def get_connection(cls):
        if cls.pool is None:
            cls.pool = cls.get_pool()
        return cls.pool.get_connection()

    @classmethod
    def close_connection(cls, connection):
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":

    conn = Connection().get_connection()

    print(conn)
    
    
    # Test the connection
    if conn.is_connected():
        print(f"Connected to the database: {conn}" )
        Conexion.close_connection(conn)
    else:
        print("Failed to connect to the database")
    