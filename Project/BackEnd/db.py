from flask import Flask, render_template, request, redirect
import Controllers.userController as userController

app = Flask(__name__)



@app.route('/register', methods = ['POST'])
def upload():  
    name = request.json['name']
    password = request.json['password']
    amount = request.json['amount']
    isAdmin = request.json['isAdmin']
    code = userController.registerUser(name, password, amount, isAdmin)
    return f'''{code}'''

if __name__ == '__main__':
    app.run(debug=True)