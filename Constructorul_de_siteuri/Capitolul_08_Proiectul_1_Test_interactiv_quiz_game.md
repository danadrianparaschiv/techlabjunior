# Capitolul 8: Proiectul 1 — Quiz Game 🧠

> *„Spune-mi și voi uita. Arată-mi și poate voi reține. Implică-mă și voi înțelege."*
> — Confucius

---

## Ce vei construi în acest capitol

Un **joc de quiz complet** — nu un exercițiu, ci un proiect real pe care îl poți arăta prietenilor!

```
  ┌─────────────────────────────────────────────┐
  │                                             │
  │   🧠 Quiz de Cultură Generală              │
  │                                             │
  │   ╔═══════════════════════════════════════╗ │
  │   ║         Întrebarea 3 din 8           ║ │
  │   ╚═══════════════════════════════════════╝ │
  │   ┌───────────────────────────────────────┐ │
  │   │ ██████████░░░░░░░░░░░░░ 37%          │ │
  │   └───────────────────────────────────────┘ │
  │                                             │
  │   Care este cel mai mare ocean              │
  │   de pe Pământ?                             │
  │                                             │
  │   ┌───────────────────────────────────────┐ │
  │   │  A) Oceanul Atlantic                  │ │
  │   ├───────────────────────────────────────┤ │
  │   │  B) Oceanul Pacific            ✅    │ │
  │   ├───────────────────────────────────────┤ │
  │   │  C) Oceanul Indian                   │ │
  │   ├───────────────────────────────────────┤ │
  │   │  D) Oceanul Arctic                   │ │
  │   └───────────────────────────────────────┘ │
  │                                             │
  │   Scor: ⭐ 2/3                              │
  │                                             │
  └─────────────────────────────────────────────┘
```

### Ce va include jocul:

- **Ecran de start** cu buton de pornire
- **Întrebări** cu 4 opțiuni de răspuns
- **Feedback vizual** — verde pentru corect, roșu pentru greșit
- **Bară de progres** care avansează la fiecare întrebare
- **Scor** actualizat în timp real
- **Ecran de final** cu rezultatul, mesaj personalizat și buton de rejucare

### Ce vei practica din capitolele anterioare

```
  Cap. 2-3:  HTML + CSS     →  Structura și designul jocului
  Cap. 4:    Flexbox         →  Layout-ul cardurilor și butoanelor
  Cap. 5:    Variabile       →  Stocarea scorului, întrebării curente
  Cap. 6:    if/else, bucle  →  Verificarea răspunsurilor, logica jocului
  Cap. 6:    Funcții         →  Organizarea codului pe responsabilități
  Cap. 7:    DOM + Evenimente→  Afișarea întrebărilor, click pe răspunsuri
```

---

## 8.1 Planificarea — Gândește înainte de a coda

Programatorii profesioniști nu sar direct la cod. Mai întâi **planifică**. Hai să descompunem proiectul:

### Structura vizuală (ce vede utilizatorul)

```
  ECRANUL 1: START               ECRANUL 2: ÎNTREBARE
  ──────────────────             ───────────────────────
  ┌──────────────────┐           ┌──────────────────┐
  │                  │           │ Întrebarea 3/8   │
  │  🧠 Quiz Game   │           │ [████████░░░░] 37%│
  │                  │           │                  │
  │  8 întrebări     │           │ Care este...?    │
  │  de cultură      │           │                  │
  │  generală        │  click    │ ┌──────────────┐ │
  │                  │ ──────►   │ │ A) Răspuns 1 │ │
  │  [🚀 Începe!]   │           │ │ B) Răspuns 2 │ │
  │                  │           │ │ C) Răspuns 3 │ │
  └──────────────────┘           │ │ D) Răspuns 4 │ │
                                 │ └──────────────┘ │
  ECRANUL 3: REZULTAT            │ Scor: ⭐ 2/3    │
  ──────────────────             └──────────────────┘
  ┌──────────────────┐
  │                  │
  │  🏆 Felicitări!  │
  │                  │
  │  Scor: 6/8       │
  │  (75%)           │
  │                  │
  │  "Foarte bine!"  │
  │                  │
  │  [🔄 Rejoacă]   │
  │                  │
  └──────────────────┘
```

### Logica jocului (ce face codul)

```
  START
    │
    ▼
  Afișează ecranul de start
    │
    ▼ (click "Începe")
  ┌─────────────────────────────┐
  │  Afișează întrebarea curentă │◄─────────┐
  │  Afișează cele 4 opțiuni    │           │
  │  Actualizează bara de progres│           │
  └──────────────┬──────────────┘           │
                 │                           │
                 ▼ (click pe un răspuns)     │
           ┌─────────────┐                  │
           │ E corect?   │                  │
           └──────┬──────┘                  │
            DA    │    NU                   │
            │     │     │                   │
            ▼     │     ▼                   │
         Verde    │   Roșu                  │
        scor++    │   (arată                │
                  │   răspunsul             │
                  │   corect)               │
                  │     │                   │
                  ▼     ▼                   │
           ┌─────────────────┐              │
           │  Mai sunt       │              │
           │  întrebări?     │              │
           └──────┬──────────┘              │
            DA    │    NU                   │
            │           │                   │
            └───────────┘                   │
            (treci la                       │
             următoarea) ───────────────────┘
                        NU
                         │
                         ▼
                  Afișează ecranul
                  de rezultat
```

### Structura datelor (cum stocăm întrebările)

Fiecare întrebare are: textul, 4 opțiuni, și indexul răspunsului corect. Le vom stoca într-un **array de obiecte** — un concept nou pe care îl vom explica pe parcurs.

---

## 8.2 Pas 1: Structura HTML

Creează structura proiectului:

```
  📁 quiz-game/
  ├── index.html
  ├── stil.css
  └── script.js
```

### `index.html`:

```html
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz Game 🧠</title>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="stil.css">
</head>
<body>

    <div class="container">

        <!-- ══════ ECRANUL DE START ══════ -->
        <div id="ecran-start" class="ecran">
            <div class="start-icon">🧠</div>
            <h1>Quiz Game</h1>
            <p class="start-descriere">Testează-ți cunoștințele cu 
            <strong>8 întrebări</strong> de cultură generală!</p>
            <button id="btn-start" class="btn btn-mare">🚀 Începe quiz-ul!</button>
        </div>

        <!-- ══════ ECRANUL ÎNTREBĂRII ══════ -->
        <div id="ecran-intrebare" class="ecran ascuns">
            
            <!-- Header cu progres -->
            <div class="quiz-header">
                <span id="numar-intrebare" class="numar-intrebare">Întrebarea 1 din 8</span>
                <span id="scor-curent" class="scor-curent">⭐ 0</span>
            </div>

            <!-- Bara de progres -->
            <div class="bara-progres-container">
                <div id="bara-progres" class="bara-progres" style="width: 0%"></div>
            </div>

            <!-- Întrebarea -->
            <h2 id="text-intrebare" class="text-intrebare">Întrebarea va apărea aici...</h2>

            <!-- Opțiunile de răspuns -->
            <div id="optiuni" class="optiuni">
                <button class="btn-optiune" data-index="0">Opțiunea A</button>
                <button class="btn-optiune" data-index="1">Opțiunea B</button>
                <button class="btn-optiune" data-index="2">Opțiunea C</button>
                <button class="btn-optiune" data-index="3">Opțiunea D</button>
            </div>

            <!-- Feedback după răspuns -->
            <div id="feedback" class="feedback ascuns">
                <p id="feedback-text"></p>
                <button id="btn-urmatoarea" class="btn btn-urmatoarea">Următoarea →</button>
            </div>
        </div>

        <!-- ══════ ECRANUL DE REZULTAT ══════ -->
        <div id="ecran-rezultat" class="ecran ascuns">
            <div id="rezultat-icon" class="rezultat-icon">🏆</div>
            <h1 id="rezultat-titlu">Felicitări!</h1>
            <div class="rezultat-scor">
                <span id="rezultat-numar" class="rezultat-numar">0/8</span>
                <span id="rezultat-procent" class="rezultat-procent">0%</span>
            </div>
            <div class="rezultat-bara-container">
                <div id="rezultat-bara" class="rezultat-bara" style="width: 0%"></div>
            </div>
            <p id="rezultat-mesaj" class="rezultat-mesaj">Mesajul va apărea aici...</p>
            <button id="btn-rejuca" class="btn btn-mare">🔄 Joacă din nou</button>
        </div>

    </div>

    <script src="script.js"></script>
</body>
</html>
```

### Ce observi?

Pagina are **3 ecrane** (`div`-uri cu clasa `ecran`), dar doar unul e vizibil la un moment dat. Celelalte au clasa `ascuns` (`display: none`). JavaScript le va arăta/ascunde:

```
  La start:      ecran-start ✅    ecran-intrebare ❌    ecran-rezultat ❌
  La joc:        ecran-start ❌    ecran-intrebare ✅    ecran-rezultat ❌
  La final:      ecran-start ❌    ecran-intrebare ❌    ecran-rezultat ✅
```

Alt lucru nou: atributul `data-index` pe butoane. Acesta este un **atribut personalizat** (custom data attribute) — o modalitate de a stoca informații suplimentare pe un element HTML, pe care JavaScript le poate citi.

```html
<button class="btn-optiune" data-index="0">Opțiunea A</button>
<!--                        ─────────────
                            │
                            Stochează indexul opțiunii (0, 1, 2, 3)
                            JavaScript îl citește cu: element.dataset.index
-->
```

---

## 8.3 Pas 2: Stilizarea cu CSS

### `stil.css`:

```css
/* ══════════════════════════════
   RESET ȘI BAZĂ
   ══════════════════════════════ */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: "Nunito", sans-serif;
    background-color: #F0F4F8;
    color: #2C3E50;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
}

.container {
    width: 100%;
    max-width: 600px;
}

.ascuns {
    display: none !important;
}

/* ══════════════════════════════
   BUTOANE GENERALE
   ══════════════════════════════ */
.btn {
    font-family: "Fredoka", sans-serif;
    font-weight: 600;
    border: none;
    border-radius: 14px;
    cursor: pointer;
    transition: background-color 0.2s, transform 0.1s;
}

.btn:hover {
    transform: translateY(-2px);
}

.btn:active {
    transform: translateY(0);
}

.btn-mare {
    display: block;
    width: 100%;
    padding: 18px;
    font-size: 20px;
    background-color: #5A67D8;
    color: white;
    margin-top: 20px;
}

.btn-mare:hover {
    background-color: #434190;
}

/* ══════════════════════════════
   ECRANUL DE START
   ══════════════════════════════ */
#ecran-start {
    text-align: center;
    background-color: white;
    border-radius: 20px;
    padding: 50px 30px;
    border: 1px solid #E2E8F0;
}

.start-icon {
    font-size: 72px;
    margin-bottom: 15px;
}

#ecran-start h1 {
    font-family: "Fredoka", sans-serif;
    font-size: 40px;
    color: #5A67D8;
    margin-bottom: 12px;
}

.start-descriere {
    font-size: 17px;
    color: #718096;
    margin-bottom: 10px;
    line-height: 1.6;
}

/* ══════════════════════════════
   ECRANUL ÎNTREBĂRII
   ══════════════════════════════ */
#ecran-intrebare {
    background-color: white;
    border-radius: 20px;
    padding: 30px;
    border: 1px solid #E2E8F0;
}

/* Header */
.quiz-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 14px;
}

.numar-intrebare {
    font-size: 14px;
    color: #718096;
    font-weight: 600;
}

.scor-curent {
    font-family: "Fredoka", sans-serif;
    font-size: 16px;
    color: #5A67D8;
    font-weight: 700;
}

/* Bara de progres */
.bara-progres-container {
    width: 100%;
    height: 8px;
    background-color: #EDF2F7;
    border-radius: 4px;
    margin-bottom: 28px;
    overflow: hidden;
}

.bara-progres {
    height: 100%;
    background: linear-gradient(90deg, #667eea, #5A67D8);
    border-radius: 4px;
    transition: width 0.4s ease;
}

/* Întrebarea */
.text-intrebare {
    font-family: "Fredoka", sans-serif;
    font-size: 22px;
    color: #2D3748;
    margin-bottom: 24px;
    line-height: 1.4;
}

/* Opțiunile */
.optiuni {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.btn-optiune {
    width: 100%;
    padding: 16px 20px;
    font-family: "Nunito", sans-serif;
    font-size: 16px;
    font-weight: 600;
    text-align: left;
    background-color: #F7FAFC;
    color: #2D3748;
    border: 2px solid #E2E8F0;
    border-radius: 12px;
    cursor: pointer;
    transition: border-color 0.2s, background-color 0.2s, transform 0.1s;
}

.btn-optiune:hover:not(.dezactivat) {
    border-color: #5A67D8;
    background-color: #EBF4FF;
    transform: translateX(4px);
}

/* Stări după răspuns */
.btn-optiune.corect {
    background-color: #F0FFF4;
    border-color: #48BB78;
    color: #276749;
}

.btn-optiune.gresit {
    background-color: #FFF5F5;
    border-color: #FC8181;
    color: #9B2C2C;
}

.btn-optiune.dezactivat {
    cursor: default;
    opacity: 0.6;
}

.btn-optiune.dezactivat:hover {
    transform: none;
}

/* Feedback */
.feedback {
    margin-top: 20px;
    padding: 16px 20px;
    border-radius: 12px;
    text-align: center;
}

.feedback.corect {
    background-color: #F0FFF4;
    border: 1px solid #C6F6D5;
}

.feedback.gresit {
    background-color: #FFF5F5;
    border: 1px solid #FED7D7;
}

#feedback-text {
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 12px;
}

.btn-urmatoarea {
    padding: 12px 30px;
    font-size: 16px;
    background-color: #5A67D8;
    color: white;
}

.btn-urmatoarea:hover {
    background-color: #434190;
}

/* ══════════════════════════════
   ECRANUL DE REZULTAT
   ══════════════════════════════ */
#ecran-rezultat {
    text-align: center;
    background-color: white;
    border-radius: 20px;
    padding: 45px 30px;
    border: 1px solid #E2E8F0;
}

.rezultat-icon {
    font-size: 64px;
    margin-bottom: 10px;
}

#ecran-rezultat h1 {
    font-family: "Fredoka", sans-serif;
    font-size: 34px;
    color: #2D3748;
    margin-bottom: 24px;
}

.rezultat-scor {
    display: flex;
    justify-content: center;
    align-items: baseline;
    gap: 15px;
    margin-bottom: 16px;
}

.rezultat-numar {
    font-family: "Fredoka", sans-serif;
    font-size: 48px;
    font-weight: 700;
    color: #5A67D8;
}

.rezultat-procent {
    font-size: 22px;
    color: #718096;
    font-weight: 600;
}

.rezultat-bara-container {
    width: 80%;
    max-width: 350px;
    height: 12px;
    background-color: #EDF2F7;
    border-radius: 6px;
    margin: 0 auto 24px;
    overflow: hidden;
}

.rezultat-bara {
    height: 100%;
    border-radius: 6px;
    transition: width 1s ease;
}

.rezultat-mesaj {
    font-size: 17px;
    color: #4A5568;
    line-height: 1.6;
    margin-bottom: 5px;
}

/* ══════════════════════════════
   RESPONSIVE
   ══════════════════════════════ */
@media (max-width: 480px) {
    #ecran-start {
        padding: 35px 20px;
    }

    .start-icon {
        font-size: 56px;
    }

    #ecran-start h1 {
        font-size: 30px;
    }

    .text-intrebare {
        font-size: 19px;
    }

    .btn-optiune {
        padding: 14px 16px;
        font-size: 15px;
    }
    
    .rezultat-numar {
        font-size: 40px;
    }
}
```

---

## 8.4 Concept nou: Array-uri (liste) — Depozitul de întrebări

Înainte de a scrie logica jocului, trebuie să înveți un concept nou esențial: **array-urile** (listele).

Un **array** este o **listă ordonată** de valori. Gândește-te la el ca la un **tren** cu vagoane numerotate:

```
  Index:     0           1          2           3
           ┌───┐      ┌───┐      ┌───┐      ┌───┐
  Array:   │ 🍎│──────│ 🍊│──────│ 🍋│──────│ 🍇│
           └───┘      └───┘      └───┘      └───┘
           primul     al doilea   al treilea  ultimul
           element    element     element     element
```

### Cum creezi un array

```javascript
// Array de numere
let scoruri = [450, 720, 380, 910];

// Array de texte
let culori = ["roșu", "verde", "albastru"];

// Array de orice
let mixt = ["Maria", 14, true, null];
```

### Cum accesezi elemente

```javascript
let fructe = ["măr", "portocală", "lămâie", "strugure"];

console.log(fructe[0]);      // "măr"        (primul — index 0!)
console.log(fructe[1]);      // "portocală"
console.log(fructe[3]);      // "strugure"   (ultimul)
console.log(fructe.length);  // 4            (câte elemente are)
```

