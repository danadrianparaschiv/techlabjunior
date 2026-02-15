# Capitolul 6: Decizii și repetiții 🧠

> *„Un program bun ia decizii corecte și nu se obosește niciodată."*
> — adaptat

---

## Ce vei învăța în acest capitol

- Cum ia codul tău **decizii** cu `if`, `else if` și `else`
- **Operatori de comparare** și **operatori logici**
- Cum **repeti** acțiuni cu buclele `for` și `while`
- Ce sunt **funcțiile** și de ce sunt cele mai importante piese din programare
- Cum scrii funcții cu **parametri** și **return**
- **Funcții arrow** — varianta modernă și compactă

---

## 6.1 De ce are nevoie codul de decizii?

Până acum, codul tău a fost ca un tren pe o șină dreaptă — merge doar înainte, linie cu linie, fără oprire. Dar programele reale trebuie să ia decizii:

- Un joc verifică: **scorul e destul de mare?** Dacă da → nivel nou. Dacă nu → mai încearcă.
- Un site verifică: **parola e corectă?** Dacă da → intră. Dacă nu → eroare.
- O aplicație meteo verifică: **plouă?** Dacă da → umbrela. Dacă nu → ochelari de soare.

**JavaScript ia decizii cu `if` / `else`** — exact ca tine când te gândești „dacă... atunci... altfel...".

---

## 6.2 `if` — Dacă se întâmplă ceva, fă ceva

Cea mai simplă decizie: **dacă** o condiție e adevărată, **execută** un bloc de cod.

```javascript
let temperatura = 35;

if (temperatura > 30) {
    console.log("E foarte cald afară! ☀️");
}
```

Structura:

```
  if  ( condiția )  {
  ──    ─────────    ─
  │         │        │
  │         │        └── acolada deschide blocul de cod
  │         │
  │         └── expresia care se verifică (true sau false?)
  │
  └── cuvântul cheie ("dacă")
  
  
      instrucțiuni...     ← se execută DOAR dacă condiția e true
  
  }
  ─
  └── acolada închide blocul
```

Vizual:

```
              ┌─────────────┐
              │ temperatura │
              │   > 30 ?    │
              └──────┬──────┘
                     │
              ┌──────┴──────┐
              │             │
           DA (true)     NU (false)
              │             │
              ▼             ▼
     ┌────────────────┐   (nu se
     │ "E foarte cald │    întâmplă
     │  afară! ☀️"    │    nimic)
     └────────────────┘
```

---

## 6.3 `if / else` — Dacă da... altfel...

Ce facem când condiția e falsă? Adăugăm `else`:

```javascript
let varsta = 14;

if (varsta >= 18) {
    console.log("Ești adult! Poți vota.");
} else {
    console.log("Ești minor. Mai ai de așteptat.");
}
```

```
              ┌─────────────┐
              │ varsta >= 18?│
              └──────┬──────┘
                     │
              ┌──────┴──────┐
              │             │
           DA (true)     NU (false)
              │             │
              ▼             ▼
     ┌──────────────┐  ┌───────────────┐
     │ "Ești adult! │  │ "Ești minor.  │
     │  Poți vota." │  │  Mai ai de    │
     └──────────────┘  │  așteptat."   │
                       └───────────────┘
```

### Metafora: Răscrucea din drum

Gândește-te la `if/else` ca la o **răscruce**. Ajungi la un indicator și alegi:

```
                    🚶 Tu
                     │
                     ▼
              ╔══════════════╗
              ║  CONDIȚIA    ║
              ║  e adevărată?║
              ╚══════╤═══════╝
                     │
            ┌────────┼────────┐
            │ DA     │     NU │
            ▼        │        ▼
       ┌─────────┐   │   ┌─────────┐
       │ Drum    │   │   │ Drum    │
       │ STÂNGA  │   │   │ DREAPTA │
       │ (if)    │   │   │ (else)  │
       └────┬────┘   │   └────┬────┘
            │        │        │
            └────────┼────────┘
                     │
                     ▼
              Codul continuă...
```

Nu poți merge pe ambele drumuri simultan — mergi pe **unul sau pe celălalt**, în funcție de condiție.

---

## 6.4 `else if` — Mai multe opțiuni

Ce faci când ai mai mult de două posibilități? Folosești `else if`:

```javascript
let nota = 8;

if (nota === 10) {
    console.log("Excelent! Nota maximă! 🌟");
} else if (nota >= 8) {
    console.log("Foarte bine! 👏");
} else if (nota >= 6) {
    console.log("Bine, dar poți mai mult!");
} else if (nota >= 5) {
    console.log("Suficient. Trebuie să mai lucrezi.");
} else {
    console.log("Nepromovat. Nu renunța! 💪");
}

// Rezultat: "Foarte bine! 👏" (nota e 8, deci >= 8 e prima condiție adevărată)
```

```
              ┌──────────────┐
              │ nota === 10? │──── DA ──── "Excelent! 🌟"
              └──────┬───────┘
                  NU │
              ┌──────┴───────┐
              │ nota >= 8?   │──── DA ──── "Foarte bine! 👏"  ← AICI
              └──────┬───────┘
                  NU │
              ┌──────┴───────┐
              │ nota >= 6?   │──── DA ──── "Bine!"
              └──────┬───────┘
                  NU │
              ┌──────┴───────┐
              │ nota >= 5?   │──── DA ──── "Suficient."
              └──────┬───────┘
                  NU │
                     ▼
              "Nepromovat. 💪"
```

