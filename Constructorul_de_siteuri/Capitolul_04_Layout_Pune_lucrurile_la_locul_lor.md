# Capitolul 4: Layout — Pune lucrurile la locul lor 📐

> *„Ordinea este prima lege a cerului."*
> — Alexander Pope

---

## Ce vei învăța în acest capitol

- Diferența dintre elemente **block** și **inline**
- **Flexbox** — instrumentul magic pentru aranjarea elementelor
- Cum să construiești un **meniu de navigație**
- Cum să creezi **layout-uri** cu mai multe coloane
- **Responsive design** — pagina ta arată bine pe orice ecran
- Cum funcționează **media queries**

---

## 4.1 Problema: de ce nu stau lucrurile unde vreau?

Ai scris HTML, ai adăugat CSS frumos, dar elementele se comportă ciudat. Titlul e sus, paragrafele se întind pe toată pagina, imaginile nu stau una lângă alta. De ce?

Pentru că fiecare element HTML are un **comportament implicit** — un mod în care ocupă spațiul pe pagină. Înainte de a învăța Flexbox, trebuie să înțelegi acest comportament.

---

## 4.2 Block vs. Inline — Cele două personalități

Fiecare element HTML este fie **block** (bloc), fie **inline** (în linie). Gândește-te la ele ca la două tipuri de cărămizi LEGO:

```
  BLOCK (bloc)                          INLINE (în linie)
  ══════════════                        ═══════════════════
  
  ┌──────────────────────────────┐      Text normal și un <a>link</a> și
  │           <h1>               │      un cuvânt <strong>bold</strong>
  └──────────────────────────────┘      într-o propoziție care curge...
  ┌──────────────────────────────┐
  │           <p>                │
  └──────────────────────────────┘      Elementele inline curg ca
  ┌──────────────────────────────┐      apa într-o propoziție —
  │           <div>              │      una după alta, pe aceeași
  └──────────────────────────────┘      linie, fără a "rupe" rândul.
  
  Fiecare bloc ocupă o LINIE              
  ÎNTREAGĂ, chiar dacă conținutul        
  e mic. Următorul element               
  începe DEDESUBT.                       
```

### Elemente Block (ca niște canapele)

O canapea ocupă tot peretele — nimeni nu se mai poate așeza lângă ea pe același rând.

```
  ┌─────────────────────────────────────┐
  │ <h1> — Titlu                        │  ← ocupă tot rândul
  └─────────────────────────────────────┘
  ┌─────────────────────────────────────┐
  │ <p> — Paragraf                      │  ← ocupă tot rândul
  └─────────────────────────────────────┘
  ┌─────────────────────────────────────┐
  │ <div> — Diviziune                   │  ← ocupă tot rândul
  └─────────────────────────────────────┘
  ┌─────────────────────────────────────┐
  │ <ul> — Listă                         │  ← ocupă tot rândul
  └─────────────────────────────────────┘
```

**Elemente block comune:** `<h1>`–`<h6>`, `<p>`, `<div>`, `<ul>`, `<ol>`, `<li>`, `<section>`, `<header>`, `<footer>`

### Elemente Inline (ca niște cuvinte)

Un cuvânt stă pe același rând cu celelalte cuvinte — nu forțează o linie nouă.

```
  Aceasta este o propoziție cu un ┌──────┐ și un cuvânt
  ┌──────────┐ care continuă pe  │ link │ 
  │ <strong>  │ aceeași linie.   └──────┘
  └──────────┘                    <a>
```

**Elemente inline comune:** `<a>`, `<strong>`, `<em>`, `<span>`, `<img>`, `<br>`

### `<div>` și `<span>` — Cutii universale

Două tag-uri speciale pe care le vei folosi **foarte des**:

| Tag | Tip | Scop |
|---|---|---|
| `<div>` | Block | Cutie invizibilă care **grupează** elemente block |
| `<span>` | Inline | Cutie invizibilă care **marchează** text într-o propoziție |

```html
<!-- div grupează mai multe elemente -->
<div class="card">
    <h2>Titlu card</h2>
    <p>Conținut card...</p>
</div>

<!-- span marchează o bucată de text -->
<p>Prețul este <span class="pret">49.99 lei</span> pe lună.</p>
```

De ce sunt utile? Singure, nu fac nimic vizibil. Dar cu CSS, le poți stiliza:

```css
.card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #E2E8F0;
}

.pret {
    color: green;
    font-weight: bold;
    font-size: 24px;
}
```

### Schimbarea comportamentului cu `display`

Poți transforma un element block în inline și invers:

```css
/* Fă un element block să fie inline */
li {
    display: inline;    /* elementele din listă stau pe același rând */
}

/* Fă un element inline să fie block */
a {
    display: block;     /* linkul ocupă tot rândul */
}

/* Cel mai util: inline-block (combină avantajele ambelor!) */
.buton {
    display: inline-block;  /* stă pe rând cu altele, DAR acceptă width/height */
    width: 150px;
    padding: 10px;
}
```

```
  block:         Ocupă tot rândul. Acceptă width/height.
  inline:        Stă pe rând. NU acceptă width/height.
  inline-block:  Stă pe rând. Acceptă width/height. ✨ Best of both worlds!
```

---

## 4.3 Flexbox — Superputerea layout-ului 💪

Flexbox (Flexible Box) este instrumentul modern care rezolvă aproape orice problemă de layout. Înainte de Flexbox, programatorii se chinuiau cu trucuri complicate. Acum e simplu!

### Metafora: Banda de bagaje la aeroport

Imaginează-ți o **bandă de bagaje** la aeroport:

