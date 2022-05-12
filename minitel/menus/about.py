import platform
import os  
import psutil
from termcolor import colored 
import subprocess   
import time




from datetime import datetime

user = os.environ.get('USER')

nom = colored(user,'green') 
debian = colored("@minitel",'green')

a = ':'
b = colored('~', 'blue')
c = '$ '


def menu_dialogue(): 
    os.system('clear')
    bool = True 
    print_dialogue()

    while bool == True : 
        
        question = input((nom+debian+a+b+c)).strip()

        if question == "quit": 
            bool = False 
            clear()
        
        elif question == "help": 
            clear()
            print_dialogue()

        elif question == "os":
            clear()
            choix("os")

        elif question == "up": 
            clear()
            choix("up")

        elif question == "uname": 
            clear()
            choix("uname")

        elif question == "hardwares": 
            clear()
            choix("hardwares")
        
        elif question == "ip": 
            clear()
            choix("ip")
        
        elif question == "running": 
            clear()
            choix("running")
        
        elif question == "allpid": 
            clear()
            choix("allpid")

        elif question == "pid": 
            clear()
            choix("pid")

        elif question == "name": 
            clear()
            print("\n\nVotre nom est : ",user,"\n\n\n")
        
        elif question == "run":
            clear()
            choix("run")

        elif question == "kill":
            clear()
            choix("kill")

        elif question == "pstree":
            clear()
            choix("pstree")
        
        elif question == "pssearch":
            clear()
            choix("pssearch")
        
        elif question == "nroutes":
            clear()
            choix("nroutes")
        
        elif question == "netstat":
            clear()
            choix("netstat")
        
        elif question == "listroutes":
            clear()
            choix("listroutes")

        else :  
            print('Invalid command, enter "help" to check our pretty man')

"""
Outils 
"""

def clear(): 
    os.system('clear')

"""
Informations générales 
"""
def print_dialogue():

    print(("""\
Man\n
            Navigation : 

help                                Pour afficher le man de navigation 
quit                                Pour se deconnecter de la session

            Informations : 

os                                  Os version
up                                  Pour voir depuis quand le pc est en marche  
uname                               Afficher la version du Kernel 
hardwares                           Afficher les informations hardwares
ip                                  Toutes informations concernant les IPs

            Réseaux : 

ip                                  Toutes informations concernant les IPs
netstat                             Tanble du routage de routage du Kernel
nroutes                             Ip des routes du Kernel
listroutes                          Liste d'itinéraires ip

            Processus : 

running                             Pour afficher les processus en cours 
allpid                              Pour afficher les PID de tous les utilisateurs 
pid                                 Pour afficher les PID de votre session
name                                Pour afficher votre nom
run                                 Pour demarrer un processus 
pstree                              Pour afficher l'arborescence des PID
pssearch                            Pour chercher un PID
        """))

def choix(reponse):

    if reponse == "os" : 
        os_version()
 
    elif reponse == "up":
        uptime()

    elif reponse == "uname": 
        kernel_version()   

    elif reponse == "hardwares":
        hardware()  
    
    elif reponse == "ip":
        ip()

    elif reponse == "running":
        running()

    elif reponse == "allpid":
        allpid()
    
    elif reponse == "pid":
        pid()
    
    elif reponse == "run":
        run()
    
    elif reponse == "pstree":
        pstree()
    
    elif reponse == "pssearch":
        pssearch()
    
    elif reponse == "listroutes":
        listroutes()
    
    elif reponse == "netstat":
        netstat()

    elif reponse == "nroutes":
        nroutes()
    
    elif reponse == "kill":
        sudo = convert_sudo(pull_sudo())
        kill(sudo)

def listroutes(): 
    print("""

$$$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$$\  $$$$$$\        $$\       $$$$$$\  $$$$$$\ $$$$$$$$\  $$$$$$\  
$$  __$$\ $$  __$$\ $$ |  $$ |\__$$  __|$$  _____|$$  __$$\       $$ |      \_$$  _|$$  __$$\\__$$  __|$$  __$$\ 
$$ |  $$ |$$ /  $$ |$$ |  $$ |   $$ |   $$ |      $$ /  \__|      $$ |        $$ |  $$ /  \__|  $$ |   $$ /  \__|
$$$$$$$  |$$ |  $$ |$$ |  $$ |   $$ |   $$$$$\    \$$$$$$\        $$ |        $$ |  \$$$$$$\    $$ |   \$$$$$$\  
$$  __$$< $$ |  $$ |$$ |  $$ |   $$ |   $$  __|    \____$$\       $$ |        $$ |   \____$$\   $$ |    \____$$\ 
$$ |  $$ |$$ |  $$ |$$ |  $$ |   $$ |   $$ |      $$\   $$ |      $$ |        $$ |  $$\   $$ |  $$ |   $$\   $$ |
$$ |  $$ | $$$$$$  |\$$$$$$  |   $$ |   $$$$$$$$\ \$$$$$$  |      $$$$$$$$\ $$$$$$\ \$$$$$$  |  $$ |   \$$$$$$  |
\__|  \__| \______/  \______/    \__|   \________| \______/       \________|\______| \______/   \__|    \______/ 
                                                                                                                 
                                                                                                                 
                                                                                                                                                                                                                                                                                                                                                                                                                                   
""")
    cmd = "ip route list"
    run = os.popen(cmd).read().strip()
    print(run,"\n\n\n") 


