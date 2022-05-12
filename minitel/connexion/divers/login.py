#!/usr/bin/env python3

import os
# import register
import progress 

def login():
    os.system('clear')
    print("""



                                 ________________________________________________________________
                                |                                                                |
                                |          _____                             _                   | 
                                |         /  __ \                           (_)                  |
                                |        | /  \/ ___  _ __  _ __   _____  ___  ___  _ __         |
                                |        | |    / _ \| '_ \| '_ \ / _ \ \/ / |/ _ \| '_ \        |  
                                |        | \__/\ (_) | | | | | | |  __/>  <| | (_) | | | |       | 
                                |         \____/\___/|_| |_|_| |_|\___/_/\_\_|\___/|_| |_|       |
                                |                                                                |
                                |________________________________________________________________|




    Cliquez juste sur entrer pour vous créer un compte. 


    """)
    db = open("db.txt", "r")
    username = input("Entrez votre pseudo : ")

    if not username: 
        # register()
        # login()
        return 'pasusername'

    if len(username)> 0 : 
        login = []
        passwd = []
        for i in db: 
            a,b = i.split(", ")
            b = b.strip()
            login.append(a)
            passwd.append(b)
        data = dict(zip(login, passwd))

        if username not in data.keys(): 
            print("\nL'utilisateur entré ne correspond à aucun compte enregistré. Recommencez !\n")
            login()

        password = input("Entrez votre mot de passe : ")

        if data[username]: 
            if password == data[username]: 
                print("\nConnexion avec succès  \n")
                print("Bonjour ", username, ", vous serz redirigez vers le minitel dans quelques instants. \n")
                progress.progressbar()
                # os.system('python3 ~/.envvar/minitel/main.py')
            elif passwd != data[username]:  
                print("\nMauvais mot de passe, recommencez !\n ")
                # time.sleep(0.03)
                login()

