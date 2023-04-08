temperature = float((input("Veuillez indiquer la temperature en (d°): ")))
if temperature < 0:
    print("L'eau est à l'état solide")

elif temperature >0 and temperature <= 100:

    print("L'eau est à l'état liquide")

else:

    print("l'eau est à l'était gazeux")