def netstat():
    print("""

$$\   $$\ $$$$$$$$\ $$$$$$$$\  $$$$$$\ $$$$$$$$\  $$$$$$\ $$$$$$$$\  $$$$$$\  
$$$\  $$ |$$  _____|\__$$  __|$$  __$$\\__$$  __|$$  __$$\\__$$  __|$$  __$$\ 
$$$$\ $$ |$$ |         $$ |   $$ /  \__|  $$ |   $$ /  $$ |  $$ |   $$ /  \__|
$$ $$\$$ |$$$$$\       $$ |   \$$$$$$\    $$ |   $$$$$$$$ |  $$ |   \$$$$$$\  
$$ \$$$$ |$$  __|      $$ |    \____$$\   $$ |   $$  __$$ |  $$ |    \____$$\ 
$$ |\$$$ |$$ |         $$ |   $$\   $$ |  $$ |   $$ |  $$ |  $$ |   $$\   $$ |
$$ | \$$ |$$$$$$$$\    $$ |   \$$$$$$  |  $$ |   $$ |  $$ |  $$ |   \$$$$$$  |
\__|  \__|\________|   \__|    \______/   \__|   \__|  \__|  \__|    \______/ 
                                                                              
                                                                              
                                                                                                                                                                                                                                                                
""")
    cmd = "netstat -rn"
    run = os.popen(cmd).read().strip()
    print(run,"\n\n\n")

def nroutes():
    print("""

$$\   $$\ $$$$$$$$\ $$$$$$$\  $$\   $$\ $$$$$$$$\ $$\             $$$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$$\  $$$$$$\        
$$ | $$  |$$  _____|$$  __$$\ $$$\  $$ |$$  _____|$$ |            $$  __$$\ $$  __$$\ $$ |  $$ |\__$$  __|$$  _____|$$  __$$\       
$$ |$$  / $$ |      $$ |  $$ |$$$$\ $$ |$$ |      $$ |            $$ |  $$ |$$ /  $$ |$$ |  $$ |   $$ |   $$ |      $$ /  \__|      
$$$$$  /  $$$$$\    $$$$$$$  |$$ $$\$$ |$$$$$\    $$ |            $$$$$$$  |$$ |  $$ |$$ |  $$ |   $$ |   $$$$$\    \$$$$$$\        
$$  $$<   $$  __|   $$  __$$< $$ \$$$$ |$$  __|   $$ |            $$  __$$< $$ |  $$ |$$ |  $$ |   $$ |   $$  __|    \____$$\       
$$ |\$$\  $$ |      $$ |  $$ |$$ |\$$$ |$$ |      $$ |            $$ |  $$ |$$ |  $$ |$$ |  $$ |   $$ |   $$ |      $$\   $$ |      
$$ | \$$\ $$$$$$$$\ $$ |  $$ |$$ | \$$ |$$$$$$$$\ $$$$$$$$\       $$ |  $$ | $$$$$$  |\$$$$$$  |   $$ |   $$$$$$$$\ \$$$$$$  |      
\__|  \__|\________|\__|  \__|\__|  \__|\________|\________|      \__|  \__| \______/  \______/    \__|   \________| \______/       
                                                                                                                                    
                                                                                                                                    
                                                                                                                                                                                                                                                                                                                        
""")
    cmd = "route -n"
    run = os.popen(cmd).read().strip()
    print(run,"\n\n\n")

