# import math

# # Epaisseur de la feuille de départ
# epaisseur_depart = 0.1 # en mm

# # Calcul du nombre de pliages nécessaires pour dépasser 400m
# epaisseur_max = 400000 # en mm
# nb_pliages = math.ceil(math.log2(epaisseur_max/epaisseur_depart))

# print("Il faut plier la feuille environ", nb_pliages, "fois pour que l'épaisseur dépasse 400m.")

# Calcul du nombre de dépliages nécessaires pour atteindre 0.1mm d'épaisseur
# epaisseur_min = 0.1 # en mm
# nb_depliages = math.ceil(math.log2(1000))

# print("Il faut déplier une feuille de 400m environ", nb_depliages, "fois pour que l'épaisseur dépasse 0.1mm.")

import math

# Épaisseur initiale de la feuille de papier en mètres
epaisseur_initiale = 0.0001

# Épaisseur souhaitée de la feuille pliée en mètres
epaisseur_pliee = 400

# Calcul du nombre minimum de pliages pour atteindre l'épaisseur souhaitée
nb_pliages = math.ceil(math.log2(epaisseur_pliee / epaisseur_initiale + 1))

print("Il faut plier la feuille environ", nb_pliages, "fois pour atteindre une épaisseur de 400 m.")

# Calcul du nombre minimum de dépliages pour atteindre l'épaisseur souhaitée
epaisseur_depliee = 0.1 / 1000  # Épaisseur souhaitée de la feuille dépliée en mètres
nb_depliages = math.ceil(epaisseur_pliee / epaisseur_depliee)

print("Il faut déplier une feuille de 400 m environ", nb_depliages, "fois pour atteindre une épaisseur de 0.1 mm.")