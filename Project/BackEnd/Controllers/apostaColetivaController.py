import mysql.connector
from mysql.connector import Error
import userController as User

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


# função para o admin criar uma aposta
# oddsw -> odds de clube 1 ganhar; oddsd -> odds de draw; oddsl -> odds de clube 2 ganhar
def criarAposta(clube1, clube2, oddsw, oddsd, oddsl):
    connection = create_server_connection("localhost", "root", "JprG7654", "mydb")
    
    query = f'''
        INSERT INTO apostaColetiva (estado, clube1, clube2, oddsw, oddsd, oddsl) 
        VALUES (1, '{clube1}', '{clube2}', {oddsw}, {oddsd}, {oddsl});
    '''

    return execute_query(connection,query)


# função que devolve todas as aposta abertas (estado = 1)
def getApostas():
    connection = create_server_connection("localhost", "root", "JprG7654", "mydb")
    query = f'''
        SELECT * FROM apostaColetiva WHERE estado = 1;
    '''

    return read_query(query)

# função quando um user quiser fazer uma aposta
# resultado = 1 se clube 1 ganhar, 0 se draw, -1 se clube 2 ganhar
def fazerAposta(user_id, apostaColetiva_id, resultado, moeda_id, valor):
    connection = create_server_connection("localhost", "root", "JprG7654", "mydb")
    query = f'''
        INSERT INTO userApostaColectiva (user_id, apostaColetiva_id, resultado, moeda_id, valor)
        VALUES ({user_id},{apostaColetiva_id}, {resultado}, {moeda_id},{valor})
    '''

    return execute_query(connection, query)

def closeAposta (aposta_id, result):

    connection = create_server_connection("localhost", "root", "JprG7654", "mydb")
    query = f'''
        SELECT oddsw, oddsd, oddsl FROM apostaColetiva WHERE id={aposta_id};
    '''

    result1 = read_query(query)

    if (result == 1):
        odds = [result1][0]
    elif(result == 0):
        odds = [result1][1]
    else:
        odds = [result1][2]

    query = f'''
        SELECT * FROM userApostaColectiva WHERE apostaColetiva_id={aposta_id};
    '''

    result = read_query(query)
    
    for x in result:
        if (x[3] == result):
            valor = x[5] * odds
            moeda_id = x[4]

            query = f'''
                UPDATE userMoeda SET valor={valor} WHERE user_id={x[1]} AND moeda_id={x[4]};
            '''
            execute_query(connection, query)
    
    query = f'''
            UPDATE apostaColetiva SET estado={0} WHERE id={aposta_id};
        '''

    execute_query(connection,query)



