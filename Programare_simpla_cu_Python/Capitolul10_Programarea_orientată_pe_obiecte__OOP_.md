
# Capitolul 10 – Clase și obiecte: Aventurieri și monștri

## De ce avem nevoie de clase și obiecte?

Până acum am folosit variabile și dicționare pentru a ține datele jucătorului. Dar pe măsură ce jocul crește:

- Avem mai multe personaje (jucător, monștri, NPC-uri).
- Fiecare are proprietăți (viață, aur, atac) și acțiuni (atacă, vindecă).
- Repetăm codul pentru fiecare entitate.

Clasele ne ajută să:

- Grupăm datele și funcțiile într-un singur loc.
- Creăm obiecte multiple după același model (mai mulți monștri, mai mulți jucători).
- Facem jocul ușor de extins (adăugăm tipuri noi de monștri fără să rescriem codul).

## Ce este o clasă?

- O clasă este un „plan” (șablon) pentru a crea obiecte.
- Un obiect este o instanță a clasei, cu propriile date și comportamente.

## Cum definim o clasă simplă

```python
class Aventurier:
    def __init__(self, nume, viata, aur):
        self.nume = nume
        self.viata = viata
        self.aur = aur

    def salut(self):
        print(f"Salut, eu sunt {self.nume} cu {self.viata} viață și {self.aur} aur!")

```

### Explicație

- __init__ – metoda specială care se apelează automat când creăm un obiect.
- self – se referă la obiectul curent (obligatoriu în metode).
- nume, viata, aur – parametrii pe care îi trimitem la crearea obiectului.

## Crearea și folosirea unui obiect

```python
jucator = Aventurier("Eliza", 10, 5)
jucator.salut()
aldoileajucator = Aventurier("David", 8, 8)
aldoileajucator.salut()
```

## Adăugăm o clasă pentru monștri

```python
class Monstru:
    def __init__(self, nume, viata, atac):
        self.nume = nume
        self.viata = viata
        self.atac = atac

    def ataca(self, tinta):
        print(f"{self.nume} atacă pe {tinta.nume} și îi scade {self.atac} viață!")
        tinta.viata -= self.atac

```

## Simulăm o luptă simplă

```python
# Creăm jucătorul și monstrul
jucator = Aventurier("Eliza", 10, 5)
monstru = Monstru("Lupul întunecat", 6, 2)

# Lupta
jucator.salut()
monstru.ataca(jucator)
print(f"Viața lui {jucator.nume} este acum {jucator.viata}.")
```

## Extindem jocul de aventură cu OOP

- Jucătorul devine o clasă cu metode: muta(), colecteaza_obiect(), afiseaza_status().
- Monștrii devin clase cu proprietăți și atacuri diferite.
- Putem crea tipuri noi: monștri slabi, monștri de elită, șefi finali.

### Cod extins cu clase

```python
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
```


## Casetă bonus: Avantajele OOP în jocuri

Poți crea zeci de personaje rapid, fără să repeți codul.

- Poți extinde jocul: adaugi monștri, obiecte, arme, fără să rescrii logica de bază.
- Codul e mai organizat și ușor de întreținut.
- Într-o clasă, avem două tipuri principale de elemente:
    - Proprietăți (atribute) – informații despre obiect (de exemplu: viața jucătorului, aurul monstrului).
    - Metode – acțiuni pe care obiectul le poate face (de exemplu: atacă, vindecă, afișează statusul).

### Proprietăți (Atribute)

- Sunt variabile stocate în obiect.
- Se definesc de obicei în metoda __init__.
- Le accesăm cu self.nume_proprietate.
Exemplu:
```python
class Aventurier:
    def __init__(self, nume):
        self.nume = nume       # proprietate: numele jucătorului
        self.viata = 10        # proprietate: viața curentă
        self.aur = 0           # proprietate: aurul acumulat

```

Accesarea proprietăților:
```python
jucator = Aventurier("Eliza")
print(jucator.nume)   # Afișează: Eliza
print(jucator.viata)  # Afișează: 10

```

### Metode

- Sunt funcții definite într-o clasă.
- Se apelează folosind numele obiectului urmat de . și numele metodei.
- Pot folosi și modifica proprietățile obiectului.
- Parametrul self este mereu prezent – se referă la instanța curentă a clasei.

Exemplu:
```python
class Aventurier:
    def __init__(self, nume):
        self.nume = nume
        self.viata = 10
        self.aur = 0

    def afiseaza_status(self):
        print(f"{self.nume} – Viață: {self.viata}, Aur: {self.aur}")

    def colecteaza_aur(self, cantitate):
        self.aur += cantitate
        print(f"Ai colectat {cantitate} aur!")

```

Folosire:

```python
jucator = Aventurier("Eliza")
jucator.afiseaza_status()   # Afișează statusul curent
jucator.colecteaza_aur(5)   # Crește aurul cu 5
jucator.afiseaza_status()
```

- 
- ### Legătura dintre proprietăți și metode
- 
Proprietățile stochează datele despre obiect.
Metodele manipulează aceste date sau oferă informații despre ele.
Împreună fac obiectul complet – cu date (ce are) și comportamente (ce face).

## De ce sunt importante în jocul nostru?

În jocul de aventură:

- Jucătorul are proprietăți: nume, viață, aur, inventar.
- Jucătorul are metode: afiseaza_status(), colecteaza(), vindeca().
- Monstrul are proprietăți: nume, viață, atac.
- Monstrul are metode: ataca().

### Exemplu complet: Jucător și Monstru

```python
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

```

## Exerciții practice

- Creează un monstru nou (ex. „Goblin” cu 5 viață și 1 atac).
- Adaugă o metodă vindeca() pentru jucător, care crește viața când folosește o poțiune.
- Creează un șef final cu viață mare și atac puternic, care apare doar dacă ai o cheie magică.
- Adaugă o proprietate nouă „nivel” pentru jucător și crește-l când colectează suficient aur.
- Creează o metodă fugi() pentru jucător, care are o șansă aleatorie să evite un atac al monstrului.
- Adaugă o metodă raneste() la monștri, care scade viața lor când sunt atacați de jucător.

