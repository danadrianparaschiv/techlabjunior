
# Capitolul 5 – Evenimente aleatorii și surprize în joc

## De ce avem nevoie de evenimente aleatorii?

În aventurile reale, nu știi niciodată ce urmează să se întâmple. Poți să găsești o comoară sau să dai peste un monstru. Pentru ca jocurile să fie mai interesante, putem introduce elemente de întâmplare (eng. random events) – lucruri care apar diferit de fiecare dată când joci.

## Ce vei învăța în acest capitol

Cum să folosești modulul random pentru a crea evenimente neașteptate.
Cum să alegi obiecte aleatorii dintr-o listă.
Cum să creezi lupte și recompense aleatorii.
Cum să adaugi surprize care fac jocul mai distractiv și rejucabil.

## Importăm modulul random

În Python, pentru a genera numere sau alegeri aleatoare, folosim modulul random:
```python
import random

```

## Generăm un număr aleator

Exemplu simplu:
```python
numar_secret = random.randint(1, 10)  # număr între 1 și 10

```

De fiecare dată când rulezi codul, vei obține un alt număr.

## Alegem aleatoriu dintr-o listă

Putem alege un obiect surpriză dintr-o listă:
```python
obiecte = ["sabie veche", "poțiune magică", "scut de lemn"]
obiect_gasit = random.choice(obiecte)
print("Ai găsit:", obiect_gasit)

```

## Eveniment aleator: întâlnirea cu un monstru

Să simulăm o întâlnire care poate apărea sau nu:
```python
import random

if random.randint(1, 3) == 1:  # 1 din 3 șanse
    print("Un monstru sălbatic apare!")
else:
    print("Drumul e liniștit și sigur.")

```

## Luptă simplă cu elemente aleatorii

Exemplu de luptă:
```python
import random

viata_jucator = 10
viata_monstru = random.randint(5, 12)

print("Un monstru a apărut cu", viata_monstru, "viață!")

while viata_monstru > 0 and viata_jucator > 0:
    atac = random.randint(1, 4)
    print("Ataci monstrul și îi scazi", atac, "viață.")
    viata_monstru -= atac

    if viata_monstru <= 0:
        print("Ai învins monstrul!")
        break

    # Monstrul atacă
    atac_monstru = random.randint(1, 3)
    print("Monstrul te lovește și pierzi", atac_monstru, "viață.")
    viata_jucator -= atac_monstru

if viata_jucator <= 0:
    print("Ai pierdut lupta!")

```

## Exerciții pentru tine

Creează o listă de monștri diferiți (dragon, goblin, liliac) și alege unul aleatoriu.
Fă ca monstrul să lase un obiect aleatoriu dacă este învins.
Adaugă o șansă aleatorie ca jucătorul să primească un bonus de viață în pădure.

## Casetă explicativă: random.randint vs random.choice

random.randint(a, b) → alege un număr întreg între a și b (inclusiv).
random.choice(lista) → alege un element aleatoriu dintr-o listă.
Ambele sunt esențiale pentru a crea variație în jocurile tale.

## Casetă bonus: Jocul „Spânzurătoarea”

### Descriere

Calculatorul alege un cuvânt secret dintr-o listă.
Jucătorul trebuie să ghicească literele cuvântului, una câte una.
Dacă ghicește toate literele, câștigă. Dacă greșește de prea multe ori, pierde.
Jocul se repetă până când cuvântul e complet sau încercările s-au terminat.

### Codul jocului bonus

```python
import random

print("Bine ai venit la jocul BONUS: Spânzurătoarea!")
print("Ghicește cuvântul literă cu literă.")

# Lista de cuvinte
cuvinte = ["python", "aventura", "magie", "padure", "sabie"]

# Alegem un cuvânt aleator
cuvant_secret = random.choice(cuvinte)
ghicit = ["_"] * len(cuvant_secret)  # listă cu liniuțe pentru fiecare literă

incercari = 6  # numărul maxim de greșeli

while incercari > 0 and "_" in ghicit:
    print("\nCuvânt:", " ".join(ghicit))
    litera = input("Alege o literă: ").lower()

    if litera in cuvant_secret:
        print("Bravo! Litera este în cuvânt.")
        for i, l in enumerate(cuvant_secret):
            if l == litera:
                ghicit[i] = litera
    else:
        incercari -= 1
        print(f"Litera nu există. Mai ai {incercari} încercări.")

if "_" not in ghicit:
    print("\nFelicitări! Ai ghicit cuvântul:", cuvant_secret)
else:
    print("\nAi pierdut! Cuvântul era:", cuvant_secret)

```

### Ce înveți din acest joc bonus

Cum să folosești liste pentru a afișa progresul jucătorului.
Cum să verifici pozițiile literelor în cuvânt.
Cum să implementezi condiții de câștig/pierdere pe baza încercărilor rămase.

# 

# Codul complet al capitolului 5 – Mini-joc cu evenimente aleatorii

```python
import random

viata = 10
aur = 0
inventar = ["sabie"]

print("Începe aventura ta plină de surprize!")

while viata > 0:
    actiune = input("\nUnde vrei să mergi? (padure/pestera/exit) ")

    if actiune == "exit":
        print("Ai ales să închei aventura.")
        break

    if actiune == "padure":
        # Șansă să găsești aur sau să întâlnești un monstru
        if random.randint(1, 2) == 1:
            aur_gasit = random.randint(1, 5)
            aur += aur_gasit
            print(f"Ai găsit {aur_gasit} monede de aur!")
        else:
            print("Un monstru apare în pădure!")
            viata_monstru = random.randint(5, 10)
            while viata_monstru > 0 and viata > 0:
                atac = random.randint(1, 4)
                viata_monstru -= atac
                print(f"Lovești monstrul cu {atac} puncte!")

                if viata_monstru <= 0:
                    print("Ai învins monstrul și câștigi 2 aur!")
                    aur += 2
                    break

                atac_monstru = random.randint(1, 3)
                viata -= atac_monstru
                print(f"Monstrul te lovește cu {atac_monstru} puncte!")

    elif actiune == "pestera":
        if aur >= 5:
            print("Cumperi o poțiune magică și câștigi 3 viață!")
            inventar.append("poțiune magică")
            aur -= 5
            viata += 3
        else:
            print("Nu ai suficient aur. Peștera e pustie.")

    else:
        print("Loc necunoscut. Alege padure, pestera sau exit.")

print("\nAventura s-a încheiat!")
print("Inventarul tău:", inventar)
print("Aur:", aur, "| Viață:", viata)

```