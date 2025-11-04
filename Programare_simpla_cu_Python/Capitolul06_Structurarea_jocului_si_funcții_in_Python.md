
# Capitolul 6 – Structurarea jocului și funcții în Python

## De ce avem nevoie de funcții?

Pe măsură ce jocul devine mai mare, codul începe să se aglomereze: bucăți repetate, secțiuni greu de citit. Funcțiile (eng. functions) ne ajută să:

- Grupăm codul care face o anumită acțiune (ex.: afișează inventarul, calculează daunele).
- Refolosim codul de câte ori avem nevoie.
- Facem jocul mai organizat și mai ușor de extins.

## Ce vei învăța în acest capitol

- Cum să definești o funcție în Python.
- Cum să apelezi o funcție.
- Cum să folosești parametri și valori returnate.
- Cum să reorganizezi codul jocului nostru în funcții.

## Cum definim o funcție

În Python, o funcție se definește cu `def`:

```python
def salut():
    print("Salut, aventurierule!")
    print("Pregătește-te de o nouă misiune!")
```

Pentru a o folosi, o apelăm scriind numele ei:

```python
salut()
```

## Funcții cu parametri

Putem trimite informații către o funcție folosind parametri:

```python
def afiseaza_status(viata, aur):
    print("Viață:", viata, "| Aur:", aur)

afiseaza_status(10, 5)
```

## Funcții care returnează valori

Uneori avem nevoie ca funcția să calculeze ceva și să ne dea înapoi rezultatul. Pentru asta folosim return:
```python
def calculeaza_daune(putere_atac):
    return putere_atac * 2

daune = calculeaza_daune(3)
print("Ai produs", daune, "puncte de daune!")

```

## Reorganizăm jocul cu funcții

Să luăm elementele din capitolele trecute și să le transformăm în funcții:

- `salut()` → afișează mesajul de început.
- `afiseaza_status()` → arată viața și aurul curent.
- `exploreaza_padure()` → întoarce câte aur și viață câștigi sau pierzi.
- `viziteaza_pestera()` → verifică dacă poți cumpăra poțiuni.

### Cod reorganizat cu funcții

```python
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
```

## Exerciții pentru tine

- Creează o funcție `lupteaza_monstru()` care să folosească parametri pentru viața jucătorului și a monstrului și să returneze viața rămasă.
- Adaugă o funcție `misiune_bonus()` care să apară uneori aleatoriu.
- Reorganizează complet jocul tău astfel încât fiecare acțiune să fie într-o funcție separată.


## Casetă bonus: Avantajele funcțiilor
- 
- Cod mai scurt și mai ușor de citit.
- Poți modifica o singură funcție și se schimbă tot jocul.
- Ușor de extins: adaugi funcții noi pentru locuri, monștri sau obiecte.


## Casetă bonus: Jocul „Ghicitori magice”

### Descriere

- Jocul pune pe rând mai multe ghicitori.
- Jucătorul trebuie să răspundă corect pentru a câștiga puncte.
- Folosim funcții pentru a afișa întrebările, pentru a verifica răspunsurile și pentru a ține scorul.

### Codul jocului bonus

```python
# Funcția care pune o ghicitoare și verifică răspunsul
def pune_ghicitoare(intrebare, raspuns_corect):
    raspuns = input(intrebare + "\nRăspunsul tău: ").lower()
    if raspuns == raspuns_corect:
        print("Corect! Ai câștigat 1 punct.")
        return 1  # punct câștigat
    else:
        print("Greșit! Răspunsul corect era:", raspuns_corect)
        return 0  # fără puncte

# Jocul principal
def joc_ghicitori():
    print("Bine ai venit la jocul BONUS: Ghicitori magice!")
    scor = 0

    # Lista de ghicitori (intrebare, raspuns_corect)
    ghicitori = [
        ("Ce are chei dar nu poate deschide uși?", "pian"),
        ("Ce are gât dar nu are cap?", "sticla"),
        ("Ce urcă dar nu coboară niciodată?", "varsta"),
    ]

    for intrebare, raspuns_corect in ghicitori:
        scor += pune_ghicitoare(intrebare, raspuns_corect)

    print("\nAi terminat jocul! Scorul tău este:", scor, "din", len(ghicitori))

# Pornim jocul
joc_ghicitori()
```

### Ce înveți din acest joc bonus

- Cum să structurezi codul în funcții (una pentru ghicitoare, alta pentru joc).
- Cum să iterezi printr-o listă de întrebări.
- Cum să acumulezi scorul folosind valorile returnate de funcții.
