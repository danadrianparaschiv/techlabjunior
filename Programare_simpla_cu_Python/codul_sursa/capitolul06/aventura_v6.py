import random

# Funcție pentru afișarea mesajului de început
def salut():
    print("Bun venit în aventura funcțiilor!")
    print("Scrie 'exit' pentru a ieși din joc.\n")

# Funcție pentru afișarea statusului
def afiseaza_status(viata, aur, inventar):
    print(f"Viață: {viata} | Aur: {aur} | Inventar: {inventar}")

# Funcție pentru explorarea pădurii
def exploreaza_padure(viata, aur):
    if random.randint(1, 2) == 1:
        aur_gasit = random.randint(1, 5)
        print(f"Ai găsit {aur_gasit} monede de aur în pădure!")
        aur += aur_gasit
    else:
        print("Un lup sălbatic te-a zgâriat! Pierzi 2 viață.")
        viata -= 2
    return viata, aur

# Funcție pentru vizitarea peșterii
def viziteaza_pestera(viata, aur, inventar):
    if aur >= 5:
        print("Cumperi o poțiune magică!")
        inventar.append("poțiune magică")
        aur -= 5
    else:
        print("Nu ai suficient aur pentru poțiuni.")
    return viata, aur, inventar

# Joc principal
def joc():
    viata = 10
    aur = 0
    inventar = ["sabie"]
    salut()

    while viata > 0:
        afiseaza_status(viata, aur, inventar)
        actiune = input("\nUnde vrei să mergi? (padure/pestera/exit) ")

        if actiune == "exit":
            print("Ai ales să părăsești aventura.")
            break
        elif actiune == "padure":
            viata, aur = exploreaza_padure(viata, aur)
        elif actiune == "pestera":
            viata, aur, inventar = viziteaza_pestera(viata, aur, inventar)
        else:
            print("Loc necunoscut.")

    print("\nJoc încheiat! Inventar final:", inventar)

# Pornim jocul
joc()