
# Capitolul 9 – Hărți mai mari și mișcare liberă

## Ce am învățat până acum

- Am făcut un joc de aventură simplu cu locații (sat, pădure, peșteră).
- Am introdus inventar, aur și viață.
- Am folosit funcții pentru a organiza codul.
- Am adăugat evenimente aleatorii și mici misiuni.

Acum facem următorul pas: hărți mai mari și mișcare liberă. Jucătorul va putea merge în mai multe direcții (nord, sud, est, vest), iar locațiile vor fi conectate între ele.

## Ce vei învăța în acest capitol

- Cum să reprezinți o hartă folosind dicționare.
- Cum să permiți jucătorului să se deplaseze între locații.
- Cum să adaugi descrieri diferite pentru fiecare loc.
- Cum să combini evenimentele și inventarul într-un joc mai mare.

## Reprezentarea hărții cu dicționare

Vom folosi un dicționar unde:

- Cheia este numele locației.
- Valoarea este un alt dicționar care descrie direcțiile posibile și destinațiile.

Exemplu de hartă:

```python
harta = {
    "sat": {"nord": "pădure", "est": "pajiște"},
    "pădure": {"sud": "sat", "est": "peșteră"},
    "peșteră": {"vest": "pădure"},
    "pajiște": {"vest": "sat"}
}
```

### Descrieri pentru locații

Adăugăm un dicționar cu descrieri text:

```python
descrieri = {
    "sat": "Ești în sat. Casele sunt mici și prietenoase.",
    "pădure": "Pădurea e deasă și răsună de cântece de păsări.",
    "peșteră": "Peștera e întunecoasă și rece. Simți un curent de aer misterios.",
    "pajiște": "Pajiștea e plină de flori colorate și fluturi."
}
```

## Mișcarea jucătorului

Pentru a te deplasa:

1. Vezi unde ești.
2. Afișează direcțiile posibile.
3. Ceri o comandă de la jucător (nord, sud, est, vest).
4. Actualizezi locația curentă dacă direcția e validă.

### Cod pas cu pas

#### Pas 1 – Starea inițială

```python
locatie = "sat"  # începem în sat
```

#### Pas 2 – Bucla jocului

```python
while True:
    print("\n" + descrieri[locatie])  # descrierea locului
    print("Poți merge în:", ", ".join(harta[locatie].keys()))

    comanda = input("Unde vrei să mergi? (scrie exit pentru a ieși) ").lower()

    if comanda == "exit":
        print("Ai ales să închei aventura.")
        break
    elif comanda in harta[locatie]:
        locatie = harta[locatie][comanda]  # schimbăm locația
    else:
        print("Nu poți merge în acea direcție!")
```

## Integrarea inventarului și aurului

Combinăm codul cu inventarul și viața din capitolele anterioare:

- Jucătorul poate găsi obiecte în pădure sau peșteră.
- Poate vinde/comercializa obiecte în sat.
- Poate primi aur sau pierde viață în anumite locații.

### Cod complet extins

```python
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

```

## Exerciții pentru tine

- Adaugă o a cincea locație – un turn misterios care oferă obiecte rare.
- Creează o misiune: colectează 3 flori din pajiște și du-le la sat pentru o recompensă.
- Fă ca evenimentele din pădure să fie mai variate (monstru, comoară, nimic).
- Adaugă un sistem de niveluri: la fiecare 10 aur strâns, crește nivelul jucătorului.

## Casetă bonus: Cum să faci hărți mai complexe

- Folosește liste bidimensionale (matrice) pentru o hartă tip grilă (similară cu jocurile clasice).
- Creează locații dinamice – apar și dispar în funcție de progresul jucătorului.
- Leagă harta cu povești: fiecare loc are un mini-dialog sau o legendă.
