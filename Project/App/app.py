import view

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

        print(username + password)

        