> ⚠️ **Atenție!**
> Condițiile se verifică **de sus în jos**, și JavaScript se oprește la **prima condiție adevărată**. De aceea ordinea contează! Dacă ai pus `nota >= 5` prima, un elev cu nota 10 ar primi „Suficient" — nu ce vrei.

---

## 6.5 Operatori de comparare

Acești operatori compară două valori și returnează `true` sau `false`:

```javascript
console.log(5 === 5);      // true   (egal?)
console.log(5 !== 3);      // true   (diferit?)
console.log(5 > 3);        // true   (mai mare?)
console.log(5 < 3);        // false  (mai mic?)
console.log(5 >= 5);       // true   (mai mare sau egal?)
console.log(5 <= 3);       // false  (mai mic sau egal?)
```

| Operator | Înseamnă | Exemplu | Rezultat |
|---|---|---|---|
| `===` | Strict egal (valoare ȘI tip) | `5 === 5` | `true` |
| `!==` | Strict diferit | `5 !== "5"` | `true` |
| `>` | Mai mare | `10 > 5` | `true` |
| `<` | Mai mic | `3 < 1` | `false` |
| `>=` | Mai mare sau egal | `5 >= 5` | `true` |
| `<=` | Mai mic sau egal | `3 <= 7` | `true` |

### `===` vs `==` — De ce trei egaluri?

```javascript
// === (strict) — verifică valoarea ȘI tipul
console.log(5 === "5");      // false (number vs string)
console.log(5 === 5);        // true  (ambele number, ambele 5)

// == (slab) — verifică doar valoarea (convertește automat)
console.log(5 == "5");       // true  (convertește "5" în 5, apoi compară)
console.log(0 == false);     // true  (convertește false în 0)
```

> 💡 **Regulă de aur:**
> Folosește **mereu `===`** (trei egaluri). Operatorul `==` face conversii ascunse care duc la bug-uri surprinzătoare. Chiar și programatorii experimentați evită `==`.

---

## 6.6 Operatori logici — Combină condițiile

Ce faci când ai mai multe condiții de verificat simultan? Folosești operatori logici:

### `&&` (ȘI logic) — Ambele trebuie să fie adevărate

```javascript
let varsta = 14;
let arePermisiune = true;

if (varsta >= 10 && arePermisiune) {
    console.log("Poți juca acest joc! 🎮");
}
// Ambele condiții sunt true → se execută
```

```
  Condiția 1    &&    Condiția 2    =    Rezultat
  ──────────          ──────────         ────────
  true          &&    true          =    true  ✅
  true          &&    false         =    false ❌
  false         &&    true          =    false ❌
  false         &&    false         =    false ❌
  
  Ambele trebuie să fie true! (ca un lanț — dacă o verigă cedează, tot lanțul cedează)
```

### `||` (SAU logic) — Cel puțin una trebuie să fie adevărată

```javascript
let esteWeekend = true;
let esteVacanta = false;

if (esteWeekend || esteVacanta) {
    console.log("Zi liberă! 🎉");
}
// Cel puțin una e true → se execută
```

```
  Condiția 1    ||    Condiția 2    =    Rezultat
  ──────────          ──────────         ────────
  true          ||    true          =    true  ✅
  true          ||    false         =    true  ✅
  false         ||    true          =    true  ✅
  false         ||    false         =    false ❌
  
  Cel puțin una trebuie să fie true! (ca un plan B — dacă unul nu merge, celălalt salvează situația)
```

### `!` (NU logic / negare) — Inversează valoarea

```javascript
let plouaAfara = false;

if (!plouaAfara) {
    console.log("Nu plouă! Ieși la joacă! ☀️");
}
// !false === true → se execută
```

```
  !true  = false    (inversează)
  !false = true     (inversează)
```

### Exemplu combinat

```javascript
let varsta = 14;
let esteElev = true;
let areCarnet = true;

// Poate primi reducere dacă: (e elev ȘI are carnet) SAU e sub 12 ani
if ((esteElev && areCarnet) || varsta < 12) {
    console.log("Ai reducere 50%! 🎟️");
} else {
    console.log("Preț normal.");
}
```

> 💡 **Sfat!**
> Când combini `&&` și `||`, folosește **paranteze** pentru claritate — exact ca în matematică. `(a && b) || c` este mai clar decât `a && b || c`.

---

## 6.7 Bucle — Repetă fără să obosești 🔁

Imaginează-ți că trebuie să scrii `console.log("Salut!")` de 100 de ori. Ai putea copia manual linia de 100 de ori, dar... de ce ai face asta când poți folosi o **buclă**?

**O buclă repetă un bloc de cod** de mai multe ori — automat, rapid, fără greșeli.

### Metafora: Ticăitul unui ceas

O buclă funcționează ca un **ceas cu alarmă**: tic-tac, tic-tac, tic-tac... până când sună alarma (condiția de oprire):

