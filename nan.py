import random

class jeu:
    def __init__(self, nom, numero, somme, ticket):
        self.nom = nom
        self.numero = numero
        self.somme = somme
        self.ticket = ticket

    liste = []
    gagnant = []

    i = 0
    nb_joueur = 10
    min_numero = 1
    max_numero = 99


    while i<nb_joueur:
        print("Bienvenue, vous êtes le joueur n{}".format(i+1));
        nom = input("Veuillez entrer votre nom:");
        print("Ravi de vous rencontrer {}\n".format(nom))

        while True:
            numero = int(input("Veuillez choisir un nombre entre 1 et 99:"))
        if numero >= min_numero and numero <= max_numero:
            break
        while True:
            somme = int(input("Veuillez entrer une sommes a miser:"))
            if somme > 0:
                break
            jeu = jeu(nom, numero, somme, i)
            liste.append(jeu)
            print("------------------------------------------------")
            i+=1

            tirer = random.random(min_numero, max_numero)

            for jeu in liste:
                if jeu.numero == tirer:
                    gagnant.append(jeu)
            print("Le numerongagnant est le numero {}".format(tirer))

            if len(gagnant) == 0:
                print("Malheureusement pas de gagnant aujourd\'hui:")
            else:
                print("Voici les gagnants du jour:")
                for jeu in gagnant:
                    print("Nom : {}, Ticket : {}".format(jeu.nom, jeu.ticket))
                              
                              
