import view
import requests
import json

currentLogInUser = "" # variavel que vai manter o valor do ser que está logged in neste momento


view.showFirstScreen()

while (True):
    if (input() == "1"): #user quer fazer log in
        view.showAskUsername()
        username = input()
        if (username == "quit"): 
            break

        view.showAskPassword()
        password = input()
        if (password == "quit"):
            break
        
        payload =   {
                        "name": username, 
                        "password": password
                    }
                    
        r = requests.post('http://127.0.0.1:5000/login', json=payload, headers={'Content-Type':'application/json'})
        response = json.loads(r.text)
        print(response)
        break

        

        



