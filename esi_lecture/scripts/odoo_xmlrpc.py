import xmlrpc.client
# Demander les informations de connexion
url="http://localhost:8069"
db = "dev01"
boucle=True
use_api_key = input("Voulez-vous utiliser une clé API ? (oui/non) : ").lower() == "oui"
username = ""
password = ""

while boucle:
    if use_api_key:
        username = input("Entrez votre login : ")
        password = input("Entrez votre clé API : ")
    else:
        username = input("Entrez votre login : ")
        password = input("Entrez votre mot de passe : ")
    try:
    # Récupération de la version d’ODOO installée
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    # Connexion de l’utilisateur
        uid = common.authenticate(db, username, password, {})
        if uid is False:
            raise Exception("Authentification échouée. Vérifiez votre login/clé API et mot de passe.")
        else:
            boucle=False
    # Connexion au service d'objets
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    except Exception as e:
        print("Une erreur est survenue :", e)

# Boucle de recherche
while True:
    search_term = input("Entrez le titre du livre à rechercher (ou 'exit' pour quitter) : ")
    if search_term == 'exit':
        break
    # Recherche de livres
    try:
        books = models.execute_kw(db, uid, password,
            'livre.livre', 'search_read',
            [[['name', 'ilike', search_term]]],
            {'fields': ['name', 'description']})
        for book in books:
            print("Titre:", book['name'])
            print("Description:", book['description'])
    except Exception as e:
        print("Erreur:", e)