### Proprietăți utile

```javascript
let fructe = ["măr", "portocală", "lămâie"];

// Lungimea
console.log(fructe.length);           // 3

// Adaugă la final
fructe.push("strugure");             // ["măr", "portocală", "lămâie", "strugure"]

// Parcurge cu for
for (let i = 0; i < fructe.length; i++) {
    console.log(`${i}: ${fructe[i]}`);
}
```

### Obiecte — Fișe cu mai multe informații

Un **obiect** este ca o **fișă** care grupează mai multe informații legate între ele:

```javascript
// O singură întrebare — ca o fișă de examen
let intrebare = {
    text: "Care este capitala Franței?",
    optiuni: ["Berlin", "Paris", "Roma", "Madrid"],
    raspunsCorect: 1     // indexul 1 = "Paris"
};

// Accesăm proprietățile cu punct
console.log(intrebare.text);              // "Care este capitala Franței?"
console.log(intrebare.optiuni[1]);        // "Paris"
console.log(intrebare.raspunsCorect);     // 1
```

```
  Obiectul "intrebare":
  ┌─────────────────────────────────────────────┐
  │                                             │
  │  text: "Care este capitala Franței?"        │
  │                                             │
  │  optiuni: ["Berlin","Paris","Roma","Madrid"]│
  │             [0]      [1]    [2]    [3]     │
  │                                             │
  │  raspunsCorect: 1  (→ "Paris")             │
  │                                             │
  └─────────────────────────────────────────────┘
```

### Array de obiecte — Lista completă de întrebări

Combinăm array-urile cu obiectele: un **array care conține mai multe obiecte**. Este ca un **dosar** cu mai multe fișe:

```javascript
let intrebari = [
    {
        text: "Care este capitala Franței?",
        optiuni: ["Berlin", "Paris", "Roma", "Madrid"],
        raspunsCorect: 1
    },
    {
        text: "Câte continente are Pământul?",
        optiuni: ["5", "6", "7", "8"],
        raspunsCorect: 2
    }
];

// Accesăm prima întrebare
console.log(intrebari[0].text);           // "Care este capitala Franței?"
console.log(intrebari[0].optiuni[1]);     // "Paris"

// Accesăm a doua întrebare
console.log(intrebari[1].text);           // "Câte continente are Pământul?"
```

```
  intrebari (array):
  
  Index 0:                          Index 1:
  ┌───────────────────────┐        ┌───────────────────────┐
  │ text: "Care este..."  │        │ text: "Câte conti..." │
  │ optiuni: [...]        │        │ optiuni: [...]        │
  │ raspunsCorect: 1      │        │ raspunsCorect: 2      │
  └───────────────────────┘        └───────────────────────┘
```

Acum ai tot ce trebuie pentru a înțelege logica quiz-ului!

---

## 8.5 Pas 3: Logica JavaScript — Creierul jocului

### `script.js`:

```javascript
// ══════════════════════════════════════════════
// 🧠 QUIZ GAME — SCRIPT PRINCIPAL
// ══════════════════════════════════════════════


// ── DATELE QUIZ-ULUI ── 
// Array de obiecte: fiecare obiect = o întrebare

const intrebari = [
    {
        text: "Care este cel mai mare ocean de pe Pământ?",
        optiuni: [
            "Oceanul Atlantic",
            "Oceanul Pacific",
            "Oceanul Indian",
            "Oceanul Arctic"
        ],
        raspunsCorect: 1
    },
    {
        text: "În ce an a aterizat primul om pe Lună?",
        optiuni: [
            "1965",
            "1969",
            "1972",
            "1959"
        ],
        raspunsCorect: 1
    },
    {
        text: "Care este cea mai lungă serie de numere: PI sau numărul lui Euler (e)?",
        optiuni: [
            "PI",
            "Numărul lui Euler",
            "Sunt la fel de lungi",
            "Ambele sunt infinite"
        ],
        raspunsCorect: 3
    },
    {
        text: "Ce limbaj de programare a fost creat în doar 10 zile?",
        optiuni: [
            "Python",
            "Java",
            "JavaScript",
            "C++"
        ],
        raspunsCorect: 2
    },
    {
        text: "Câte oase are corpul uman adult?",
        optiuni: [
            "186",
            "206",
            "226",
            "256"
        ],
        raspunsCorect: 1
    },
    {
        text: "Ce element chimic are simbolul 'O'?",
        optiuni: [
            "Aur",
            "Osmiu",
            "Oxigen",
            "Oțel"
        ],
        raspunsCorect: 2
    },
    {
        text: "Care este cea mai vorbită limbă din lume (ca limbă maternă)?",
        optiuni: [
            "Engleză",
            "Spaniolă",
            "Hindi",
            "Chineză Mandarină"
        ],
        raspunsCorect: 3
    },
    {
        text: "Ce tag HTML creează un link către altă pagină?",
        optiuni: [
            "&lt;link&gt;",
            "&lt;a&gt;",
            "&lt;href&gt;",
            "&lt;url&gt;"
        ],
        raspunsCorect: 1
    }
];


// ── STAREA JOCULUI ──
// Variabile care se schimbă pe parcursul jocului

let intrebareCurenta = 0;    // indexul întrebării afișate (0-7)
let scor = 0;                // câte răspunsuri corecte
let aRaspuns = false;        // a ales deja un răspuns la întrebarea curentă?


// ── SELECTĂM ELEMENTELE DIN DOM ──

// Ecranele
const ecranStart = document.querySelector("#ecran-start");
const ecranIntrebare = document.querySelector("#ecran-intrebare");
const ecranRezultat = document.querySelector("#ecran-rezultat");

// Elementele din ecranul întrebării
const numarIntrebare = document.querySelector("#numar-intrebare");
const scorCurent = document.querySelector("#scor-curent");
const baraProgres = document.querySelector("#bara-progres");
const textIntrebare = document.querySelector("#text-intrebare");
const containerOptiuni = document.querySelector("#optiuni");
const btnOptiuni = document.querySelectorAll(".btn-optiune");
const feedback = document.querySelector("#feedback");
const feedbackText = document.querySelector("#feedback-text");
const btnUrmatoarea = document.querySelector("#btn-urmatoarea");

// Elementele din ecranul de rezultat
const rezultatIcon = document.querySelector("#rezultat-icon");
const rezultatTitlu = document.querySelector("#rezultat-titlu");
const rezultatNumar = document.querySelector("#rezultat-numar");
const rezultatProcent = document.querySelector("#rezultat-procent");
const rezultatBara = document.querySelector("#rezultat-bara");
const rezultatMesaj = document.querySelector("#rezultat-mesaj");

// Butoanele de navigare
const btnStart = document.querySelector("#btn-start");
const btnRejuca = document.querySelector("#btn-rejuca");


// ══════════════════════════════════════════════
// FUNCȚII
// ══════════════════════════════════════════════


// ── Schimbă ecranul vizibil ──
function arataEcran(ecranDeAratat) {
    // Ascunde toate ecranele
    ecranStart.classList.add("ascuns");
    ecranIntrebare.classList.add("ascuns");
    ecranRezultat.classList.add("ascuns");
    
    // Arată doar ecranul dorit
    ecranDeAratat.classList.remove("ascuns");
}


// ── Afișează întrebarea curentă ──
function afiseazaIntrebare() {
    // Preia datele întrebării curente din array
    let intrebare = intrebari[intrebareCurenta];
    
    // Actualizează header-ul
    numarIntrebare.textContent = `Întrebarea ${intrebareCurenta + 1} din ${intrebari.length}`;
    scorCurent.textContent = `⭐ ${scor}`;
    
    // Actualizează bara de progres
    let procent = (intrebareCurenta / intrebari.length) * 100;
    baraProgres.style.width = `${procent}%`;
    
    // Afișează textul întrebării
    textIntrebare.innerHTML = intrebare.text;
    
    // Afișează opțiunile pe butoane
    let litere = ["A", "B", "C", "D"];
    for (let i = 0; i < btnOptiuni.length; i++) {
        btnOptiuni[i].innerHTML = `${litere[i]}) ${intrebare.optiuni[i]}`;
        
        // Resetează stilurile (elimină clasele de la întrebarea anterioară)
        btnOptiuni[i].classList.remove("corect", "gresit", "dezactivat");
    }
    
    // Ascunde feedback-ul
    feedback.classList.add("ascuns");
    feedback.classList.remove("corect", "gresit");
    
    // Resetează starea
    aRaspuns = false;
}


// ── Verifică răspunsul ales ──
function verificaRaspuns(indexAles) {
    // Dacă a răspuns deja, nu face nimic
    if (aRaspuns) return;
    aRaspuns = true;
    
    let intrebare = intrebari[intrebareCurenta];
    let esteCorect = indexAles === intrebare.raspunsCorect;
    
    // Evidențiază răspunsul corect (mereu verde)
    btnOptiuni[intrebare.raspunsCorect].classList.add("corect");
    
    if (esteCorect) {
        // Răspuns corect!
        scor++;
        scorCurent.textContent = `⭐ ${scor}`;
        
        feedbackText.textContent = "✅ Corect! Bravo!";
        feedback.classList.add("corect");
    } else {
        // Răspuns greșit
        btnOptiuni[indexAles].classList.add("gresit");
        
        let raspunsCorectText = intrebare.optiuni[intrebare.raspunsCorect];
        feedbackText.textContent = `❌ Greșit! Răspunsul corect era: ${raspunsCorectText}`;
        feedback.classList.add("gresit");
    }
    
    // Dezactivează toate butoanele
    for (let i = 0; i < btnOptiuni.length; i++) {
        btnOptiuni[i].classList.add("dezactivat");
    }
    
    // Arată feedback-ul
    feedback.classList.remove("ascuns");
    
    // Schimbă textul butonului dacă e ultima întrebare
    if (intrebareCurenta === intrebari.length - 1) {
        btnUrmatoarea.textContent = "Vezi rezultatul 🏆";
    } else {
        btnUrmatoarea.textContent = "Următoarea →";
    }
}


// ── Treci la următoarea întrebare (sau la rezultat) ──
function urmatoareaIntrebare() {
    intrebareCurenta++;
    
    if (intrebareCurenta < intrebari.length) {
        // Mai sunt întrebări
        afiseazaIntrebare();
    } else {
        // S-au terminat — arată rezultatul
        afiseazaRezultat();
    }
}


// ── Afișează ecranul de rezultat ──
function afiseazaRezultat() {
    arataEcran(ecranRezultat);
    
    let totalIntrebari = intrebari.length;
    let procent = Math.round((scor / totalIntrebari) * 100);
    
    // Scorul numeric
    rezultatNumar.textContent = `${scor}/${totalIntrebari}`;
    rezultatProcent.textContent = `${procent}%`;
    
    // Bara de progres (cu animație)
    setTimeout(function() {
        rezultatBara.style.width = `${procent}%`;
    }, 100);
    
    // Culoarea barei în funcție de scor
    if (procent >= 80) {
        rezultatBara.style.background = "linear-gradient(90deg, #48BB78, #38A169)";
    } else if (procent >= 50) {
        rezultatBara.style.background = "linear-gradient(90deg, #ECC94B, #D69E2E)";
    } else {
        rezultatBara.style.background = "linear-gradient(90deg, #FC8181, #E53E3E)";
    }
    
    // Icon, titlu și mesaj personalizat
    if (procent === 100) {
        rezultatIcon.textContent = "🏆";
        rezultatTitlu.textContent = "Perfecțiune!";
        rezultatMesaj.textContent = "Scor perfect! Ești un adevărat geniu! Nicio greșeală!";
    } else if (procent >= 80) {
        rezultatIcon.textContent = "🌟";
        rezultatTitlu.textContent = "Excelent!";
        rezultatMesaj.textContent = "Impresionant! Ai cunoștințe solide de cultură generală!";
    } else if (procent >= 60) {
        rezultatIcon.textContent = "👏";
        rezultatTitlu.textContent = "Foarte bine!";
        rezultatMesaj.textContent = "Bun rezultat! Mai exersează și vei ajunge la scor maxim!";
    } else if (procent >= 40) {
        rezultatIcon.textContent = "💪";
        rezultatTitlu.textContent = "Bine!";
        rezultatMesaj.textContent = "Un start promițător! Citește mai mult și încearcă din nou!";
    } else {
        rezultatIcon.textContent = "📚";
        rezultatTitlu.textContent = "Mai încearcă!";
        rezultatMesaj.textContent = "Nu te descuraja! Fiecare încercare te face mai bun!";
    }
}


// ── Resetează și repornește jocul ──
function resetJoc() {
    intrebareCurenta = 0;
    scor = 0;
    aRaspuns = false;
    rezultatBara.style.width = "0%";
    
    arataEcran(ecranIntrebare);
    afiseazaIntrebare();
}


// ══════════════════════════════════════════════
// EVENIMENTE
// ══════════════════════════════════════════════


// Butonul "Începe quiz-ul"
btnStart.addEventListener("click", function() {
    arataEcran(ecranIntrebare);
    afiseazaIntrebare();
});

// Click pe opțiunile de răspuns (delegare de evenimente)
containerOptiuni.addEventListener("click", function(e) {
    // Verifică dacă s-a apăsat pe un buton de opțiune
    if (e.target.classList.contains("btn-optiune")) {
        let indexAles = Number(e.target.dataset.index);
        verificaRaspuns(indexAles);
    }
});

// Butonul "Următoarea"
btnUrmatoarea.addEventListener("click", urmatoareaIntrebare);

// Butonul "Joacă din nou"
btnRejuca.addEventListener("click", resetJoc);
```

