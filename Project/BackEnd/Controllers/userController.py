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
    connection = create_server_connection("localhost", "root", "JprG7654", "mydb")
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except Error as err:
        return 400

# função a usar para registar um user
def registerUser(username, name, password, isAdmin, valor, moeda):
    connection = create_server_connection("localhost", "root", "JprG7654", "mydb")
    query = f'''
        INSERT INTO user (username, name, password, isAdmin) 
        VALUES  ('{username}', '{name}', {password}, {isAdmin});
    '''
    if (execute_query(connection,query) == 200):
        queryUser = f'''
            SELECT user_id FROM user WHERE username = "{username}";
        ''' 
        user_id = (read_query(queryUser)[0])[0]

        queryMoeda = f'''
            SELECT moeda_id FROM moeda WHERE nome = "{moeda}";
        ''' 
        moeda_id = (read_query(queryMoeda)[0])[0]
        query3 = f'''
            INSERT INTO userMoeda (user_id, moeda_id, valor)
            VALUES ({user_id},{moeda_id},{valor});
        '''

        return execute_query(connection,query3)

# função a usar para receber a lista de todos os users e os seus dados
def getUsers():
    connection = create_server_connection("localhost", "root", "JprG7654", "mydb")
    query = f'''
        SELECT * FROM user;
    '''
    return read_query(query)

# função a usar para receber os dados de um user dado o ser name
def getUser(username):
    connection = create_server_connection("localhost", "root", "JprG7654", "mydb")
    query = f'''
        SELECT * FROM user WHERE user.username = "{username}";
    '''
    return read_query(query)
    

# função que verifica que se já existe na bd um user com um dado name, util para verificar quando alguem tentar fazer um registo
def checkUserExists(username):
    result = getUser(username)
    if not result:  # veio resultado vazio, ou seja, nao existe uma entrada na bd com este name
        return "0"

    return "1"
        
# função que verifica se as credenciais estão corretas. para ser usada no log in
def checkCredentials(name,password):
    connection = create_server_connection("localhost", "root", "JprG7654", "mydb")
    query = f'''
        SELECT * FROM user WHERE (user.name = "{name}") AND (user.password = "{password}");
    '''
    result = read_query(query)
    if not result: return "0"

    return "1"

# função que verifica se um dado user tem dinheiro para fazer a aposta que pretende

def checkCredito(moeda_id, valor, user_id):
    connection = create_server_connection("localhost", "root", "JprG7654", "mydb")
    query = f'''
        SELECT valor FROM userMoeda WHERE user_id = {user_id} AND moeda_id = {moeda_id}
    '''

    valorBD = (read_query(query)[0])[0]

    if (valorBD < valor):
        return 0

    return 1

    