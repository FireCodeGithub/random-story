import random
femme = ["une femme", "une progameuse", "une folle", "une pute", "une grosse dégeulasse", "une caissière"]
homme = ["un homme", "un progammeur", "un fou", "un striptiser", "un fan de film pornos", "Robin", "Celyan"]
lieu = ["sur la lune", "dans le désert", "au supermarché", "à Namur", "dans un bar à striptease"]
ElleDit = ["donnez moi une idée !", "glup glup bziiiiiii bzibzi aaaaaah", "pardonnez moi, je cherche de la mozzarela", "gouzi gouzi", "Miam", "Qui a peté ?"]
IlDit = ["IL dit : aime tu les frites ?", "Il dit : sais tu programmer en python ?", "Il dit : est-ce que ton prenom est Robin ?", "Il dit : C'est toi qui a peté ?" ]
Oui1 = ["comme moi", "comme celui qui m'a progamé", "moi aussi !"]
Non1 = ["dommage", "moi si"]
while True:
    print("un jour", random.choice(femme), "rencontre", random.choice(homme), random.choice(lieu))
    print("elle dit :", random.choice(ElleDit))
    choix1 = input(random.choice(IlDit))
    if choix1 == "oui":
        print(random.choice(Oui1))
    elif choix1 == "non":
        print(random.choice(Non1))
    else:
        print("reponds !")
    print()
    print("Appuie sur entrée pour rejouer")
    print()