```
  ┌─ Container (banda de bagaje) ──────────────────────┐
  │                                                     │
  │    ┌─────┐   ┌─────┐   ┌─────┐   ┌─────┐         │
  │    │Geam.│   │Geam.│   │Geam.│   │Geam.│         │
  │    │ #1  │   │ #2  │   │ #3  │   │ #4  │         │
  │    └─────┘   └─────┘   └─────┘   └─────┘         │
  │                                                     │
  └─────────────────────────────────────────────────────┘
  
  Tu controlezi:
  • Direcția benzii (orizontal sau vertical)
  • Spațierea între bagaje
  • Alinierea bagajelor (sus, centru, jos)
  • Ordinea bagajelor
```

**Containerul** = banda (părintele)
**Elementele** = bagajele (copiii)

Tu dai instrucțiuni **benzii** (containerul), iar bagajele (elementele) se aranjează automat!

### Cum activezi Flexbox

Doar o linie de CSS pe **părinte**:

```css
.container {
    display: flex;
}
```

Asta e tot! Copiii se aranjează automat **pe orizontală**:

```html
<div class="container">
    <div class="item">1</div>
    <div class="item">2</div>
    <div class="item">3</div>
</div>
```

```
  FĂRĂ display: flex            CU display: flex
  ──────────────────            ────────────────
  ┌──────────────┐              ┌────┐ ┌────┐ ┌────┐
  │      1       │              │ 1  │ │ 2  │ │ 3  │
  └──────────────┘              └────┘ └────┘ └────┘
  ┌──────────────┐              
  │      2       │              Elementele stau acum
  └──────────────┘              pe ACELAȘI RÂND!
  ┌──────────────┐              
  │      3       │              
  └──────────────┘              
```

---

## 4.4 Proprietăți Flexbox pe container (părinte)

### `flex-direction` — Direcția benzii

```css
.container { display: flex; flex-direction: row; }           /* implicit */
.container { display: flex; flex-direction: row-reverse; }
.container { display: flex; flex-direction: column; }
.container { display: flex; flex-direction: column-reverse; }
```

```
  row (implicit)          row-reverse
  ─────────────           ──────────────
  ┌───┐ ┌───┐ ┌───┐      ┌───┐ ┌───┐ ┌───┐
  │ 1 │ │ 2 │ │ 3 │      │ 3 │ │ 2 │ │ 1 │
  └───┘ └───┘ └───┘      └───┘ └───┘ └───┘
  ──────────────►         ◄──────────────
  
  column                  column-reverse
  ──────                  ──────────────
  ┌───┐                   ┌───┐
  │ 1 │  │                │ 3 │  ▲
  └───┘  │                └───┘  │
  ┌───┐  │                ┌───┐  │
  │ 2 │  ▼                │ 2 │  │
  └───┘                   └───┘
  ┌───┐                   ┌───┐
  │ 3 │                   │ 1 │
  └───┘                   └───┘
```

### `justify-content` — Spațierea pe axa principală

Aceasta controlează cum sunt distribuite elementele **pe direcția benzii**:

```css
.container {
    display: flex;
    justify-content: flex-start;       /* implicit — la început */
}
```

```
  flex-start (implicit)     
  ┌───┬───┬───┬──────────────────────┐
  │ 1 │ 2 │ 3 │                      │
  └───┴───┴───┴──────────────────────┘
  
  flex-end                  
  ┌──────────────────────┬───┬───┬───┐
  │                      │ 1 │ 2 │ 3 │
  └──────────────────────┴───┴───┴───┘
  
  center                    
  ┌──────────┬───┬───┬───┬───────────┐
  │          │ 1 │ 2 │ 3 │           │
  └──────────┴───┴───┴───┴───────────┘
  
  space-between             
  ┌───┬──────────┬───┬───────────┬───┐
  │ 1 │          │ 2 │           │ 3 │
  └───┴──────────┴───┴───────────┴───┘
         spațiu egal între elemente
  
  space-around              
  ┌───┬───┬──────┬───┬──────┬───┬───┐
  │   │ 1 │      │ 2 │      │ 3 │   │
  └───┴───┴──────┴───┴──────┴───┴───┘
     spațiu egal în jurul fiecăruia
  
  space-evenly              
  ┌────┬───┬─────┬───┬──────┬───┬───┐
  │    │ 1 │     │ 2 │      │ 3 │   │
  └────┴───┴─────┴───┴──────┴───┴───┘
        spații perfect egale peste tot
```

### `align-items` — Alinierea pe axa secundară

Dacă `justify-content` controlează axa **orizontală** (la `flex-direction: row`), atunci `align-items` controlează axa **verticală**:

```css
.container {
    display: flex;
    height: 200px;                 /* trebuie să aibă înălțime */
    align-items: center;           /* centrează vertical */
}
```

```
  flex-start          center              flex-end
  ──────────          ──────              ────────
  ┌───┬───┬───┐      ┌─────────────┐     ┌─────────────┐
  │ 1 │ 2 │ 3 │      │             │     │             │
  │   │   │   │      ├───┬───┬───┤     │             │
  │   │   │   │      │ 1 │ 2 │ 3 │     │             │
  │   │   │   │      ├───┴───┴───┤     ├───┬───┬───┤
  │   │   │   │      │             │     │ 1 │ 2 │ 3 │
  └───┴───┴───┘      └─────────────┘     └───┴───┴───┘
  (sus)               (mijloc)            (jos)
  
  
  stretch (implicit)
  ──────────────────
  ┌───┬───┬───┐
  │   │   │   │       Elementele se ÎNTIND
  │ 1 │ 2 │ 3 │       pe toată înălțimea
  │   │   │   │       containerului
  └───┴───┴───┘
```

### Centrarea perfectă — Sfântul Graal al CSS-ului

Înainte de Flexbox, centrarea unui element atât orizontal cât și vertical era un coșmar. Acum sunt suficiente 3 linii:

```css
.container {
    display: flex;
    justify-content: center;    /* centrează orizontal */
    align-items: center;        /* centrează vertical */
}
```

