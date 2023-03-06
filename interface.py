def print_logo():
  print("""
 #####     ######  ######     ###    ######    ######   ######  ##   ##   ######  ##   ##   ######           #####     ######            ##        ###             ##   ##    ###    ######   ##   ##   ######  
##  ##    ##      ##   ##   ## ##   ##   ##   # ## #   ##      ### ###   ##      ###  ##   # ## #           ##  ##    ##                ##       ## ##            ### ###   ## ##   ##   ##  ###  ##   ##      
##   ##   ##      ##   ##  ##   ##  ##   ##     ##     ##      #######   ##      #### ##     ##             ##   ##   ##                ##      ##   ##           #######  ##   ##  ##   ##  #### ##   ##      
##   ##   #####   ##   ##  ##   ##  ##  ###     ##     #####   #######   #####   #######     ##             ##   ##   #####             ##      ##   ##           #######  ##   ##  ##  ###  #######   #####   
##   ##   ##      ######   #######  #####       ##     ##      ## # ##   ##      ## ####     ##             ##   ##   ##                ##      #######           ## # ##  #######  #####    ## ####   ##      
##  ##    ##      ##       ##   ##  ## ###      ##     ##      ##   ##   ##      ##  ###     ##             ##  ##    ##                ##   #  ##   ##           ##   ##  ##   ##  ## ###   ##  ###   ##      
#####     ######  ##       ##   ##  ##  ###     ##     ######  ##   ##   ######  ##   ##     ##             #####     ######            ######  ##   ##           ##   ##  ##   ##  ##  ###  ##   ##   ######  
                                                                                                                                                                                                               
                                                        
                                                         """)

def option_1():
  print("Vous avez choisi l'option 1")
  print("Exécution du script associé à l'option 1...")
  exec(open("nouveau55.py").read())

def option_2():
  print("Vous avez choisi l'option 2")
  print("Exécution du script associé à l'option 2...")
  exec(open("script2.py").read())

# Affichage du logo ASCII
print_logo()

# Demande à l'utilisateur de choisir entre les options
choice = input("Choisissez entre les options 1 et 2 : ")

# Exécution du script associé au choix de l'utilisateur
if choice == "1":
  option_1()
elif choice == "2":
  option_2()
else:
  print("Option non valide. Veuillez choisir entre les options 1 et 2.")
