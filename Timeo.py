############################################
###### I M P O R T   M O D U L E 
############################################
import time
import string

############################################
###### V A R I A B L E S
############################################
startTime = time.time() # Pour calculer le temps d'execution

## Creation de la liste des caractères à utiliser (ascii_letters : toutes les lettres en majuscule et minuscule / digits : tous les chiffres / punctuation : tous les caractères de ponctuation)
#liste = string.ascii_letters
liste = string.ascii_lowercase
#liste += string.digits
#liste += string.punctuation

# Le mot a chercher :
secret = "timeo"

# Définition d'une limite du nombre de caractères a chercher. si maxCharacter = 5 le mot a chercher ne doit pas dépasser 5 caractères
maxCharacter=5

counter = 0 # Définition d'un compteur
mylistInit = [] # Définition d'une premiere liste

############################################
###### F U N C T I O N S
############################################
def Aggregate(mylistInit):
    mylistNext = []
    for item in mylistInit:
        for char in liste:
            tmp = item + char
            mylistNext.append(tmp)
    return(mylistNext)

def testsecret(mylist):
    flag = False
    for item in mylist:
        print ("Test de : " + str (item))
        if item == secret:
            print ("Found it ! => " + item)
            flag = True
            break
    return(flag)

############################################
###### M A I N 
############################################

while counter < maxCharacter:
    counter = counter + 1
    if counter == 1:
        for mychar in liste:
            mylistInit.append(mychar)
        result = testsecret(mylistInit)
        if result is True:
            break
    else:
        mylistNext = Aggregate(mylistInit)
        mylistInit = []
        for item in mylistNext:
            mylistInit.append(item)

        result = testsecret(mylistInit)
        if result is True:
            break

# Calculate elapsed time and display final status
elapsedTime = time.time() - startTime
elapsedTime = time.strftime("%H:%M:%S", time.gmtime(elapsedTime))
if result is True:
    print ("Found in : " + elapsedTime)
else: 
    print ("NOT Found in : " + elapsedTime)