```
  Buclă "for" care numără de la 1 la 5:
  
  ┌──────────┐
  │ Start:   │
  │ i = 1    │
  └────┬─────┘
       │
       ▼
  ┌──────────┐    NU
  │ i <= 5 ? │──────────► STOP! Ieșire din buclă.
  └────┬─────┘
       │ DA
       ▼
  ┌──────────┐
  │ Afișează │
  │ "Tic" + i│
  └────┬─────┘
       │
       ▼
  ┌──────────┐
  │ i = i + 1│──────┐
  └──────────┘      │
       ▲            │
       └────────────┘
       (revino la verificare)
```

### Bucla `for` — Cea mai folosită

```javascript
for (let i = 1; i <= 5; i++) {
    console.log(`Tic ${i}`);
}
```

Rezultat:
```
  Tic 1
  Tic 2
  Tic 3
  Tic 4
  Tic 5
```

Anatomia buclei `for`:

```
  for ( let i = 1 ;   i <= 5 ;    i++    ) {
        ─────────     ──────      ───
            │            │          │
            │            │          └── PASUL: ce se întâmplă după fiecare repetare
            │            │              (aici: crește i cu 1)
            │            │
            │            └── CONDIȚIA: continuă cât timp e adevărată
            │                (aici: cât timp i e mai mic sau egal cu 5)
            │
            └── INIȚIALIZAREA: punctul de start
                (aici: i începe de la 1)
  
      console.log(`Tic ${i}`);    ← CORPUL: ce se execută la fiecare repetare
  
  }
```

Pas cu pas:

```
  Runda 1:  i = 1  →  1 <= 5? DA  →  afișează "Tic 1"  →  i devine 2
  Runda 2:  i = 2  →  2 <= 5? DA  →  afișează "Tic 2"  →  i devine 3
  Runda 3:  i = 3  →  3 <= 5? DA  →  afișează "Tic 3"  →  i devine 4
  Runda 4:  i = 4  →  4 <= 5? DA  →  afișează "Tic 4"  →  i devine 5
  Runda 5:  i = 5  →  5 <= 5? DA  →  afișează "Tic 5"  →  i devine 6
  Runda 6:  i = 6  →  6 <= 5? NU  →  STOP! Ieșire din buclă.
```

### Exemple practice cu `for`

**Numărătoare inversă:**

```javascript
for (let i = 10; i >= 1; i--) {
    console.log(i);
}
console.log("🚀 LANSARE!");
// 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 🚀 LANSARE!
```

**Tabla înmulțirii:**

```javascript
let numar = 7;

console.log(`Tabla lui ${numar}:`);
for (let i = 1; i <= 10; i++) {
    console.log(`  ${numar} x ${i} = ${numar * i}`);
}
// 7 x 1 = 7
// 7 x 2 = 14
// ...
// 7 x 10 = 70
```

**Sumă de numere:**

```javascript
let suma = 0;

for (let i = 1; i <= 100; i++) {
    suma += i;       // adaugă fiecare număr la sumă
}

console.log(`Suma numerelor de la 1 la 100 este: ${suma}`);
// Suma numerelor de la 1 la 100 este: 5050
```

> 💡 **Știai că?**
> Legenda spune că matematicianul Carl Friedrich Gauss, pe când avea 10 ani, a fost rugat de profesor să adune numerele de la 1 la 100. În timp ce colegii calculau, Gauss a găsit formula: `n × (n + 1) / 2 = 100 × 101 / 2 = 5050`. Programul tău tocmai a făcut același lucru, dar „brut" — adunând fiecare număr pe rând!

### Bucla `while` — Repetă cât timp condiția e adevărată

`while` este mai simplă: repetă cât timp condiția rămâne `true`.

```javascript
let vieti = 3;

while (vieti > 0) {
    console.log(`Ai ${vieti} vieți. Joci...`);
    vieti--;     // pierzi o viață la fiecare rundă
}

console.log("💀 Game Over!");
```

Rezultat:

```
  Ai 3 vieți. Joci...
  Ai 2 vieți. Joci...
  Ai 1 vieți. Joci...
  💀 Game Over!
```

### Când folosești `for` vs `while`?

```
  FOR — când știi CÂTE repetări vrei
  ─────────────────────────────────
  "Repetă de 10 ori"
  "Parcurge numerele de la 1 la 100"
  "Fă ceva pentru fiecare element"
  
  WHILE — când NU știi câte repetări, dar știi CONDIȚIA de oprire
  ──────────────────────────────────────────────────────────────
  "Repetă până când utilizatorul ghicește numărul"
  "Continuă până când viețile ajung la 0"
  "Repetă până când datele se termină"
```

### Exemplu `while` — Jocul de ghicit numărul

```javascript
let numarSecret = 7;    // în viitor, vom folosi Math.random()
let incercare = 0;
let ghicit = false;

console.log("🎯 Ghicește numărul de la 1 la 10!");

while (!ghicit) {
    incercare++;
    let raspuns = Number(prompt(`Încercarea ${incercare}: Ce număr am ales?`));
    
    if (raspuns === numarSecret) {
        ghicit = true;
        console.log(`🎉 Bravo! Ai ghicit din ${incercare} încercări!`);
    } else if (raspuns < numarSecret) {
        console.log("📈 Mai mare!");
    } else {
        console.log("📉 Mai mic!");
    }
}
```

