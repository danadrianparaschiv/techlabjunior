# Cum rulam/executam programele scrise in Python

Acest scurt ghid explica cum sa instalati interprtorul Pyhton impreuna cu librariile de baza ce va vor permite sa rulati exemplele din aceasta carte. Alegeti sectiunea in functie de sistemul de operare si urmati pasii descrisi in ghid.

## Scriem primul program

Creează un fișier numit **`salut.py`** cu conținutul:

```python
print("Salut, lume! Eu sunt un mic program Python.")
```

Îl vom rula la fiecare sistem de operare. 👇

---

## Windows: instalare și rulare

### 1) Instalează Python

1. Deschide browserul și caută „Download Python”. Intră pe site-ul oficial **python.org** (butonul mare „Download Python 3.x”).
2. Descarcă installerul pentru **Windows** (fișier `.exe`).
3. **Foarte important:** la primul ecran, bifează **„Add Python to PATH”**.
4. Apasă **Install Now** și așteaptă finalizarea.

### 2) Verifică instalarea

1. Deschide **Command Prompt** (caută „cmd” în Start).
2. Tastează una dintre variantele acestea (încearcă pe rând):

   ```bat
   python --version
   ```

   sau

   ```bat
   py --version
   ```

   Ar trebui să vezi ceva ca **Python 3.x.x**.

### 3) Rulează fișierul `salut.py`

* Dacă folosești **IDLE**: vezi secțiunea [Rularea dintr-un editor simplu](#rularea-dintr-un-editor-simplu).
* Dacă vrei din **Command Prompt**:

  1. Mergi în folderul unde ai `salut.py`, de exemplu:

     ```bat
     cd C:\Proiecte\python
     ```
  2. Rulează:

     ```bat
     py salut.py
     ```

     sau (pe unele sisteme)

     ```bat
     python salut.py
     ```

---

## Mac: instalare și rulare

> Pe multe Mac-uri există un Python vechi. Vrem **Python 3** nou.

### 1) Instalează Python 3

1. Mergi pe **python.org** și descarcă installerul pentru **macOS** (`.pkg`).
2. Deschide fișierul descărcat și urmează pașii (Next → Continue → Install).

### 2) Verifică instalarea

1. Deschide **Terminal** (Spotlight: `⌘` + `Space`, scrie „Terminal”).
2. Tastează:

   ```bash
   python3 --version
   ```

   Ar trebui să vezi **Python 3.x.x**.

### 3) Rulează fișierul `salut.py`

* Din **IDLE**: vezi [Rularea dintr-un editor simplu](#rularea-dintr-un-editor-simplu).
* Din **Terminal**:

  1. Mergi în folderul proiectului, ex.:

     ```bash
     cd ~/Documents/python
     ```
  2. Rulează:

     ```bash
     python3 salut.py
     ```

---

## Linux: instalare și rulare

> Multe distribuții (Ubuntu, Debian, Fedora etc.) au deja Python 3 instalat.

### 1) Verifică dacă ai Python 3

Deschide **Terminal** și scrie:

```bash
python3 --version
```

Dacă vezi o versiune 3.x, ești gata. Dacă **nu**, instalează:

* **Ubuntu/Debian**:

  ```bash
  sudo apt update
  sudo apt install -y python3 python3-pip
  ```
* **Fedora**:

  ```bash
  sudo dnf install -y python3 python3-pip
  ```

### 2) Rulează fișierul `salut.py`

1. Mergi în folderul fișierului:

   ```bash
   cd ~/Documents/python
   ```
2. Rulează:

   ```bash
   python3 salut.py
   ```

---

## Rularea dintr-un editor simplu

### Varianta A: **IDLE** (vine cu Python)

* **Windows/Mac**: după instalare, caută „**IDLE (Python 3.x)**”.
* **Pași:**

  1. Deschide IDLE.
  2. `File` → `New File`.
  3. Scrie codul (ex: `print("Salut!")`).
  4. Salvează ca `salut.py`.
  5. Apasă `F5` sau `Run` → `Run Module`.
  6. Vezi rezultatul în fereastra Shell.

### Varianta B: **Thonny** (editor prietenos pentru copii)

* Descarcă **Thonny** (căută „Thonny download”).
* Instalează (Windows/Mac/Linux).
* Deschide Thonny → scrie codul → `File` → `Save` → `Run` (butonul „Play”).

> Oricare variantă alegi, pașii sunt similari: **scrii**, **salvezi**, **Rulezi**.

---

## Rularea din Terminal/Command Prompt

### 1) Creează folderul proiectului

* Windows: `C:\Proiecte\python`
* Mac/Linux: `~/Documents/python`

### 2) Creează fișierul

Poți folosi un editor (IDLE/Thonny) sau chiar un editor simplu (Notepad/TextEdit în modul text simplu). Salvează ca **`salut.py`**.

### 3) Deschide Terminalul și mergi în folder

* **Windows (Command Prompt):**

  ```bat
  cd C:\Proiecte\python
  ```
* **Mac/Linux (Terminal):**

  ```bash
  cd ~/Documents/python
  ```

### 4) Rulează

* **Windows:**

  ```bat
  py salut.py
  ```

  sau

  ```bat
  python salut.py
  ```
* **Mac/Linux:**

  ```bash
  python3 salut.py
  ```

> Dacă vezi textul „Salut, lume!…”, ai reușit! 🎉

---

## Greșeli frecvente și cum le reparăm

* **Comanda nu există**

  * Mesaj: `python: command not found` sau `py is not recognized`.
  * Soluție: pe Windows reinstalează Python **bifând** „Add Python to PATH”. Pe Mac/Linux folosește `python3`.

* **Ești în folderul greșit**

  * Mesaj: `No such file or directory: salut.py`.
  * Soluție: verifică unde ai salvat fișierul și folosește `cd` până ajungi în folderul corect.

* **Ai salvat ca text, nu ca .py**

  * Asigură-te că numele chiar se termină cu `.py` (nu `salut.py.txt`).

* **Ghilimele greșite**

  * Folosește `"` sau `'` drepte: `print("Salut")`.

* **Spații/taste lipsă**

  * În Python, spațiile la începutul liniei contează (se numește *indentare*). Fii atent la aliniere.

---

## Mini-proiect: joculeț de ghicit numărul

Creează un fișier **`ghiceste.py`**:

```python
import random

numar_secret = random.randint(1, 20)
incercari = 0

print("Am ales un număr între 1 și 20. Îl poți ghici?")

while True:
    text = input("Scrie un număr: ")
    # transformăm textul în număr
    try:
        ghicire = int(text)
    except ValueError:
        print("Te rog un NUMĂR (ex: 7).")
        continue

    incercari += 1

    if ghicire < numar_secret:
        print("Prea mic! Încearcă mai mare.")
    elif ghicire > numar_secret:
        print("Prea mare! Încearcă mai mic.")
    else:
        print(f"Bravo! Ai ghicit în {incercari} încercări! 🎉")
        break
```

Rulează-l ca mai sus (IDLE/Thonny sau Terminal).
Dacă vrei, schimbă intervalul (`1, 20`) și mesajele ca să fie mai amuzante!