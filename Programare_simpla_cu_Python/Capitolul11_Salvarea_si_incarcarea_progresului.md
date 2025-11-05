# Capitolul 11 – Salvarea și încărcarea progresului

## De ce să salvăm progresul jocului?

În jocurile mai lungi:

- Jucătorul explorează mai multe locații și adună obiecte.
- Nu e practic să reia totul de la zero la fiecare pornire.
- O funcție de Save/Load permite continuarea aventurii din același punct.

Vom folosi fișiere și modulul JSON pentru a salva datele jucătorului (viață, aur, inventar, locație).

## Lucrul cu fișiere în Python

Python oferă funcția `open()` pentru a lucra cu fișiere:

- `open("fisier.txt", "w")` – deschide pentru scriere (șterge conținutul existent).
- `open("fisier.txt", "r")` – deschide pentru citire.
- `open("fisier.txt", "a")` – deschide pentru adăugare (append).

### Instrucțiunea with

Forma recomandată este:
```python
with open("fisier.txt", "w") as f:
    f.write("Salut!")

```

Avantaje:

- Închide automat fișierul când blocul `with` se termină.
- Evită erorile dacă uiți să chemi `f.close()`.
- Cod mai curat și mai scurt.

## Ce este JSON?

JSON (JavaScript Object Notation) este un format simplu pentru salvarea datelor structurate:

- Poate stoca dicționare și liste (ca în Python).
- Este ușor de citit și folosit de multe aplicații (jocuri, web, API-uri).

Exemplu JSON:

```json
{
  "nume": "Eliza",
  "viata": 10,
  "aur": 5,
  "inventar": ["sabie", "poțiune"],
  "locatie": "sat"
}
```

## Modulul json în Python

Python are modulul integrat `json` care oferă funcții utile:

- `json.dump(obj, file)` – salvează obiectul Python în fișier ca JSON.
- `json.load(file)` – încarcă și convertește JSON-ul din fișier în obiect Python.
- `json.dumps(obj)` – returnează un șir JSON (nu scrie în fișier).
- `json.loads(text)` – convertește un șir JSON în obiect Python.

### Exemplu simplu cu dump și load

```python
import json

# Salvare (dump)
date = {"nume": "Eliza", "viata": 10}
with open("save.json", "w") as f:
    json.dump(date, f)

# Încărcare (load)
with open("save.json", "r") as f:
    date_incarcate = json.load(f)

print(date_incarcate)  # {'nume': 'Eliza', 'viata': 10}

```

## Funcții pentru Save și Load în joc

### Funcția de salvare

```python
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

```

### Funcția de încărcare

```python
def incarca_joc():
    try:
        with open("save.json", "r") as f:
            date_joc = json.load(f)
        print("Progres încărcat!")
        return date_joc
    except FileNotFoundError:
        print("Nu există un fișier de salvare.")
        return None

```

## Integrarea în joc

Când jucătorul vrea să salveze:

```python
salveaza_joc(jucator, locatie_curenta)
```

Când vrea să încarce:

```python
date = incarca_joc()
if date:
    jucator = Aventurier(date["nume"])
    jucator.viata = date["viata"]
    jucator.aur = date["aur"]
    jucator.inventar = date["inventar"]
    locatie_curenta = date["locatie"]
```

## Exerciții practice

- Adaugă salvarea misiunilor completate în fișierul JSON.
- Permite mai multe sloturi de salvare (save1.json, save2.json).
- Creează un meniu care întreabă: „Vrei să continui jocul salvat sau să începi unul nou?”.
- Încearcă să încarci manual fișierul JSON și să modifici valorile (ex.: aur mai mult).

## Casetă bonus: De ce e util JSON pentru jocuri

- Se pot salva structuri complexe (inventar, misiuni, hartă).
- Fișierele sunt compatibile cu alte programe – poți folosi aceleași date și în alt joc.
- Permite editare manuală (pentru debugging sau modding).
