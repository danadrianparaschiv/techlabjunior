# Capitolul 3: Îmbracă-ți pagina cu CSS — Stilul contează! 🎨

> *„Designul nu e doar cum arată. Designul e cum funcționează."*
> — Steve Jobs

---

## Ce vei învăța în acest capitol

- Ce este CSS și **unde** se scrie
- Cum funcționează **selectorii** (cui îi spui să se schimbe)
- Cum să lucrezi cu **culori** (nume, hex, RGB)
- Cum să alegi **fonturi** și dimensiuni de text
- **Modelul cutiei** (box model) — cel mai important concept din CSS!
- Cum să adaugi **chenare** (borders) și **fundaluri** (backgrounds)
- Cum să transformi pagina „Despre mine" dintr-un document plictisitor într-un site frumos

---

## 3.1 CSS — Garderoba paginii tale

Ți-aminteștii metafora din Capitolul 1?

- **HTML** = scheletul (ce există pe pagină)
- **CSS** = hainele și machiajul (cum arată)

Hai să facem asta concret. Iată aceeași pagină HTML, **fără** și **cu** CSS:

```
  ┌─────────── FĂRĂ CSS ───────────┐   ┌──────────── CU CSS ────────────┐
  │                                 │   │  ┌─────────────────────────┐   │
  │  Titlul meu                    │   │  │  ╔═══════════════════╗  │   │
  │                                 │   │  │  ║   Titlul meu     ║  │   │
  │  Un paragraf de text simplu.   │   │  │  ╚═══════════════════╝  │   │
  │                                 │   │  │                         │   │
  │  • Element 1                   │   │  │  Un paragraf de text    │   │
  │  • Element 2                   │   │  │  stilizat frumos.       │   │
  │  • Element 3                   │   │  │                         │   │
  │                                 │   │  │  ● Element 1           │   │
  │  Un link                       │   │  │  ● Element 2           │   │
  │                                 │   │  │  ● Element 3           │   │
  │  Text negru pe alb.            │   │  │                         │   │
  │  Arial, 16px.                  │   │  │  🔗 Un link colorat    │   │
  │  Zero personalitate.           │   │  │                         │   │
  │                                 │   │  │  Culori, spații,       │   │
  └─────────────────────────────────┘   │  │  fonturi, personalitate│   │
                                        │  └─────────────────────────┘   │
                                        └────────────────────────────────┘
```

**Același HTML. Doar CSS diferit.** Este ca și cum ai schimba hainele unei persoane — corpul rămâne același, dar aspectul se transformă complet.

---

## 3.2 Unde scrii CSS? Trei metode

Ai trei opțiuni pentru a adăuga CSS la pagina ta. Gândește-te la ele ca la trei moduri de a-ți alege hainele:

### Metoda 1: CSS Inline (pe element) — „Haine lipite de corp"

Scrii stilul direct pe elementul HTML, folosind atributul `style`:

```html
<h1 style="color: blue; font-size: 36px;">Titlul meu albastru</h1>
<p style="color: gray;">Un paragraf gri.</p>
```

**Când o folosești:** Aproape niciodată! Este ca și cum ai coase hainele direct pe piele — funcționează, dar e incomod și greu de schimbat.

### Metoda 2: CSS Intern (în `<head>`) — „Haine în dulap, dar doar pentru o cameră"

Scrii CSS-ul într-un tag `<style>` în secțiunea `<head>`:

```html
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <title>Pagina mea</title>
    <style>
        h1 {
            color: blue;
            font-size: 36px;
        }
        p {
            color: gray;
        }
    </style>
</head>
<body>
    <h1>Titlul meu albastru</h1>
    <p>Un paragraf gri.</p>
</body>
</html>
```

**Când o folosești:** Pentru pagini mici sau pentru a testa rapid. Stilurile se aplică doar acestei pagini.

### Metoda 3: CSS Extern (fișier separat) — „Garderobă profesionistă" ⭐

Creezi un fișier `.css` separat și îl conectezi la HTML. **Aceasta este metoda profesională!**

**Pasul 1:** Creează fișierul `stil.css`:

```css
h1 {
    color: blue;
    font-size: 36px;
}

p {
    color: gray;
}
```

**Pasul 2:** Conectează-l la HTML cu tag-ul `<link>`:

```html
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <title>Pagina mea</title>
    <link rel="stylesheet" href="stil.css">
</head>
<body>
    <h1>Titlul meu albastru</h1>
    <p>Un paragraf gri.</p>
</body>
</html>
```

**Structura folderului:**

```
  📁 proiectul-meu/
  ├── index.html
  └── stil.css          ← fișierul CSS extern
```

**De ce e cea mai bună metodă?**

1. **Separare** — HTML-ul se ocupă de conținut, CSS-ul de aspect (fiecare face ce știe mai bine)
2. **Reutilizare** — același CSS poate fi folosit pe 100 de pagini HTML diferite
3. **Ordine** — codul e mai ușor de citit și de întreținut

> 💡 **Sfat!**
> De acum încolo, vom folosi mereu **metoda externă** (fișier `.css` separat). Este ce folosesc toți programatorii profesioniști.

---

## 3.3 Anatomia unei reguli CSS

Fiecare instrucțiune CSS se numește o **regulă**. Hai să vedem cum arată:

```
         selectorul
      (PE CINE stilizezi?)
            │
            ▼
          ┌───┐
          │   │
          h1  {
              color: blue;           ← declarație (proprietate: valoare)
              font-size: 36px;       ← altă declarație
              text-align: center;    ← și încă una
          }
          │                │
          └──── bloc de ───┘
               declarații
               (CUM stilizezi?)
```

Descompunere:

| Parte | Ce este | Exemplu |
|---|---|---|
| **Selector** | PE CINE vrei să stilizezi | `h1`, `p`, `.clasa-mea` |
| **Proprietate** | CE vrei să schimbi | `color`, `font-size`, `text-align` |
| **Valoare** | CUM vrei să arate | `blue`, `36px`, `center` |
| **Declarație** | Proprietate + valoare | `color: blue;` |
| **Bloc** | Tot ce e între `{ }` | `{ color: blue; font-size: 36px; }` |