```
  ┌─────────────────────────┐
  │                         │
  │                         │
  │       ┌─────────┐      │
  │       │ CENTRAT │      │
  │       │ PERFECT │      │
  │       └─────────┘      │
  │                         │
  │                         │
  └─────────────────────────┘
```

> 💡 **Știai că?**
> Înainte de Flexbox (introdus în CSS3, ~2012), programatorii aveau nevoie de 10+ linii de cod hacky pentru a centra un element vertical. Era atât de dificil încât „cum centrezi un div vertical" a fost una dintre cele mai căutate întrebări pe internet timp de un deceniu!

### `gap` — Spațiu între elemente

În loc de margin pe fiecare element, poți folosi `gap` pe container:

```css
.container {
    display: flex;
    gap: 20px;        /* 20px între fiecare element */
}
```

```
  Fără gap:                    Cu gap: 20px:
  ┌───┬───┬───┐               ┌───┐    ┌───┐    ┌───┐
  │ 1 │ 2 │ 3 │               │ 1 │    │ 2 │    │ 3 │
  └───┴───┴───┘               └───┘    └───┘    └───┘
                                   ◄20px► ◄20px►
```

### `flex-wrap` — Ce se întâmplă când nu mai e loc?

Implicit, Flexbox încearcă să încapă totul pe un singur rând, micșorând elementele. Cu `flex-wrap`, le spui să „sară" pe rândul următor:

```css
.container {
    display: flex;
    flex-wrap: wrap;     /* treci pe rândul următor dacă nu e loc */
    gap: 15px;
}
```

```
  flex-wrap: nowrap (implicit)     flex-wrap: wrap
  ─────────────────────────        ────────────────
  ┌──┬──┬──┬──┬──┬──┬──┬──┐       ┌────┬────┬────┬────┐
  │1 │2 │3 │4 │5 │6 │7 │8 │       │ 1  │ 2  │ 3  │ 4  │
  └──┴──┴──┴──┴──┴──┴──┴──┘       ├────┼────┼────┼────┤
  (totul micșorat pe un rând)      │ 5  │ 6  │ 7  │ 8  │
                                   └────┴────┴────┴────┘
                                   (trec pe rândul următor)
```

---

## 4.5 Proprietăți Flexbox pe elemente (copii)

### `flex-grow` — Cât de mult crește un element

```css
.item-1 { flex-grow: 1; }     /* crește normal */
.item-2 { flex-grow: 2; }     /* crește de 2x mai mult */
.item-3 { flex-grow: 1; }     /* crește normal */
```

```
  ┌──────────┬────────────────────┬──────────┐
  │  Item 1  │      Item 2       │  Item 3  │
  │  (1 parte)│   (2 părți)       │ (1 parte)│
  └──────────┴────────────────────┴──────────┘
  
  Spațiul liber se împarte: 1 + 2 + 1 = 4 părți
  Item 1 primește 1/4, Item 2 primește 2/4, Item 3 primește 1/4
```

### Scurtătura `flex`

```css
.item {
    flex: 1;          /* fiecare element ocupă spațiu egal */
}
```

Aceasta este forma pe care o vei folosi cel mai des. Când toate elementele au `flex: 1`, își împart spațiul **în mod egal**:

```css
.coloana { flex: 1; }
```

```html
<div class="container">
    <div class="coloana">Coloana 1</div>
    <div class="coloana">Coloana 2</div>
    <div class="coloana">Coloana 3</div>
</div>
```

```
  ┌──────────────┬──────────────┬──────────────┐
  │  Coloana 1   │  Coloana 2   │  Coloana 3   │
  │   (flex:1)   │   (flex:1)   │   (flex:1)   │
  │  ──33.3%──   │  ──33.3%──   │  ──33.3%──   │
  └──────────────┴──────────────┴──────────────┘
```

---

## 4.6 Flexbox în practică — Exerciții vizuale

Hai să construim câteva layout-uri reale. Creează un fișier `layout.html` cu CSS-ul inclus:

### Exercițiul 1: Meniu de navigație orizontal

```html
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exerciții Layout</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: "Segoe UI", sans-serif; padding: 20px; }

        /* ── Meniu de navigație ── */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #2C3E50;
            padding: 15px 25px;
            border-radius: 10px;
        }

        .logo {
            color: white;
            font-size: 22px;
            font-weight: bold;
        }

        .meniu {
            display: flex;
            gap: 20px;
            list-style: none;      /* elimină bulinele */
        }

        .meniu a {
            color: #BDC3C7;
            text-decoration: none;
            font-size: 15px;
            padding: 8px 14px;
            border-radius: 6px;
        }

        .meniu a:hover {
            background-color: rgba(255, 255, 255, 0.1);
            color: white;
        }
    </style>
</head>
<body>

    <nav class="navbar">
        <div class="logo">🚀 Site-ul Meu</div>
        <ul class="meniu">
            <li><a href="#">Acasă</a></li>
            <li><a href="#">Despre</a></li>
            <li><a href="#">Proiecte</a></li>
            <li><a href="#">Contact</a></li>
        </ul>
    </nav>

</body>
</html>
```

Cum funcționează:

```
  ┌─────────────────────────────────────────────────┐
  │  🚀 Site-ul Meu           Acasă Despre Proiecte │
  │  ◄── logo                         meniu ──►    │
  │                                                  │
  │  justify-content: space-between                 │
  │  (logo la stânga, meniu la dreapta)              │
  └─────────────────────────────────────────────────┘
  
  Meniul intern:
  ┌─────────────────────────────────────┐
  │  Acasă    Despre    Proiecte    Contact  │
  │  ◄── display: flex + gap: 20px ──►  │
  └─────────────────────────────────────┘
```

### Exercițiul 2: Carduri în rând

Adaugă acest cod sub navbar (în `<body>`):

