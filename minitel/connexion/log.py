import subprocess
import os 
import crypt 
import time

etc_passwd = []
names = []
user = os.environ.get('USER')
path = os.getcwd()
username = ""
tmp = []
sudo = None
# Doit s'exécuter qu'au premier démarrage


def previous_option(option):

    top = "+"
    midlle = "|   "
    bottom = "+"
    previous_option = "option précédente : "
    spaces = 0
    letters = 16
    char = 28

    for i in range(len(option.strip())): 
        if option[i] == " ": 
            spaces += 1
        else: 
            letters += 1 
        char += 1
    
    for j in range(char-2): 
        top += "-"
        bottom += "-"
    
    for f in range(len(previous_option)):
        midlle += previous_option[f]

    for u in range(len(option.strip())):
        midlle += option[u]

    top += "+"
    bottom += "+"
    midlle += "   |"
    ascii = """
%s
%s
%s
""" % (top,midlle, bottom)
    print(ascii)

def pull_etc_passwd(list): 
    with open ("/etc/passwd", "r") as myfile: 
        for line in myfile: 
            list.append(line.strip().split(":"))
    return list

def add_names(list1, list2): 
    for i in list1:
        list2.append(i[0]) 

def clear_list(l1, l2):
    l1.clear()
    l2.clear()
    add_names(pull_etc_passwd(l1), l2)

def check_name(name, list): 
    username = name.strip()
    if username in list : 
        return True 
    else: 
        return False    
    
def make_clean(): 
    time.sleep(0.001)
    os.system("cd ../../;make clean;clear ")
    time.sleep(0.001)
    os.system("cd minitel/connexion;clear")
    time.sleep(0.001)
    os.system("python3 log.py")

def install(): 
    sudo = convert_sudo(pull_sudo())
    nettools = "apt install net-tools" 
    cmd1 = "echo " + sudo + "| sudo -S " + nettools
    if (os.system(cmd1)) != 0:
        make_clean()

def start(name): 
    username = name.strip()
    cmd = "cd "+ path + ";" + "cd ../..;make install;cd minitel;python3 main.py" 
   
    try: 
        subprocess.check_call(['su','-',username,'-c',cmd])
    except subprocess.CalledProcessError: 
        bool = True
        while bool: 
            os.system('clear')
            question = input("""
\nMot de passe incorrect! Veuillez recommencer.\n
    [1] : recommencer 
    [2] : changer d'utilisateur  
    [3] : quitter

        |
        +-> """).strip()
            if question == "1": 
                bool = False
                os.system('clear')
                previous_option("se reconnecter à la machine")
                start(name)
            elif question == "2": 
                bool = False 
                os.system('clear')
                previous_option("changer d'uilisateur")
                login()
            elif question == "3": 
                os.system('clear')
                bool = False

def pull_sudo():
    list = []
    with open("sudo.txt", "r") as myfile:
        line = myfile.read()
        list.append(line)
    return list

def convert_sudo(list): 
    str = ""
    str = str + ''.join(list)
    return str

def add_sudo(): 
    for i in range(1):
        try:   
            if (os.system("cat sudo.txt") != 1): 
                append = open("sudo.txt", "a")
                os.system('clear')
                print("\nPour le premier démarrage de votre machine veillez à bien noter le mot de passe sudo. Tout retour en arrière devra se faire depuis l'écran de connexion. Merci de votre compréhension.\n")
                root = input("Tappez votre mot de passe sudo : ").strip()
                append.write((root))
                append.close()
                os.system("chmod -w sudo.txt")
                # os.system("clear")
            else: 
                os.system('clear')
                
                main()
                # print("Le fichier a déjà été modifié")
        except OSError: 
            return 
            # os.system('clear')
            main()