> ⚠️ **Atenție la bucle infinite!**
> Dacă condiția nu devine niciodată `false`, bucla rulează **la infinit** și browserul se blochează!
> 
> ```javascript
> // ❌ BUCLĂ INFINITĂ — i nu se schimbă niciodată!
> let i = 1;
> while (i <= 5) {
>     console.log(i);
>     // Am uitat i++ !!! Bucla nu se oprește niciodată!
> }
> 
> // ✅ CORECT — i crește la fiecare pas
> let j = 1;
> while (j <= 5) {
>     console.log(j);
>     j++;           // ← ESENȚIAL! Face ca bucla să se oprească eventual
> }
> ```
>
> Dacă browserul se blochează, închide tab-ul (`Ctrl + W`) sau forțează oprirea.

---

## 6.8 `break` și `continue` — Controlul buclei

### `break` — Oprește bucla complet

```javascript
// Caută primul număr care se divide exact la 7 între 50 și 100
for (let i = 50; i <= 100; i++) {
    if (i % 7 === 0) {
        console.log(`Găsit! ${i} se divide la 7.`);
        break;      // oprește bucla, nu mai căuta
    }
}
// Găsit! 56 se divide la 7.
```

### `continue` — Sari peste runda curentă

```javascript
// Afișează doar numerele IMPARE de la 1 la 10
for (let i = 1; i <= 10; i++) {
    if (i % 2 === 0) {
        continue;    // dacă e par, sari la următorul
    }
    console.log(i);
}
// 1, 3, 5, 7, 9
```

```
  break:     "OPREȘTE tot! Am terminat."
  continue:  "Sari peste asta, treci la următorul."
  
  for (...)  ──┐
    │          │
    ├── cod    │
    ├── break ─┘ ← iese din buclă complet
    └── cod (nu se mai execută)
    
  for (...)  ──┐
    │          │
    ├── cod    │
    ├── continue ──┐
    │              │ ← sare direct la pasul următor
    └── cod ◄──────┘   (sare restul corpului buclei)
```

---

## 6.9 Funcții — Rețete de cod 📋

Imaginează-ți că faci clătite. Prima dată, urmezi rețeta pas cu pas. A doua oară, o cunoști deja. A zecea oară, o faci din memorie. Dar nu rescrii rețeta de fiecare dată — o ai deja notată undeva.

**O funcție este exact ca o rețetă**: o scrii o singură dată, și o poți folosi de câte ori vrei.

```
  ┌─────────────────────────────────────────────┐
  │                                             │
  │  📋 Rețeta "faClătite"                      │
  │                                             │
  │  Ingrediente (parametri):                   │
  │    - cantitate ouă                          │
  │    - cantitate făină                        │
  │                                             │
  │  Pași:                                      │
  │    1. Amestecă ouăle cu făina               │
  │    2. Pune în tigaie                        │
  │    3. Gătește 2 minute pe fiecare parte     │
  │                                             │
  │  Rezultat (return):                         │
  │    → o farfurie de clătite 🥞               │
  │                                             │
  └─────────────────────────────────────────────┘
  
  Folosire:
    faClătite(3, 200)    → 🥞 (3 ouă, 200g făină)
    faClătite(5, 350)    → 🥞🥞 (5 ouă, 350g făină)
```

### Cum creezi o funcție

```javascript
function saluta() {
    console.log("Salut, lume!");
}
```

Anatomia:

```
  function   saluta   ()   {
  ────────   ──────   ──   ─
      │         │      │   │
      │         │      │   └── acolada deschide corpul funcției
      │         │      │
      │         │      └── paranteze (aici vor sta parametrii)
      │         │
      │         └── numele funcției (la fel ca la variabile: camelCase)
      │
      └── cuvântul cheie ("definesc o funcție")
  
      console.log("Salut, lume!");    ← corpul funcției (ce face)
  
  }
```

### Cum o folosești (apelezi)

Definirea funcției **nu o execută**! E ca și cum scrii o rețetă fără a gătit. Trebuie să o **apelezi** (să o chemi):

```javascript
// Definire (scriu rețeta)
function saluta() {
    console.log("Salut, lume!");
}

// Apelare (gătesc după rețetă)
saluta();     // "Salut, lume!"
saluta();     // "Salut, lume!"  — o pot folosi de câte ori vreau!
saluta();     // "Salut, lume!"
```

> 💡 **Regulă importantă:**
> Definirea = **scrii** rețeta (o singură dată). Apelarea = **folosești** rețeta (de câte ori vrei). Parantezele `()` la apelare sunt cele care „pornesc" funcția.

---

## 6.10 Parametri — Ingredientele funcției

O rețetă de clătite fără ingrediente nu e foarte utilă. **Parametrii** sunt datele pe care le „dai" funcției ca să lucreze cu ele:

```javascript
function salutaPersoana(nume) {
    console.log(`Salut, ${nume}! 👋`);
}

salutaPersoana("Maria");     // "Salut, Maria! 👋"
salutaPersoana("Alex");      // "Salut, Alex! 👋"
salutaPersoana("Ioana");     // "Salut, Ioana! 👋"
```

