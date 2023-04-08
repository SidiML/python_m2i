def candidature_valable(age, salaire, experience):
    if age < 30:
        print("L'âge minimum pour le poste est 30 ans.")
        return False
    if salaire > 40000:
        print("Le salaire maximum possible est 40 000 euros.")
        return False
    if experience < 5:
        print("Le nombre d'années d'expérience minimum est de 5 ans.")
        return False
    return True

# Exemple d'utilisation
age = 35
salaire = 40000
experience = 5 

if candidature_valable(age, salaire, experience):
    print("Candidature valable.")
else:
    print("Candidature non valable.")