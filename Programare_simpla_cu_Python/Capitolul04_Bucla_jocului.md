
# Capitolul 4 – Bucla jocului și explorarea liberă

## Ce este bucla principală a jocului?

În capitolele anterioare, programele noastre se terminau după o singură alegere. Dar jocurile adevărate nu se opresc după prima decizie – continuă până când jucătorul câștigă, pierde sau alege să iasă.
Aici intervine bucla principală (eng. game loop). Este o instrucțiune care face ca jocul să se repete, verificând continuu ce vrea să facă jucătorul.

## Ce vei învăța în acest capitol

Cum să folosești o buclă while pentru a crea un joc care rulează continuu.
Cum să oferi jucătorului opțiuni multiple de explorare.
Cum să creezi condiții de victorie sau pierdere.
Cum să implementezi comanda „ieșire” (eng. exit command).

## Bucla while – cum funcționează

Instrucțiunea while repetă un bloc de cod atâta timp cât condiția este adevărată.
Exemplu simplu:
```python
numar = 0

while numar < 5:
    print("Număr:", numar)
    numar += 1

```

## Aplicăm la jocul nostru

Vom crea un joc unde:
Jucătorul poate merge la sat, pădure sau peșteră.
Poate aduna aur, pierde sau câștiga viață.
Jocul continuă până când jucătorul scrie exit sau viața scade la 0.

### Pas 1 – Starea inițială

```python
viata = 10
aur = 0
inventar = ["sabie"]

print("Bun venit în aventura ta!")
print("Scrie 'exit' dacă vrei să închei jocul.")

```

### Pas 2 – Bucla principală

```python
while viata > 0:
    print("\nAi", viata, "viață și", aur, "aur.")
    print("Locuri disponibile: sat / pădure / peșteră")
    loc = input("Unde vrei să mergi? ")

    if loc == "exit":
        print("Ai ales să părăsești aventura.")
        break

    if loc == "sat":
        print("Te odihnești și recuperezi 2 viață.")
        viata += 2
    elif loc == "pădure":
        print("Ai găsit 3 aur, dar te-a zgâriat un lup (pierzi 1 viață).")
        aur += 3
        viata -= 1
    elif loc == "peșteră":
        if aur >= 5:
            print("Plătești 5 aur și găsești o poțiune magică.")
            inventar.append("poțiune magică")
            aur -= 5
        else:
            print("Peștera e periculoasă și pierzi 3 viață!")
            viata -= 3
    else:
        print("Nu știu locul acesta. Alege sat, pădure sau peșteră.")

```

### Pas 3 – Finalul jocului

```python
print("\nJoc încheiat!")
print("Inventar final:", inventar)
print("Aur:", aur, "| Viață:", viata)

```

## Exerciții pentru tine

Adaugă un dragon în peșteră care apare aleatoriu și reduce viața cu 5 dacă nu ai poțiune.
Permite jucătorului să vândă poțiuni în sat pentru aur.
Creează o condiție de victorie – de exemplu, dacă jucătorul strânge 20 aur, afișează mesajul „Ai câștigat aventura!”.

## Casetă explicativă: Bucla infinită și break

O buclă infinită este o buclă care rulează la nesfârșit, de obicei scrisă ca while True:.
Folosim break pentru a ieși din buclă atunci când jucătorul scrie exit sau când se întâmplă ceva important (victorie/pierdere).
Exemple:
```python
while True:
    comanda = input("Scrie ceva sau 'exit': ")
    if comanda == "exit":
        break
    print("Ai scris:", comanda)

```

Iată cum putem adăuga în Capitolul 4 o casetă cu un joc bonus „Ghicește numărul”. Acesta e un exercițiu clasic și foarte bun pentru exersarea buclelor și condițiilor.

## Casetă bonus: Jocul „Ghicește numărul”

### Descriere

Calculatorul alege un număr aleator între 1 și 20.
Jucătorul trebuie să ghicească numărul.
După fiecare încercare, jocul spune dacă numărul e prea mic sau prea mare.
Jocul se termină când ghicești sau după 5 încercări.

### Codul jocului bonus

```python
import random

print("Bine ai venit la jocul BONUS: Ghicește numărul!")
print("Am ales un număr între 1 și 20. Ai 5 încercări să-l ghicești.")

# Alegem un număr aleator
numar_secret = random.randint(1, 20)

# Jucătorul are 5 încercări
incercari = 5

while incercari > 0:
    ghicire = int(input("Introdu numărul tău: "))

    if ghicire == numar_secret:
        print("Felicitări! Ai ghicit numărul!")
        break
    elif ghicire < numar_secret:
        print("Numărul este MAI MARE decât atât.")
    else:
        print("Numărul este MAI MIC decât atât.")

    incercari -= 1
    print("Îți mai rămân", incercari, "încercări.")

if incercari == 0:
    print("Ai pierdut! Numărul era", numar_secret)

```

### Ce înveți din acest joc bonus

Folosirea bibliotecii random pentru a genera numere aleatoare.
Cum să folosești bucla while cu un număr limitat de încercări.
Cum să folosești condiții multiple (if/elif/else) pentru a ghida jucătorul.

# Codul complet al jocului din capitolul 4

```python
viata = 10
aur = 0
inventar = ["sabie"]

print("Bun venit în aventura ta!")
print("Scrie 'exit' dacă vrei să închei jocul.")

while viata > 0:
    print("\nAi", viata, "viață și", aur, "aur.")
    print("Locuri disponibile: sat / pădure / peșteră")
    loc = input("Unde vrei să mergi? ")

    if loc == "exit":
        print("Ai ales să părăsești aventura.")
        break

    if loc == "sat":
        print("Te odihnești și recuperezi 2 viață.")
        viata += 2
    elif loc == "pădure":
        print("Ai găsit 3 aur, dar te-a zgâriat un lup (pierzi 1 viață).")
        aur += 3
        viata -= 1
    elif loc == "peșteră":
        if aur >= 5:
            print("Plătești 5 aur și găsești o poțiune magică.")
            inventar.append("poțiune magică")
            aur -= 5
        else:
            print("Peștera e periculoasă și pierzi 3 viață!")
            viata -= 3
    else:
        print("Nu știu locul acesta. Alege sat, pădure sau peșteră.")

print("\nJoc încheiat!")
print("Inventar final:", inventar)
print("Aur:", aur, "| Viață:", viata)

```