import random

# Harta jocului
harta = {
    "sat": {"nord": "pădure", "est": "pajiște"},
    "pădure": {"sud": "sat", "est": "peșteră"},
    "peșteră": {"vest": "pădure"},
    "pajiște": {"vest": "sat"}
}

# Descrieri locații
descrieri = {
    "sat": "Ești în sat. Aici poți să te odihnești și să vinzi obiecte.",
    "pădure": "Pădurea e deasă și plină de sunete misterioase.",
    "peșteră": "Peștera e rece și întunecoasă. Parcă cineva te urmărește...",
    "pajiște": "Pajiștea e plină de flori colorate și lumină caldă."
}

# Starea jucătorului
locatie = "sat"
viata = 10
aur = 0
inventar = {}

# Funcții
def adauga_obiect(obiect):
    global inventar
    if obiect in inventar:
        inventar[obiect] += 1
    else:
        inventar[obiect] = 1

def afiseaza_status():
    print(f"Viață: {viata} | Aur: {aur} | Inventar: {inventar}")

# Joc principal
print("Bun venit în aventura extinsă!")
while True:
    print("\n" + descrieri[locatie])
    afiseaza_status()
    print("Poți merge în:", ", ".join(harta[locatie].keys()))

    comanda = input("Unde vrei să mergi? (scrie exit pentru a ieși) ").lower()

    if comanda == "exit":
        print("Ai ales să închei aventura.")
        break
    elif comanda in harta[locatie]:
        locatie = harta[locatie][comanda]

        # Evenimente în funcție de locație
        if locatie == "pădure":
            if random.randint(1, 2) == 1:
                print("Ai găsit o poțiune!")
                adauga_obiect("poțiune")
            else:
                print("Un lup te-a atacat! Pierzi 2 viață.")
                viata -= 2
        elif locatie == "peșteră":
            if "cheie magică" not in inventar:
                print("Ai găsit o cheie magică!")
                adauga_obiect("cheie magică")
            else:
                print("Peștera e liniștită... nu găsești nimic nou.")
        elif locatie == "pajiște":
            print("Culegi flori și vinzi la sat. Primești 3 aur!")
            aur += 3
        elif locatie == "sat":
            print("Te odihnești și recuperezi 2 viață.")
            viata += 2

        # Condiții de joc
        if viata <= 0:
            print("Ai rămas fără viață! Joc terminat.")
            break
        if "cheie magică" in inventar and aur >= 10:
            print("Ai cheia magică și suficient aur. Ai câștigat aventura!")
            break

    else:
        print("Nu poți merge în acea direcție!")
