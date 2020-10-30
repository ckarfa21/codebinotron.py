#import de fonction
import mysql.connector
import random
#connexion au serveur sql
config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'port':'8082',
  'database': 'binomotron',
  'raise_on_warnings': True,
}

connection = mysql.connector.connect(**config)
cursor=connection.cursor()
#recuperation de la liste apprenant à partir de la base de donnees 
cursor.execute("""select * from apprenant""")
#creation d'un tableau avec la liste des apprenants
liste_apprenant=cursor.fetchall()

numero_equipe=1 
#melange de la liste des apprenants
random.shuffle(liste_apprenant)
#donne le choix du nom de projet a l'utilisateur
nom_projet=input("quel est le nom du projet ?")
#affichage des equipes et des binômes
for i in range(0,20,2):
    print("equipe",numero_equipe)
    print(liste_apprenant[i:i+2])
    sql_groupe=("INSERT INTO groupe(libelle) VALUES (%s)")

    var_groupe=("equipe"+str(numero_equipe))
    cursor.execute(sql_groupe,(var_groupe,))
    numero_equipe+=1

#insertion des donnees dans les tables

sql=("INSERT INTO projet(libelle) VALUES (%s)")

var=(nom_projet)

cursor.execute(sql,(var,))

connection.commit()
#fin du programme
connection.close()





    

    



