import math as mt

rayon = int(input('Saisir un rayon r: '))
hauteur = int(input('Saisir hauteur h: '))
rayon = pow (rayon, 2)
V =  round((mt.pi*rayon*hauteur)/3,2)
print ("Le volume du cone est", V)