```html
<style>
    /* ── Secțiune carduri ── */
    .sectiune-titlu {
        text-align: center;
        margin: 40px 0 25px;
        font-size: 26px;
        color: #2C3E50;
    }

    .carduri {
        display: flex;
        gap: 20px;
    }

    .card {
        flex: 1;
        background-color: white;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 25px;
    }

    .card h3 {
        color: #5A67D8;
        margin-bottom: 10px;
    }

    .card p {
        color: #4A5568;
        font-size: 14px;
        line-height: 1.6;
    }
</style>

<h2 class="sectiune-titlu">Ce vei învăța</h2>
<div class="carduri">
    <div class="card">
        <h3>🧱 HTML</h3>
        <p>Scheletul paginii — structura, textele, imaginile și linkurile.</p>
    </div>
    <div class="card">
        <h3>🎨 CSS</h3>
        <p>Stilul paginii — culori, fonturi, spații și animații.</p>
    </div>
    <div class="card">
        <h3>⚡ JavaScript</h3>
        <p>Creierul paginii — interactivitate, jocuri și logică.</p>
    </div>
</div>
```

```
  ┌──────────────┬──────────────┬──────────────┐
  │  🧱 HTML     │  🎨 CSS     │  ⚡ JS       │
  │              │              │              │
  │  Scheletul   │  Stilul      │  Creierul    │
  │  paginii...  │  paginii...  │  paginii...  │
  │              │              │              │
  │  (flex: 1)   │  (flex: 1)   │  (flex: 1)   │
  └──────────────┴──────────────┴──────────────┘
       ◄── Toate au aceeași lățime (flex: 1) ──►
```

### Exercițiul 3: Layout cu sidebar

```html
<style>
    /* ── Layout cu sidebar ── */
    .layout {
        display: flex;
        gap: 20px;
        margin-top: 30px;
    }

    .sidebar {
        width: 250px;                   /* lățime fixă */
        background-color: #F7FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 20px;
    }

    .continut-principal {
        flex: 1;                        /* ocupă restul spațiului */
        background-color: white;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 25px;
    }
</style>

<div class="layout">
    <aside class="sidebar">
        <h3>📋 Meniu lateral</h3>
        <ul>
            <li>Capitolul 1</li>
            <li>Capitolul 2</li>
            <li>Capitolul 3</li>
            <li>Capitolul 4</li>
        </ul>
    </aside>
    <main class="continut-principal">
        <h2>Conținutul principal</h2>
        <p>Aceasta este zona de conținut care ocupă tot spațiul rămas 
        după sidebar. Cu flex: 1, se adaptează automat la orice lățime 
        de ecran!</p>
    </main>
</div>
```

```
  ┌──────────────┬──────────────────────────────────┐
  │  📋 Meniu    │                                   │
  │  lateral     │       Conținutul principal         │
  │              │                                   │
  │  Cap. 1      │       Aceasta este zona de        │
  │  Cap. 2      │       conținut care ocupă tot     │
  │  Cap. 3      │       spațiul rămas...            │
  │  Cap. 4      │                                   │
  │              │                                   │
  │ width: 250px │          flex: 1                  │
  └──────────────┴──────────────────────────────────┘
     ◄── fix ──►  ◄── se adaptează ──────────────►
```

### Exercițiul 4: Centrare verticală și orizontală

```html
<style>
    .centru-perfect {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 300px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 12px;
        margin-top: 30px;
    }

    .mesaj-centrat {
        background-color: white;
        padding: 30px 50px;
        border-radius: 12px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        color: #5A67D8;
    }
</style>

<div class="centru-perfect">
    <div class="mesaj-centrat">
        ✨ Sunt centrat perfect! ✨
    </div>
</div>
```

---

## 4.7 Flexbox Cheat Sheet — Referință rapidă

Pune această pagină la semn de carte. O vei folosi mereu!

### Proprietăți pe CONTAINER (părinte):

```css
.container {
    display: flex;              /* ACTIVEAZĂ Flexbox */
    
    /* Direcție */
    flex-direction: row;        /* orizontal (implicit) */
    flex-direction: column;     /* vertical */
    
    /* Spațiere pe axa principală */
    justify-content: flex-start;    /* la început */
    justify-content: center;        /* centrat */
    justify-content: flex-end;      /* la sfârșit */
    justify-content: space-between; /* spațiu ÎNTRE elemente */
    justify-content: space-evenly;  /* spațiu EGAL peste tot */
    
    /* Aliniere pe axa secundară */
    align-items: stretch;       /* se întinde (implicit) */
    align-items: flex-start;    /* sus */
    align-items: center;        /* centru */
    align-items: flex-end;      /* jos */
    
    /* Spațiere */
    gap: 20px;                  /* spațiu între elemente */
    
    /* Wrap */
    flex-wrap: wrap;            /* trece pe rândul următor */
}
```

### Proprietăți pe ELEMENT (copil):

```css
.element {
    flex: 1;                    /* crește pentru a umple spațiul */
    flex: 2;                    /* crește de 2x mai mult */
    align-self: center;         /* se aliniază diferit de frați */
}
```

---

## 4.8 Tag-uri HTML semantice — Structură cu sens

Până acum am folosit `<div>` pentru tot. Dar HTML5 oferă tag-uri speciale care **descriu** ce conțin:

```
  ┌─────────────────────────────────────────────┐
  │                  <header>                    │
  │   Logo            Navigație                  │
  ├─────────────────────────────────────────────┤
  │                   <nav>                      │
  │   Acasă | Despre | Proiecte | Contact        │
  ├──────────────────────┬──────────────────────┤
  │                      │                      │
  │       <main>         │     <aside>          │
  │                      │                      │
  │  ┌─ <section> ─────┐ │  Sidebar cu          │
  │  │  Conținut 1      │ │  informații          │
  │  └─────────────────┘ │  suplimentare        │
  │                      │                      │
  │  ┌─ <section> ─────┐ │                      │
  │  │  Conținut 2      │ │                      │
  │  └─────────────────┘ │                      │
  │                      │                      │
  ├──────────────────────┴──────────────────────┤
  │                  <footer>                    │
  │   © 2025 Numele meu                         │
  └─────────────────────────────────────────────┘
```

