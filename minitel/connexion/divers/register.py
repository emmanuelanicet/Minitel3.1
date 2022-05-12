#!/usr/bin/env python3

import os
import sys
# import login

def register(): 
    os.system('clear')
    print("""



                                 _____________________________________________________________________________________
                                |                                                                                     |
                                |         _____                     _     _                                 _         |   
                                |        |  ___|                   (_)   | |                               | |        |   
                                |        | |__ _ __  _ __ ___  __ _ _ ___| |_ _ __ ___ _ __ ___   ___ _ __ | |_       | 
                                |        |  __| '_ \| '__/ _ \/ _` | / __| __| '__/ _ \ '_ ` _ \ / _ \ '_ \| __|      | 
                                |        | |__| | | | | |  __/ (_| | \__ \ |_| | |  __/ | | | | |  __/ | | | |_       | 
                                |        \____/_| |_|_|  \___|\__, |_|___/\__|_|  \___|_| |_| |_|\___|_| |_|\__|      | 
                                |                              __/ |                                                  |
                                |                             |___/                                                   |
                                |_____________________________________________________________________________________|





    Cliquez juste sur entrer pour passer directement à l'écran de connexion. 


    """)

    db = open("db.txt", "r") #r = droit de lecture (chmod -r) 
    username = input("Choisissez votre pseudo : ")

    login = []
    passwd = []

    for i in db: 
        a,b = i.split(", ")    #["hello, my name is Peter, I am 26 years old"] => ['hello', 'my name is Peter', 'I am 26 years old']
        b = b.strip()           #supprime les caratères de début et de fin ex : '     Learn Python  ' =>Learn Python
        login.append(a)
        passwd.append(b)
    datas = dict(zip(login, passwd))

    if username == "": 
        login()

    if username in login: 
            print("\nCe pseudo est déjà prit, recommencez !\n")
            register()

    password = input("Choisissez un mot de passe avec minimum 8 caractères : ")

    if len(password) < 8 : 
            print("\nMot de passe trop court, recommencez ! \n")
            register()

    cpassword = input("Confirmez : ")

    if password != cpassword: 
        print("\nCe ne sont pas les mêmes mot de passe, recommencez ! \n")
        register()

    else: 
        if username == password: 
            print("\n Utilisez un mot de passe autre que votre pseudo... Recommencez !\n")
            register()
        
        else: 
            db = open("db.txt", "a")    #"a", append (chmod -a)
            db.write(username+", "+password+"\n")
            print("\nVotre compte créé avec succès ! !\n")
            print("Votre pseudo est : ",username)
            print("Votre mot de passe est :",password)
            # login()