def register(user, sudo):
    print("""
                                                  $$\            $$\                                                           $$\     
                                                  \__|           $$ |                                                          $$ |    
 $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  $$\  $$$$$$$\$$$$$$\    $$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$$$$$$\$$$$$$\   
$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$ |$$  _____\_$$  _|  $$  __$$\ $$  __$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\_$$  _|  
$$$$$$$$ |$$ |  $$ |$$ |  \__|$$$$$$$$ |$$ /  $$ |$$ |\$$$$$$\   $$ |    $$ |  \__|$$$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |$$ |  $$ |$$ |    
$$   ____|$$ |  $$ |$$ |      $$   ____|$$ |  $$ |$$ | \____$$\  $$ |$$\ $$ |      $$   ____|$$ | $$ | $$ |$$   ____|$$ |  $$ |$$ |$$\ 
\$$$$$$$\ $$ |  $$ |$$ |      \$$$$$$$\ \$$$$$$$ |$$ |$$$$$$$  | \$$$$  |$$ |      \$$$$$$$\ $$ | $$ | $$ |\$$$$$$$\ $$ |  $$ |\$$$$  |
 \_______|\__|  \__|\__|       \_______| \____$$ |\__|\_______/   \____/ \__|       \_______|\__| \__| \__| \_______|\__|  \__| \____/ 
                                        $$\   $$ |                                                                                     
                                        \$$$$$$  |                                                                                     
                                         \______/  

""")
    pull_sudo()
    username = user.strip() 
    password = ""
    useradd = "useradd -m -s /bin/bash %s -p $(openssl passwd -1 %s)" % (username,password)
    cmd1 = "echo " + sudo + "| sudo -S " + useradd

    try: 
            if os.system(cmd1) != 0 : 
                os.system('clear')
                bool = True
                time = 0
                
                while bool: 
                    os.system('clear')
                    question = input("""
Les mots de passe saisies ne sont pas identiques.

    [1] : rééssayer 
    [2] : retourner à l'écran de connexion
    [3] : quitter 

        |
        +-> """).strip()
                    if question == "1": 
                        os.system('clear')
                        bool = False 
                        previous_option("rééssayer")
                        register(user,sudo)
                    elif question == "2": 
                        os.system('clear')
                        previous_option("connexion")
                        bool = False 
                        return login()
                    elif question == "3" :
                        bool = False 
                        os.system('clear')
                    elif time == 3: 
                        os.system('clear')
                        print("\nVous avez automatiquement redirigé vers l'ecran de connexion\n")
                    else: 
                        time += 1
            else :
                os.system('clear')
                print("\nL'utilisateur " + username +  " est créé\n")
                login() 
                pass

    except:
        if os.system(cmd1) == 0: 
            os.system('clear')
            print("""
Vous allez être redirigé vers l'écran de connexion. 
        
""")
            clear_list(etc_passwd, names)
            login()

        if os.system(cmd1) != 0 : 
            os.system('clear')
            register(user,sudo)
            os.system('clear')
                       