| Tag | Înlocuiește | Înseamnă |
|---|---|---|
| `<header>` | `<div class="header">` | Antetul paginii (logo, titlu) |
| `<nav>` | `<div class="nav">` | Meniu de navigație |
| `<main>` | `<div class="main">` | Conținutul principal |
| `<section>` | `<div class="section">` | O secțiune tematică |
| `<aside>` | `<div class="aside">` | Conținut lateral (sidebar) |
| `<footer>` | `<div class="footer">` | Subsolul paginii |
| `<article>` | `<div class="article">` | Un articol independent |

De ce contează? Aceste tag-uri ajută:
1. **Browserele** să înțeleagă structura paginii
2. **Motoarele de căutare** (Google) să indexeze mai bine conținutul
3. **Screen reader-urile** să navigheze mai ușor (accesibilitate)
4. **Tu** să citești codul mai ușor (mai clar decât 100 de div-uri)

> 💡 **Sfat!**
> Folosește tag-uri semantice ori de câte ori poți. Dacă secțiunea are un rol clar (header, footer, navigație), folosește tag-ul potrivit. Dacă e doar un container generic de stilizare, folosește `<div>`.

---

## 4.9 Responsive Design — Pagina ta pe orice ecran 📱

Responsive design înseamnă că pagina ta **se adaptează** la dimensiunea ecranului: desktop mare, laptop, tabletă, telefon.

### Metafora: Apa se adaptează vasului

```
  Desktop (1200px)          Tabletă (768px)        Telefon (375px)
  ┌─────────────────┐       ┌───────────┐          ┌─────┐
  │ ┌──┐ ┌──┐ ┌──┐ │       │ ┌──┐ ┌──┐ │          │┌───┐│
  │ │1 │ │2 │ │3 │ │       │ │1 │ │2 │ │          ││ 1 ││
  │ └──┘ └──┘ └──┘ │       │ └──┘ └──┘ │          │└───┘│
  │                 │       │ ┌──┐      │          │┌───┐│
  │                 │       │ │3 │      │          ││ 2 ││
  │                 │       │ └──┘      │          │└───┘│
  └─────────────────┘       └───────────┘          │┌───┐│
                                                   ││ 3 ││
  3 coloane                 2 coloane               │└───┘│
                                                   └─────┘
                                                   1 coloană
```

Pagina e ca **apa**: se adaptează formei vasului (ecranului).

### `<meta viewport>` — Obligatoriu!

Acest tag (pe care l-am adăugat deja) spune telefoanelor să nu micșoreze pagina:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Fără el, telefonul afișează pagina ca pe un desktop minuscul. Cu el, pagina se adaptează la lățimea ecranului.

### Media Queries — CSS-ul se schimbă la diferite dimensiuni

Media queries sunt instrucțiuni CSS de tipul „**dacă** ecranul e mai mic de X pixeli, **atunci** aplică aceste stiluri":

```css
/* Stiluri pentru TOATE ecranele (mobile first) */
.carduri {
    display: flex;
    flex-direction: column;    /* pe telefon: cardurile una sub alta */
    gap: 15px;
}

/* Dacă ecranul e cel puțin 768px (tabletă) */
@media (min-width: 768px) {
    .carduri {
        flex-direction: row;   /* pe tabletă: cardurile una lângă alta */
    }
}
```

Cum funcționează:

```
  Lățime ecran:    0px ──────── 767px ──────── 768px+ ──────────►
                   
  flex-direction:  column                      row
                   (una sub alta)              (una lângă alta)
                   
  Vizual:          ┌────┐                      ┌────┬────┬────┐
                   │ 1  │                      │ 1  │ 2  │ 3  │
                   ├────┤                      └────┴────┴────┘
                   │ 2  │
                   ├────┤
                   │ 3  │
                   └────┘
```

### Breakpoints comune

**Breakpoint** = dimensiunea la care layout-ul se schimbă:

```css
/* Telefon: 0 - 767px (stilurile de bază, fără media query) */

/* Tabletă: 768px+ */
@media (min-width: 768px) {
    /* stiluri pentru tabletă și mai mare */
}

/* Desktop: 1024px+ */
@media (min-width: 1024px) {
    /* stiluri pentru desktop */
}

/* Desktop mare: 1200px+ */
@media (min-width: 1200px) {
    /* stiluri pentru ecrane mari */
}
```

### Exemplu practic complet

```css
/* ── BAZĂ (telefon) ── */
.container {
    padding: 15px;
}

.navbar {
    display: flex;
    flex-direction: column;     /* logo sus, meniu jos */
    align-items: center;
    gap: 15px;
}

.carduri {
    display: flex;
    flex-direction: column;     /* carduri una sub alta */
    gap: 15px;
}

.layout {
    display: flex;
    flex-direction: column;     /* sidebar jos, conținut sus */
}

/* ── TABLETĂ (768px+) ── */
@media (min-width: 768px) {
    .container {
        padding: 25px;
    }

    .navbar {
        flex-direction: row;        /* logo și meniu pe același rând */
        justify-content: space-between;
    }

    .carduri {
        flex-direction: row;        /* carduri una lângă alta */
    }

    .layout {
        flex-direction: row;        /* sidebar + conținut alăturate */
    }
}

/* ── DESKTOP (1024px+) ── */
@media (min-width: 1024px) {
    .container {
        max-width: 1000px;
        margin: 0 auto;            /* centrează pe ecrane mari */
    }
}
```

