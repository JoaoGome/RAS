import mysql.connector
from mysql.connector import Error

# criar ligação com a base de dados
def create_server_connection(host_name, user_name, user_password,db_name):
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

# executa a query @query 
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        return (200)
    except Error as err:
        return (400)


def registerUser(name, password, amount, isAdmin):
    connection = create_server_connection("localhost", "root", "JprG7654", "RAS")
    query = f'''
        INSERT INTO user VALUES
        (4, '{name}', '{password}', {amount}, {isAdmin});
    '''
    code = execute_query(connection,query)
    return code