**Analogie**: Gândește-te la CSS ca la un regizor de film care dă instrucțiuni:

```
  "Actorul principal (h1) {
      poartă: costum albastru;
      vorbește: cu voce mare;
      stă: în centrul scenei;
  }"
```

> ⚠️ **Atenție!**
> Nu uita **punct și virgulă** (`;`) la finalul fiecărei declarații! Este ca punctul la finalul propoziției. Dacă lipsește, CSS-ul se poate strica.
>
> ```css
> /* ❌ GREȘIT — lipsește ; după prima declarație */
> h1 {
>     color: blue
>     font-size: 36px;
> }
> 
> /* ✅ CORECT */
> h1 {
>     color: blue;
>     font-size: 36px;
> }
> ```

---

## 3.4 Selectori — Cui îi vorbești?

Selectorul este **cel mai important concept** din CSS. El decide **cărui element** i se aplică stilul. Gândește-te la selectori ca la diferite moduri de a striga pe cineva:

```
  "Hei, TOȚI elevii!"              →  selector de element
  "Hei, echipa ALBASTRĂ!"          →  selector de clasă
  "Hei, TU, căpitanul echipei!"    →  selector de id
```

### Selector de element — „Toate elementele de acest tip"

Selectezi **toate** elementele de un anumit tip:

```css
/* Toate paragrafele vor fi gri */
p {
    color: gray;
}

/* Toate titlurile h2 vor fi albastre */
h2 {
    color: blue;
}

/* Toate linkurile vor fi roșii */
a {
    color: red;
}
```

### Selector de clasă (`.`) — „Doar elementele din această echipă"

O clasă e ca un **ecuson de echipă** — îl pui pe mai multe elemente care au ceva în comun.

**În HTML**, adaugi atributul `class`:

```html
<p class="important">Acest paragraf e important!</p>
<p>Acest paragraf e normal.</p>
<p class="important">Și acesta e important!</p>
```

**În CSS**, folosești **punct** (`.`) înaintea numelui clasei:

```css
.important {
    color: red;
    font-weight: bold;
}
```

**Rezultat:** Doar paragrafele cu `class="important"` vor fi roșii și bold. Celelalte rămân normale.

Un element poate avea **mai multe clase** (ca un elev care e și la echipa de fotbal, și la cea de robotică):

```html
<p class="important evidențiat">Text special!</p>
```

```css
.important {
    color: red;
}

.evidențiat {
    background-color: yellow;
}
```

### Selector de ID (`#`) — „Tu, exact TU!"

Un ID este **unic** — ca un CNP sau un număr de legitimație. Doar **un singur element** pe pagină poate avea un anumit ID.

**În HTML:**

```html
<h1 id="titlu-principal">Bun venit!</h1>
```

**În CSS**, folosești **diez** (`#`) înaintea numelui:

```css
#titlu-principal {
    color: darkblue;
    text-align: center;
    font-size: 48px;
}
```

### Când folosești fiecare?

```
  ┌──────────────────────────────────────────────────────┐
  │                                                      │
  │   ELEMENT (p, h1, a...)                             │
  │   └── Când vrei să stilizezi TOATE elementele        │
  │       de acel tip                                    │
  │                                                      │
  │   CLASĂ (.nume)                                     │
  │   └── Când vrei să stilizezi un GRUP specific        │
  │       de elemente (cele mai folosite!)                │
  │                                                      │
  │   ID (#nume)                                        │
  │   └── Când vrei să stilizezi UN SINGUR element       │
  │       unic pe pagină                                 │
  │                                                      │
  └──────────────────────────────────────────────────────┘
```

> 💡 **Sfat practic!**
> Programatorii profesioniști folosesc **clase** în 90% din cazuri. ID-urile le păstrează pentru elemente cu adevărat unice (header, footer, navigație). Regula de aur: dacă nu ești sigur, folosește o clasă.

### Selectori multipli — „Și tu, și tu!"

Poți aplica același stil mai multor selectori deodată, separându-i cu **virgulă**:

```css
/* h1, h2 și h3 — toate centrate */
h1, h2, h3 {
    text-align: center;
}

/* Atât clasa .eroare cât și clasa .avertisment — text roșu */
.eroare, .avertisment {
    color: red;
}
```

### Selectori descendenți — „Copiii din interiorul lui..."

Poți selecta elemente care sunt **în interiorul** altor elemente:

```css
/* Doar linkurile care sunt în interiorul paragrafelor */
p a {
    color: green;
}

/* Doar elementele li din interiorul listelor cu clasa "meniu" */
.meniu li {
    font-weight: bold;
}
```

```
  Selector:  p a { color: green; }
  
  Înseamnă: "găsește toate <a> care sunt în interiorul unui <p>"
  
  <p>                              ← părintele
    Text normal și un              
    <a href="...">link verde</a>   ← SELECTAT! (a în p)
  </p>
  
  <a href="...">link normal</a>    ← NU e selectat (a nu e în p)
```

---

## 3.5 Culori — Pictează-ți pagina!

CSS îți oferă **mai multe moduri** de a specifica culori. Gândește-te la ele ca la diferite moduri de a descrie aceeași culoare:

### Metoda 1: Nume de culori (în engleză)

CSS cunoaște **147 de culori** cu nume:

```css
h1 { color: tomato; }
p  { color: steelblue; }
a  { color: forestgreen; }
```

Câteva culori utile:

