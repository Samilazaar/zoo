class Animal:
    def __init__(self, nom, espèce, âge, sexe):
        self.nom = nom
        self.espèce = espèce
        self.âge = âge
        self.sexe = sexe

    def afficher_details(self):
        print(f"{self.nom} ({self.espèce}), {self.âge} ans, {self.sexe}")

    def émettre_son(self):
        print("Cri indéfini !")


class Enclos:
    def __init__(self, nom, capacité_max):
        self.nom = nom
        self.capacité_max = capacité_max
        self.animaux = []

    def ajouter_animal(self, animal):
        if len(self.animaux) < self.capacité_max:
            self.animaux.append(animal)
            print(f"{animal.nom} a été ajouté à l'enclos {self.nom}")
        else:
            print(
                f"L'enclos {self.nom} est plein, impossible d'ajouter {animal.nom}")

    def retirer_animal(self, animal):
        if animal in self.animaux:
            self.animaux.remove(animal)
            print(f"{animal.nom} a été retiré de l'enclos {self.nom}")
        else:
            print(f"{animal.nom} n'est pas dans l'enclos {self.nom}")

    def afficher_animaux(self):
        print(f"Animaux dans l'enclos {self.nom}:")
        for animal in self.animaux:
            animal.afficher_details()


class Soigneur:
    def __init__(self, nom, spécialité):
        self.nom = nom
        self.spécialité = spécialité
        self.animaux_soigneur = []

    def afficher_animaux_soigneur(self):
        print(
            f"Animaux dont s'occupe le soigneur {self.nom} ({self.spécialité}):")
        for animal in self.animaux_soigneur:
            animal.afficher_details()

    def nourrir_animal(self, animal):
        print(f"{self.nom} nourrit {animal.nom}")


class Zoo:
    def __init__(self, nom):
        self.nom = nom
        self.enclos = []
        self.soigneurs = []

    def ajouter_enclo(self, enclo):
        self.enclos.append(enclo)
        print(f"Enclos {enclo.nom} ajouté au zoo {self.nom}")

    def ajouter_soigneur(self, soigneur):
        self.soigneurs.append(soigneur)
        print(f"Soigneur {soigneur.nom} ajouté au zoo {self.nom}")

    def afficher_enclos(self):
        print(f"Enclos dans le zoo {self.nom}:")
        for enclo in self.enclos:
            print(enclo.nom)

    def afficher_soigneurs(self):
        print(f"Soigneurs dans le zoo {self.nom}:")
        for soigneur in self.soigneurs:
            print(soigneur.nom)


class SimulationZoo:
    def __init__(self):
        self.zoo = Zoo("Zoo Fantastique")

    def afficher_menu(self):
        print("\nMenu:")
        print("1. Ajouter un animal à un enclos")
        print("2. Afficher les animaux dans un enclos")
        print("3. Ajouter un soigneur au zoo")
        print("4. Nourrir un animal")
        print("0. Quitter")

    def executer_simulation(self):
        choix = None
        while choix != "0":
            self.afficher_menu()
            choix = input("Choisissez une option (0-4): ")

            if choix == "1":
                self.ajouter_animal_enclos()
            elif choix == "2":
                self.afficher_animaux_enclos()
            elif choix == "3":
                self.ajouter_soigneur_zoo()
            elif choix == "4":
                self.nourrir_animal()

    def ajouter_animal_enclos(self):
        nom_animal = input("Nom de l'animal: ")
        espèce_animal = input("Espèce de l'animal: ")
        âge_animal = int(input("Âge de l'animal: "))
        sexe_animal = input("Sexe de l'animal: ")

        nouvel_animal = Animal(nom_animal, espèce_animal,
                               âge_animal, sexe_animal)

        # Sélectionner un enclos existant (vous pouvez ajouter une logique pour gérer les enclos)
        enclo = self.zoo.enclos[0] if self.zoo.enclos else None

        if enclo:
            enclo.ajouter_animal(nouvel_animal)
            print(f"{nouvel_animal.nom} a été ajouté à l'enclos {enclo.nom}")
        else:
            print("Aucun enclos disponible pour ajouter l'animal.")

    def afficher_animaux_enclos(self):
        # Sélectionner un enclos existant (vous pouvez ajouter une logique pour gérer les enclos)
        enclo = self.zoo.enclos[0] if self.zoo.enclos else None

        if enclo:
            enclo.afficher_animaux()
        else:
            print("Aucun enclos disponible pour afficher les animaux.")

    def ajouter_soigneur_zoo(self):
        nom_soigneur = input("Nom du soigneur: ")
        spécialité_soigneur = input("Spécialité du soigneur: ")

        nouveau_soigneur = Soigneur(nom_soigneur, spécialité_soigneur)

        self.zoo.ajouter_soigneur(nouveau_soigneur)
        print(f"{nouveau_soigneur.nom} a été ajouté au zoo.")

    def nourrir_animal(self):
        nom_soigneur = input("Nom du soigneur: ")
        nom_animal = input("Nom de l'animal à nourrir: ")

        # Sélectionner un soigneur existant (vous pouvez ajouter une logique pour gérer les soigneurs)
        soigneur = next(
            (s for s in self.zoo.soigneurs if s.nom == nom_soigneur), None)

        # Sélectionner un animal existant dans le zoo (vous pouvez ajouter une logique pour gérer les animaux)
        animal = next(
            (a for enclo in self.zoo.enclos for a in enclo.animaux if a.nom == nom_animal), None)

        if soigneur and animal:
            soigneur.nourrir_animal(animal)
        else:
            print("Soigneur ou animal non trouvé.")


# Créer une instance de la simulation et l'exécuter
simulation = SimulationZoo()
simulation.executer_simulation()

# Création d'objets
lion = Animal("Simba", "Lion", 5, "Mâle")
enclo_lions = Enclos("Enclos des Lions", 3)
zoo = Zoo("Zoo Fantastique")

# Ajout d'objets au zoo
zoo.ajouter_enclo(enclo_lions)

# Ajout d'animaux à l'enclos
enclo_lions.ajouter_animal(lion)

# Affichage des animaux dans l'enclos
enclo_lions.afficher_animaux()

# Création d'un soigneur et ajout au zoo
soigneur_jane = Soigneur("Jane", "Mammifères")
zoo.ajouter_soigneur(soigneur_jane)

# Soigneur prenant soin d'un animal
soigneur_jane.nourrir_animal(lion)
