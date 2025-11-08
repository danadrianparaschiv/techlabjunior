import json
import random

# ======== Clase ========
class Aventurier:
    def __init__(self, nume):
        self.nume = nume
        self.viata = 15
        self.aur = 0
        self.inventar = []

    def afiseaza_status(self):
        print(f"\n{self.nume} – Viață: {self.viata}, Aur: {self.aur}, Inventar: {self.inventar}")

    def colecteaza(self, obiect):
        self.inventar.append(obiect)
        print(f"Ai colectat {obiect}!")

    def vindeca(self):
        if "poțiune" in self.inventar:
            self.viata += 5
            self.inventar.remove("poțiune")
            print("Ai folosit o poțiune și te-ai vindecat cu 5 viață!")
        else:
            print("Nu ai nicio poțiune de folosit.")

class Monstru:
    def __init__(self, nume, viata, atac):
        self.nume = nume
        self.viata = viata
        self.atac = atac

    def ataca(self, tinta):
        print(f"{self.nume} atacă pe {tinta.nume} și îi scade {self.atac} viață!")
        tinta.viata -= self.atac

# ======== Funcții pentru salvare/încărcare ========
def salveaza_joc(jucator, locatie):
    date_joc = {
        "nume": jucator.nume,
        "viata": jucator.viata,
        "aur": jucator.aur,
        "inventar": jucator.inventar,
        "locatie": locatie
    }
    with open("save.json", "w") as f:
        json.dump(date_joc, f)
    print("Progres salvat!")

def incarca_joc():
    try:
        with open("save.json", "r") as f:
            date_joc = json.load(f)
        print("Progres încărcat!")
        return date_joc
    except FileNotFoundError:
        print("Nu există un fișier de salvare.")
        return None

# ======== Harta și descrieri ========
harta = {
    "sat": {"nord": "pădure", "est": "pajiște"},
    "pădure": {"sud": "sat", "est": "peșteră"},
    "peșteră": {"vest": "pădure", "est": "vizuina dragonului"},
    "pajiște": {"vest": "sat"},
    "vizuina dragonului": {"vest": "peșteră"}
}

descrieri = {
    "sat": "Ești în sat. Casele sunt mici și primitoare.",
    "pădure": "Pădurea e deasă și misterioasă. Poți găsi comori sau monștri.",
    "peșteră": "Peștera e întunecoasă. Se spune că ascunde o cheie magică.",
    "pajiște": "Pajiștea e liniștită, plină de flori.",
    "vizuina dragonului": "În fața ta se află Dragonul Final. Lupta decisivă începe!"
}

# ======== Evenimente speciale ========
def intalnire_monstru(jucator):
    monstru = Monstru("Lup sălbatic", random.randint(4, 8), random.randint(1, 3))
    print(f"\nUn {monstru.nume} apare!")
    while monstru.viata > 0 and jucator.viata > 0:
        actiune = input("Ataci sau fugi? ").lower()
        if actiune == "ataci":
            daune = random.randint(1, 4)
            monstru.viata -= daune
            print(f"Ai lovit monstrul cu {daune} daune!")
            if monstru.viata <= 0:
                print("Ai învins monstrul și primești 3 aur.")
                jucator.aur += 3
                break
            monstru.ataca(jucator)
        elif actiune == "fugi":
            print("Ai fugit din luptă!")
            break
        else:
            print("Comandă necunoscută.")

def eveniment_padure(jucator):
    if random.randint(1, 2) == 1:
        intalnire_monstru(jucator)
    else:
        print("Ai găsit o poțiune în pădure!")
        jucator.colecteaza("poțiune")

def eveniment_pestera(jucator):
    if "cheie magică" not in jucator.inventar:
        print("Ai găsit Cheia Magică!")
        jucator.colecteaza("cheie magică")
    else:
        print("Peștera e goală acum.")

def lupta_finala(jucator):
    dragon = Monstru("Dragonul Final", 15, 4)
    print("\nDragonul Final își aruncă flăcările asupra ta!")
    while dragon.viata > 0 and jucator.viata > 0:
        actiune = input("Ataci sau folosești poțiune? ").lower()
        if actiune == "ataci":
            daune = random.randint(2, 5)
            dragon.viata -= daune
            print(f"Ai lovit dragonul cu {daune} daune!")
            if dragon.viata <= 0:
                print("Ai învins Dragonul Final! Lumea e salvată!")
                return True
            dragon.ataca(jucator)
        elif actiune == "poțiune":
            jucator.vindeca()
        else:
            print("Comandă necunoscută.")
    return False

# ======== Joc principal ========
def joc():
    # Pornire: încarcă sau joc nou
    opt = input("Vrei să încarci jocul salvat? (da/nu) ").lower()
    if opt == "da":
        date = incarca_joc()
        if date:
            jucator = Aventurier(date["nume"])
            jucator.viata = date["viata"]
            jucator.aur = date["aur"]
            jucator.inventar = date["inventar"]
            locatie = date["locatie"]
        else:
            jucator = Aventurier("Eliza")
            locatie = "sat"
    else:
        jucator = Aventurier("Eliza")
        locatie = "sat"

    # Bucla jocului
    while True:
        print("\n" + descrieri[locatie])
        jucator.afiseaza_status()
        print("Direcții disponibile:", ", ".join(harta[locatie].keys()))

        comanda = input("Ce faci? (nord/sud/est/vest/salveaza/exit) ").lower()

        if comanda == "salveaza":
            salveaza_joc(jucator, locatie)
        elif comanda == "exit":
            print("Ai încheiat jocul.")
            break
        elif comanda in harta[locatie]:
            locatie = harta[locatie][comanda]

            # Evenimente în funcție de locație
            if locatie == "pădure":
                eveniment_padure(jucator)
            elif locatie == "peșteră":
                eveniment_pestera(jucator)
            elif locatie == "vizuina dragonului":
                if "cheie magică" in jucator.inventar:
                    rezultat = lupta_finala(jucator)
                    if rezultat:
                        break
                else:
                    print("Ușa magică e încuiată. Îți trebuie Cheia Magică!")
                    locatie = "peșteră"
        else:
            print("Nu poți merge în acea direcție.")

        # Condiție de pierdere
        if jucator.viata <= 0:
            print("Ai murit în aventură. Joc terminat.")
            break

# Pornire joc
joc()