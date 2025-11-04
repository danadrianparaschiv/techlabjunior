# Capitolul 1 – Bun venit în lumea jocurilor text în Python

## De ce jocuri text?

Ai auzit vreodată de „Aventura Colossală" (*Colossal Cave Adventure*) sau „Zork"? Sunt printre primele jocuri pe computer și... surpriză! Erau doar text. Nu grafice, nu efecte 3D, doar cuvinte care te invitau să explorezi o lume imaginară:

> „Te afli într-o peșteră întunecoasă. În fața ta vezi o ușă grea. Ce faci?"

Și tu scriai răspunsul: „Deschid ușa" sau „Aprind o torță".

Asta e frumusețea jocurilor text: **folosesc imaginația ta** și sunt **super potrivite pentru a învăța programare**.

În această carte, vom învăța **Python** – un limbaj de programare foarte popular și prietenos cu începătorii – construind pas cu pas propriul nostru joc text.

## Ce vei învăța în acest capitol

- Cum să rulezi primul tău program în Python.
- Cum să afișezi mesaje pe ecran.
- Cum să ceri informații de la jucător și să răspunzi la ce introduce el.
- Ce este o **variabilă** (eng. *variable*) și de ce e importantă.
- Cum să îți faci primul mini-joc: **Salutul personalizat**.

## Să pornim la drum – Primul tău program

### 1. Instalează Python

Dacă nu ai Python instalat:

- Mergi pe site-ul oficial https://www.python.org
- Descarcă ultima versiune (3.x) pentru sistemul tău (Windows, Mac sau Linux).
- Instalează urmând pașii standard (bifează opțiunea „Add to PATH" dacă apare).

### 2. Creează primul fișier

- Deschide un editor simplu: **Notepad**, **VS Code** sau **Thonny**.
- Creează un fișier nou și salvează-l cu numele `primul_joc.py`.

### 3. Scrie primul tău cod

```python
print("Salut, aventurierule!")
```

Salvează fișierul și rulează-l:

- În terminal/command prompt tastează:

```bash
python primul_joc.py
```

Ar trebui să vezi pe ecran:

```
Salut, aventurierule!
```

**Felicitări! Tocmai ai scris primul tău program în Python!**

## Explicații – Ce am făcut aici?

### Instrucțiunea `print()`

Aceasta spune calculatorului: „Afișează asta pe ecran!".

Cuvântul „print" în engleză înseamnă „tipărește", dar în programare înseamnă „arată pe ecran".

### Textul dintre ghilimele

Se numește **șir de caractere** (eng. *string*). Practic, orice scris între ghilimele este text.

## Facem jocul interactiv

Jocurile nu ar fi amuzante dacă nu am putea răspunde, nu? Hai să cerem numele jucătorului:

```python
nume = input("Cum te cheamă, aventurierule? ")
print("Bine ai venit în lumea magică, " + nume + "!")
```

### Ce s-a întâmplat aici?

1. **`input()`** – O funcție care oprește programul și așteaptă ca jucătorul să scrie ceva.
2. **Variabila `nume`** – O **variabilă** (eng. *variable*) este ca o cutie unde stocăm informații. Aici am stocat numele introdus de jucător.
3. **Concatenarea textului** – Am unit două texte folosind semnul `+`.

## Primul mini-joc: Salutul personalizat

### Cod complet

```python
print("Salut, aventurierule!")

nume = input("Cum te cheamă, aventurierule? ")
print("Bine ai venit în lumea magică, " + nume + "!")

raspuns = input("Vrei să începi aventura? (da/nu) ")

if raspuns == "da":
    print("Minunat! O să fie o aventură de neuitat!")
else:
    print("Poate data viitoare!")
```

### Cum funcționează?

- Folosim **instrucțiunea condițională `if`** (eng. *if statement*) pentru a decide ce mesaj afișăm în funcție de răspuns.
- Dacă jucătorul scrie `da`, primim un mesaj de încurajare.
- Dacă scrie altceva, primim mesajul „Poate data viitoare!".

## Exerciții pentru tine

1. Schimbă mesajele jocului și fă-le mai amuzante (de exemplu: „Vrei să pornești spre castel?").
2. Adaugă o altă întrebare: „Ce armă alegi? Sabie sau arc?" și răspunde diferit în funcție de alegere.
3. Încearcă să faci jocul să repete întrebarea dacă utilizatorul scrie altceva decât „da" sau „nu".

## Ce urmează în capitolul 2

- Cum să lucrăm cu **numere** și **alegeri multiple**.
- Cum să facem primele noastre **decizii ramificate** – unde fiecare alegere schimbă povestea.
- Să începem să desenăm **harta aventurii** noastre.