```
  Funcția ca o mașină:
  
       parametru       
       (ingredientul)  
           │           
           ▼           
  ┌────────────────┐   
  │   "Maria"  ──► │   
  │                │───► "Salut, Maria! 👋"
  │  salutaPersoana│   
  │                │   
  └────────────────┘   
       funcția         
       (mașina)        
```

### Mai mulți parametri

```javascript
function prezinta(nume, varsta, oras) {
    console.log(`${nume} are ${varsta} ani și locuiește în ${oras}.`);
}

prezinta("Maria", 14, "Cluj");
// "Maria are 14 ani și locuiește în Cluj."

prezinta("Alex", 12, "București");
// "Alex are 12 ani și locuiește în București."
```

| Termen | Ce înseamnă | Unde apare |
|---|---|---|
| **Parametru** | Variabila din **definiție** (placeholder) | `function saluta(nume)` |
| **Argument** | Valoarea concretă la **apelare** | `saluta("Maria")` |

Gândește-te la parametru ca la **locul de parcare** (gol, cu etichetă) și la argument ca la **mașina** care parchează acolo.

### Parametri cu valori implicite

```javascript
function saluta(nume = "Străine") {
    console.log(`Salut, ${nume}!`);
}

saluta("Maria");     // "Salut, Maria!"
saluta();            // "Salut, Străine!" — folosește valoarea implicită
```

---

## 6.11 `return` — Rezultatul funcției

O funcție poate nu doar să **facă** ceva, ci și să **returneze** (dea înapoi) o valoare:

```javascript
function aduna(a, b) {
    return a + b;
}

let rezultat = aduna(5, 3);
console.log(rezultat);         // 8
console.log(aduna(10, 20));    // 30
```

```
  Funcția cu return = o mașină cu intrare ȘI ieșire:
  
    Intrare               Ieșire
  (parametri)           (return)
       │                    │
       ▼                    ▼
  ┌────────────────┐   
  │  5, 3  ──────► │───►  8
  │                │   
  │    aduna()     │   
  └────────────────┘   
  
  "Ia 5 și 3, adună-le, dă-mi înapoi rezultatul"
```

### De ce e important `return`?

Fără `return`, funcția face ceva dar **nu dă nimic înapoi**. Cu `return`, poți folosi rezultatul mai departe:

```javascript
// FĂRĂ return — doar afișează, nu poți folosi rezultatul
function adunaSiAfiseaza(a, b) {
    console.log(a + b);     // afișează 8
}
let x = adunaSiAfiseaza(5, 3);
console.log(x);              // undefined! Funcția nu a returnat nimic.

// CU return — poți folosi rezultatul
function adunaSiReturneaza(a, b) {
    return a + b;
}
let y = adunaSiReturneaza(5, 3);
console.log(y);              // 8
console.log(y * 2);          // 16 — poți face calcule cu rezultatul!
```

### Exemple practice

```javascript
// Calculează aria unui dreptunghi
function ariadreptunghi(latime, inaltime) {
    return latime * inaltime;
}

console.log(`Aria: ${ariadreptunghi(5, 3)} m²`);    // "Aria: 15 m²"


// Verifică dacă un număr e par
function estePar(numar) {
    return numar % 2 === 0;
}

console.log(estePar(4));     // true
console.log(estePar(7));     // false


// Convertește Celsius în Fahrenheit
function celsiusLaFahrenheit(celsius) {
    return (celsius * 9/5) + 32;
}

console.log(`25°C = ${celsiusLaFahrenheit(25)}°F`);  // "25°C = 77°F"
```

> ⚠️ **Atenție!**
> `return` **oprește** funcția imediat. Orice cod după `return` nu se mai execută:
>
> ```javascript
> function test() {
>     return "Salut";
>     console.log("Acest text nu apare niciodată!");  // ← IGNORAT
> }
> ```

---

## 6.12 Funcții Arrow — Varianta modernă ➡️

JavaScript modern oferă o sintaxă mai scurtă pentru funcții, numită **arrow function** (funcție săgeată):

```javascript
// Funcție clasică
function aduna(a, b) {
    return a + b;
}

// Arrow function — echivalent mai scurt
const aduna = (a, b) => {
    return a + b;
};

// Arrow function — și mai scurt (pentru funcții cu o singură expresie)
const aduna = (a, b) => a + b;
```

Evoluția:

```
  CLASICĂ:
  function aduna(a, b) {
      return a + b;
  }
  
  ARROW (forma completă):
  const aduna = (a, b) => {
      return a + b;
  };
  
  ARROW (forma scurtă — fără { } și return):
  const aduna = (a, b) => a + b;
       ─────   ──────  ──  ─────
         │       │      │    │
      numele  param.  săgeata  corpul (se returnează automat)
```

### Când folosești forma scurtă?

Forma scurtă (fără `{ }`) funcționează doar când funcția are **o singură expresie** care se returnează direct:

