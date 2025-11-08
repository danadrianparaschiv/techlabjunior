
# 🐍 „Ups! Programul meu are un bug!” — Ghid vesel pentru micii programatori Python

Salut, tânăr explorator al lumii Python! 🧑‍💻  
Știi momentul acela când rulezi programul tău și... 💥 apare o eroare ciudată? Nu te speria! Se întâmplă și celor mai buni programatori.  
Acele greșeluțe se numesc **bug-uri** — adică mici „gândăcei” care se strecoară în codul nostru.  
Dar vestea bună e că putem învăța să-i prindem și să-i reparăm ușor!

Hai să vedem împreună cele mai **comune bug-uri** și cum le putem rezolva! 🪲⚙️

---

## 🧩 1. Greșeli de scriere (typos)

Uneori scriem ceva greșit fără să ne dăm seama:

```python
prit("Salut!")
````

➡️ Python va spune: `NameError: name 'prit' is not defined`

🔧 **Cum se rezolvă:** verifică atent literele! Ar fi trebuit să scriem:

```python
print("Salut!")
```

👉 Sfat: citește-ți codul cu voce tare sau lasă un mic spațiu de gândire între linii.

---

## 🪄 2. Uităm ghilimelele sau parantezele

Python e foarte atent la semnele de punctuație. Dacă uiți ceva, se supără:

```python
print("Salut!)
```

➡️ Eroare: `SyntaxError: EOL while scanning string literal`

🔧 **Rezolvare:** închide mereu ghilimelele și parantezele corect:

```python
print("Salut!")
```

👉 Poți număra: pentru fiecare `(` trebuie un `)`, iar pentru fiecare `"` trebuie alt `"`!

---

## 🧮 3. Încurcăm tipurile de date

Uneori vrem să adunăm lucruri care nu se potrivesc:

```python
numar = 5
text = "mere"
print(numar + text)
```

➡️ Eroare: `TypeError: unsupported operand type(s)`

🔧 **Rezolvare:** transformă tipurile ca să se potrivească:

```python
print(str(numar) + " " + text)
```

👉 Acum Python știe că vrem un text complet: `5 mere`.

---

## 🧱 4. Uităm indentarea (spațiile din fața liniilor)

Python iubește ordinea și spațiile corecte! Dacă uiți să pui spații în blocuri de cod:

```python
if True:
print("Bună!")
```

➡️ Eroare: `IndentationError: expected an indented block`

🔧 **Rezolvare:**

```python
if True:
    print("Bună!")
```

👉 Folosește **4 spații** sau tasta „Tab” pentru indentare.

---

## 🎯 5. Variabile nedeclarate sau scrise greșit

Dacă scrii:

```python
nume = "Ana"
print(nummee)
```

➡️ Eroare: `NameError: name 'nummee' is not defined`

🔧 **Rezolvare:** verifică ortografia! Variabilele trebuie să fie scrise identic:

```python
print(nume)
```

👉 Poți evita asta alegând nume simple și clare: `scor`, `jucator`, `mesaj`.

---

## 🔁 6. Probleme cu buclele

Dacă uiți să adaugi ceva care schimbă variabila în interiorul unei bucle, programul poate rula la infinit! 😱

```python
x = 0
while x < 5:
    print(x)
```

➡️ Programul nu se oprește, pentru că `x` nu crește niciodată!

🔧 **Rezolvare:**

```python
x = 0
while x < 5:
    print(x)
    x = x + 1
```

---

## 🧠 7. Uităm că Python face diferență între majuscule și minuscule

```python
Animal = "Pisică"
print(animal)
```

➡️ `NameError: name 'animal' is not defined`

🔧 **Rezolvare:** scrie mereu variabilele la fel:

```python
animal = "Pisică"
print(animal)
```

👉 În Python, `Animal` și `animal` sunt **două lucruri diferite**.

---

## 🧩 Exerciții practice: „Găsește bug-ul!”

Acum e rândul tău! Poți descoperi bug-urile din codurile de mai jos?
Citește cu atenție și încearcă să le corectezi.

---

### 🐞 Exercițiul 1

```python
print("Bun venit la cursul de Python!)
```

💭 Ce lipsește?

---

### 🐞 Exercițiul 2

```python
x = 10
if x > 5:
print("X e mare!")
```

💭 Ce trebuie adăugat?

---

### 🐞 Exercițiul 3

```python
numar = 7
text = "noroc"
print(numar + text)
```

💭 Cum poți face ca linia să funcționeze corect?

---

### 🐞 Exercițiul 4

```python
for i in range(3)
    print("Salut")
```

💭 Ce simbol lipsește după range(3)?

---

### 🐞 Exercițiul 5

```python
Scor = 100
print(scor)
```

💭 De ce spune Python că „scor” nu există?

---

## 🚀 Cum să devii „vânător de bug-uri” profesionist!

1. **Citește mesajul de eroare** – Python îți spune exact unde e problema.
2. **Folosește `print()`** ca să verifici valorile în timpul rulării.
3. **Testează pas cu pas** – rulează bucăți mici de cod.
4. **Nu te enerva!** Chiar și programatorii de la NASA greșesc. 🙂
5. **Notează greșelile** ca să le recunoști mai ușor data viitoare.

---

🎉 **Concluzie:**

Bug-urile sunt doar semne că înveți ceva nou!
Fiecare eroare e o lecție ascunsă care te face mai bun la programare.

Așa că data viitoare când vezi o eroare... zâmbește și spune:

> „Super! Am mai găsit un gândăcel de prins!” 🕵️‍♀️🐞