---

## 8.6 Cum funcționează — Explicație pas cu pas

Hai să urmărim ce se întâmplă de la start până la final:

### Pasul 1: Pornirea jocului

```
  Utilizatorul apasă "🚀 Începe quiz-ul!"
  │
  ▼
  btnStart → addEventListener("click") → se execută:
  │
  ├── arataEcran(ecranIntrebare)
  │   ├── Ascunde ecran-start
  │   └── Arată ecran-intrebare
  │
  └── afiseazaIntrebare()
      ├── intrebari[0] → prima întrebare
      ├── Actualizează "Întrebarea 1 din 8"
      ├── Actualizează "⭐ 0"
      ├── Bara de progres → 0%
      ├── Afișează textul întrebării
      └── Afișează cele 4 opțiuni pe butoane
```

### Pasul 2: Alegerea unui răspuns

```
  Utilizatorul apasă "B) Oceanul Pacific"
  │
  ▼
  containerOptiuni → addEventListener("click")
  │
  ├── e.target = butonul apăsat
  ├── e.target.dataset.index = "1"
  ├── Number("1") = 1
  │
  └── verificaRaspuns(1)
      │
      ├── intrebari[0].raspunsCorect = 1
      ├── 1 === 1? → DA! E corect!
      │
      ├── scor++ → scor devine 1
      ├── Butonul B devine VERDE (clasa "corect")
      ├── Feedback: "✅ Corect! Bravo!"
      ├── Toate butoanele devin "dezactivat"
      └── Apare butonul "Următoarea →"
```

### Pasul 3: Următoarea întrebare

```
  Utilizatorul apasă "Următoarea →"
  │
  ▼
  urmatoareaIntrebare()
  │
  ├── intrebareCurenta++ → devine 1
  ├── 1 < 8? → DA, mai sunt întrebări
  │
  └── afiseazaIntrebare()
      ├── intrebari[1] → a doua întrebare
      ├── "Întrebarea 2 din 8"
      ├── Bara → 12.5%
      ├── Resetează stilurile butoanelor
      └── Ascunde feedback-ul
```

### Pasul 4: Ultima întrebare și rezultatul

```
  intrebareCurenta = 7 (ultima)
  Utilizatorul răspunde
  │
  ▼
  Butonul arată "Vezi rezultatul 🏆" (nu "Următoarea →")
  │
  ▼ (click)
  urmatoareaIntrebare()
  │
  ├── intrebareCurenta++ → devine 8
  ├── 8 < 8? → NU! S-au terminat!
  │
  └── afiseazaRezultat()
      ├── Calculează procentul: scor / 8 * 100
      ├── Afișează scorul și procentul
      ├── Animează bara de rezultat
      ├── Alege icon, titlu și mesaj personalizat
      └── Arată butonul "🔄 Joacă din nou"
```

---

## 8.7 Concepte cheie explicate

### Schimbarea ecranelor cu clase

Întregul quiz are 3 „ecrane", dar de fapt sunt 3 div-uri pe aceeași pagină. Trucul e simplu — clasa `ascuns` (cu `display: none`) le face invizibile:

```javascript
function arataEcran(ecranDeAratat) {
    // 1. Ascunde TOATE ecranele
    ecranStart.classList.add("ascuns");
    ecranIntrebare.classList.add("ascuns");
    ecranRezultat.classList.add("ascuns");
    
    // 2. Arată doar unul
    ecranDeAratat.classList.remove("ascuns");
}

// Utilizare:
arataEcran(ecranIntrebare);    // arată întrebarea
arataEcran(ecranRezultat);     // arată rezultatul
```

