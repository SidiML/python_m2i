def count_notes():
    print('Faites votre choix :') 
    print("----------------------") 
    print("1 - Afficher la note maximale") 
    print("2 - Afficher la note minimale") 
    print("3 - Afficher la moyenne") 
    print("4 - Quitter programme") 
    print("-----------------------") 
    choix1 = int(input("Votre choix: ")) 
    if choix1 == 1:
        print(f"Note maxixmale : {max(notes)}")
    elif choix1 == 2:
        print(f"Note mininmale : {min(notes)}") 
    elif choix1 == 3: 
        print(f"Moyenne : {sum(notes)/len(notes)}") 
    else: exit() 
    
notes = [] 
saisie_notes = int( input("Veuillez indiquer le nombre de notes à saisir sinon taper 0: "))
if saisie_notes > 0: # 
    n = int(input("Combien de notes voulez-vous entrer ? ")) 
    for i in range(saisie_notes): 
        note = int(input(f"Entrez la note {i+1} : ")) 
        notes.append(note) 
        count_notes() 
else: saisie_notes == 0 
note = int( input("Entrez une note (entrez une note négative pour arrêter) : ")) 
while note >= 0: 
    notes.append(note) 
    note = int( input("Entrez une note (entrez une note négative pour arrêter) : ")) 
    if note < 0:
        exit 
count_notes()