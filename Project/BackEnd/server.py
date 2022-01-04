from flask import Flask, render_template, request, redirect
import Controllers.userController as userController

app = Flask(__name__)


# rota usada para devolver a lista de todos os users e os seus dados
# devolve em formato json/dict 
@app.route('/users')
def users():
    lista = userController.getUsers()
    result = {}
    for l in lista:
        tmp = {l[0]: {
                "name": l[1],
                "password": l[2],
                "amount": l[3],
                "isAdmin": l[4]
              }}
        result.update(tmp)

    return result


# rota a usar para receber os dados de um user em particular, definido pelo user_name
# devolve o resultado em json/dict
@app.route('/user/<user_name>')
def user(user_name):
    user = userController.getUser(user_name)
    if not user:
        return {}

    return {
            "user_id": user[0][0],
            "name": user[0][1],
            "password": user[0][2],
            "amount": user[0][3],
            "isAdmin": user[0][4]
           }
    

# rota usada para registar um user. 
# os dados do User (name, password, amount, isAdmin) devem ser passados em formato json ou entao da erro
@app.route('/register', methods = ['POST'])
def register():  
    name = request.json['name']

    available = userController.checkUserExists(name)
    if (available == "0"):
        password = request.json['password']
        amount = request.json['amount']
        isAdmin = request.json['isAdmin']

   
        code = userController.registerUser(name, password, amount, isAdmin)
        if (code == 200):
            return {"sucess": "User registado com sucesso"}
        else:
            return {"error": "Erro a inserir user. Tente outra vez mais tarde"}

    else:
        return {"error": "Name já utilizado."}

# rota usada para fazer log in de um user
@app.route('/login', methods = ['POST'])
def login():
    print(request.json)
    name = request.json['name']
    password = request.json['password']

    logIn = userController.checkCredentials(name,password)

    if (logIn == "0"): 
        return {"error": "Credenciais erradas"}

    else:
        return {"sucess": "Log in com sucesso"}

if __name__ == '__main__':
    app.run(debug=True)