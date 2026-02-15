# Capitolul 5: JavaScript — Pagina prinde viață! ⚡

> *„Orice idee suficient de bună poate fi exprimată prin cod."*
> — adaptat după Alan Kay

---

## Ce vei învăța în acest capitol

- Ce este JavaScript și de ce e **esențial** pentru web
- Cum să comunici cu browserul prin **`console.log()`**
- Ce sunt **variabilele** și cum stochezi informații
- **Tipurile de date**: text (string), numere (number), adevărat/fals (boolean)
- Cum să faci **calcule** și să combini texte
- **Template literals** — modul modern de a construi texte

---

## 5.1 De ce avem nevoie de JavaScript?

Până acum ai construit pagini web frumoase cu HTML și CSS. Dar încearcă ceva: apasă pe un buton de pe pagina ta. Se întâmplă ceva? Nu. Scrie ceva într-un câmp de text. Reacționează pagina? Nu.

Pagina ta este ca un **tablou frumos într-un muzeu** — poți să-l admiri, dar nu poți interacționa cu el.

**JavaScript** schimbă totul. Este limbajul care transformă tabloul într-un **joc video** — poți apăsa butoane, lucrurile se mișcă, pagina reacționează la ce faci tu.

```
  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │         FĂRĂ JavaScript          CU JavaScript              │
  │         ──────────────           ─────────────              │
  │                                                             │
  │   📄 Pagină statică         🎮 Pagină interactivă          │
  │                                                             │
  │   • Textul stă pe loc       • Butoanele funcționează       │
  │   • Imaginile nu se mișcă   • Jocuri se pot juca           │
  │   • Butoanele nu fac nimic  • Formularele verifică datele  │
  │   • Zero reacție la click   • Animații la scroll            │
  │                              • Mesaje pop-up                │
  │   Ca o carte tipărită       • Conținut care se schimbă     │
  │                                                             │
  │                              Ca o aplicație pe telefon      │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘
```

Reamintire din Capitolul 1:

- **HTML** = scheletul (ce există)
- **CSS** = hainele (cum arată)
- **JavaScript** = creierul și mușchii (ce face, cum reacționează)

---

## 5.2 Unde scrii JavaScript?

La fel ca la CSS, ai mai multe opțiuni. Și la fel ca la CSS, una este clar cea mai bună.

### Metoda 1: Intern — tag `<script>` în HTML

```html
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <title>Primul meu JavaScript</title>
</head>
<body>
    <h1>Salut!</h1>

    <script>
        // Codul JavaScript se scrie aici
        console.log("JavaScript funcționează!");
    </script>
</body>
</html>
```

> ⚠️ **Atenție!**
> Tag-ul `<script>` se pune la **sfârșitul lui `<body>`**, chiar înainte de `</body>`. De ce? Pentru că browserul citește pagina de sus în jos. Dacă pui JavaScript în `<head>`, el va încerca să manipuleze elemente HTML care **nu există încă** (nu au fost citite). Pune-l la final și totul va funcționa.

### Metoda 2: Extern — fișier `.js` separat ⭐

**Aceasta este metoda profesională** (la fel ca CSS extern).

**Pasul 1:** Creează fișierul `script.js`:

```javascript
// Codul JavaScript se scrie aici
console.log("JavaScript funcționează!");
```

**Pasul 2:** Conectează-l la HTML:

```html
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <title>Primul meu JavaScript</title>
    <link rel="stylesheet" href="stil.css">
</head>
<body>
    <h1>Salut!</h1>

    <script src="script.js"></script>
</body>
</html>
```

Structura folderului:

```
  📁 proiectul-meu/
  ├── index.html
  ├── stil.css          ← stilurile (CSS)
  └── script.js         ← comportamentul (JavaScript)
```

De acum încolo, vom folosi mereu **fișier extern**. Cele trei fișiere — `index.html`, `stil.css`, `script.js` — sunt echipa de bază a oricărui proiect web.

---

## 5.3 `console.log()` — Walkie-talkie-ul tău cu browserul 📻

Primul instrument pe care trebuie să-l înveți se numește `console.log()`. Este **cel mai important instrument de debugging** (depanare) din JavaScript.

### Ce este consola?

Consola este un panou **ascuns** în browser unde JavaScript poate afișa mesaje. Este ca un walkie-talkie: tu trimiți mesaje din cod, iar consola le primește și le afișează.

```
  Codul tău                      Consola browserului
  ┌──────────────────┐           ┌──────────────────────┐
  │                  │           │                      │
  │  console.log(    │ ═══════► │  Salut, lume!        │
  │    "Salut, lume!"│           │                      │
  │  );              │           │                      │
  │                  │           │                      │
  └──────────────────┘           └──────────────────────┘
       script.js                      DevTools → Console
```

### Cum deschizi consola

1. Deschide pagina ta în Chrome
2. Apasă **`F12`** (sau `Ctrl + Shift + J`)
3. Click pe tab-ul **Console**
4. Aici vor apărea mesajele tale!

### Primele tale mesaje

Scrie în `script.js`:

```javascript
console.log("Salut, lume!");
console.log("Acesta este primul meu program JavaScript!");
console.log("Am 12 ani și învăț programare.");
```

Salvează, reîncarcă pagina, și uită-te în consolă. Vei vedea:

```
  Salut, lume!
  Acesta este primul meu program JavaScript!
  Am 12 ani și învăț programare.
```

### Consola poate afișa orice

```javascript
console.log("Text simplu");
console.log(42);
console.log(3.14);
console.log(true);
console.log(10 + 5);
console.log("Răspunsul este:", 6 * 7);
```

