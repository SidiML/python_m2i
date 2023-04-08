prenom, nom = [x for x in input("Entrer votre prenom et nom: ").split(",",2)]
print("Bonjour M. ou Mme {} {}".format(prenom, nom.upper()))