> 🚀 **Provocare!**
> Deschide pagina ta în browser, apoi trage marginea ferestrei pentru a o face mai îngustă sau mai lată. Sau apasă `F12` → click pe iconița de telefon/tabletă (Device Toolbar) → alege diferite dispozitive. Observă cum se schimbă layout-ul!

---

## 4.10 Unități relative — Dimensiuni flexibile

Pe lângă `px`, CSS oferă unități care se **adaptează**:

### Procente (`%`)

```css
.imagine {
    width: 100%;       /* ocupă toată lățimea părintelui */
    max-width: 600px;  /* dar nu mai mult de 600px */
}
```

### `em` și `rem`

```css
/* em = relativ la fontul PĂRINTELUI */
.copil {
    font-size: 1.5em;      /* 1.5x fontul părintelui */
    padding: 1em;           /* padding = 1x fontul curent */
}

/* rem = relativ la fontul paginii (html) — mai previzibil! */
h1 {
    font-size: 2rem;        /* 2x fontul de bază (de obicei 32px) */
    margin-bottom: 1rem;    /* 16px dacă baza e 16px */
}
```

### `vh` și `vw` — Viewport units

```css
/* vh = procent din ÎNĂLȚIMEA ecranului */
.hero {
    height: 100vh;     /* ocupă TOT ecranul pe înălțime */
}

/* vw = procent din LĂȚIMEA ecranului */
.linie {
    width: 50vw;       /* jumătate din lățimea ecranului */
}
```

```
  100vh = întreg ecranul pe verticală
  ┌─────────────────────────┐  ▲
  │                         │  │
  │                         │  │
  │     100vh               │  │ înălțimea
  │                         │  │ browserului
  │                         │  │
  │                         │  │
  └─────────────────────────┘  ▼
  ◄────── 100vw ──────────►
         lățimea
         browserului
```

### Când folosești fiecare unitate?

| Unitate | Folosire ideală | Exemplu |
|---|---|---|
| `px` | Dimensiuni fixe, mici (borders, shadows) | `border: 2px solid gray;` |
| `%` | Lățimi flexibile relative la părinte | `width: 80%;` |
| `rem` | Dimensiuni de font și spațiere generală | `font-size: 1.2rem;` |
| `em` | Spațiere relativă la fontul elementului | `padding: 0.5em 1em;` |
| `vh/vw` | Secțiuni full-screen | `min-height: 100vh;` |

---

## 4.11 Proiect practic: Pagină de prezentare completă 🚀

Hai să construim o pagină de prezentare completă care folosește **tot** ce am învățat: Flexbox, responsive design, tag-uri semantice.

Creează structura:

```
  📁 pagina-prezentare/
  ├── index.html
  └── stil.css
```

### HTML (`index.html`):

```html
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Micul Constructor Web</title>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="stil.css">
</head>
<body>

    <!-- NAVIGAȚIE -->
    <nav class="navbar">
        <div class="container navbar-interior">
            <div class="logo">🏗️ Constructor<span class="logo-accent">Web</span></div>
            <ul class="meniu">
                <li><a href="#acasa">Acasă</a></li>
                <li><a href="#lectii">Lecții</a></li>
                <li><a href="#proiecte">Proiecte</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- HERO (secțiunea principală) -->
    <header id="acasa" class="hero">
        <div class="container hero-interior">
            <h1>Învață să construiești<br>site-uri web! 🚀</h1>
            <p class="hero-subtitlu">HTML, CSS și JavaScript — pas cu pas, 
            de la zero la propriul tău site.</p>
            <a href="#lectii" class="buton-hero">Începe aventura</a>
        </div>
    </header>

    <!-- LECȚII (carduri) -->
    <section id="lectii" class="sectiune">
        <div class="container">
            <h2 class="sectiune-titlu">Ce vei învăța</h2>
            <div class="carduri">
                <div class="card">
                    <div class="card-icon">🧱</div>
                    <h3>HTML</h3>
                    <p>Construiește structura paginii: texte, imagini, 
                    liste, linkuri și formulare.</p>
                </div>
                <div class="card">
                    <div class="card-icon">🎨</div>
                    <h3>CSS</h3>
                    <p>Dă viață paginii cu culori, fonturi, animații 
                    și layout-uri responsive.</p>
                </div>
                <div class="card">
                    <div class="card-icon">⚡</div>
                    <h3>JavaScript</h3>
                    <p>Adaugă interactivitate: butoane, jocuri, 
                    quiz-uri și efecte dinamice.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- PROIECTE -->
    <section id="proiecte" class="sectiune sectiune-colorata">
        <div class="container">
            <h2 class="sectiune-titlu">Proiecte practice</h2>
            <div class="proiecte-lista">
                <div class="proiect">
                    <span class="proiect-numar">01</span>
                    <div>
                        <h3>Quiz Game</h3>
                        <p>Un joc de întrebări și răspunsuri cu scor și feedback vizual.</p>
                    </div>
                </div>
                <div class="proiect">
                    <span class="proiect-numar">02</span>
                    <div>
                        <h3>Catch the Stars</h3>
                        <p>Un joc 2D pe Canvas unde prinzi stele care cad din cer.</p>
                    </div>
                </div>
                <div class="proiect">
                    <span class="proiect-numar">03</span>
                    <div>
                        <h3>Portofoliul Meu</h3>
                        <p>Propriul tău site web cu toate proiectele prezentate frumos.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer id="contact" class="footer">
        <div class="container footer-interior">
            <p>Creat cu ❤️ de [Numele tău]</p>
            <p class="footer-mic">Constructorul de Site-uri — Capitolul 4</p>
        </div>
    </footer>

</body>
</html>
```

### CSS (`stil.css`):

