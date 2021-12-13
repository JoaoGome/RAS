import mysql.connector
from mysql.connector import Error


# Função que começa a conexão com a base de dados. Aqui o user e a password é o que vocês definiram ao dar setp ao mysql

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

# Correr para criar a base de dados e as tabelas

connection = create_server_connection("localhost", "root", "JprG7654")
database_creation_query = "CREATE DATABASE RAS"
create_database(connection,database_creation_query)