Rezultat în consolă:

```
  Text simplu
  42
  3.14
  true
  15
  Răspunsul este: 42
```

> 💡 **Sfat!**
> Poți scrie JavaScript direct în consolă! Deschide DevTools (F12), mergi la tab-ul Console, scrie `2 + 2` și apasă Enter. Consola va răspunde `4`. Este ca un calculator super-inteligent. Experimentează!

> 🚀 **Provocare!**
> Deschide consola și încearcă:
> - `100 * 365` (câte zile sunt în 100 de ani?)
> - `"Salut" + " " + "lume"` (ce se întâmplă când „aduni" texte?)
> - `2 ** 10` (2 la puterea 10 — câte valori poate stoca un computer cu 10 biți?)

---

## 5.4 Variabile — Cutii cu etichete 📦

Imaginează-ți că ai mai multe **cutii** și pe fiecare lipești o **etichetă** cu un nume. Poți pune orice înăuntru, iar când ai nevoie de conținut, cauți cutia după etichetă.

**Exact asta e o variabilă** — o cutie cu etichetă în care stochezi o informație.

```
  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
  │   "Maria"   │  │     14      │  │   "Iași"     │
  │             │  │             │  │             │
  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
         │               │               │
    ┌────┴────┐     ┌────┴────┐     ┌────┴────┐
    │  nume   │     │ varsta  │     │  oras   │
    └─────────┘     └─────────┘     └─────────┘
     eticheta        eticheta        eticheta
```

### Cum creezi o variabilă

Folosești cuvântul magic **`let`**:

```javascript
let nume = "Maria";
let varsta = 14;
let oras = "Iași";

console.log(nume);      // Maria
console.log(varsta);    // 14
console.log(oras);      // Iași
```

Descompunere:

```
  let   nume   =   "Maria"  ;
  ───   ────   ─   ───────  ─
   │      │    │      │     │
   │      │    │      │     └── punct și virgulă (finalul instrucțiunii)
   │      │    │      │
   │      │    │      └── valoarea (ce pui în cutie)
   │      │    │
   │      │    └── operatorul de atribuire ("pune în cutie")
   │      │
   │      └── numele variabilei (eticheta cutiei)
   │
   └── cuvântul cheie ("creează o cutie nouă")
```

### `let` vs `const` — Cutii reutilizabile și cutii sigilate

JavaScript are două moduri principale de a crea variabile:

**`let`** = cutie **reutilizabilă** — poți schimba conținutul oricând:

```javascript
let scor = 0;
console.log(scor);    // 0

scor = 10;            // schimb conținutul cutiei
console.log(scor);    // 10

scor = scor + 5;      // adaug 5 la valoarea existentă
console.log(scor);    // 15
```

**`const`** = cutie **sigilată** — odată pusă valoarea, nu o mai poți schimba:

```javascript
const PI = 3.14159;
console.log(PI);      // 3.14159

PI = 3;               // ❌ EROARE! Nu poți schimba o constantă!
// TypeError: Assignment to constant variable.
```

```
  let                              const
  ───                              ─────
  ┌─────────────┐                  ┌═════════════╗
  │   valoare   │  ← poți         ║   valoare   ║  ← NU poți
  │   veche     │    schimba      ║   fixă      ║    schimba!
  └──────┬──────┘                  ╚══════╤══════╝
         │                                │
    ┌────┴────┐                      ┌────┴────┐
    │  scor   │                      │   PI    │
    └─────────┘                      └─────────┘
   cutie normală                    cutie sigilată
```

### Când folosești fiecare?

| Tip | Când | Exemple |
|---|---|---|
| **`const`** | Valoarea **nu se va schimba** niciodată | `const PI = 3.14`, `const TAXA = 0.19` |
| **`let`** | Valoarea **se poate schimba** pe parcurs | `let scor = 0`, `let nivel = 1` |

> 💡 **Sfat de profesionist!**
> Programatorii buni folosesc `const` implicit și trec la `let` doar când e nevoie. Regula: **folosește `const` până când ai un motiv să folosești `let`**. Asta face codul mai sigur și mai ușor de înțeles.

### Reguli pentru numele variabilelor

Nu orice text poate fi un nume de variabilă. Iată regulile:

```javascript
// ✅ CORECT
let nume = "Maria";
let varsta = 14;
let culoarePreferata = "albastru";     // camelCase — recomandat!
let numar_elevi = 30;                  // cu underscore — ok
let _secret = "ascuns";               // începe cu _ — ok
let $pret = 99;                        // începe cu $ — ok

// ❌ GREȘIT
let 2cool = "nu merge";               // nu poate începe cu cifră!
let numele meu = "Maria";             // nu poate conține spații!
let let = "confuz";                    // nu poate fi un cuvânt rezervat!
let culoare-preferată = "albastru";    // nu poate conține - sau ă/î/ș/ț!
```

### camelCase — Convenția programatorilor

Când numele unei variabile are mai multe cuvinte, programatorii JavaScript folosesc **camelCase**: primul cuvânt e cu literă mică, fiecare cuvânt următor începe cu MAJUSCULĂ.

```javascript
let culoarePreferata = "albastru";     // culoare + Preferata
let numarDeElevi = 30;                 // numar + De + Elevi
let esteLogat = true;                  // este + Logat
let scorMaximPosibil = 100;            // scor + Maxim + Posibil
```

Se numește **camelCase** pentru că majusculele din mijloc arată ca **cocoașele unei cămile** 🐫.

```
  scorMaximPosibil
       ▲       ▲
       │       │
       cocoașe de cămilă!
```

---

## 5.5 Tipuri de date — Ce poți pune în cutie?

Nu toate informațiile sunt la fel. Un nume e diferit de un număr, care e diferit de un răspuns da/nu. JavaScript recunoaște mai multe **tipuri de date**.

Cele trei tipuri fundamentale:

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         │
  │  📝 STRING (text)        🔢 NUMBER (număr)              │
  │  ─────────────────       ──────────────────             │
  │                                                         │
  │  "Salut!"                42                             │
  │  "Maria"                 3.14                           │
  │  "Iași"                  -7                             │
  │  ""  (text gol)          0                              │
  │                                                         │
  │  Mereu între             Fără ghilimele.                │
  │  ghilimele!              Poate fi întreg                │
  │  "..." sau '...'        sau zecimal.                   │
  │                                                         │
  │                                                         │
  │  🔘 BOOLEAN (adevărat/fals)                            │
  │  ────────────────────────────                           │
  │                                                         │
  │  true     (adevărat / da / pornit)                     │
  │  false    (fals / nu / oprit)                          │
  │                                                         │
  │  Doar două valori posibile!                            │
  │  Ca un întrerupător: ON sau OFF.                        │
  │                                                         │
  └─────────────────────────────────────────────────────────┘
```

### String (text) — Cuvinte și propoziții

Un string este orice text, scris între **ghilimele**:

```javascript
const prenume = "Maria";           // ghilimele duble — cel mai comun
const familie = 'Popescu';          // ghilimele simple — la fel de ok
const mesaj = "Salut, lume!";
const gol = "";                     // string gol (text fără conținut)

console.log(prenume);    // Maria
console.log(mesaj);      // Salut, lume!
```

Ghilimelele simple și duble funcționează la fel. Alege un stil și fii **consistent**. Majoritatea programatorilor JavaScript preferă ghilimelele duble (`"..."`).

Ce faci când textul conține ghilimele?

```javascript
// Problemă: apostroful „rupe" stringul
// let text = 'Asta e Maria's carte';   ← ❌ EROARE!

// Soluția 1: folosește celălalt tip de ghilimele
let text1 = "Asta e Maria's carte";     // ✅ dublu în exterior

// Soluția 2: „scapă" caracterul cu backslash
let text2 = 'Asta e Maria\'s carte';    // ✅ \' = apostrof literal
```

### Number (număr) — Calcule și cantități

Numerele **nu** au ghilimele:

```javascript
const varsta = 14;
const temperatura = -5;
const pi = 3.14159;
const miliard = 1000000000;

console.log(varsta);        // 14
console.log(pi);            // 3.14159
```

> ⚠️ **Atenție!**
> `"42"` și `42` sunt **complet diferite**!
> - `"42"` este un **string** (text care arată ca un număr)
> - `42` este un **number** (un număr cu adevărat)
>
> ```javascript
> console.log("42" + 8);    // "428" — a lipit textele!
> console.log(42 + 8);      // 50   — a calculat suma!
> ```
>
> Ghilimelele fac toată diferența!

### Boolean (adevărat / fals) — Întrerupătorul

Un boolean este cel mai simplu tip de dată: are doar două valori posibile.

```javascript
const esteSoare = true;
const plouaAfara = false;
const amTerminatTema = true;

console.log(esteSoare);         // true
console.log(plouaAfara);        // false
```

Gândește-te la un boolean ca la un **întrerupător de lumină**: e fie pornit (`true`), fie oprit (`false`). Nu există „pe jumătate".

```
  true                    false
  ┌─────────┐            ┌─────────┐
  │  ┌───┐  │            │         │
  │  │ ● │  │ PORNIT     │         │ OPRIT
  │  │   │  │            │  ┌───┐  │
  │  └───┘  │            │  │ ○ │  │
  └─────────┘            │  └───┘  │
                         └─────────┘
```

Booleanele vor deveni **esențiale** în capitolul următor când vom învăța `if/else` (decizii).

### `typeof` — Întreabă JavaScript „Ce tip e asta?"

```javascript
console.log(typeof "Maria");     // "string"
console.log(typeof 42);          // "number"
console.log(typeof true);        // "boolean"
console.log(typeof 3.14);       // "number"
```

### Două valori speciale: `undefined` și `null`

```javascript
let ceva;                        // declarată dar fără valoare
console.log(ceva);               // undefined — "nu i-ai dat nimic"

let cutieGoala = null;           // intenționat goală
console.log(cutieGoala);         // null — "am decis să fie goală"
```

Diferența: `undefined` = ai uitat să pui ceva în cutie. `null` = ai decis **în mod intenționat** că cutia e goală.

```
  undefined                     null
  ┌─────────────┐              ┌─────────────┐
  │      ?      │              │             │
  │   (uitat)   │              │  (intenționat│
  │             │              │    goală)   │
  └──────┬──────┘              └──────┬──────┘
    ┌────┴────┐                 ┌────┴────┐
    │  ceva   │                 │cutieGoala│
    └─────────┘                 └─────────┘
```

---

## 5.6 Operatori aritmetici — JavaScript, calculatorul suprem 🧮

JavaScript poate face orice calcul matematic:

```javascript
console.log(10 + 3);      // 13  — adunare
console.log(10 - 3);      // 7   — scădere
console.log(10 * 3);      // 30  — înmulțire
console.log(10 / 3);      // 3.333... — împărțire
console.log(10 % 3);      // 1   — rest (modulo)
console.log(10 ** 3);     // 1000 — ridicare la putere (10³)
```

| Operator | Operație | Exemplu | Rezultat |
|---|---|---|---|
| `+` | Adunare | `7 + 3` | `10` |
| `-` | Scădere | `7 - 3` | `4` |
| `*` | Înmulțire | `7 * 3` | `21` |
| `/` | Împărțire | `7 / 2` | `3.5` |
| `%` | Rest (modulo) | `7 % 3` | `1` |
| `**` | Putere | `2 ** 8` | `256` |

### Operatorul modulo (`%`) — Ce rămâne după împărțire

Acesta e mai puțin intuitiv dar foarte util:

```javascript
console.log(10 % 3);     // 1    (10 ÷ 3 = 3 rest 1)
console.log(15 % 5);     // 0    (15 ÷ 5 = 3 rest 0)
console.log(7 % 2);      // 1    (7 ÷ 2 = 3 rest 1)
console.log(8 % 2);      // 0    (8 ÷ 2 = 4 rest 0)
```

La ce e util? La a verifica dacă un număr e **par sau impar**:

```javascript
// Dacă restul împărțirii la 2 este 0 → numărul e par
console.log(10 % 2);     // 0 → par
console.log(7 % 2);      // 1 → impar
```

### Calcule cu variabile

```javascript
let pret = 50;
let cantitate = 3;
let total = pret * cantitate;

console.log(total);       // 150

// Adaugăm TVA (19%)
const TVA = 0.19;
let totalCuTVA = total + (total * TVA);

console.log(totalCuTVA);  // 178.5
```

### Scurtături utile

```javascript
let scor = 10;

scor = scor + 5;         // varianta lungă: 15
scor += 5;               // varianta scurtă: 20 (la fel ca cea de sus)

scor -= 3;               // scor = scor - 3 → 17
scor *= 2;               // scor = scor * 2 → 34

// Cel mai comun: incrementare / decrementare cu 1
let vieti = 3;
vieti++;                  // vieti = vieti + 1 → 4
vieti--;                  // vieti = vieti - 1 → 3
```

| Scurtătură | Înseamnă | Exemplu (dacă `x = 10`) |
|---|---|---|
| `x += 5` | `x = x + 5` | `x` devine `15` |
| `x -= 3` | `x = x - 3` | `x` devine `7` |
| `x *= 2` | `x = x * 2` | `x` devine `20` |
| `x /= 4` | `x = x / 4` | `x` devine `2.5` |
| `x++` | `x = x + 1` | `x` devine `11` |
| `x--` | `x = x - 1` | `x` devine `9` |

### Ordinea operațiilor

JavaScript respectă aceleași reguli din matematică:

```javascript
console.log(2 + 3 * 4);       // 14  (nu 20! — înmulțirea se face prima)
console.log((2 + 3) * 4);     // 20  (parantezele schimbă ordinea)
```

**PEMDAS** — Paranteze, Exponenți, Multiplicare/Divizare, Adunare/Scădere:

```
  Prioritate:
  1. ( )    Paranteze         — prima!
  2. **     Exponenți
  3. * / %  Înmulțire, împărțire, modulo
  4. + -    Adunare, scădere  — ultima!
```

---

## 5.7 Operații cu string-uri — Jocuri de cuvinte

### Concatenarea — Lipirea textelor

Operatorul `+` funcționează diferit pentru texte — le **lipește** (concatenează):

```javascript
let prenume = "Maria";
let familie = "Popescu";

let numeComplet = prenume + " " + familie;
console.log(numeComplet);    // "Maria Popescu"
```

```
  "Maria"  +  " "  +  "Popescu"
  ───────     ───     ─────────
     │         │          │
     └────┬────┘          │
          │               │
      "Maria "   +   "Popescu"
      ────────        ─────────
          │               │
          └───────┬───────┘
                  │
           "Maria Popescu"
```

Mai multe exemple:

```javascript
let salut = "Salut, " + "lume!";
console.log(salut);                    // "Salut, lume!"

let varsta = 14;
let mesaj = "Am " + varsta + " ani.";
console.log(mesaj);                    // "Am 14 ani."
```

Când „aduni" un text cu un număr, JavaScript transformă totul în text:

```javascript
console.log("Scorul: " + 100);        // "Scorul: 100" (text!)
console.log("5" + 3);                 // "53" (text! nu 8!)
console.log(5 + 3);                   // 8 (număr!)
```

> ⚠️ **Atenție!**
> `"5" + 3` dă `"53"`, nu `8`! Dacă **oricare** operand e string, `+` devine lipire, nu adunare. Este una dintre cele mai comune surse de bug-uri în JavaScript!

### Lungimea unui string: `.length`

```javascript
let cuvant = "JavaScript";
console.log(cuvant.length);    // 10 (are 10 caractere)

let gol = "";
console.log(gol.length);      // 0

let propozitie = "Salut, lume!";
console.log(propozitie.length); // 12 (spațiile și ! se numără)
```

### Accesarea caracterelor

Fiecare caracter dintr-un string are un **index** (poziție). Atenție: numerotarea începe de la **0**, nu de la 1!

```
  Cuvântul:  "JavaScript"
  Index:      0123456789
              │         │
              J         t
              (primul)  (ultimul)
```

```javascript
let limbaj = "JavaScript";

console.log(limbaj[0]);       // "J"  (primul caracter)
console.log(limbaj[1]);       // "a"  (al doilea)
console.log(limbaj[4]);       // "S"
console.log(limbaj[9]);       // "t"  (ultimul)
```

> 💡 **Știai că?**
> De ce numărăm de la 0? Este o convenție din anii '60, legată de cum funcționează memoria computerului. Indexul reprezintă **distanța** de la început: primul element e la distanță 0 de start. Este contraintuitiv la început, dar te vei obișnui rapid — toți programatorii numără de la 0!

### Metode utile pentru string-uri

JavaScript oferă funcții gata făcute pentru a manipula textul:

```javascript
let text = "Salut, Lume!";

// Transformări de caz
console.log(text.toUpperCase());     // "SALUT, LUME!"
console.log(text.toLowerCase());     // "salut, lume!"

// Căutare
console.log(text.includes("Lume")); // true (conține "Lume"?)
console.log(text.includes("xyz"));  // false

// Înlocuire
console.log(text.replace("Lume", "România"));  // "Salut, România!"

// Extragere
console.log(text.slice(0, 5));      // "Salut" (de la 0, 5 caractere)
console.log(text.slice(7));         // "Lume!" (de la indexul 7 până la final)

// Eliminare spații de la capete
let dezordonat = "   text cu spații   ";
console.log(dezordonat.trim());     // "text cu spații"
```

| Metodă | Ce face | Exemplu | Rezultat |
|---|---|---|---|
| `.toUpperCase()` | Totul MAJUSCUL | `"abc".toUpperCase()` | `"ABC"` |
| `.toLowerCase()` | Totul minuscul | `"ABC".toLowerCase()` | `"abc"` |
| `.includes(x)` | Conține x? | `"Salut".includes("lu")` | `true` |
| `.replace(a, b)` | Înlocuiește a cu b | `"da".replace("da", "nu")` | `"nu"` |
| `.slice(start, end)` | Extrage o porțiune | `"ABCDE".slice(1, 4)` | `"BCD"` |
| `.trim()` | Elimină spații | `" ab ".trim()` | `"ab"` |
| `.length` | Lungimea textului | `"Salut".length` | `5` |

---

## 5.8 Template Literals — Modul modern de a construi texte ✨

Concatenarea cu `+` merge, dar devine complicată rapid:

```javascript
let nume = "Maria";
let varsta = 14;
let oras = "Iași";

// Cu concatenare (+) — greu de citit
let mesaj = "Salut! Mă numesc " + nume + ", am " + varsta + " ani și locuiesc în " + oras + ".";
```

Toate acele `+`, `" "` și ghilimele sunt confuze. Există un mod **mult mai elegant**: **template literals**.

### Cum funcționează

Folosești **backtick-uri** (`` ` ``) în loc de ghilimele, iar variabilele le pui în `${ }`:

```javascript
let nume = "Maria";
let varsta = 14;
let oras = "Iași";

// Cu template literal — clar și curat!
let mesaj = `Salut! Mă numesc ${nume}, am ${varsta} ani și locuiesc în ${oras}.`;
console.log(mesaj);
// "Salut! Mă numesc Maria, am 14 ani și locuiesc în Iași."
```

```
  Backtick-uri: `...`     (tasta de sub Esc pe tastatură)
  
  `Salut, ${nume}! Ai ${varsta} ani.`
            ──────       ────────
               │             │
         se înlocuiește  se înlocuiește
         cu valoarea     cu valoarea
         variabilei      variabilei
```

> 💡 **Sfat!**
> Tasta **backtick** ( `` ` `` ) se găsește de obicei sub tasta `Esc` sau lângă tasta `1`, în stânga sus pe tastatură. Pe tastaturile românești, poate fi accesibilă cu `AltGr + 7` sau o combinație similară.

### Poți pune orice expresie în `${ }`

```javascript
let pret = 50;
let cantitate = 3;

console.log(`Total: ${pret * cantitate} lei`);
// "Total: 150 lei"

console.log(`Este ieftin? ${pret < 100}`);
// "Este ieftin? true"

let nume = "maria";
console.log(`Nume cu majusculă: ${nume[0].toUpperCase() + nume.slice(1)}`);
// "Nume cu majusculă: Maria"
```

### Template literals pe mai multe linii

Un alt avantaj uriaș — poți scrie pe **mai multe linii** fără `\n` sau concatenare:

```javascript
// Cu ghilimele normale — complicat
let card1 = "Nume: Maria\nVârstă: 14\nOraș: Iași";

// Cu template literal — natural și curat
let card2 = `
Nume: Maria
Vârstă: 14
Oraș: Iași
`;

console.log(card2);
// Nume: Maria
// Vârstă: 14
// Oraș: Iași
```

> 🚀 **Provocare!**
> Creează variabile pentru: numele tău, vârsta ta, culoarea preferată, hobby-ul preferat și mâncarea preferată. Apoi afișează un mesaj în consolă folosind template literals care le combină pe toate într-o propoziție frumoasă. De exemplu:
> `"Salut! Sunt Ana, am 12 ani, ador culoarea turcoaz, îmi place să desenez și nu pot trăi fără pizza!"`

---

## 5.9 Comentarii JavaScript — Note pentru tine din viitor

La fel ca în HTML și CSS, poți lăsa note în codul JavaScript:

```javascript
// Aceasta este un comentariu pe o singură linie

/* 
   Aceasta este un comentariu
   pe mai multe linii.
   Util pentru explicații mai lungi.
*/

let scor = 0;    // comentariu la sfârșitul unei linii de cod

// Comentariile sunt ignorate de browser — sunt doar pentru tine!
```

Când folosești comentarii:
- **Explică DE CE** faci ceva (nu CE faci — codul arată deja asta)
- **Organizează** codul pe secțiuni
- **Dezactivează** temporar cod fără a-l șterge

```javascript
// ── VARIABILE JUCĂTOR ──
let numeJucator = "Ana";
let vieti = 3;
let scor = 0;

// ── VARIABILE JOC ──
let nivel = 1;
let esteActiv = true;

// Calculează scorul bonus (x2 dacă nu a pierdut nicio viață)
let scorBonus = vieti === 3 ? scor * 2 : scor;
```

Diferențele de sintaxă între cele trei limbaje:

| Limbaj | Comentariu pe o linie | Comentariu pe mai multe linii |
|---|---|---|
| **HTML** | — | `<!-- comentariu -->` |
| **CSS** | — | `/* comentariu */` |
| **JavaScript** | `// comentariu` | `/* comentariu */` |

---

## 5.10 Proiect practic: Profil de jucător în consolă 🚀

Hai să punem totul cap la cap și să creăm un „profil de jucător" complet, afișat în consolă.

Creează structura:

```
  📁 profil-jucator/
  ├── index.html
  └── script.js
```

### HTML (`index.html`):

```html
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profil Jucător</title>
</head>
<body>
    <h1>Deschide consola (F12) pentru a vedea profilul! 🎮</h1>
    <p>Apasă F12, apoi click pe tab-ul "Console".</p>

    <script src="script.js"></script>
</body>
</html>
```

### JavaScript (`script.js`):

```javascript
// ══════════════════════════════════════
// PROFILUL MEU DE JUCĂTOR
// ══════════════════════════════════════

// ── Date personale ──
const numeJucator = "CyberWolf_42";
const varsta = 13;
const orasul = "Cluj-Napoca";
const esteOnline = true;

// ── Statistici joc ──
let nivel = 15;
let experienta = 7800;
let expPentruNivelUrmator = 10000;
let vieti = 3;
let monede = 2450;

// ── Inventar ──
const arma = "Sabia Luminii";
const armura = "Scutul de Cristal";
const companionul = "Dragonul Spark";

// ══════════════════════════════════════
// CALCULE
// ══════════════════════════════════════

// Cât mai e până la nivelul următor?
let expRamasa = expPentruNivelUrmator - experienta;
let procentComplet = Math.round((experienta / expPentruNivelUrmator) * 100);

// Bara de progres vizuală (din caractere)
let baraPlin = "█".repeat(Math.round(procentComplet / 5));
let baraGol = "░".repeat(20 - Math.round(procentComplet / 5));
let baraProgres = baraPlin + baraGol;

// ══════════════════════════════════════
// AFIȘARE ÎN CONSOLĂ
// ══════════════════════════════════════

console.log("╔══════════════════════════════════════╗");
console.log("║       🎮 PROFIL JUCĂTOR 🎮           ║");
console.log("╚══════════════════════════════════════╝");
console.log("");

console.log(`  👤 Nume:    ${numeJucator}`);
console.log(`  🎂 Vârstă:  ${varsta} ani`);
console.log(`  📍 Oraș:    ${orasul}`);
console.log(`  🟢 Status:  ${esteOnline ? "ONLINE" : "OFFLINE"}`);
console.log("");

console.log("── Statistici ──────────────────────────");
console.log(`  ⭐ Nivel:       ${nivel}`);
console.log(`  📊 Experiență:  ${experienta} / ${expPentruNivelUrmator}`);
console.log(`  📈 Progres:     [${baraProgres}] ${procentComplet}%`);
console.log(`  ❤️  Vieți:       ${"♥".repeat(vieti)}${"♡".repeat(5 - vieti)}`);
console.log(`  💰 Monede:      ${monede}`);
console.log("");

console.log("── Inventar ────────────────────────────");
console.log(`  ⚔️  Armă:       ${arma}`);
console.log(`  🛡️  Armură:     ${armura}`);
console.log(`  🐉 Companion:  ${companionul}`);
console.log("");

// ── Simulare: câștigă experiență ──
console.log("── Simulare luptă ──────────────────────");

let expCastigata = 350;
experienta += expCastigata;
monede += 120;

console.log(`  ⚔️  Ai câștigat o luptă!`);
console.log(`  +${expCastigata} EXP | +120 monede`);
console.log(`  📊 Experiență nouă: ${experienta} / ${expPentruNivelUrmator}`);
console.log(`  💰 Monede noi: ${monede}`);

// Verificăm dacă am avansat de nivel
if (experienta >= expPentruNivelUrmator) {
    nivel++;
    experienta -= expPentruNivelUrmator;
    console.log(`  🎉 LEVEL UP! Acum ești nivel ${nivel}!`);
} else {
    let ramasa = expPentruNivelUrmator - experienta;
    console.log(`  📈 Mai ai nevoie de ${ramasa} EXP pentru nivelul ${nivel + 1}`);
}

console.log("");
console.log("═══════════════════════════════════════");
console.log("  Creat cu ❤️ — Constructorul de Site-uri, Cap. 5");
console.log("═══════════════════════════════════════");
```

Deschide `index.html` în browser, apoi apasă `F12` → Console. Vei vedea ceva de genul:

```
  ╔══════════════════════════════════════╗
  ║       🎮 PROFIL JUCĂTOR 🎮           ║
  ╚══════════════════════════════════════╝
  
    👤 Nume:    CyberWolf_42
    🎂 Vârstă:  13 ani
    📍 Oraș:    Cluj-Napoca
    🟢 Status:  ONLINE
  
  ── Statistici ──────────────────────────
    ⭐ Nivel:       15
    📊 Experiență:  7800 / 10000
    📈 Progres:     [████████████████░░░░] 78%
    ❤️  Vieți:       ♥♥♥♡♡
    💰 Monede:      2450
  
  ── Inventar ────────────────────────────
    ⚔️  Armă:       Sabia Luminii
    🛡️  Armură:     Scutul de Cristal
    🐉 Companion:  Dragonul Spark
  
  ── Simulare luptă ──────────────────────
    ⚔️  Ai câștigat o luptă!
    +350 EXP | +120 monede
    📊 Experiență nouă: 8150 / 10000
    💰 Monede noi: 2570
    📈 Mai ai nevoie de 1850 EXP pentru nivelul 16
```

### Ce am folosit în acest proiect

```
  ✅ Variabile cu const (date fixe) și let (date care se schimbă)
  ✅ Tipuri: string, number, boolean
  ✅ Operatori aritmetici: +, -, *, /, %
  ✅ Scurtături: +=, -=, ++
  ✅ Template literals cu ${ }
  ✅ Metode string: .repeat()
  ✅ Math.round() pentru rotunjire
  ✅ console.log() pentru afișare
  ✅ Comentarii organizate pe secțiuni
  ✅ Un mic if/else (preview capitolul 6!)
```

---

## 5.11 Conversia între tipuri

Uneori ai nevoie să transformi un tip de dată în altul:

### String → Number

```javascript
let textNumar = "42";

let numar1 = Number(textNumar);        // 42 (number)
let numar2 = parseInt(textNumar);      // 42 (număr întreg)
let numar3 = parseFloat("3.14");       // 3.14 (număr zecimal)

console.log(typeof textNumar);         // "string"
console.log(typeof numar1);            // "number"
```

### Number → String

```javascript
let numar = 42;

let text1 = String(numar);            // "42"
let text2 = numar.toString();         // "42"
let text3 = `${numar}`;               // "42" (cu template literal)

console.log(typeof text1);            // "string"
```

### Orice → Boolean

```javascript
// Valori "falsy" (devin false)
console.log(Boolean(0));          // false
console.log(Boolean(""));         // false (string gol)
console.log(Boolean(null));       // false
console.log(Boolean(undefined));  // false

// Valori "truthy" (devin true)
console.log(Boolean(1));          // true
console.log(Boolean("text"));    // true (orice string ne-gol)
console.log(Boolean(42));        // true (orice număr nenul)
```

> 💡 **Regulă simplă:**
> Zero, string gol și null/undefined sunt **false**. Tot restul este **true**. Vom folosi mult această regulă mai târziu!

---

## 5.12 `alert()`, `prompt()` și `confirm()` — Dialoguri cu utilizatorul

Pe lângă consolă, JavaScript poate afișa **ferestre pop-up** direct pe ecran:

### `alert()` — Afișează un mesaj

```javascript
alert("Bine ai venit pe site-ul meu!");
```

Apare o fereastră cu mesajul și un buton OK.

### `prompt()` — Cere informații de la utilizator

```javascript
let numeUtilizator = prompt("Cum te cheamă?");
console.log(`Salut, ${numeUtilizator}!`);
```

Apare o fereastră cu un câmp de text. Ce scrie utilizatorul devine valoarea variabilei.

### `confirm()` — Întreabă da sau nu

```javascript
let sigur = confirm("Ești sigur că vrei să continui?");
console.log(sigur);    // true dacă a apăsat OK, false dacă a apăsat Cancel
```

### Exemplu combinat

```javascript
let nume = prompt("Cum te cheamă?");
let varstaText = prompt("Câți ani ai?");
let varsta = Number(varstaText);      // convertim din text în număr!

alert(`Salut, ${nume}! Ai ${varsta} ani.`);

if (varsta >= 10) {
    alert("Ești la vârsta perfectă pentru a învăța programare! 🚀");
}
```

> ⚠️ **Atenție!**
> `prompt()` returnează mereu un **string**, chiar dacă utilizatorul scrie un număr! De aceea trebuie să convertești cu `Number()` dacă vrei să faci calcule. 
> `prompt("Vârsta?")` → `"14"` (string) → `Number("14")` → `14` (number)

---

## 5.13 Greșeli frecvente (și cum le repari) 🔧

### ❌ Greșeala 1: Confuzie între `=` și `===`

```javascript
// ❌ Atenție: = înseamnă ATRIBUIRE (pune valoarea în cutie)
let x = 5;        // pune 5 în cutia x

// === înseamnă COMPARARE (verifică dacă sunt egale)
// Vom folosi mult === în capitolul următor
console.log(x === 5);    // true
console.log(x === 3);    // false
```

### ❌ Greșeala 2: „Adunare" de text cu numere

```javascript
// ❌ Surpriză nedorită
let rezultat = "5" + 3;
console.log(rezultat);     // "53" (text, nu 8!)

// ✅ Convertește mai întâi
let rezultat2 = Number("5") + 3;
console.log(rezultat2);    // 8 (număr!)
```

### ❌ Greșeala 3: Modificarea unei constante

```javascript
const culoare = "albastru";
culoare = "roșu";           // ❌ TypeError! const nu poate fi schimbat

let culoare2 = "albastru";
culoare2 = "roșu";          // ✅ let poate fi schimbat
```

### ❌ Greșeala 4: Ghilimele în loc de backtick-uri

```javascript
// ❌ GREȘIT — template literal NU funcționează cu ghilimele
let mesaj = "Salut, ${nume}!";
console.log(mesaj);    // "Salut, ${nume}!" (textul literal, nu valoarea!)

// ✅ CORECT — trebuie backtick-uri
let mesaj2 = `Salut, ${nume}!`;
console.log(mesaj2);   // "Salut, Maria!" (valoarea variabilei)
```

### ❌ Greșeala 5: Script.js încărcat prea devreme

```html
<!-- ❌ GREȘIT — JavaScript în head, înainte de body -->
<head>
    <script src="script.js"></script>
</head>
<body>
    <h1>Titlu</h1>
</body>

<!-- ✅ CORECT — JavaScript la final, înainte de </body> -->
<body>
    <h1>Titlu</h1>
    <script src="script.js"></script>
</body>
```

---

## 5.14 Mini-quiz — Verifică ce ai învățat! ✅

**1.** Ce afișează `console.log(typeof "42")`?

**2.** Care e diferența dintre `let` și `const`?

**3.** Ce afișează `console.log("Salut" + " " + "lume")`?

**4.** Ce afișează `console.log(10 % 3)`?

**5.** Rescrie acest cod folosind template literals:
```javascript
let mesaj = "Mă numesc " + nume + " și am " + varsta + " ani.";
```

**6.** Ce tip de dată este valoarea `false`?

**7.** `prompt()` returnează mereu ce tip de dată, chiar dacă utilizatorul scrie un număr?

---

<details>
<summary>🔑 Click aici pentru răspunsuri</summary>

1. **`"string"`** — `"42"` este un text (are ghilimele), chiar dacă arată ca un număr.

2. **`let`** creează o variabilă care poate fi **modificată** ulterior. **`const`** creează o constantă care **nu poate fi modificată** după atribuire.

3. **`"Salut lume"`** — operatorul `+` între string-uri le **concatenează** (lipește).

4. **`1`** — operatorul `%` (modulo) returnează **restul** împărțirii: 10 ÷ 3 = 3 rest **1**.

5. ```javascript
   let mesaj = `Mă numesc ${nume} și am ${varsta} ani.`;
   ```
   Cu backtick-uri și `${}` pentru variabile.

6. **Boolean** — `true` și `false` sunt cele două valori de tip boolean.

7. **String** — `prompt()` returnează mereu un string. Chiar dacă utilizatorul scrie `14`, valoarea primită este `"14"` (text). Trebuie convertit cu `Number()` pentru calcule.

</details>

---

## 5.15 Știai că? — Curiozități din lumea tech 🤓

☕ **JavaScript a fost creat în doar 10 zile!** Brendan Eich l-a scris în mai 1995, la compania Netscape. Inițial se numea „Mocha", apoi „LiveScript", și în final „JavaScript" — doar pentru că Java era popular la acea vreme. Este probabil cel mai „grăbit" limbaj de programare care a ajuns să fie folosit de miliarde de oameni.

🌍 **JavaScript este cel mai popular limbaj de programare din lume**, conform sondajului Stack Overflow din fiecare an. Peste 65% din toți programatorii îl folosesc. Motivul? Este singurul limbaj care rulează direct în browser — dacă faci web, trebuie să știi JavaScript.

🔢 **Problema „0.1 + 0.2"** este o curiozitate celebră. Deschide consola și scrie `0.1 + 0.2`. Rezultatul? `0.30000000000000004` — nu exact `0.3`! Asta se întâmplă din cauza modului în care computerele stochează numerele zecimale în binar. Nu e un bug al JavaScript — se întâmplă în aproape toate limbajele de programare.

🎮 **Multe jocuri de browser** sunt făcute în JavaScript! Jocuri precum Wordle, 2048, sau jocul cu dinozaurul din Chrome (apare când nu ai internet) sunt scrise în JavaScript. Până la finalul acestei cărți, vei putea crea propriile tale jocuri!

---

## Recapitulare — Ce ai învățat în Capitolul 5

```
  ✅ JavaScript face pagina interactivă (creierul paginii)
  ✅ Se scrie în fișier extern .js, conectat la final în <body>
  ✅ console.log() — afișează mesaje în consola browserului
  ✅ Variabile: let (modificabilă) și const (fixă)
  ✅ Reguli de numire: camelCase, fără spații, nu începe cu cifră
  ✅ Tipuri de date: string ("text"), number (42), boolean (true/false)
  ✅ undefined și null — lipsa valorii (accidentală vs. intenționată)
  ✅ Operatori aritmetici: +, -, *, /, %, **
  ✅ Scurtături: +=, -=, *=, ++, --
  ✅ Operatorul + între string-uri = concatenare (lipire)
  ✅ "5" + 3 = "53" (text!), dar 5 + 3 = 8 (număr!)
  ✅ String-uri: .length, [index], .toUpperCase(), .includes()
  ✅ Template literals: `text ${variabila}` cu backtick-uri
  ✅ Conversie: Number(), String(), Boolean()
  ✅ alert(), prompt(), confirm() — dialoguri cu utilizatorul
  ✅ Comentarii: // pe o linie, /* */ pe mai multe linii
  ✅ Ai creat un profil de jucător afișat în consolă! 🎮
```

---

## Ce urmează?

În **Capitolul 6: Decizii și repetiții**, JavaScript va învăța să **gândească**! Cu `if/else`, codul tău va lua decizii: „Dacă scorul e mare, afișează Felicitări! Altfel, afișează Mai încearcă." Cu bucle (`for`, `while`), va repeta acțiuni de mii de ori în milisecunde. Și cu **funcțiile**, vei învăța să scrii „rețete" de cod reutilizabile.

Pregătește-te — programarea adevărată abia a început! 🧠

---

> *„Simplitatea este o condiție prealabilă a fiabilității."*
> — Edsger W. Dijkstra, pionier al informaticii