def ip():
    ip = 'ip link show'
    I = "hostname -I"
    print("""


$$$$$$\ $$$$$$$\        $$$$$$\            $$$$$$\                     
\_$$  _|$$  __$$\       \_$$  _|          $$  __$$\                    
  $$ |  $$ |  $$ |        $$ |  $$$$$$$\  $$ /  \__|$$$$$$\   $$$$$$$\ 
  $$ |  $$$$$$$  |        $$ |  $$  __$$\ $$$$\    $$  __$$\ $$  _____|
  $$ |  $$  ____/         $$ |  $$ |  $$ |$$  _|   $$ /  $$ |\$$$$$$\  
  $$ |  $$ |              $$ |  $$ |  $$ |$$ |     $$ |  $$ | \____$$\ 
$$$$$$\ $$ |            $$$$$$\ $$ |  $$ |$$ |     \$$$$$$  |$$$$$$$  |
\______|\__|            \______|\__|  \__|\__|      \______/ \_______/ 
                                                                       
                                                                       
                                                                                               
""")
    str = ""
    info = os.popen(ip).read().strip()
    print("IP's\n")
    for i in info: 
        str += i 
        
    print(str)

    grand = os.popen(I).read().strip()
    print("\n\n+------------------+")
    print("|   hostname -I    |",)
    print("+------------------+") 
    print("| ",grand," |")
    print("+------------------+\n\n")

    i = "hostname -i"
    petit = os.popen(i).read().strip()
    print("+------------------+")
    print("|   hostname -i    |",)
    print("+------------------+") 
    print("|   ",petit,"    |")
    print("+------------------+")


def run(): 
    print("""

$$$$$$$\  $$\   $$\ $$\   $$\ 
$$  __$$\ $$ |  $$ |$$$\  $$ |
$$ |  $$ |$$ |  $$ |$$$$\ $$ |
$$$$$$$  |$$ |  $$ |$$ $$\$$ |
$$  __$$< $$ |  $$ |$$ \$$$$ |
$$ |  $$ |$$ |  $$ |$$ |\$$$ |
$$ |  $$ |\$$$$$$  |$$ | \$$ |
\__|  \__| \______/ \__|  \__|
                              
                              
                              
    """)
    cmd = input("Processus à lancer : ").strip() 
    cmd += " &"
    if os.system(cmd) != 0: 
        os.system('clear') 
        print('\n\nVeuiller saissir correctement la commande à lancer.\n\n')
        run()
    else:   
        time.sleep(0.05)
        bool = True
        while bool : 
            
            question = input("""

Voulez - vous continuer ? 

    [1] : oui
    [2] : non 

        |
        +-> """)
            if question == "1": 
                bool = False 
                run()
            elif question == "2": 
                bool = False
                menu_dialogue()
            else: 
                os.system('clear')

def pull_sudo():
    list = []
    with open("connexion/sudo.txt", "r") as myfile:
        line = myfile.read()
        list.append(line)
    return list

def convert_sudo(list): 
    str = ""
    str = str + ''.join(list)
    return str

def kill(sudo): 
    print(sudo)
    print("""

$$\   $$\ $$$$$$\ $$\       $$\       
$$ | $$  |\_$$  _|$$ |      $$ |      
$$ |$$  /   $$ |  $$ |      $$ |      
$$$$$  /    $$ |  $$ |      $$ |      
$$  $$<     $$ |  $$ |      $$ |      
$$ |\$$\    $$ |  $$ |      $$ |      
$$ | \$$\ $$$$$$\ $$$$$$$$\ $$$$$$$$\ 
\__|  \__|\______|\________|\________|
                                                                    
                              
                              
    """)

    pid =  input("PID du à stopper : ")
    kill = "echo " + sudo + "| sudo -S kill -9 " + pid
    try : 
        if os.system(kill) != 0: 
            os.system('clear') 
            print('\n\nVeuiller bien saissir le PID à stopper.\n\n')
            kill(sudo)
     
        else:   
            time.sleep(0.05)
            bool = True
            while bool : 
                
                question = input("""

Voulez - vous continuer ? 

    [1] : oui
    [2] : non 

        |
        +-> """)
                if question == "1": 
                    bool = False 
                    kill(sudo)
                elif question == "2": 
                    bool = False
                    menu_dialogue()
                else: 
                    os.system('clear')
    except OSError:
        boool = True
        while boool: 
            question2 = input("""
Une erreur à été rencontré voulez - vous poursuivre ou retourner au menu principal ? 

    [1] : oui
    [2] : non

        |
        +-> """)
            if question2 == "1": 
                bool = False 
                kill()
            elif question2 == "2": 
                bool = False
                menu_dialogue()
            else: 
                os.system('clear')

