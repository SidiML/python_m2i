def menu():
    mylist = [
     {
    "numero de voie": 15,
    "complement": "appt 22",
    "intitulé de voie": "Square Vaugirad",
    "commune": "Paris",
    "code postal": 75000}
    ]
       
    while True:
        print("=== MENU PRINCIPAL ===")
        print("1. Voir les adresses")
        print("2. Ajouter une adresse")
        print("3. Editer une adresse")
        print("4. Supprimer une adresse")
        print("0. Quitter programme")
        print("-"*80)
        choix = input("Votre choix : ")
        print("-"*80)
        
        match choix:
            case "1":
                print("=== LISTE DES ADRESSES ===")
                print(mylist)
                print("-"*80)
            case "2": 
                print("=== AJOUTER UNE ADRESSE ===")  
                print()
                nom_addres=input("Veuillez un nom d'adresse SVP : ")
                nom_addres["numero de voie"]= input("Veuillez entrer le numero de voie SVP :  ")  
                nom_addres["complement"] = input("Veuillez entrer le complement d'adresse SVP :  ")  
                nom_addres["intitulé de voie"] = input("Veuillez entrer l'intitulé de voie SVP :  ")  
                nom_addres["commune"] = input("Veuillez entrer la commune SVP :  ")  
                nom_addres["code postal"]= input("Veuillez entrer le numero de code postal SVP :  ")  
                          
                
            case "3":
                nom1=input("Numero d'adresse à editer: ") 
                if nom1 in myliste_set:
                           
                    print(nom1) 
                    # nom1=input("Saisir un nom: ")
                else:
                    print("Nom non trouvé...") 
  
            case "4":
                nom2=input("Saisir un nom: ")   
                myliste_set.remove(nom2)
                
            case "0":
                return
menu()