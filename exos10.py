pop_initiale=int(input("Saisir la population actuelle: "))
taux_accroisements =float(input("saisir le taux accroisements: "))
pop_ciblee=int(input("la population visée est : "))

nbres_annee = 0
while pop_initiale < pop_ciblee:
    nbres_annee+=1
    pop_initiale = pop_initiale * (1 + (taux_accroisements/100))
    
print("La population visée sera atteinte en {} années pour une population de {} habitants".format(nbres_annee,round(pop_initiale),2))