Aceasta este o tehnică foarte comună în aplicațiile web — se numește **SPA** (Single Page Application): o singură pagină HTML în care „navigarea" se face prin arătarea/ascunderea secțiunilor.

### `dataset` — Citirea atributelor `data-*`

```html
<button class="btn-optiune" data-index="2">C) Opțiunea</button>
```

```javascript
element.dataset.index    // "2" (string!)
Number(element.dataset.index)   // 2 (number — convertit)
```

Orice atribut `data-ceva` din HTML devine `element.dataset.ceva` în JavaScript. Este o modalitate curată de a stoca informații pe elemente.

### Variabila „semafor" (`aRaspuns`)

```javascript
let aRaspuns = false;

function verificaRaspuns(indexAles) {
    if (aRaspuns) return;    // STOP — a răspuns deja!
    aRaspuns = true;         // Marchează că a răspuns
    
    // ... restul logicii
}
```

Fără acest „semafor", utilizatorul ar putea apăsa pe mai multe răspunsuri și ar primi puncte multiple pentru aceeași întrebare. `aRaspuns` acționează ca un **lacăt**: odată închis, nu mai poți intra.

### Buclă `for` pentru resetarea butoanelor

```javascript
for (let i = 0; i < btnOptiuni.length; i++) {
    btnOptiuni[i].classList.remove("corect", "gresit", "dezactivat");
}
```

La fiecare întrebare nouă, trebuie să „curățăm" butoanele de clasele vizuale ale întrebării anterioare. Bucla parcurge toate cele 4 butoane și le resetează.

---

## 8.8 Provocări — Extinde jocul! 🚀

Acum că ai un quiz funcțional, iată câteva idei de îmbunătățire. Încearcă-le singur înainte de a căuta soluții!

### 🟢 Ușor: Adaugă mai multe întrebări

Adaugă încă 4 întrebări la array-ul `intrebari`. Actualizează textele din HTML dacă era menționat „8 întrebări".

### 🟡 Mediu: Amestecă ordinea întrebărilor

Adaugă această funcție și apeleaz-o la începutul jocului:

```javascript
// Amestecă un array (algoritm Fisher-Yates)
function amesteca(array) {
    for (let i = array.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));
        // Interschimbă elementele i și j
        let temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}

// Folosire: amestecă întrebările la fiecare joc nou
function resetJoc() {
    intrebareCurenta = 0;
    scor = 0;
    aRaspuns = false;
    amesteca(intrebari);     // ← ordinea se schimbă!
    // ... restul codului
}
```

`Math.random()` generează un număr aleatoriu între 0 și 1. `Math.floor()` rotunjește în jos. Împreună, creează un index aleatoriu. Algoritmul **Fisher-Yates** este cel mai eficient mod de a amesteca o listă — aceeași tehnică e folosită de jocurile de cărți digitale!

### 🟡 Mediu: Timer per întrebare

Adaugă un cronometru de 15 secunde pentru fiecare întrebare:

```javascript
let timerID = null;
let secundeRamase = 15;

function pornesteTimer() {
    secundeRamase = 15;
    afiseazaTimer();
    
    timerID = setInterval(function() {
        secundeRamase--;
        afiseazaTimer();
        
        if (secundeRamase <= 0) {
            clearInterval(timerID);
            verificaRaspuns(-1);    // -1 = nu a ales nimic (time's up!)
        }
    }, 1000);
}

function opresteTimer() {
    clearInterval(timerID);
}
```

### 🔴 Avansat: Categorii de întrebări

Grupează întrebările pe categorii și lasă utilizatorul să aleagă:

```javascript
const intrebariPeCategorie = {
    geografie: [ /* ... */ ],
    știință: [ /* ... */ ],
    tehnologie: [ /* ... */ ],
    istorie: [ /* ... */ ]
};
```

---

## 8.9 Greșeli frecvente (și cum le repari) 🔧

### ❌ Greșeala 1: Confuzie index vs. lungime

```javascript
let intrebari = ["A", "B", "C"];    // length = 3

// ❌ GREȘIT — indexul 3 NU există! (ultimul e 2)
console.log(intrebari[3]);           // undefined

// ✅ CORECT — ultimul element
console.log(intrebari[intrebari.length - 1]);    // "C"
```

```
  Array:    ["A", "B", "C"]
  Indexuri:   0     1     2
  Length:          3
  
  Ultimul index = length - 1 = 2
```

### ❌ Greșeala 2: Uiți să resetezi starea

```javascript
// ❌ La rejucare, scorul rămâne de la jocul anterior!
function resetJoc() {
    arataEcran(ecranIntrebare);
    afiseazaIntrebare();
    // Am uitat să resetez scor, intrebareCurenta, aRaspuns!
}

// ✅ CORECT — resetează TOT
function resetJoc() {
    intrebareCurenta = 0;
    scor = 0;
    aRaspuns = false;
    arataEcran(ecranIntrebare);
    afiseazaIntrebare();
}
```

### ❌ Greșeala 3: `dataset` returnează mereu string

```javascript
let index = e.target.dataset.index;
console.log(typeof index);     // "string"!
console.log(index === 1);      // false! ("1" !== 1)

// ✅ Convertește la number
let index = Number(e.target.dataset.index);
console.log(index === 1);      // true ✅
```

### ❌ Greșeala 4: Click multiplu pe același răspuns