def pstree():
    print("""

$$$$$$$\   $$$$$$\        $$$$$$$$\ $$$$$$$\  $$$$$$$$\ $$$$$$$$\ 
$$  __$$\ $$  __$$\       \__$$  __|$$  __$$\ $$  _____|$$  _____|
$$ |  $$ |$$ /  \__|         $$ |   $$ |  $$ |$$ |      $$ |      
$$$$$$$  |\$$$$$$\           $$ |   $$$$$$$  |$$$$$\    $$$$$\    
$$  ____/  \____$$\          $$ |   $$  __$$< $$  __|   $$  __|   
$$ |      $$\   $$ |         $$ |   $$ |  $$ |$$ |      $$ |      
$$ |      \$$$$$$  |         $$ |   $$ |  $$ |$$$$$$$$\ $$$$$$$$\ 
\__|       \______/          \__|   \__|  \__|\________|\________|
                                                                  
                                                                  
                                                                                                                                 
""")
    cmd = "pstree -p"
    run = os.popen(cmd).read().strip()
    print(run,"\n\n\n")

def pssearch():
    print("""

$$$$$$$\   $$$$$$\         $$$$$$\  $$$$$$$$\  $$$$$$\  $$$$$$$\   $$$$$$\  $$\   $$\ 
$$  __$$\ $$  __$$\       $$  __$$\ $$  _____|$$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |
$$ |  $$ |$$ /  \__|      $$ /  \__|$$ |      $$ /  $$ |$$ |  $$ |$$ /  \__|$$ |  $$ |
$$$$$$$  |\$$$$$$\        \$$$$$$\  $$$$$\    $$$$$$$$ |$$$$$$$  |$$ |      $$$$$$$$ |
$$  ____/  \____$$\        \____$$\ $$  __|   $$  __$$ |$$  __$$< $$ |      $$  __$$ |
$$ |      $$\   $$ |      $$\   $$ |$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |  $$ |
$$ |      \$$$$$$  |      \$$$$$$  |$$$$$$$$\ $$ |  $$ |$$ |  $$ |\$$$$$$  |$$ |  $$ |
\__|       \______/        \______/ \________|\__|  \__|\__|  \__| \______/ \__|  \__|
                                           


""")
    tree = input("Processus à chercher : ").strip() 
    cmd = "pstree -p | grep '%s'" % (tree)
    if os.system(cmd) != 0: 
        os.system('clear') 
        print('\n\nVeuiller saissir correctement le PID à chercher.\n\n')
        pssearch()
    else:   
        time.sleep(0.05)
        bool = True
        while bool : 
            
            question = input("""

Voulez - vous continuer ? 

    [1] : oui
    [2] : non 

        |   
        +-> """)
            if question == "1": 
                bool = False 
                pssearch()
            elif question == "2": 
                bool = False
                menu_dialogue()
            else: 
                os.system('clear')

def allpid(): 
    print("""

 $$$$$$\  $$\       $$\             $$$$$$$\ $$$$$$\ $$$$$$$\  
$$  __$$\ $$ |      $$ |            $$  __$$\\_$$  _|$$  __$$\ 
$$ /  $$ |$$ |      $$ |            $$ |  $$ | $$ |  $$ |  $$ |
$$$$$$$$ |$$ |      $$ |            $$$$$$$  | $$ |  $$ |  $$ |
$$  __$$ |$$ |      $$ |            $$  ____/  $$ |  $$ |  $$ |
$$ |  $$ |$$ |      $$ |            $$ |       $$ |  $$ |  $$ |
$$ |  $$ |$$$$$$$$\ $$$$$$$$\       $$ |     $$$$$$\ $$$$$$$  |
\__|  \__|\________|\________|      \__|     \______|\_______/ 
                                                               
                                                               
                                                               
""")
    cmd = "ps -faux"
    run = os.popen(cmd).read().strip()
    print(run,"\n\n\n")

def pid(): 
    print("""

$$$$$$$\ $$$$$$\ $$$$$$$\  
$$  __$$\\_$$  _|$$  __$$\ 
$$ |  $$ | $$ |  $$ |  $$ |
$$$$$$$  | $$ |  $$ |  $$ |
$$  ____/  $$ |  $$ |  $$ |
$$ |       $$ |  $$ |  $$ |
$$ |     $$$$$$\ $$$$$$$  |
\__|     \______|\_______/ 
                           
                           
                           
""")
    cmd = "ps -fux"
    run = os.popen(cmd).read().strip()
    print(run,"\n\n\n")

