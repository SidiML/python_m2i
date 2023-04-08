age = int(input("Entrez votre âge: "))
salaire = int(input("Entrez votre pretention salariale: "))
nbre_annee_exp = int(input("Entrez le nombre d'années d'experiences professionnels: "))

if age >=30 and salaire <= 40000 and nbre_annee_exp >=5:

    print("Votre profil est valable")
elif age >=30 and salaire <= 40000:
    print("le nombre d'année d'experience est insuffisant")
elif salaire <= 40000 and nbre_annee_exp >=5:
    print("Vous n'avez pas l'age requis pour le poste")
else :
    print("le salaire demandé est élevé")