```javascript
// O singură expresie → forma scurtă
const dublu = (n) => n * 2;
const salut = (nume) => `Salut, ${nume}!`;
const estePar = (n) => n % 2 === 0;

// Mai multe linii → forma completă cu { }
const calculeaza = (a, b) => {
    let suma = a + b;
    let produs = a * b;
    return { suma, produs };
};
```

### Un singur parametru? Fără paranteze!

```javascript
// Cu un singur parametru, parantezele sunt opționale
const dublu = n => n * 2;
const salut = nume => `Salut, ${nume}!`;

// Cu zero sau mai mulți parametri, parantezele sunt obligatorii
const zeroParam = () => "Salut!";
const doiParam = (a, b) => a + b;
```

> 💡 **Sfat pentru începători:**
> Nu te stresa dacă arrow functions ți se par confuze acum. Forma clasică (`function`) funcționează perfect. Arrow functions sunt o scurtătură elegantă pe care o vei folosi tot mai mult pe măsură ce devii mai confortabil cu JavaScript.

---

## 6.13 Proiect practic: Calculator de statistici pentru joc 🚀

Hai să punem totul cap la cap — `if/else`, bucle și funcții — într-un proiect concret.

Creează structura:

```
  📁 calculator-joc/
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
    <title>Calculator Statistici Joc</title>
</head>
<body>
    <h1>🎮 Calculator Statistici — Deschide consola (F12)</h1>
    <script src="script.js"></script>
</body>
</html>
```

### JavaScript (`script.js`):

```javascript
// ══════════════════════════════════════════════
// 🎮 CALCULATOR DE STATISTICI PENTRU JOC
// ══════════════════════════════════════════════

// ── FUNCȚII UTILITARE ──

// Calculează media unui set de scoruri
function calculeazaMedia(scoruri) {
    let suma = 0;
    for (let i = 0; i < scoruri.length; i++) {
        suma += scoruri[i];
    }
    return suma / scoruri.length;
}

// Găsește scorul maxim
function gasestMaxim(scoruri) {
    let maxim = scoruri[0];
    for (let i = 1; i < scoruri.length; i++) {
        if (scoruri[i] > maxim) {
            maxim = scoruri[i];
        }
    }
    return maxim;
}

// Găsește scorul minim
function gasestMinim(scoruri) {
    let minim = scoruri[0];
    for (let i = 1; i < scoruri.length; i++) {
        if (scoruri[i] < minim) {
            minim = scoruri[i];
        }
    }
    return minim;
}

// Determină rangul pe baza scorului mediu
function determinaRang(mediaSc) {
    if (mediaSc >= 900) {
        return "🏆 LEGENDĂ";
    } else if (mediaSc >= 700) {
        return "⭐ MAESTRU";
    } else if (mediaSc >= 500) {
        return "🥈 AVANSAT";
    } else if (mediaSc >= 300) {
        return "🥉 INTERMEDIAR";
    } else {
        return "🌱 ÎNCEPĂTOR";
    }
}

// Creează o bară de progres vizuală
const baraProgres = (valoare, maxim, lungime = 20) => {
    let procent = Math.round((valoare / maxim) * lungime);
    let plin = "█".repeat(procent);
    let gol = "░".repeat(lungime - procent);
    let procentText = Math.round((valoare / maxim) * 100);
    return `[${plin}${gol}] ${procentText}%`;
};

// Numără câte scoruri sunt peste un prag
const numărăPestePrag = (scoruri, prag) => {
    let count = 0;
    for (let i = 0; i < scoruri.length; i++) {
        if (scoruri[i] >= prag) {
            count++;
        }
    }
    return count;
};


// ── DATE JOC ──

const numeJucator = "CyberWolf_42";
const scoruriPartide = [450, 720, 380, 910, 650, 830, 290, 770, 560, 880];
const scorMaximPosibil = 1000;


// ── CALCULE ──

const media = calculeazaMedia(scoruriPartide);
const maxim = gasestMaxim(scoruriPartide);
const minim = gasestMinim(scoruriPartide);
const rang = determinaRang(media);
const partidePeste500 = numărăPestePrag(scoruriPartide, 500);
const partidePeste800 = numărăPestePrag(scoruriPartide, 800);


// ── AFIȘARE ──

console.log("╔══════════════════════════════════════════╗");
console.log("║     🎮 RAPORT STATISTICI JUCĂTOR 🎮      ║");
console.log("╚══════════════════════════════════════════╝");
console.log("");

console.log(`  👤 Jucător: ${numeJucator}`);
console.log(`  🏅 Rang:    ${rang}`);
console.log("");

console.log("── Scoruri partide ─────────────────────────");
for (let i = 0; i < scoruriPartide.length; i++) {
    let scor = scoruriPartide[i];
    let indicator = scor >= 800 ? "🔥" : scor >= 500 ? "✅" : "📉";
    console.log(`  Partida ${i + 1}: ${scor.toString().padStart(4)} ${indicator} ${baraProgres(scor, scorMaximPosibil, 15)}`);
}
console.log("");

console.log("── Statistici generale ─────────────────────");
console.log(`  📊 Media scorurilor:   ${media.toFixed(1)}`);
console.log(`  🏆 Scor maxim:         ${maxim}`);
console.log(`  📉 Scor minim:         ${minim}`);
console.log(`  📈 Diferență max-min:  ${maxim - minim}`);
console.log(`  🎯 Partide peste 500:  ${partidePeste500} din ${scoruriPartide.length}`);
console.log(`  🔥 Partide peste 800:  ${partidePeste800} din ${scoruriPartide.length}`);
console.log("");

console.log("── Performanță generală ────────────────────");
console.log(`  ${baraProgres(media, scorMaximPosibil)}`);
console.log("");

// Sfat personalizat bazat pe statistici
console.log("── Recomandare ─────────────────────────────");
if (media >= 800) {
    console.log("  🏆 Ești un jucător de elită! Continuă așa!");
} else if (maxim >= 800 && media < 800) {
    console.log("  💡 Ai potențial de top — trebuie să fii mai constant!");
    console.log(`  📈 Dacă aduci minimul de la ${minim} la cel puțin 500,`);
    console.log(`     media ta va crește semnificativ.`);
} else if (media >= 500) {
    console.log("  👍 Progres bun! Concentrează-te pe partidele slabe.");
} else {
    console.log("  🌱 Ești la început de drum. Exersează zilnic!");
}

console.log("");
console.log("════════════════════════════════════════════");
console.log("  Constructorul de Site-uri — Capitolul 6");
console.log("════════════════════════════════════════════");
```

