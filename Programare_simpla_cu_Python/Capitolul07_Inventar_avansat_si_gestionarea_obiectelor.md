
# Capitolul 7 – Inventar avansat și gestionarea obiectelor

## De ce avem nevoie de un inventar mai avansat?

Până acum, inventarul nostru era doar o listă cu obiecte. Dar, în aventurile mai complexe:

- Unele obiecte au cantități (ex.: 3 poțiuni).
- Altele au proprietăți speciale (ex.: sabie care dă +2 atac).
- Trebuie să putem adăuga, scoate și folosi obiectele în joc.

Pentru asta, vom folosi dicționare (eng. dictionaries), care ne permit să stocăm perechi cheie–valoare.

## Ce vei învăța în acest capitol

- Cum să folosești dicționare pentru inventar.
- Cum să adaugi și să elimini obiecte din inventar.
- Cum să afișezi inventarul într-un mod prietenos.
- Cum să faci un mini-sistem de cumpărare și folosire a obiectelor.

## Dicționarele în Python

Un dicționar este ca o listă de cutii etichetate: fiecare cheie are o valoare asociată.

Exemplu simplu:

```python
inventar = {
    "sabie": 1,
    "poțiune": 3
}
```

### Accesarea valorilor

```python
print("Ai", inventar["poțiune"], "poțiuni.")
```

### Adăugarea unui obiect

```python
inventar["scut"] = 1
```

### Modificarea unei valori

```python
inventar["poțiune"] += 1  # adaugi o poțiune
```

### Ștergerea unui obiect

```python
del inventar["sabie"]
```

## Afișarea frumoasă a inventarului

```python
def afiseaza_inventar(inventar):
    print("\nInventarul tău:")
    for obiect, cantitate in inventar.items():
        print(f"- {obiect}: {cantitate}")

```

## Mini-sistem de cumpărături

### Cod complet

```python
def afiseaza_inventar(inventar):
    print("\nInventarul tău:")
    for obiect, cantitate in inventar.items():
        print(f"- {obiect}: {cantitate}")

# Inventarul și aurul
inventar = {"sabie": 1}
aur = 10

# Magazinul
magazin = {
    "poțiune": 3,
    "scut": 5
}

print("Bun venit la magazinul magic!")
afiseaza_inventar(inventar)
print("Ai", aur, "aur.")

while True:
    print("\nArticole disponibile:")
    for obiect, pret in magazin.items():
        print(f"- {obiect}: {pret} aur")
    alegere = input("Ce vrei să cumperi? (scrie 'exit' pentru a ieși) ")

    if alegere == "exit":
        break
    elif alegere in magazin:
        if aur >= magazin[alegere]:
            aur -= magazin[alegere]
            if alegere in inventar:
                inventar[alegere] += 1
            else:
                inventar[alegere] = 1
            print(f"Ai cumpărat {alegere}!")
        else:
            print("Nu ai suficient aur!")
    else:
        print("Articol necunoscut.")

afiseaza_inventar(inventar)
print("Aur rămas:", aur)
```

## Exerciții pentru tine

- Adaugă un magazin ascuns care vinde obiecte rare dacă ai mai mult de 10 aur.
- Creează o funcție `foloseste_obiect(obiect)` care scade cantitatea și are efecte diferite (poțiune = +2 viață, scut = protecție).
- Fă ca inventarul să salveze numărul total de obiecte folosite.

## Casetă bonus: Diferența dintre liste și dicționare

- **Listă** – bună pentru obiecte unice sau când ordinea contează.
- **Dicționar** – bun pentru obiecte cu cantități sau proprietăți.

În jocurile complexe, vei folosi adesea ambele: listă pentru locații, dicționar pentru inventar.


## Casetă bonus: Jocul „Simon Says”

### Descriere

- Calculatorul generează o secvență de cuvinte (ex.: „sus”, „jos”, „stânga”, „dreapta”).
- Jucătorul trebuie să repete exact secvența.
- De fiecare dată când jucătorul reușește, secvența devine mai lungă.
- Jocul se termină când jucătorul greșește.

### Codul jocului bonus

```python
import random
import time

def joc_simon():
    print("Bine ai venit la jocul BONUS: Simon Says!")
    print("Repetă secvența de cuvinte exact cum apare.")
    print("Scrie cuvintele separate prin spațiu.")

    directii = ["sus", "jos", "stânga", "dreapta"]
    secventa = []
    scor = 0

    while True:
        # Adaugă o nouă direcție aleatoare în secvență
        secventa.append(random.choice(directii))

        # Afișează secvența
        print("\nSecvența este:")
        for pas in secventa:
            print(pas)
            time.sleep(0.7)  # pauză scurtă pentru fiecare pas

        # Șterge ecranul cu linii noi (simulare)
        print("\n" * 20)

        # Cere jucătorului să introducă secvența
        raspuns = input("Repetă secvența: ").lower().split()

        # Verifică răspunsul
        if raspuns == secventa:
            scor += 1
            print("Corect! Scorul tău este:", scor)
        else:
            print("Greșit! Joc încheiat.")
            print("Secvența corectă era:", " ".join(secventa))
            print("Scor final:", scor)
            break

# Pornim jocul
joc_simon()
```

### Ce înveți din acest joc

- Folosirea listelor pentru memorarea unei secvențe dinamice.
- Adăugarea de elemente aleatorii cu `random.choice()`.
- Compararea listelor pentru a verifica corectitudinea inputului.
- Creșterea dificultății progresive în buclă.