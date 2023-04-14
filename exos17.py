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
print('Faites votre choix :')
print()
print("1 - Afficher note maximale")
print("2 - Afficher note minimale")
print("3 - Afficher moyenne")
print("4 - Quitter programme")
print()
choix1=int(input("Votre choix: "))
if choix1 == 1:
    print(f"Note max : {max(notes)}")
elif choix1 == 2:
    print(f"Note min : {min(notes)}")
elif choix1 == 3:
    print(f"Moyenne : {sum(notes)/len(notes)}")
else:
    exit()