### Ce am folosit în acest proiect

```
  ✅ Funcții clasice cu parametri și return
  ✅ Funcții arrow (const baraProgres = (...) => { })
  ✅ Parametri cu valori implicite (lungime = 20)
  ✅ if / else if / else pentru determinarea rangului și recomandări
  ✅ Bucle for pentru parcurgerea scorurilor
  ✅ Operatori de comparare (>=, <) și logici (&&)
  ✅ Operatorul ternar (? :) — un mic preview!
  ✅ Template literals pentru afișare
  ✅ Metode: .toFixed(), .toString(), .padStart(), .repeat()
```

---

## 6.14 Operatorul ternar — `if/else` pe scurt

Ai observat în proiect linia cu `? :` ? Acela este **operatorul ternar** — un `if/else` condensat pe o singură linie:

```javascript
// if/else clasic
let mesaj;
if (scor >= 500) {
    mesaj = "Bine!";
} else {
    mesaj = "Mai încearcă!";
}

// Operatorul ternar — exact același lucru, dar pe o linie
let mesaj = scor >= 500 ? "Bine!" : "Mai încearcă!";
```

Structura:

```
  condiție    ?    valoare dacă true    :    valoare dacă false
  ────────    ─    ───────────────────  ─    ──────────────────
  scor >= 500 ?    "Bine!"             :    "Mai încearcă!"
```

Exemple:

```javascript
let varsta = 14;
let status = varsta >= 18 ? "adult" : "minor";
console.log(status);    // "minor"

let temp = 35;
let sfat = temp > 30 ? "Bea multă apă! ☀️" : "Bucură-te de vreme! 🌤️";
console.log(sfat);      // "Bea multă apă! ☀️"
```

Folosește operatorul ternar doar pentru condiții **simple**. Dacă logica e complexă, rămâi la `if/else` — claritatea e mai importantă decât scurtimea.

---

## 6.15 Greșeli frecvente (și cum le repari) 🔧

### ❌ Greșeala 1: `=` în loc de `===` în condiții

```javascript
// ❌ GREȘIT — = atribuie valoarea, nu compară!
if (varsta = 18) {
    console.log("Ești adult");  // se execută MEREU!
}

// ✅ CORECT — === compară
if (varsta === 18) {
    console.log("Ești adult");
}
```

### ❌ Greșeala 2: Buclă infinită

```javascript
// ❌ GREȘIT — variabila nu se schimbă, bucla nu se oprește
let i = 0;
while (i < 10) {
    console.log(i);
    // am uitat i++ !
}

// ✅ CORECT
let i = 0;
while (i < 10) {
    console.log(i);
    i++;              // ← ESENȚIAL!
}
```

### ❌ Greșeala 3: Funcție definită dar neapelată

```javascript
// ❌ Funcția există dar nu face nimic — nu e apelată
function afiseazaSalut() {
    console.log("Salut!");
}
// ... liniște ... nimic pe ecran

// ✅ CORECT — o apelezi cu ()
function afiseazaSalut() {
    console.log("Salut!");
}
afiseazaSalut();       // "Salut!"
```

### ❌ Greșeala 4: Uiți `return` în funcție

```javascript
// ❌ Funcția nu returnează nimic
function aduna(a, b) {
    let rezultat = a + b;
    // am uitat return!
}
console.log(aduna(5, 3));    // undefined

// ✅ CORECT
function aduna(a, b) {
    let rezultat = a + b;
    return rezultat;
}
console.log(aduna(5, 3));    // 8
```

### ❌ Greșeala 5: `else if` scris ca `elseif` sau `else  if`

```javascript
// ❌ GREȘIT
elseif (nota >= 8) { }       // nu există "elseif" (un cuvânt)

// ✅ CORECT — două cuvinte separate
else if (nota >= 8) { }
```

---

## 6.16 Mini-quiz — Verifică ce ai învățat! ✅