```
  ┌─────────────────────────────────────────────┐
  │  Roșii       │  Albastre     │  Verzi       │
  │  ──────      │  ──────       │  ──────      │
  │  red         │  blue         │  green       │
  │  tomato      │  steelblue    │  forestgreen │
  │  coral       │  dodgerblue   │  limegreen   │
  │  crimson     │  navy         │  darkgreen   │
  │  orangered   │  royalblue    │  seagreen    │
  ├─────────────────────────────────────────────┤
  │  Alte culori                                │
  │  ──────                                     │
  │  gold   orange   purple   pink   teal       │
  │  gray   silver   white    black  ivory      │
  └─────────────────────────────────────────────┘
```

### Metoda 2: Coduri HEX — Limba secretă a culorilor

Codul hexadecimal (HEX) e o modalitate precisă de a defini culori. Începe cu `#` și are 6 caractere:

```css
h1 { color: #FF6B6B; }     /* roșu-coral */
p  { color: #4ECDC4; }     /* turcoaz */
a  { color: #2C3E50; }     /* albastru-închis */
```

Cum funcționează?

```
        #  F  F  6  B  6  B
        │  ──────  ──────  ──────
        │    │       │       │
        │  ROȘU   VERDE   ALBASTRU
        │  (00-FF) (00-FF) (00-FF)
        │
        │  00 = nimic din acea culoare
        │  FF = maxim din acea culoare
        │
        └── simbolul care spune "acesta e un cod de culoare"
```

Exemple:

```
  #FF0000 = Roșu pur     (roșu maxim, zero verde, zero albastru)
  #00FF00 = Verde pur     (zero roșu, verde maxim, zero albastru)
  #0000FF = Albastru pur  (zero roșu, zero verde, albastru maxim)
  #FFFFFF = Alb           (totul la maxim)
  #000000 = Negru         (totul la zero)
  #808080 = Gri           (totul la mijloc)
```

> 💡 **Știai că?**
> HEX vine de la „hexadecimal" — un sistem de numerație cu 16 cifre (0-9 și A-F). Poți crea peste **16 milioane** de culori diferite cu coduri HEX! Ochiul uman poate distinge „doar" vreo 10 milioane, deci CSS-ul poate genera culori pe care nici nu le poți vedea.

### Metoda 3: RGB — Amestec de lumini

RGB (Red, Green, Blue) funcționează ca un amestec de lumini colorate:

```css
h1 { color: rgb(255, 107, 107); }    /* roșu-coral */
p  { color: rgb(78, 205, 196); }     /* turcoaz */
```

Fiecare valoare merge de la **0** (nimic) la **255** (maxim):

```
  rgb(255,   0,   0)  = Roșu pur
  rgb(  0, 255,   0)  = Verde pur
  rgb(  0,   0, 255)  = Albastru pur
  rgb(255, 255, 255)  = Alb
  rgb(  0,   0,   0)  = Negru
```

### RGBA — Culori transparente!

Adaugi un al patrulea număr — **alpha** (transparența), de la 0 (invizibil) la 1 (complet opac):

```css
.suprapunere {
    background-color: rgba(0, 0, 0, 0.5);   /* negru 50% transparent */
}

.evidențiat {
    background-color: rgba(255, 255, 0, 0.3); /* galben 30% transparent */
}
```

```
  alpha = 1.0    alpha = 0.7    alpha = 0.3    alpha = 0.0
  ┌────────┐     ┌────────┐     ┌────────┐     ┌────────┐
  │████████│     │▓▓▓▓▓▓▓▓│     │░░░░░░░░│     │        │
  │████████│     │▓▓▓▓▓▓▓▓│     │░░░░░░░░│     │        │
  │████████│     │▓▓▓▓▓▓▓▓│     │░░░░░░░░│     │        │
  └────────┘     └────────┘     └────────┘     └────────┘
   opac 100%      opac 70%       opac 30%      invizibil
```

### Cum aplici culori

Există două proprietăți principale de culoare:

```css
p {
    color: #333333;                /* culoarea TEXTULUI */
    background-color: #F0F0F0;    /* culoarea FUNDALULUI */
}
```

```
  ┌──────────────────────────────────┐  ← background-color
  │                                  │
  │    Textul tău apare aici         │  ← color
  │                                  │
  └──────────────────────────────────┘
```

---

## 3.6 Fonturi — Dă-i paginii o voce

Fontul este „vocea" paginii tale. Gândește-te la diferența dintre scrisul de mână al unui doctor și caligrafia elegantă — ambele transmit text, dar „sună" complet diferit.

### Familia de fonturi: `font-family`

```css
body {
    font-family: "Segoe UI", Tahoma, Geneva, sans-serif;
}
```

De ce sunt mai multe fonturi listate? Este un **plan de rezervă**: dacă primul font nu există pe computerul vizitatorului, browserul încearcă următorul, și tot așa:

```
  "Segoe UI"  →  există?  DA  → folosește-l!
                           NU ↓
  Tahoma      →  există?  DA  → folosește-l!
                           NU ↓
  Geneva      →  există?  DA  → folosește-l!
                           NU ↓
  sans-serif  →  fontul generic de sistem (mereu există)
```

### Categorii de fonturi

```
  SERIF (cu „piciorușe")              SANS-SERIF (fără „piciorușe")
  ─────────────────────               ──────────────────────────────
  
  T i m e s                           A r i a l
  │                                   
  └── Aceste mici linii               Litere curate, moderne,
      de la capetele                  fără ornamente. Ușor
      literelor se numesc             de citit pe ecran.
      „serife".                       
                                      
  Folosite în: cărți,                 Folosite în: site-uri web,
  ziare, documente                    aplicații, prezentări
  formale                             
  
  Exemple:                            Exemple:
  Georgia, Times New Roman            Arial, Verdana, Helvetica
  
  
  MONOSPACE (lățime egală)
  ─────────────────────────
  
  C o d u l   a r a t ă   a ș a
  
  Fiecare literă ocupă exact
  același spațiu. Perfect
  pentru afișarea codului.
  
  Exemple:
  Courier New, Consolas
```

### Dimensiunea fontului: `font-size`

