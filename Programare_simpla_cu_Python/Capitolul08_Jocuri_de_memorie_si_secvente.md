
# Capitolul 8 – Jocuri de memorie și secvențe

## De ce jocuri de memorie?

Jocurile de memorie sunt excelente pentru a exersa:

- Lucrul cu liste (eng. lists) – stocarea și compararea elementelor.
- Bucla principală – repetarea jocului cu creșterea dificultății.
- Funcții – separarea logicii pentru afișare, verificare și generare.

Un exemplu celebru este jocul „Simon Says", unde trebuie să repeți o secvență din ce în ce mai lungă.

## Ce vei învăța în acest capitol

- Cum să generezi secvențe aleatorii.
- Cum să folosești liste pentru a memora și verifica inputul jucătorului.
- Cum să creezi dificultate progresivă (secvența crește pe măsură ce joci).
- Cum să structurezi codul cu funcții clare: afișare, generare, verificare.

## Concepte noi explicate

### 1. Adăugarea elementelor într-o listă

O listă poate fi extinsă folosind metoda `.append()`:

```python
culori = []
culori.append("roșu")
culori.append("albastru")
print(culori)  # ['roșu', 'albastru']
```

### 2. Comparația listelor

În Python, două liste sunt egale dacă au aceleași elemente în aceeași ordine:

```python
corect = ["sus", "jos"]
raspuns = ["sus", "jos"]

if raspuns == corect:
    print("Ai ghicit!")
```

### 3. Generarea aleatoare dintr-o listă

Folosim `random.choice(lista)` pentru a alege un element aleatoriu:

```python
import random
directii = ["sus", "jos", "stânga", "dreapta"]
alegere = random.choice(directii)
print(alegere)  # exemplu: "stânga"
```

### 4. Creșterea dificultății

Pentru a face jocul mai greu pe parcurs, adăugăm câte un element nou în secvență la fiecare rundă.

## Jocul principal: Simon Says (versiune completă)

Vom construi jocul pas cu pas, folosind funcții:

### Pasul 1 – Generarea secvenței

```python
import random

directii = ["sus", "jos", "stânga", "dreapta"]
secventa = []

def adauga_directie(secventa):
    secventa.append(random.choice(directii))
```

### Pasul 2 – Afișarea secvenței

Pentru ca jucătorul să o memoreze, afișăm fiecare pas cu o scurtă pauză:
```python
import time

def afiseaza_secventa(secventa):
    print("\nMemorează secvența!")
    for pas in secventa:
        print(pas)
        time.sleep(0.7)  # pauză de 0,7 secunde între cuvinte
    print("\n" * 20)  # „curățăm” ecranul cu spații

```

### Pasul 3 – Verificarea răspunsului

Jucătorul scrie răspunsul sub formă de cuvinte separate prin spațiu:

```python
def verifica_raspuns(secventa):
    raspuns = input("Repetă secvența: ").lower().split()
    return raspuns == secventa
```

### Pasul 4 – Bucla principală

Ciclul se repetă:

1. Adăugăm o direcție.
2. Afișăm secvența.
3. Verificăm dacă jucătorul a răspuns corect.
4. Continuăm până greșește.

### Cod complet

```python
import random
import time

directii = ["sus", "jos", "stânga", "dreapta"]

def adauga_directie(secventa):
    secventa.append(random.choice(directii))

def afiseaza_secventa(secventa):
    print("\nMemorează secvența!")
    for pas in secventa:
        print(pas)
        time.sleep(0.7)
    print("\n" * 20)  # simulare „curățare” ecran

def verifica_raspuns(secventa):
    raspuns = input("Repetă secvența: ").lower().split()
    return raspuns == secventa

def joc_simon():
    print("Bine ai venit la jocul BONUS: Simon Says!")
    print("Repetă secvența de cuvinte exact cum apare.")
    print("Scrie cuvintele separate prin spațiu.")

    secventa = []
    scor = 0

    while True:
        adauga_directie(secventa)
        afiseaza_secventa(secventa)

        if verifica_raspuns(secventa):
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

## Exerciții pentru tine

- Schimbă direcțiile cu culori (roșu, verde, albastru, galben).
- Fă ca secvența să se afișeze mai repede după fiecare rundă (scurtează `time.sleep`).
- Adaugă un nivel de dificultate ales la început (ușor, mediu, greu) care să afecteze viteza sau lungimea inițială.
- Permite jucătorului să repornească jocul automat după ce greșește.

## Casetă explicativă: Cum să faci jocurile mai interesante

- Adaugă sunete sau efecte vizuale (chiar simple, ca „BEEP” sau simboluri speciale).
- Pune un sistem de scoruri maxime (high score).
- Combină jocul cu tematica aventurii din capitolele anterioare (ex.: „Simon te învață o vrajă, repetă pașii corect”).

