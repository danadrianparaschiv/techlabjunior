import random

class Aventurier:
    def __init__(self, nume):
        self.nume = nume
        self.viata = 10
        self.aur = 0
        self.inventar = []

    def afiseaza_status(self):
        print(f"{self.nume} – Viață: {self.viata}, Aur: {self.aur}, Inventar: {self.inventar}")

    def colecteaza(self, obiect):
        self.inventar.append(obiect)
        print(f"Ai colectat {obiect}!")

class Monstru:
    def __init__(self, nume, viata, atac):
        self.nume = nume
        self.viata = viata
        self.atac = atac

    def ataca(self, tinta):
        print(f"{self.nume} atacă pe {tinta.nume} și îi scade {self.atac} viață!")
        tinta.viata -= self.atac

# Joc simplu cu luptă
jucator = Aventurier("Eliza")
monstru = Monstru("Dragon mic", 8, 3)

jucator.afiseaza_status()
monstru.ataca(jucator)
jucator.afiseaza_status()

# Colectăm un obiect
jucator.colecteaza("poțiune magică")