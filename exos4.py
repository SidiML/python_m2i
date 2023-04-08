temp = float(input("Saisir une temperature en (d°): "))
if temp<0:
    print("l'etat de l'eau est: SOLIDE")
elif temp <=100:
    print("l'etat de l'eau est: LIQUIDE")
else:
    print("l'etat de l'eau est GAZEUX")
