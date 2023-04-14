# Définition des clés pour le dictionnaire
NUMERO_VOIE = 'numero_voie'
COMPLEMENT = 'complement'
INTITULE_VOIE = 'intitule_voie'
COMMUNE = 'commune'
CODE_POSTAL = 'code_postal'

# Initialisation de la liste d'adresses
adresses = []

# Fonction pour ajouter une adresse
def ajouter_adresse():
    # Saisie des informations de l'adresse
    numero_voie = input("Numéro de voie : ")
    complement = input("Complément : ")
    intitule_voie = input("Intitulé de voie : ")
    commune = input("Commune : ")
    code_postal = input("Code postal : ")
    # Création du dictionnaire pour l'adresse
    adresse = {
        NUMERO_VOIE: numero_voie,
        COMPLEMENT: complement,
        INTITULE_VOIE: intitule_voie,
        COMMUNE: commune,
        CODE_POSTAL: code_postal
    }
    # Ajout de l'adresse à la liste
    adresses.append(adresse)
    print("Adresse ajoutée.")

# Fonction pour éditer une adresse
def editer_adresse():
    # Affichage des adresses existantes
    for i, adresse in enumerate(adresses):
        print(f"{i+1}. {adresse[NUMERO_VOIE]} {adresse[INTITULE_VOIE]}, {adresse[CODE_POSTAL]} {adresse[COMMUNE]}")
    # Saisie de l'adresse à éditer
    choix = int(input("Choisissez l'adresse à éditer : "))
    adresse = adresses[choix-1]
    # Modification des informations de l'adresse
    adresse[NUMERO_VOIE] = input(f"Nouveau numéro de voie ({adresse[NUMERO_VOIE]}) : ")
    adresse[COMPLEMENT] = input(f"Nouveau complément ({adresse[COMPLEMENT]}) : ")
    adresse[INTITULE_VOIE] = input(f"Nouvel intitulé de voie ({adresse[INTITULE_VOIE]}) : ")
    adresse[COMMUNE] = input(f"Nouvelle commune ({adresse[COMMUNE]}) : ")
    adresse[CODE_POSTAL] = input(f"Nouveau code postal ({adresse[CODE_POSTAL]}) : ")
    print("Adresse modifiée.")

# Fonction pour supprimer une adresse
def supprimer_adresse():
    # Affichage des adresses existantes
    for i, adresse in enumerate(adresses):
        print(f"{i+1}. {adresse[NUMERO_VOIE]} {adresse[INTITULE_VOIE]}, {adresse[CODE_POSTAL]} {adresse[COMMUNE]}")
    # Saisie de l'adresse à supprimer
    choix = int(input("Choisissez l'adresse à supprimer : "))
    # Suppression de l'adresse de la liste
    del adresses[choix-1]
    print("Adresse supprimée.")

# Fonction pour afficher toutes les adresses
def afficher_adresses():
    # Affichage de toutes les adresses existantes
    for adresse in adresses:
        print(f"{adresse[NUMERO_VOIE]} {adresse[INTITULE_VOIE]}, {
