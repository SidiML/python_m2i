def menu():
    myliste_set={"Balamou","Mane"}
    
    while True:
        print("=== MENU PRINCIPAL ===")
        print("1. Voir les noms de famille")
        print("2. Ajouter un nom de famille")
        print("3. Editer un nom de famille")
        print("4. Supprimer un nom de famille")
        print("0. Quitter programme")
        
        choix = input("Votre choix : ")
        print() 
        
        match choix:
            case "1":
                print("=== LISTE NOM DE FAMILLE ===")
                
                print(myliste_set)
                print()
            case "2":   
                nom = input("Saisir un nom: ")  
                myliste_set.add(nom)           
                
            case "3":
                nom1=input("Saisir un nom: ") 
                if nom1 in myliste_set:
                           
                    print(nom1) 
                    # nom1=input("Saisir un nom: ")
                else:
                    print("Nom non trouvé...") 
  
            case "4":
                nom2=input("Saisir un nom: ")   
                myliste_set.remove(nom2)
                
            case "0":
                exit()
menu()