**1.** Ce afișează acest cod?
```javascript
let x = 15;
if (x > 20) {
    console.log("A");
} else if (x > 10) {
    console.log("B");
} else {
    console.log("C");
}
```

**2.** Ce returnează expresia `5 > 3 && 2 > 8`?

**3.** Câte repetări face bucla `for (let i = 0; i < 5; i++)`?

**4.** Care e diferența dintre o funcție cu `return` și una fără?

**5.** Rescrie această funcție ca arrow function:
```javascript
function dublu(n) {
    return n * 2;
}
```

**6.** Ce face `break` într-o buclă?

**7.** Ce afișează `console.log(10 === "10")`?

---

<details>
<summary>🔑 Click aici pentru răspunsuri</summary>

1. **`"B"`** — `x` este 15: prima condiție (`15 > 20`) e falsă, a doua (`15 > 10`) e adevărată, deci se execută „B". Restul se ignoră.

2. **`false`** — Operatorul `&&` cere ca **ambele** condiții să fie adevărate. `5 > 3` e `true`, dar `2 > 8` e `false`. `true && false = false`.

3. **5 repetări** — `i` ia valorile 0, 1, 2, 3, 4. Când `i` devine 5, condiția `5 < 5` e falsă și bucla se oprește.

4. O funcție **cu `return`** dă înapoi o valoare pe care o poți folosi mai departe (stoca într-o variabilă, folosi în calcule). O funcție **fără `return`** face acțiuni (ex: afișează în consolă) dar returnează `undefined`.

5. ```javascript
   const dublu = (n) => n * 2;
   // sau și mai scurt:
   const dublu = n => n * 2;
   ```

6. **Oprește bucla complet**, chiar dacă condiția ar fi încă adevărată. Execuția continuă cu codul de după buclă.

7. **`false`** — Operatorul `===` (strict egal) verifică atât valoarea cât și **tipul**. `10` este number, `"10"` este string — tipuri diferite, deci nu sunt egale.

</details>

---

## 6.17 Știai că? — Curiozități din lumea tech 🤓

🐛 **Primul „bug" din istoria informaticii** a fost literalmente un insect! În 1947, programatoarea Grace Hopper a găsit o molie prinsă într-un releu al computerului Harvard Mark II. A lipit-o în jurnalul de bord cu nota „First actual case of bug being found" (Primul caz real de bug găsit). De atunci, erorile din programe se numesc „bugs" (insecte), iar repararea lor se numește „debugging" (eliminarea insectelor).

🔁 **Cele mai rapide bucle din lume** rulează de miliarde de ori pe secundă. Procesorul din computerul tău execută circa 3–5 miliarde de operații pe secundă. Deci o buclă `for` cu un miliard de repetări durează sub o secundă! JavaScript nu e chiar atât de rapid (fiind interpretat, nu compilat), dar tot poate face milioane de repetări pe secundă.

📦 **Funcțiile au fost inventate matematic** în secolul al XIX-lea de matematicieni ca Gottlob Frege. Conceptul de funcție din programare (intrare → procesare → ieșire) este identic cu cel din matematică: f(x) = x². Când scrii `const dublu = n => n * 2`, faci exact ce a făcut Frege, dar pe computer!

🏗️ **Codul repetat este dușmanul programatorului.** Există un principiu celebru în programare: **DRY** — Don't Repeat Yourself (Nu te repeta). De fiecare dată când te trezești scriind același cod de două ori, ar trebui să-l pui într-o funcție. Funcțiile sunt instrumentul principal pentru a respecta DRY.

---

## Recapitulare — Ce ai învățat în Capitolul 6

```
  ✅ if / else — ramificarea codului pe baza unei condiții
  ✅ else if — mai multe ramuri (verificate în ordine)
  ✅ Operatori de comparare: ===, !==, >, <, >=, <=
  ✅ === (strict) vs == (slab) — folosește mereu ===
  ✅ Operatori logici: && (ȘI), || (SAU), ! (NU)
  ✅ Bucla for — repetă de un număr cunoscut de ori
  ✅ Bucla while — repetă cât timp condiția e adevărată
  ✅ break (oprește bucla) și continue (sari la pasul următor)
  ✅ Funcții: function numeFunctie(parametri) { ... }
  ✅ Parametri = ingredientele funcției
  ✅ return = rezultatul pe care funcția îl dă înapoi
  ✅ Funcții arrow: const f = (x) => x * 2
  ✅ Operatorul ternar: condiție ? daTrue : daFalse
  ✅ DRY — Don't Repeat Yourself
  ✅ Ai creat un calculator de statistici pentru joc! 🎮
```

---

## Ce urmează?

În **Capitolul 7: DOM — JavaScript învață să atingă pagina**, vei face ceva magic: JavaScript va ieși din consolă și va începe să **modifice pagina direct pe ecran**. Vei selecta elemente HTML, le vei schimba textul, culorile, le vei face să dispară sau să apară. Și cel mai important — vei învăța **evenimente**: ce se întâmplă când utilizatorul face click, scrie text sau mișcă mouse-ul.

Aceasta este momentul în care programarea devine **vizibilă**! 👀

---

> *„Măsura inteligenței este abilitatea de a te schimba."*
> — Albert Einstein
