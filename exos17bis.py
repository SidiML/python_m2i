notes = []
choix = input("Voulez-vous saisir le nombre de notes à entrer (O/N) ? ")
if choix == "O":
    n = int(input("Combien de notes voulez-vous entrer ? "))
    for i in range(n):
        note = float(input(f"Entrez la note {i+1} : "))
        notes.append(note)
else:
    note = float(input("Entrez une note (entrez une note négative pour arrêter) : "))
    while note >= 0:
        notes.append(note)
        note = float(input("Entrez une note (entrez une note négative pour arrêter) : "))


def menu():
    while True:
        print("Faites votre choix :")
        print("  1 - Afficher la note maximale")
        print("  2 - Afficher la note minimale")
        print("  3 - Afficher la moyenne")
        print("  4 -Quitter programme")
        choix = input("Votre choix : ")

        match choix:
            case "1":
                # comportement si choix 1
                print(f"Note maxixmale : {max(notes)}")
            case "2":
                # comportement si choix 2
                print(f"Note mininmale : {min(notes)}") 
            case "3":
                # comportement si choix 3
                print(f"Moyenne : {sum(notes)/len(notes)}") 
            case "4":
                return #on sort de la fonction (possible de faire exit() pour quitter directement le programme)
            case _:
                print("Erreur de saisie ! Réessayez.")
menu()