def running(): 
    print("""

$$$$$$$\  $$\   $$\ $$\   $$\ $$\   $$\ $$$$$$\ $$\   $$\  $$$$$$\  
$$  __$$\ $$ |  $$ |$$$\  $$ |$$$\  $$ |\_$$  _|$$$\  $$ |$$  __$$\ 
$$ |  $$ |$$ |  $$ |$$$$\ $$ |$$$$\ $$ |  $$ |  $$$$\ $$ |$$ /  \__|
$$$$$$$  |$$ |  $$ |$$ $$\$$ |$$ $$\$$ |  $$ |  $$ $$\$$ |$$ |$$$$\ 
$$  __$$< $$ |  $$ |$$ \$$$$ |$$ \$$$$ |  $$ |  $$ \$$$$ |$$ |\_$$ |
$$ |  $$ |$$ |  $$ |$$ |\$$$ |$$ |\$$$ |  $$ |  $$ |\$$$ |$$ |  $$ |
$$ |  $$ |\$$$$$$  |$$ | \$$ |$$ | \$$ |$$$$$$\ $$ | \$$ |\$$$$$$  |
\__|  \__| \______/ \__|  \__|\__|  \__|\______|\__|  \__| \______/ 
                                                                    
                                                                    
                                                                        
    """)
    cmd = "ps ux"
    run = os.popen(cmd).read().strip()
    print(run,"\n\n\n")

def os_version(): 
    print(""" 
    ________________________________
    |                               |
    |         Os version :          |     
    |_______________________________|

    """)
    print(" ", platform.system(), platform.release())
    print("")

def uptime(): 
    print(""" 
    ________________________________
    |                               |
    |           Uptime :            |     
    |_______________________________|

    """)
    print(" ", os.popen('uptime -p').read()[:-1])
    print("")

def kernel_version(): 
    print(""" 
    ________________________________
    |                               |
    |       Kernel version :        |     
    |_______________________________|

    """)
    print(" ", platform.release())
    print("")

def hardware(): 
    print ("""
            ____________________________________________________________________________
            |                                                                           |
            |                 _    _               _                                    |
            |                | |  | |             | |                                   | 
            |                | |__| | __ _ _ __ __| |_      ____ _ _ __ ___             |
            |                |  __  |/ _` | '__/ _` \ \ /\ / / _` | '__/ _ \            |
            |                | |  | | (_| | | | (_| |\ V  V / (_| | | |  __/            |
            |                |_|  |_|\__,_|_|  \__,_| \_/\_/ \__,_|_|  \___|            |                                                   
            |                                                                           |
            |                                                                           |
            |___________________________________________________________________________|                                             
    """)
    cpufreq = psutil.cpu_freq()
    print("""
______________________________________________      ______________________________________________
|                                             |     |                                             |
|                  Cores                      |     |                 Frequency                   |
|_____________________________________________|     |_____________________________________________|
|                                             |     |                                             |""")
    print("|","     ","Physical cores:", psutil.cpu_count(logical=False),"                   ","|","    |","     ",f"Max Frequency: {cpufreq.max:.2f}Mhz","              ","|")
    print("|","     ","Non-logical cores", psutil.cpu_count(logical=True)-psutil.cpu_count(logical=False),"                 ","|","    |","     ",f"Min Frequency: {cpufreq.min:.2f}Mhz","              ","|")
    print("|","     ","Total cores:", psutil.cpu_count(logical=True),"                      ","|","    |","     ",f"Current Frequency: {cpufreq.current:.2f}Mhz","       ","|")
    print("""|_____________________________________________|     |_____________________________________________|""")

    print("""
______________________________________________
|                                             |
|                  Frequency                  |
|_____________________________________________|
|                                             |""")
    print("|","     ",f"Min Frequency: {cpufreq.min:.2f}Mhz","              ","|")
    print("|","     ",f"Max Frequency: {cpufreq.max:.2f}Mhz","              ","|")
    print("|","     ",f"Current Frequency: {cpufreq.current:.2f}Mhz","       ","|")
    print("""|_____________________________________________|""")

    print("""
______________________________________________
|                                             |
|               CPU per Core                  |
|_____________________________________________|
|                                             |""")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print("|          ","     ",f"Core {i}: {percentage}%","              ","|")
    print("""|_____________________________________________|""")
    print("""       |                                |""")
    print("    ","  |   ",f"Total CPU Usage: {psutil.cpu_percent()}%","     |   ","")
    print("""       |________________________________|""")

    print("""
______________________________________________
|                                             |
|                     RAM                     |
|_____________________________________________|
|                                             |""")
    
    total_memory, used_memory, free_memory = map(
        int, os.popen('free -t -m').readlines()[-1].split()[1:])
    
 
    print("|","     ","RAM memory % used:", round((used_memory/total_memory) * 100, 2),"             ","|")
    print("""|_____________________________________________|""")
    print("")

"""
Appel de fonctions
"""

def secret(): 
    os.system('python3 ~/.envvar/minitel/main.py')





