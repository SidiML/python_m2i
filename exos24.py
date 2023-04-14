# initialisation de la liste des adresses
adresses = []

# boucle principale du programme
while True:
    # affichage du menu
    print("1 - Ajouter une adresse")
    print("2 - Editer une adresse")
    print("3 - Supprimer une adresse")
    print("4 - Visualiser les adresses")
    print("5 - Quitter")

    # saisie de l'option choisie par l'utilisateur
    choix = input("Entrez votre choix (1-5) : ")

    # traitement de l'option choisie
    if choix == "1":
        
        print("=== AJOUTER UNE ADRESSE ===")
        adresse = {}
        adresse["numero"] = input("Entrez le numéro de voie : ")
        adresse["complement"] = input("Entrez le complément : ")
        adresse["voie"] = input("Entrez l'intitulé de voie : ")
        adresse["commune"] = input("Entrez la commune : ")
        adresse["code_postal"] = input("Entrez le code postal : ")
        adresses.append(adresse)
        print("Adresse ajoutée avec succès !")
    elif choix == "2":
        
        if len(adresses) == 0:
            print("Aucune adresse à éditer.")
        else:
            index = int(input("Entrez l'indice de l'adresse à éditer (1-{}) : ".format(len(adresses))))
            if index < 1 or index > len(adresses):
                print("Indice invalide.")
            else:
                adresse = adresses[index-1]
                adresse["numero"] = input("Entrez le nouveau numéro de voie ({}): ".format(adresse["numero"]))
                adresse["complement"] = input("Entrez le nouveau complément ({}): ".format(adresse["complement"]))
                adresse["voie"] = input("Entrez le nouvel intitulé de voie ({}): ".format(adresse["voie"]))
                adresse["commune"] = input("Entrez la nouvelle commune ({}): ".format(adresse["commune"]))
                adresse["code_postal"] = input("Entrez le nouveau code postal ({}): ".format(adresse["code_postal"]))
                print("Adresse éditée avec succès !")
    elif choix == "3":
        # suppression d'une adresse
        if len(adresses) == 0:
            print("Aucune adresse à supprimer.")
        else:
            index = int(input("Entrez l'indice de l'adresse à supprimer (1-{}) : ".format(len(adresses))))
            if index < 1 or index > len(adresses):
                print("Indice invalide.")
            else:
                adresses.pop(index-1)
                print("Adresse supprimée avec succès !")
    elif choix == "4":
        # visualisation des adresses
        if len(adresses) == 0:
            print("Aucune adresse à afficher.")
        else:
            print("=== Liste des adresses ===")
            for i, adresse in enumerate(adresses):
                print("Adresse n°{} :".format(i+1))
                print("Numéro de voie : {}".format(adresse["numero"]))
                print("Complément : {}".format(adresse["complement"]))
                print("Intitulé de voie : {}".format(adresse["voie"]))
                print("Commune : {}".format(adresse["commune"]))
                print("code_postal : {}".format(adresse["code_postal"]))
    else:
       exit()