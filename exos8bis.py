n = int(input("Saisir la hauteur du triangle: "))

hauteur = n
nbres_etoiles = 1
nbres_espaces = hauteur - 1
for i in range(hauteur):
    print(nbres_espaces* "  " + nbres_etoiles*"* ")
    nbres_etoiles+=2
    nbres_espaces-=1