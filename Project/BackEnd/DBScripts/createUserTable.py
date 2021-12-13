import mysql.connector
from mysql.connector import Error

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


# Query string para criar as tabelas
create_user_table = """
CREATE TABLE user (
  user_id INT PRIMARY KEY,
  name VARCHAR(40) NOT NULL,
  amount FLOAT,
  isAdmin INT
  );
 """

# Criar conexão à base de dados
connection = create_db_connection("localhost", "root", "JprG7654", "RAS")
execute_query(connection, create_user_table)