```css
h1 { font-size: 36px; }    /* mare — titluri */
h2 { font-size: 28px; }    /* mediu-mare */
p  { font-size: 16px; }    /* normal — text de bază */
small { font-size: 12px; } /* mic — notite */
```

Unitatea **px** (pixeli) este cea mai simplă. Vom învăța și alte unități (em, rem, %) în capitolele viitoare.

### Grosimea fontului: `font-weight`

```css
.subțire  { font-weight: 300; }   /* light */
.normal   { font-weight: 400; }   /* normal (implicit) */
.gros     { font-weight: 700; }   /* bold */
.foarte-gros { font-weight: 900; } /* extra bold */

/* Sau cu cuvinte: */
.bold { font-weight: bold; }       /* = 700 */
```

### Alte proprietăți de text

```css
p {
    text-align: center;        /* aliniere: left, center, right, justify */
    text-decoration: underline; /* subliniere (folosit la linkuri) */
    text-transform: uppercase;  /* MAJUSCULE, lowercase, capitalize */
    line-height: 1.6;          /* spațierea între rânduri */
    letter-spacing: 2px;       /* spațiu între litere */
}
```

### Google Fonts — Fonturi gratuite și frumoase

Vrei fonturi mai interesante decât Arial? **Google Fonts** oferă sute de fonturi gratuite!