```css
/* ============================
   RESET ȘI BAZĂ
   ============================ */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: "Nunito", sans-serif;
    color: #2C3E50;
    line-height: 1.7;
}

.container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 0 20px;
}

/* ============================
   NAVIGAȚIE
   ============================ */
.navbar {
    background-color: white;
    border-bottom: 1px solid #E2E8F0;
    padding: 12px 0;
    position: sticky;          /* rămâne sus la scroll! */
    top: 0;
    z-index: 100;
}

.navbar-interior {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-family: "Fredoka", sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #2C3E50;
}

.logo-accent {
    color: #5A67D8;
}

.meniu {
    display: flex;
    gap: 8px;
    list-style: none;
}

.meniu a {
    text-decoration: none;
    color: #4A5568;
    font-size: 15px;
    font-weight: 600;
    padding: 8px 16px;
    border-radius: 8px;
}

.meniu a:hover {
    background-color: #EBF4FF;
    color: #5A67D8;
}

/* ============================
   HERO
   ============================ */
.hero {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    text-align: center;
    padding: 80px 20px;
}

.hero h1 {
    font-family: "Fredoka", sans-serif;
    font-size: 36px;
    font-weight: 700;
    margin-bottom: 16px;
    line-height: 1.3;
}

.hero-subtitlu {
    font-size: 18px;
    color: rgba(255, 255, 255, 0.85);
    max-width: 500px;
    margin: 0 auto 30px;
}

.buton-hero {
    display: inline-block;
    background-color: white;
    color: #5A67D8;
    font-family: "Fredoka", sans-serif;
    font-size: 16px;
    font-weight: 600;
    padding: 14px 36px;
    border-radius: 50px;
    text-decoration: none;
}

.buton-hero:hover {
    background-color: #EBF4FF;
}

/* ============================
   SECȚIUNI
   ============================ */
.sectiune {
    padding: 60px 0;
}

.sectiune-colorata {
    background-color: #F7FAFC;
}

.sectiune-titlu {
    font-family: "Fredoka", sans-serif;
    font-size: 28px;
    text-align: center;
    color: #2C3E50;
    margin-bottom: 35px;
}

/* ============================
   CARDURI
   ============================ */
.carduri {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.card {
    background-color: white;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 30px;
    text-align: center;
}

.card-icon {
    font-size: 40px;
    margin-bottom: 12px;
}

.card h3 {
    font-family: "Fredoka", sans-serif;
    color: #5A67D8;
    font-size: 22px;
    margin-bottom: 8px;
}

.card p {
    color: #4A5568;
    font-size: 15px;
}

/* ============================
   PROIECTE
   ============================ */
.proiecte-lista {
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.proiect {
    display: flex;
    align-items: center;
    gap: 20px;
    background-color: white;
    padding: 22px 28px;
    border-radius: 12px;
    border: 1px solid #E2E8F0;
}

.proiect-numar {
    font-family: "Fredoka", sans-serif;
    font-size: 32px;
    font-weight: 700;
    color: #C3DAFE;
    min-width: 50px;
}

.proiect h3 {
    font-family: "Fredoka", sans-serif;
    color: #2C3E50;
    margin-bottom: 4px;
}

.proiect p {
    color: #718096;
    font-size: 14px;
}

/* ============================
   FOOTER
   ============================ */
.footer {
    background-color: #2C3E50;
    color: rgba(255, 255, 255, 0.7);
    text-align: center;
    padding: 30px 20px;
}

.footer-mic {
    font-size: 12px;
    color: rgba(255, 255, 255, 0.4);
    margin-top: 6px;
}

/* ============================
   RESPONSIVE — TABLETĂ (768px+)
   ============================ */
@media (min-width: 768px) {
    .hero h1 {
        font-size: 48px;
    }

    .carduri {
        flex-direction: row;       /* carduri una lângă alta */
    }

    .card {
        flex: 1;
    }
}

/* ============================
   RESPONSIVE — DESKTOP (1024px+)
   ============================ */
@media (min-width: 1024px) {
    .hero {
        padding: 100px 20px;
    }

    .hero h1 {
        font-size: 54px;
    }
}
```

> ⚠️ **Atenție!**
> Observă cum CSS-ul este scris **mobile-first**: stilurile de bază sunt pentru telefon (cardurile una sub alta cu `flex-direction: column`), iar media queries le schimbă pentru ecrane mai mari (`flex-direction: row`). Aceasta este abordarea profesionistă!

---

## 4.12 Greșeli frecvente (și cum le repari) 🔧

### ❌ Greșeala 1: Flexbox pe elementul greșit

```css
/* ❌ GREȘIT — display: flex pe copil */
.card {
    display: flex;     /* Asta face conținutul INTERIOR al cardului flex */
}

/* ✅ CORECT — display: flex pe PĂRINTE */
.carduri {
    display: flex;     /* Asta aranjează cardurile una lângă alta */
}
```

**Regulă:** `display: flex` se pune pe **container** (părintele), nu pe elementele pe care vrei să le aranjezi.

### ❌ Greșeala 2: Uiți viewport meta tag

```html
<!-- ❌ Lipsește viewport → pagina arată minusculă pe telefon -->
<head>
    <title>Pagina mea</title>
</head>

<!-- ✅ Cu viewport → pagina se adaptează -->
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pagina mea</title>
</head>
```

### ❌ Greșeala 3: Lățimi fixe pe elementele responsive

```css
/* ❌ GREȘIT — lățime fixă, se tăie pe telefon */
.card {
    width: 350px;
}

/* ✅ CORECT — lățime flexibilă */
.card {
    flex: 1;
    min-width: 250px;     /* nu se micșorează sub 250px */
}
```

### ❌ Greșeala 4: Confuzie justify-content vs align-items