def login(): 
    print("""
                                                           $$\                     
                                                           \__|                    
 $$$$$$$\  $$$$$$\  $$$$$$$\  $$$$$$$\   $$$$$$\ $$\   $$\ $$\  $$$$$$\  $$$$$$$\  
$$  _____|$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\\$$\ $$  |$$ |$$  __$$\ $$  __$$\ 
$$ /      $$ /  $$ |$$ |  $$ |$$ |  $$ |$$$$$$$$ |\$$$$  / $$ |$$ /  $$ |$$ |  $$ |
$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$  $$<  $$ |$$ |  $$ |$$ |  $$ |
\$$$$$$$\ \$$$$$$  |$$ |  $$ |$$ |  $$ |\$$$$$$$\$$  /\$$\ $$ |\$$$$$$  |$$ |  $$ |
 \_______| \______/ \__|  \__|\__|  \__| \_______\__/  \__|\__| \______/ \__|  \__|
                                                                                   


Saisissez le nom de votre compte. Pour rappel un nom d'utilisateur ne doit pas comprendre d'espace. Si c'est votre première connexion mettez tout de même le nom que vous voulez. Il vous sera proposé de le réutiliser pour procéder à la création de votre compte.

    """)
    add_names(pull_etc_passwd(etc_passwd), names)
    name = input("User : ")
    username = name.strip()
    bool = True 
    while bool : 
        os.system('clear')
        if check_name(username, names) == False:  
            bool = False 
            question = input("""
Cette utilisateur n'est pas reconnu. Voulez - vous, vous reconnecter ou créer un nouveau compte à partir du nom saisi ?

    entrée  : se reconnecter 
    [2]     : créer un compte  
    [3]     : quitter   
    [4]     : changer le mot de passe sudo
    
        |
        +-> """).strip()
            if question == "1":
                bool = False 
                os.system('clear')
                previous_option('reconnecter')
                login()

            elif question == "2": 
                bool = False
                os.system('clear')
                previous_option('créer un compte')
                sudo = convert_sudo(pull_sudo())
                register(username, sudo) 

            elif question == "3": 
                bool = False
            elif question == "4": 
                bool = False 
                os.system('clear')
                make_clean()
            else: 
                os.system('clear')
                login()
        else: 
            if username == user: 
                confirmation = input("""
Cette utilisateur est déjà connecté à la session. Voulez-vous poursuivre ? 

    [1]     : oui 
    entrée  : non 
    [3]     : quitter 

        |
        +-> """).strip()
                if confirmation == "1":
                    bool = False
                    start(username)

                elif confirmation == "3": 
                    bool = False
                else: 
                    bool = False 
                    os.system('clear')
                    previous_option("changer d'utilisateur")
                    login() 

            else: 
                bool = False
                os.system('clear')
                previous_option("connexion")
                start(username)

def bienvenue():
    bool = True
    while bool: 
        os.system('clear')
        question = input("""
$$\      $$\ $$\           $$\  $$\              $$\             $$$$$$\       $$\   
$$$\    $$$ |\__|          \__| $$ |             $$ |           $$ ___$$\    $$$$ |  
$$$$\  $$$$ |$$\ $$$$$$$\  $$\$$$$$$\   $$$$$$\  $$ |           \_/   $$ |   \_$$ |  
$$\$$\$$ $$ |$$ |$$  __$$\ $$ \_$$  _| $$  __$$\ $$ |             $$$$$ /      $$ |  
$$ \$$$  $$ |$$ |$$ |  $$ |$$ | $$ |   $$$$$$$$ |$$ |             \___$$\      $$ |  
$$ |\$  /$$ |$$ |$$ |  $$ |$$ | $$ |$$\$$   ____|$$ |           $$\   $$ |     $$ |  
$$ | \_/ $$ |$$ |$$ |  $$ |$$ | \$$$$  \$$$$$$$\ $$ |           \$$$$$$  |$$\$$$$$$\ 
\__|     \__|\__|\__|  \__|\__|  \____/ \_______|\__|            \______/ \__\______|


Bienvenue dans le minitel 3.1. Tappez sur la touche entrée pour continuer ou tappez "quit" sur votre clavier pour quitter.
""").strip()
        if question == "":
            main() 
        if question == "quit":
            bool = False 
            os.system('clear')
            
def main(): 
    os.system('clear')
    for i in range(1):
        add_sudo() 
    os.system('clear')
    try : 
        install()
    except: 
        print("Net tools non installé !")
    os.system('clear')
    login()

bienvenue()

# install()

""" Debug

Pour se connecter directement à un nom. 
    start('nom')

Pour ajouter les noms du fichier /etc/passwd
    add_names(pull_etc_passwd(etc_passwd), names)

Pour voir les données du fichier /etc/passwd
    pull_etc_passwd(etc_passwd)

Pour vérifier si un nom fait partie de la liste
    print(check_name('nom', names))

Pour vérifier l'enregistrement d'un utilisateur
    register('name')

 """





