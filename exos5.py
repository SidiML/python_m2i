age = int(input("Entrez votre âge: "))
salaire = int(input("Entrez votre pretention salariale: "))
nbre_annee_exp = int(input("Entrez le nombre d'années d'experiences professionnels: "))

if age >=30:
    if salaire <= 40000:
        if nbre_annee_exp >=5:
            print("Votre profil est valable")
        else:
            print("le nombre d'année d'experience est insuffisant")
    else:
        print("le salaire demandé est élevé")
else:
    print("Vous n'avez pas l'age requis pour le poste")