```
  flex-direction: row (implicit)
  
                    justify-content
                    (axa principală)
  ◄──────────────────────────────────────────────►
  
  ▲ ┌─────────────────────────────────────────┐
  │ │                                         │
  │ │    ┌───┐    ┌───┐    ┌───┐             │
  │ │    │ 1 │    │ 2 │    │ 3 │             │
  │ │    └───┘    └───┘    └───┘             │
  │ │                                         │
  ▼ └─────────────────────────────────────────┘
  
  align-items
  (axa secundară)
  
  Regulă simplă:
  • justify-content = direcția principală (unde merg elementele)
  • align-items = direcția perpendiculară (cum se aliniază)
```

### ❌ Greșeala 5: Media query cu max-width în loc de min-width

```css
/* ❌ Poate funcționa, dar nu e "mobile first" */
@media (max-width: 768px) {
    /* stiluri pentru telefon */
}

/* ✅ Mobile first — pornești de la mic, crești */
/* Stilurile de bază sunt pentru telefon */
@media (min-width: 768px) {
    /* stiluri care SE ADAUGĂ pentru tabletă și mai mare */
}
```

---

## 4.13 Mini-quiz — Verifică ce ai învățat! ✅

**1.** Care este diferența dintre un element **block** și unul **inline**?

**2.** Ce proprietate CSS activează Flexbox?

**3.** Cum centrezi un element atât orizontal cât și vertical cu Flexbox?

**4.** Ce face `justify-content: space-between`?

**5.** Ce face `flex: 1` pe un element copil?

**6.** Ce este un „breakpoint" în responsive design?

**7.** Completează: Responsive design se scrie „_________ first" — pornind de la stiluri pentru ecrane mici.

---

<details>
<summary>🔑 Click aici pentru răspunsuri</summary>

1. Un element **block** ocupă tot rândul disponibil și forțează o linie nouă (ex: `<div>`, `<p>`, `<h1>`). Un element **inline** stă pe aceeași linie cu vecinii și nu forțează linie nouă (ex: `<span>`, `<a>`, `<strong>`).

2. **`display: flex;`** — se pune pe elementul **părinte** (containerul).

3. Cu cele trei proprietăți pe container:
   ```css
   display: flex;
   justify-content: center;
   align-items: center;
   ```

4. Distribuie elementele astfel încât **primul** e la început, **ultimul** e la sfârșit, iar **spațiul** se împarte egal între ele (nu și la margini).

5. Elementul **crește** pentru a umple spațiul disponibil. Dacă mai mulți copii au `flex: 1`, își împart spațiul **în mod egal**.

6. Dimensiunea ecranului la care **layout-ul se schimbă** (de exemplu, de la o coloană la trei coloane). Se definește cu `@media (min-width: ...)`.

7. **Mobile** first — pornești cu stiluri pentru telefon (cel mai mic ecran), apoi adaugi stiluri pentru ecrane mai mari cu media queries.

</details>

---

## 4.14 Știai că? — Curiozități din lumea tech 🤓

📱 **Primul iPhone** a fost lansat în 2007, iar responsive design-ul a devenit popular abia în 2010, când Ethan Marcotte a publicat un articol revoluționar. Înainte, multe site-uri aveau o versiune separată pentru mobil (m.facebook.com, m.youtube.com). Responsive design a eliminat nevoia de versiuni separate!

🧮 **Flexbox a fost propus pentru prima dată în 2009**, dar a durat până în 2012-2014 ca toate browserele să îl susțină complet. Înainte de Flexbox, programatorii foloseau trucuri cu `float`, `position` și `table` care erau complicate și pline de bug-uri. Generația ta are noroc — aveți Flexbox de la bun început!

📐 **CSS Grid** este „fratele mai mare" al Flexbox-ului. Dacă Flexbox aranjează elemente pe **o singură direcție** (rând sau coloană), Grid le aranjează pe **două direcții** simultan (rânduri ȘI coloane). Îl vei descoperi pe măsură ce avansezi!

🌍 **Peste 60% din traficul web global** vine de pe dispozitive mobile. În unele țări, procentul depășește 80%. De aceea, „mobile first" nu e doar o preferință — e o necesitate. Când construiești un site, telefonul e prioritatea!

---

## Recapitulare — Ce ai învățat în Capitolul 4

```
  ✅ Block vs. Inline — cum ocupă elementele spațiul
  ✅ <div> (block) și <span> (inline) — cutii universale
  ✅ display: block, inline, inline-block, flex
  ✅ FLEXBOX pe container: display: flex
  ✅ flex-direction: row (orizontal) / column (vertical)
  ✅ justify-content: spațierea pe axa principală
  ✅ align-items: alinierea pe axa secundară
  ✅ Centrare perfectă cu justify-content + align-items: center
  ✅ gap: spațiu între elemente
  ✅ flex-wrap: wrap — trece pe rândul următor
  ✅ flex: 1 pe copii — împart spațiul egal
  ✅ Tag-uri semantice: header, nav, main, section, footer, aside
  ✅ Responsive design — pagina se adaptează la orice ecran
  ✅ Media queries: @media (min-width: ...) { }
  ✅ Mobile first — pornești de la telefon, crești
  ✅ Unități: px, %, rem, em, vh, vw
  ✅ Ai construit o pagină completă de prezentare! 🎉
```

---

## Ce urmează?

Felicitări! Ai terminat **Partea I — Fundamente**. Acum știi HTML, CSS și layout responsive — ai tot ce trebuie pentru a crea pagini web frumoase și bine organizate!

În **Capitolul 5: JavaScript — Pagina prinde viață!**, vei învăța primul limbaj de **programare** din carte. Pagina ta nu va mai fi doar frumoasă — va fi și **inteligentă**! Vei învăța variabile, operații, și cum să vorbești cu browserul prin `console.log()`.

Pregătește-te — magia abia începe! ⚡

---

> *„Flexibilitatea este cheia stabilității."*
> — John Wooden