**Pasul 1:** Mergi pe [fonts.google.com](https://fonts.google.com) și alege un font.

**Pasul 2:** Adaugă linkul în `<head>` (înainte de fișierul tău CSS):

```html
<head>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="stil.css">
</head>
```

**Pasul 3:** Folosește fontul în CSS:

```css
body {
    font-family: "Fredoka", sans-serif;
}
```

> 🚀 **Provocare!**
> Mergi pe [fonts.google.com](https://fonts.google.com), explorează fonturile disponibile și alege-ți două: unul pentru titluri (bold, expresiv) și unul pentru text (clar, ușor de citit). Fiecare combinație dă un „caracter" diferit paginii tale!

---

## 3.7 Modelul cutiei (Box Model) — CEL MAI IMPORTANT CONCEPT DIN CSS! 📦

Acesta este conceptul pe care **trebuie** să-l înțelegi. Fiecare element HTML este, din punctul de vedere al browserului, o **cutie dreptunghiulară**. Chiar și un cerc făcut cu CSS este, tehnic, o cutie.

Fiecare cutie are **4 straturi**, ca o cutie de cadou:

```
  ┌──────────────────────────────────────────────────────┐
  │                     MARGIN                           │
  │    (spațiul dintre cutie și vecinii ei)              │
  │                                                      │
  │    ┌──────────────────────────────────────────┐      │
  │    │               BORDER                     │      │
  │    │    (chenarul cutiei — vizibil)            │      │
  │    │                                          │      │
  │    │    ┌──────────────────────────────┐      │      │
  │    │    │          PADDING             │      │      │
  │    │    │  (pernuța de protecție)      │      │      │
  │    │    │                              │      │      │
  │    │    │    ┌──────────────────┐      │      │      │
  │    │    │    │                  │      │      │      │
  │    │    │    │    CONTENT       │      │      │      │
  │    │    │    │  (conținutul —   │      │      │      │
  │    │    │    │   textul, imagi- │      │      │      │
  │    │    │    │   nea, etc.)     │      │      │      │
  │    │    │    │                  │      │      │      │
  │    │    │    └──────────────────┘      │      │      │
  │    │    │                              │      │      │
  │    │    └──────────────────────────────┘      │      │
  │    │                                          │      │
  │    └──────────────────────────────────────────┘      │
  │                                                      │
  └──────────────────────────────────────────────────────┘
```

### Metafora cutiei de cadou 🎁

Imaginează-ți că trimiți un cadou prin poștă:

| Strat CSS | Metafora | Ce face |
|---|---|---|
| **Content** | 🎁 Cadoul în sine | Conținutul elementului (text, imagine etc.) |
| **Padding** | 🧽 Buretele de protecție din jurul cadoului | Spațiu **între conținut și chenar**. Protejează conținutul. |
| **Border** | 📦 Cutia de carton | Chenarul vizibil al elementului |
| **Margin** | 📏 Spațiul pe raft între cutii | Spațiu **între acest element și elementele vecine** |

### Padding vs. Margin — Care e diferența?

Aceasta este cea mai frecventă confuzie pentru începători. Hai să o clarificăm:

```
                       margin
                    ◄──────────►
  ┌─────────┐                      ┌─────────┐
  │ Cutia A │      spațiu gol      │ Cutia B │
  │         │                      │         │
  │  ┌───┐  │                      │  ┌───┐  │
  │  │txt│  │                      │  │txt│  │
  │  └───┘  │                      │  └───┘  │
  │         │                      │         │
  └─────────┘                      └─────────┘
   ◄───────►
    padding
  (spațiu INTERIOR,
   între text și
   marginea cutiei)
```

**Padding** = spațiu **în interior** (între conținut și chenar)
**Margin** = spațiu **în exterior** (între chenar și vecini)

**Analogie simplă:**
- **Padding** = cât de departe stă mobilierul de pereți (în interiorul camerei)
- **Margin** = cât de departe este casa ta de casa vecinului (în exterior)

### Cum le scrii în CSS

```css
.cutie {
    /* Fiecare latură separat */
    padding-top: 20px;
    padding-right: 15px;
    padding-bottom: 20px;
    padding-left: 15px;
    
    margin-top: 30px;
    margin-right: 10px;
    margin-bottom: 30px;
    margin-left: 10px;
}
```

Dar există și **scurtături** (pe care le vei folosi cel mai des):

```css
.cutie {
    /* Toate cele 4 laturi la fel */
    padding: 20px;             /* sus, dreapta, jos, stânga = 20px */
    margin: 30px;

    /* Vertical și orizontal */
    padding: 20px 15px;        /* sus/jos = 20px, stânga/dreapta = 15px */
    margin: 30px 10px;

    /* Toate 4 separat (sens orar: sus, dreapta, jos, stânga) */
    padding: 20px 15px 20px 15px;   /* T R B L — ca ceasul */
    margin: 30px 10px 30px 10px;
}
```

Ordinea se reține ușor — merge în **sensul acelor de ceasornic**, pornind de SUS:

```
            TOP (sus)
              │
  LEFT ──── ┌─┴─┐ ──── RIGHT
  (stânga)  │   │    (dreapta)
            └─┬─┘
              │
           BOTTOM (jos)
           
  padding: 20px  15px  20px  15px;
            ↑     ↑     ↑     ↑
           TOP  RIGHT BOTTOM LEFT
```

### Exemplu practic vizual

```css
.card {
    /* Conținutul */
    width: 300px;
    
    /* Buretele de protecție (interior) */
    padding: 20px;
    
    /* Cutia de carton (chenarul) */
    border: 2px solid #333;
    
    /* Spațiul pe raft (exterior) */
    margin: 30px;
    
    /* Culoare fundal pentru a vedea padding-ul */
    background-color: #E8F4FD;
}
```

Dacă deschizi **DevTools** (F12 în Chrome), poți vedea modelul cutiei vizual! Mergi la tab-ul **Elements**, selectează un element, și uită-te în panoul din dreapta — vei vedea o diagramă colorată cu toate cele 4 straturi.

> 🚀 **Provocare importantă!**
> Deschide DevTools (`F12`) pe orice pagină web. Click pe un element. Găsește diagrama box model în panoul din dreapta-jos. Experimentează: modifică padding-ul și margin-ul unui element direct din DevTools și vezi cum se schimbă pagina în timp real! (Nu salvează modificările — e doar temporar.)

---

## 3.8 Border — Chenarul cutiei

Chenarul este linia vizibilă din jurul unui element:

```css
.cu-chenar {
    border: 2px solid #333;
}
```

Aceasta e **scurtătura**. Cele trei componente sunt:

```
  border:  2px       solid      #333;
           ───       ─────      ────
            │          │          │
         grosime     stil      culoare
```

### Stiluri de chenar

```css
.solid   { border: 2px solid black; }     /* linie continuă ───── */
.dashed  { border: 2px dashed black; }    /* linie întreruptă - - - */
.dotted  { border: 2px dotted black; }    /* puncte · · · · · */
.double  { border: 4px double black; }    /* linie dublă ═════ */
.none    { border: none; }                /* fără chenar */
```

### Chenar pe o singură latură

```css
.doar-jos {
    border-bottom: 3px solid tomato;     /* doar linie jos */
}

.stanga-colorata {
    border-left: 5px solid dodgerblue;   /* accent lateral */
}
```

### Colțuri rotunjite: `border-radius`

Aceasta e proprietatea „magică" care transformă dreptunghiuri în forme rotunjite:

```css
.rotunjit-putin   { border-radius: 8px; }     /* colțuri ușor rotunjite */
.rotunjit-mult    { border-radius: 20px; }     /* colțuri foarte rotunde */
.cerc             { border-radius: 50%; }      /* cerc perfect! */
.pastila          { border-radius: 9999px; }   /* capsulă/pastilă */
```

```
  border-radius: 0       8px          20px          50%
  
  ┌──────────┐    ╭──────────╮    ╭──────────╮    ╭──────╮
  │          │    │          │    │          │    │      │
  │          │    │          │    │          │    │      │
  │          │    │          │    │          │    │      │
  └──────────┘    ╰──────────╯    ╰──────────╯    ╰──────╯
   dreptunghi     ușor rotund     foarte rotund      cerc
```

---

## 3.9 Background — Fundalul paginii

### Culoare de fundal

```css
body {
    background-color: #F5F5F5;    /* gri deschis — odihnitor pentru ochi */
}

.card {
    background-color: white;
}

.alerta {
    background-color: #FFF3CD;    /* galben deschis — atenție! */
}
```

### Imagine de fundal

```css
.banner {
    background-image: url("imagini/fundal.jpg");
    background-size: cover;        /* acoperă tot spațiul */
    background-position: center;   /* centrează imaginea */
    background-repeat: no-repeat;  /* nu repetă imaginea */
}
```

### Gradienți — Tranziții de culoare

Gradienții sunt tranziții lin de la o culoare la alta (fără a avea nevoie de imagini!):

```css
/* Gradient de sus în jos */
.gradient-vertical {
    background: linear-gradient(to bottom, #4ECDC4, #2C3E50);
}

/* Gradient de stânga la dreapta */
.gradient-orizontal {
    background: linear-gradient(to right, #FF6B6B, #FECA57);
}

/* Gradient diagonal */
.gradient-diagonal {
    background: linear-gradient(135deg, #667eea, #764ba2);
}

/* Gradient cu mai multe culori (curcubeu!) */
.curcubeu {
    background: linear-gradient(to right, 
        red, orange, yellow, green, blue, purple);
}
```

```
  linear-gradient(to right, #4ECDC4, #FF6B6B)
  
  ┌─────────────────────────────────────────┐
  │▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓│
  │ turcoaz ──────── tranziție ──── roșu-co │
  └─────────────────────────────────────────┘
```

---

## 3.10 Dimensiuni — Cât de mare e cutia?

### Lățime și înălțime

```css
.card {
    width: 300px;       /* lățime fixă */
    height: 200px;      /* înălțime fixă */
}

.flexibil {
    width: 80%;         /* 80% din lățimea părintelui */
    max-width: 600px;   /* dar nu mai mult de 600px */
    min-width: 200px;   /* și nu mai puțin de 200px */
}
```

### Unități de măsură

| Unitate | Ce înseamnă | Exemplu | Când o folosești |
|---|---|---|---|
| `px` | Pixeli (fix) | `16px` | Dimensiuni exacte |
| `%` | Procent din părinte | `80%` | Layout-uri flexibile |
| `em` | Relativ la fontul elementului | `1.5em` | Spațiere relativă |
| `rem` | Relativ la fontul paginii | `1.2rem` | Dimensiuni consistente |
| `vh` | Procent din înălțimea ecranului | `100vh` | Secțiuni full-screen |
| `vw` | Procent din lățimea ecranului | `50vw` | Jumătate de ecran |

Pentru început, **px** și **%** sunt tot ce ai nevoie. Vom explora celelalte unități pe parcurs.

---

## 3.11 Proiect practic: Stilizează pagina „Despre mine" 🚀

Hai să transformăm pagina din Capitolul 2! Creează structura:

```
  📁 despre-mine/
  ├── index.html       (din Capitolul 2, cu mici adăugiri)
  ├── stil.css         (NOU!)
  └── 📁 imagini/
      └── avatar.jpg
```

### Pasul 1: Actualizează HTML-ul

Adaugă linkul către CSS în `<head>`, un Google Font, și câteva clase noi:

```html
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Despre Mine — Pagina mea personală</title>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="stil.css">
</head>
<body>

    <div class="container">

        <header class="hero">
            <img src="imagini/avatar.jpg" alt="Fotografia mea" class="avatar">
            <h1>Bun venit pe pagina mea! 👋</h1>
            <p class="subtitlu">Sunt [Numele tău] — constructor de site-uri în devenire</p>
        </header>

        <section class="sectiune">
            <h2>🧑 Despre mine</h2>
            <p>Salut! Mă numesc <strong>[Numele tău]</strong> și am 
            <strong>[vârsta] ani</strong>. Sunt elev/ă în clasa 
            <em>[clasa ta]</em> și tocmai am început să învăț 
            <strong>programare web</strong>!</p>
        </section>

        <section class="sectiune">
            <h2>🎮 Lucrurile mele preferate</h2>
            
            <h3>Hobby-uri</h3>
            <ul>
                <li>Programare (evident!)</li>
                <li>[Hobby-ul tău 1]</li>
                <li>[Hobby-ul tău 2]</li>
            </ul>

            <h3>🎬 Top 3 filme</h3>
            <ol>
                <li><strong>[Filmul #1]</strong> — <em>cel mai tare!</em></li>
                <li>[Filmul #2]</li>
                <li>[Filmul #3]</li>
            </ol>
        </section>

        <section class="sectiune">
            <h2>💻 Ce știu deja în HTML</h2>
            <div class="competente">
                <span class="tag-competenta">Titluri h1-h6</span>
                <span class="tag-competenta">Paragrafe</span>
                <span class="tag-competenta">Bold &amp; Italic</span>
                <span class="tag-competenta">Liste</span>
                <span class="tag-competenta">Imagini</span>
                <span class="tag-competenta">Linkuri</span>
                <span class="tag-competenta">CSS Extern</span>
                <span class="tag-competenta">Selectori</span>
                <span class="tag-competenta">Box Model</span>
            </div>
        </section>

        <section class="sectiune">
            <h2>🔗 Resurse utile</h2>
            <ul class="lista-linkuri">
                <li><a href="https://developer.mozilla.org" target="_blank">MDN Web Docs</a> 
                    — documentația oficială</li>
                <li><a href="https://www.w3schools.com" target="_blank">W3Schools</a> 
                    — tutoriale interactive</li>
                <li><a href="https://fonts.google.com" target="_blank">Google Fonts</a> 
                    — fonturi gratuite</li>
            </ul>
        </section>

        <footer class="footer">
            <p>Creat cu ❤️ de [Numele tău]</p>
            <p class="mic">Constructorul de Site-uri — Capitolul 3</p>
        </footer>

    </div>

</body>
</html>
```

### Pasul 2: Creează fișierul CSS

Creează `stil.css` și scrie:

```css
/* ============================
   STILURI GLOBALE
   ============================ */

/* Resetare de bază — elimină spațierile implicite ale browserului */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: "Nunito", sans-serif;
    font-size: 16px;
    line-height: 1.7;
    color: #2C3E50;
    background-color: #F0F4F8;
}

/* Containerul principal — centrează conținutul */
.container {
    max-width: 700px;
    margin: 0 auto;            /* centrează orizontal */
    padding: 20px;
}


/* ============================
   HEADER / HERO
   ============================ */

.hero {
    text-align: center;
    padding: 40px 20px;
    margin-bottom: 30px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-radius: 16px;
    color: white;
}

.avatar {
    width: 120px;
    height: 120px;
    border-radius: 50%;                   /* face imaginea cerc */
    border: 4px solid white;
    margin-bottom: 15px;
    object-fit: cover;                    /* imaginea se decupează frumos */
}

.hero h1 {
    font-family: "Fredoka", sans-serif;
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 8px;
}

.subtitlu {
    font-size: 16px;
    color: rgba(255, 255, 255, 0.8);     /* alb cu puțină transparență */
}


/* ============================
   SECȚIUNI
   ============================ */

.sectiune {
    background-color: white;
    border-radius: 12px;
    padding: 30px;
    margin-bottom: 20px;
    border: 1px solid #E2E8F0;
}

.sectiune h2 {
    font-family: "Fredoka", sans-serif;
    font-size: 24px;
    color: #5A67D8;
    margin-bottom: 15px;
    padding-bottom: 10px;
    border-bottom: 2px solid #E2E8F0;
}

.sectiune h3 {
    font-size: 18px;
    color: #4A5568;
    margin-top: 20px;
    margin-bottom: 10px;
}

.sectiune p {
    margin-bottom: 10px;
}


/* ============================
   LISTE
   ============================ */

ul, ol {
    padding-left: 25px;
    margin-bottom: 15px;
}

li {
    margin-bottom: 6px;
}


/* ============================
   COMPETENȚE (TAG-URI)
   ============================ */

.competente {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.tag-competenta {
    background-color: #EBF4FF;
    color: #5A67D8;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 14px;
    font-weight: 600;
    border: 1px solid #C3DAFE;
}


/* ============================
   LINKURI
   ============================ */

a {
    color: #5A67D8;
    text-decoration: none;           /* elimină sublinierea implicită */
}

a:hover {
    color: #434190;
    text-decoration: underline;      /* subliniază când treci cu mouse-ul */
}

.lista-linkuri li {
    margin-bottom: 10px;
}


/* ============================
   FOOTER
   ============================ */

.footer {
    text-align: center;
    padding: 25px;
    color: #718096;
    font-size: 14px;
}

.footer .mic {
    font-size: 12px;
    color: #A0AEC0;
    margin-top: 4px;
}
```

### Ce am folosit

```
  ✅ CSS extern (fișier separat stil.css)
  ✅ Google Fonts (Fredoka + Nunito)
  ✅ Selectori de element (body, h2, p, a, li)
  ✅ Selectori de clasă (.hero, .sectiune, .avatar, .tag-competenta)
  ✅ Selectori descendenți (.hero h1, .sectiune h2, .footer .mic)
  ✅ Pseudo-clasă :hover (a:hover)
  ✅ Culori HEX și RGBA
  ✅ Box model: margin, padding, border, border-radius
  ✅ Background: culoare solidă și gradient
  ✅ Fonturi: font-family, font-size, font-weight
  ✅ Text: text-align, text-decoration, line-height, color
  ✅ Dimensiuni: width, max-width, border-radius: 50%
  ✅ Flexbox de bază (display: flex, flex-wrap, gap)
```

---

## 3.12 Pseudo-clase — CSS reacționează!

Ai observat `:hover` în exemplul anterior? Aceasta este o **pseudo-clasă** — un stil care se activează doar în anumite **condiții**.

### `:hover` — „Când treci cu mouse-ul"

```css
.buton {
    background-color: #5A67D8;
    color: white;
    padding: 10px 24px;
    border: none;
    border-radius: 8px;
    cursor: pointer;        /* schimbă cursorul în "mânuță" */
}

.buton:hover {
    background-color: #434190;    /* se întunecă la hover */
}
```

### `:active` — „Când apeși click"

```css
.buton:active {
    transform: scale(0.95);    /* se micșorează puțin la click */
}
```

### `:first-child` și `:last-child`

```css
/* Primul element din listă — bold */
li:first-child {
    font-weight: bold;
}

/* Ultimul element — fără margine jos */
li:last-child {
    margin-bottom: 0;
}
```

```
  ul
  ├── li  ← :first-child  (PRIMUL)
  ├── li
  ├── li
  └── li  ← :last-child   (ULTIMUL)
```

---

## 3.13 Cascada și specificitatea — Cine câștigă?

**CSS** înseamnă *Cascading* Style Sheets — **stiluri în cascadă**. „Cascada" descrie ce se întâmplă când mai multe reguli se aplică aceluiași element. Cine câștigă?

### Regulile cascadei (simplificat)

```
  Prioritate (de la cea mai mică la cea mai mare):
  
  1. Selector de ELEMENT          p { color: blue; }
     │
     ▼  pierde în fața...
  2. Selector de CLASĂ            .text { color: red; }
     │
     ▼  pierde în fața...
  3. Selector de ID               #special { color: green; }
     │
     ▼  pierde în fața...
  4. CSS INLINE (pe element)      style="color: purple;"
```

Exemplu:

```html
<p id="special" class="text" style="color: purple;">Ce culoare am?</p>
```

```css
p       { color: blue; }       /* prioritate 1 — pierde */
.text   { color: red; }        /* prioritate 2 — pierde */
#special { color: green; }     /* prioritate 3 — pierde */
/* style="color: purple" */    /* prioritate 4 — CÂȘTIGĂ! → textul e purple */
```

### Ordinea contează

Dacă două reguli au **aceeași prioritate**, **ultima** câștigă:

```css
p { color: blue; }
p { color: red; }     /* Aceasta câștigă — e ultima */
/* Rezultat: textul din <p> va fi roșu */
```

> 💡 **Sfat practic!**
> Nu complica lucrurile. Folosește **clase** pentru aproape tot și vei avea rareori probleme cu cascada. Evită stilurile inline (`style="..."`) și folosește ID-uri cu moderație.

---

## 3.14 Comentarii CSS

La fel ca în HTML, poți lăsa note în CSS:

```css
/* Acesta este un comentariu CSS */

/* 
   Comentariile pot fi
   pe mai multe linii
*/

h1 {
    color: blue;          /* culoarea titlului */
    font-size: 36px;      /* dimensiunea textului */
}
```

Diferența față de HTML:
- **HTML:** `<!-- comentariu -->`
- **CSS:** `/* comentariu */`

Folosește comentarii pentru a **organiza** codul pe secțiuni (vezi exemplul din proiect).

---

## 3.15 Greșeli frecvente (și cum le repari) 🔧

### ❌ Greșeala 1: Punct și virgulă lipsă

```css
/* ❌ GREȘIT — lipsește ; după color */
h1 {
    color: blue
    font-size: 36px;
}
/* Rezultat: font-size e ignorat! */

/* ✅ CORECT */
h1 {
    color: blue;
    font-size: 36px;
}
```

### ❌ Greșeala 2: Punct lipsă la clase

```css
/* ❌ GREȘIT — lipsește punctul */
important {
    color: red;
}

/* ✅ CORECT — cu punct pentru clasă */
.important {
    color: red;
}
```

### ❌ Greșeala 3: Confuzie padding vs margin

```css
/* Vrei spațiu ÎNTRE elemente? → margin */
.card {
    margin-bottom: 20px;    /* spațiu sub card, până la următorul */
}

/* Vrei spațiu ÎN INTERIOR? → padding */
.card {
    padding: 20px;          /* spațiu între text și marginea cardului */
}
```

### ❌ Greșeala 4: Fișierul CSS nu e conectat

```html
<!-- ❌ GREȘIT — calea e greșită sau tag-ul lipsește -->
<head>
    <title>Pagina mea</title>
    <!-- Fără <link> către CSS! -->
</head>

<!-- ✅ CORECT -->
<head>
    <title>Pagina mea</title>
    <link rel="stylesheet" href="stil.css">
</head>
```

**Dacă CSS-ul nu funcționează**, verifică:
1. Ai tag-ul `<link>` în `<head>`?
2. Atributul `href` are **calea corectă** către fișier?
3. Numele fișierului e scris **exact** la fel? (stil.css ≠ Stil.css)
4. Ai salvat **ambele** fișiere (HTML și CSS)?

### ❌ Greșeala 5: Acolade neînchise

```css
/* ❌ GREȘIT — acolada de închidere lipsește */
h1 {
    color: blue;
    font-size: 36px;

p {
    color: gray;
}

/* ✅ CORECT */
h1 {
    color: blue;
    font-size: 36px;
}

p {
    color: gray;
}
```

**Sfat:** Scrie mereu acolada de închidere `}` imediat după cea de deschidere `{`, apoi completează declarațiile între ele. Așa nu uiți niciodată.

---

## 3.16 Mini-quiz — Verifică ce ai învățat! ✅

**1.** Care sunt cele trei metode de a adăuga CSS la o pagină HTML? Care este recomandată?

**2.** Ce selector folosești pentru a stiliza toate elementele cu clasa `important`?

**3.** Ce diferență este între `padding` și `margin`?

**4.** Cum faci un element cu colțuri rotunde?

**5.** Cum specifici culoarea roșie în format HEX?

**6.** Ce se întâmplă dacă ai aceste două reguli?
```css
p { color: blue; }
.text { color: red; }
```
Ce culoare va avea `<p class="text">Salut</p>`?

**7.** Ce face `a:hover { color: red; }`?

---

<details>
<summary>🔑 Click aici pentru răspunsuri</summary>

1. **Inline** (atributul `style` pe element), **intern** (tag `<style>` în `<head>`), și **extern** (fișier `.css` separat, conectat cu `<link>`). **Metoda externă** este recomandată.

2. **`.important`** — cu **punct** înaintea numelui clasei.

3. **Padding** = spațiu **interior**, între conținut și chenar. **Margin** = spațiu **exterior**, între element și vecinii lui.

4. Cu proprietatea **`border-radius`**. De exemplu: `border-radius: 12px;` pentru colțuri rotunjite, sau `border-radius: 50%;` pentru un cerc.

5. **`#FF0000`** — FF pentru roșu maxim, 00 pentru verde zero, 00 pentru albastru zero.

6. **Roșu.** Selectorul de clasă (`.text`) are prioritate mai mare decât selectorul de element (`p`), deci `color: red` câștigă.

7. Când utilizatorul **trece cu mouse-ul** peste un link (`<a>`), culoarea textului linkului devine **roșie**. Când mută mouse-ul, linkul revine la culoarea normală.

</details>

---

## 3.17 Știai că? — Curiozități din lumea tech 🤓

🎨 **CSS a fost propus în 1994** de Håkon Wium Lie, un cercetător norvegian. Înainte de CSS, stilizarea se făcea direct în HTML cu tag-uri ca `<font color="red">` — era haotic! CSS a adus ordine, separând conținutul de aspect.

🌈 **Cele 147 de culori cu nume din CSS** au povești interesante. Culoarea `rebeccapurple` (#663399) a fost adăugată în 2014 în memoria fiicei lui Eric Meyer, un pionier al CSS, care a murit de cancer cerebral la 6 ani. Este singura culoare CSS numită după o persoană.

🏆 **CSS Zen Garden** (csszengarden.com) este un proiect celebru care demonstrează puterea CSS-ului: exact același HTML este transformat radical doar prin schimbarea fișierului CSS. Sunt sute de design-uri complet diferite pentru aceeași pagină!

📱 **Peste 60% din traficul web** vine de pe telefoane mobile. De aceea, a ști CSS responsive (pe care îl vom învăța în Capitolul 4) este esențial — pagina ta trebuie să arate bine și pe un ecran de 5 inci!

---

## Recapitulare — Ce ai învățat în Capitolul 3

```
  ✅ CSS stilizează pagina (culori, fonturi, spații, chenare)
  ✅ Trei metode: inline, intern, extern (extern = recomandat)
  ✅ Anatomia unei reguli: selector { proprietate: valoare; }
  ✅ Selectori: element (p), clasă (.nume), ID (#unic)
  ✅ Selectori multipli (h1, h2, h3) și descendenți (p a)
  ✅ Culori: nume, HEX (#FF6B6B), RGB, RGBA (cu transparență)
  ✅ Fonturi: font-family, font-size, font-weight, Google Fonts
  ✅ Text: text-align, text-decoration, line-height
  ✅ BOX MODEL: content → padding → border → margin
  ✅ Padding = spațiu interior, Margin = spațiu exterior
  ✅ Border: grosime, stil, culoare + border-radius
  ✅ Background: culoare, imagine, gradient
  ✅ Dimensiuni: width, height, max-width (px, %)
  ✅ Pseudo-clase: :hover, :active, :first-child, :last-child
  ✅ Cascada: inline > ID > clasă > element
  ✅ Ai stilizat pagina "Despre mine" — arată profesional! 🎉
```

---

## Ce urmează?

În **Capitolul 4: Layout — Pune lucrurile la locul lor**, vei învăța **Flexbox** — instrumentul care îți permite să aranjezi elementele pe pagină exact unde vrei: orizontal, vertical, centrat, cu spații egale. Vei putea crea meniuri de navigație, galerii de imagini și layout-uri complexe.

Pagina ta nu va mai fi doar frumoasă — va fi și **bine organizată**! 📐

---

> *„Simplitatea este sofisticarea supremă."*
> — Leonardo da Vinci
