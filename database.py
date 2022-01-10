import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("/home/pi/Documents/Projet/projetsportrasp-firebase-adminsdk-a3vjq-bfcbc748ac.json")
default_app = firebase_admin.initialize_app(cred, {
	'databaseURL':"https://projetsportrasp-default-rtdb.europe-west1.firebasedatabase.app/"
	})
ref = db.reference("/")

# Fonction pour récupérer les programmes sur la base de données
def getProgrammes():
    programmes = db.reference("/Programmes").get()
    return programmes

# Fonction pour récupérer les statistiques sur la base de données
def getStats():
    stats = db.reference("/Stats").get()
    return stats

# Fonction pour mettre a jour les statistiques sur la base de données
def updateStat(nom,nombre):
    ref = db.reference("/Stats")
    stats = ref.get()
    for i in range(len(stats)):
        if(stats[i]["nom"] == nom):
            nombreUpdate = int(stats[i]["nombre"]) + int(nombre)
            ref.child(str(i)).update({"nombre" : nombreUpdate})


