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

# usar esta função quando for para executar uma query e só queremos saber se correu bem (200) ou mal (400)
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        return 200
    except Error as err:
        return 400

# usar esta função quando for para executar uma query e receber um resultado. Neste caso, o resultado vai ser devolvido na variavel result
def read_query(query):
    connection = create_server_connection("localhost", "root", "JprG7654", "RAS")
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        return 400


# função a usar para registar um user
def registerUser(name, password, amount, isAdmin):
    connection = create_server_connection("localhost", "root", "JprG7654", "RAS")
    query = f'''
        INSERT INTO user (name, password, amount, isAdmin) 
        VALUES  ('{name}', '{password}', {amount}, {isAdmin});
    '''
    code = execute_query(connection,query)
    return code

# função a usar para receber a lista de todos os users e os seus dados
def getUsers():
    connection = create_server_connection("localhost", "root", "JprG7654", "RAS")
    query = f'''
        SELECT * FROM user;
    '''
    return read_query(query)

# função a usar para receber os dados de um user dado o ser name
def getUser(name):
    connection = create_server_connection("localhost", "root", "JprG7654", "RAS")
    query = f'''
        SELECT * FROM user WHERE user.name = "{name}";
    '''
    return read_query(query)
    