```javascript
// ❌ Fără protecție — scorul crește la fiecare click!
function verificaRaspuns(indexAles) {
    if (indexAles === intrebari[intrebareCurenta].raspunsCorect) {
        scor++;    // Se adaugă de FIECARE DATĂ când faci click!
    }
}

// ✅ Cu protecție "semafor"
function verificaRaspuns(indexAles) {
    if (aRaspuns) return;    // Oprește dacă a răspuns deja
    aRaspuns = true;
    // ... restul codului
}
```

---

## 8.10 Mini-quiz — Verifică ce ai învățat! ✅

**1.** Ce este un array și cum accesezi al treilea element din el?

**2.** Cum stochezi mai multe informații legate între ele (text, opțiuni, răspuns corect) într-o singură structură de date?

**3.** Ce face `element.dataset.index`?

**4.** De ce e utilă variabila „semafor" (`aRaspuns`) în quiz?

**5.** Cum faci ca 3 div-uri diferite să funcționeze ca „ecrane" separate, afișând doar unul la un moment dat?

**6.** Ce face `Math.floor(Math.random() * 10)`?

**7.** Ce se întâmplă dacă accesezi `array[array.length]`?

---

<details>
<summary>🔑 Click aici pentru răspunsuri</summary>

1. Un **array** este o listă ordonată de valori (ex: `[10, 20, 30]`). Al treilea element se accesează cu **`array[2]`** — indexarea începe de la 0, deci al treilea element are indexul 2.

2. Cu un **obiect**: `{ text: "...", optiuni: [...], raspunsCorect: 1 }`. Obiectele grupează mai multe proprietăți (perechi cheie-valoare) într-o singură structură.

3. Citește valoarea atributului HTML personalizat `data-index`. De exemplu, `<button data-index="2">` → `element.dataset.index` returnează `"2"` (ca string).

4. Împiedică utilizatorul să **răspundă de mai multe ori** la aceeași întrebare. Fără ea, utilizatorul ar putea face click de 10 ori pe răspunsul corect și ar primi 10 puncte în loc de 1.

5. Toate cele 3 div-uri au clasa `ascuns` (cu `display: none`) în CSS. Funcția `arataEcran()` le ascunde pe **toate**, apoi elimină clasa `ascuns` doar de pe ecranul dorit. La un moment dat, doar **unul** e vizibil.

6. Generează un **număr întreg aleatoriu de la 0 la 9**. `Math.random()` dă un număr între 0 și 0.999..., multiplicat cu 10 dă 0–9.999..., iar `Math.floor()` rotunjește în jos.

7. Returnează **`undefined`**. Ultimul element valid este la indexul `array.length - 1`. Indexul `array.length` e cu 1 mai mare decât ultimul — nu există.

</details>

---

## 8.11 Știai că? — Curiozități din lumea tech 🤓

🎮 **Trivia Crack**, una dintre cele mai descărcate aplicații de quiz din lume (peste 500 de milioane de descărcări), a fost creată în 2013 de o companie argentiniană mică, Etermax. Prototipul inițial era mult mai simplu decât quiz-ul tău — dovadă că proiectele mari încep cu proiecte mici!

🧠 **Kahoot!**, platforma educațională de quiz, a fost creată de trei cercetători norvegieni în 2012. Acum o folosesc peste 9 miliarde de participanți cumulativ. Structura de bază? Exact ce ai construit tu: întrebări, opțiuni multiple, scor și feedback. Principiile sunt aceleași — doar scala diferă!

🔀 **Algoritmul Fisher-Yates** (de amestecare) a fost inventat în 1938 de Ronald Fisher și Frank Yates, mult înainte de era computerelor! Versiunea modernă a fost publicată de Richard Durstenfeld în 1964. Când amesteci cărți sau întrebări în cod, folosești un algoritm cu aproape 90 de ani de istorie.

📊 **A/B Testing** este o tehnică în care companiile arată două versiuni diferite ale unei pagini web la utilizatori diferiți pentru a vedea care funcționează mai bine. Quiz-urile și sondajele sunt printre cele mai eficiente instrumente de A/B testing — exact tipul de aplicație pe care tocmai ai construit-o!

---

## Recapitulare — Ce ai învățat în Capitolul 8

```
  CONCEPTE NOI:
  ✅ Array-uri — liste ordonate de valori ([1, 2, 3])
  ✅ Obiecte — fișe cu proprietăți ({ text: "...", optiuni: [...] })
  ✅ Array de obiecte — combinația perfectă pentru date structurate
  ✅ dataset (data-*) — atribute personalizate pe elemente HTML
  ✅ Math.random() și Math.floor() — numere aleatorii
  
  TEHNICI PRACTICATE:
  ✅ Planificarea unui proiect (ecrane, flux, date)
  ✅ Schimbarea ecranelor cu classList (SPA)
  ✅ Delegare de evenimente pe containerul de opțiuni
  ✅ Variabila „semafor" pentru a preveni acțiuni duble
  ✅ Feedback vizual (clase CSS) bazat pe logica JS
  ✅ Bară de progres actualizată dinamic
  ✅ Ecran de rezultat cu scor, procent și mesaj personalizat
  ✅ Funcții organizate pe responsabilități
  ✅ Buclă for pentru resetarea elementelor
  ✅ Animație CSS (transition) pe bara de progres
  ✅ setTimeout() pentru animația barei de rezultat
  
  PROIECT COMPLET:
  ✅ Quiz Game cu 8 întrebări, 3 ecrane, scor live! 🧠
```

---

## Ce urmează?

Felicitări, ai terminat primul proiect major! 🎉

În **Capitolul 9: Animații CSS și JavaScript**, vei învăța cum să aduci **mișcare** pe paginile tale: tranziții fluide, animații CSS cu `@keyframes`, și animații controlate cu JavaScript. Pagina ta nu va mai sta pe loc — va dansa! 💃

---

> *„Fiecare expert a fost cândva un începător."*
> — Helen Hayes
