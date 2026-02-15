# Capitolul 9: Animații CSS și JavaScript 💃

> *„Mișcarea este viața. Fără mișcare, viața e de neconceput."*
> — Moshe Feldenkrais

---

## Ce vei învăța în acest capitol

- **Tranziții CSS** — schimbări fluide la hover, click, focus
- **`@keyframes`** — animații complexe cu mai mulți pași
- Proprietatea **`transform`** — rotiri, scalări, translații
- Cum controlezi animații din **JavaScript**
- **Animații la scroll** — elemente care apar pe măsură ce derulezi
- Cum combini CSS și JS pentru **efecte profesionale**

---

## 9.1 De ce contează animațiile?

Deschide orice site modern — Instagram, YouTube, Spotify — și observă: butoanele se colorează lin la hover, meniurile alunecă, cardurile se ridică, conținutul apare cu fade-in. Nimic nu „sare" brusc.

Animațiile nu sunt doar decorative. Ele servesc un **scop**:

```
  ┌─────────────────────────────────────────────────────────┐
  │  DE CE ANIMĂM?                                         │
  │                                                         │
  │  🎯 Ghidare    — Atrag atenția spre ce e important     │
  │  📍 Feedback   — Confirmă că acțiunea a funcționat     │
  │  🧠 Context    — Arată de unde vine un element         │
  │  ✨ Plăcere    — Fac experiența mai plăcută            │
  │  ⏱️ Răbdare    — Fac așteptarea mai suportabilă       │
  │                                                         │
  │  FĂRĂ animații:           CU animații:                  │
  │  Buton: click → nimic    Buton: click → se colorează   │
  │  Meniu: apare brusc      Meniu: alunecă lin            │
  │  Card: static            Card: se ridică la hover      │
  └─────────────────────────────────────────────────────────┘
```

Dar atenție: animațiile trebuie să fie **subtile** și **rapide**. Nimeni nu vrea să aștepte 3 secunde ca un buton să se coloreze. Regula de aur: **200-500 milisecunde** pentru majoritatea tranzițiilor.

---

## 9.2 Tranziții CSS — Schimbări liniștite

O **tranziție** spune browserului: „Nu sări direct la noul stil — fă schimbarea **treptat**, pe o durată de timp."

### Fără vs. cu tranziție

```css
/* FĂRĂ tranziție — schimbarea e INSTANTANEE */
.buton {
    background-color: #5A67D8;
    color: white;
}
.buton:hover {
    background-color: #434190;
    /* BAM! Culoarea sare instant. */
}

/* CU tranziție — schimbarea e TREPTATĂ */
.buton {
    background-color: #5A67D8;
    color: white;
    transition: background-color 0.3s;    /* ← magia! */
}
.buton:hover {
    background-color: #434190;
    /* Culoarea se schimbă lin, în 0.3 secunde */
}
```

```
  FĂRĂ tranziție:
  Stare 1:  ████████████  →  Stare 2:  ████████████
  (albastru)      │ INSTANT!  (albastru închis)
  
  CU tranziție (0.3s):
  Stare 1:  ████████████  →→→→→→→  Stare 2:  ████████████
  (albastru)    ── 0.3 secunde ──  (albastru închis)
              schimbare treptată
```

### Anatomia proprietății `transition`

```css
.element {
    transition: proprietate  durată  funcție-timing  întârziere;
    /*          ──────────   ──────  ──────────────  ──────────
                CE se         CÂT     CUM se          CÂND
                animează     durează  mișcă           începe    */
}

/* Exemple concrete */
.card {
    transition: background-color 0.3s ease;
    transition: transform 0.5s ease-out;
    transition: opacity 0.4s ease-in 0.1s;     /* cu 0.1s întârziere */
    transition: all 0.3s ease;                  /* TOTUL se animează */
}
```

### Funcțiile de timing — Cum se mișcă

```
  ease (implicit)     ease-in           ease-out          linear
  ─────────────       ───────           ────────          ──────
  
  Viteză               Viteză            Viteză            Viteză
  │    ╭───╮          │      ╭──        │──╮              │  ╱
  │   ╱     ╲         │    ╱            │   ╲             │ ╱
  │  ╱       ╲        │  ╱              │    ╲            │╱
  │╱          ╲       │╱                │     ╲──         │
  └──────────────     └──────────────   └──────────────   └──────────
       Timp                Timp              Timp              Timp
  
  Pornește lent,      Pornește lent,    Pornește rapid,   Viteză
  accelerează,        accelerează       încetinește       constantă
  apoi încetinește    (ca o mașină      (ca o minge       (ca un tren
  (cel mai natural)    care pleacă)      care se oprește)  pe șine)
```

> 💡 **Sfat!**
> `ease` este implicit și funcționează bine în 90% din cazuri. Folosește `ease-out` pentru elemente care **apar** (intră pe ecran) și `ease-in` pentru elemente care **dispar**.

### Tranziții pe mai multe proprietăți

```css
.card {
    background-color: white;
    transform: translateY(0);
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    
    /* Separă cu virgulă sau folosește "all" */
    transition: transform 0.3s ease,
                box-shadow 0.3s ease,
                background-color 0.3s ease;
    
    /* Sau mai simplu: */
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    background-color: #F7FAFC;
}
```

> ⚠️ **Atenție!**
> `transition: all` e convenabil, dar poate anima proprietăți pe care nu le dorești (de exemplu, `width` sau `height` la resize). Pentru performanță optimă, specifică exact ce proprietăți vrei să animezi.

---

## 9.3 `transform` — Mișcă, rotește, scalează

`transform` este proprietatea care **modifică forma și poziția** unui element fără a afecta layout-ul. Este incredibil de performantă și versatilă.

### Translate — Mută elementul

```css
.element {
    transform: translateX(50px);     /* mută 50px la dreapta */
    transform: translateY(-20px);    /* mută 20px în sus */
    transform: translate(50px, -20px); /* ambele simultan */
}
```

```
  translateX(50px)         translateY(-20px)
  
  ┌───┐     ┌───┐         ┌───┐
  │ X │ ──► │ X │         │ X │
  └───┘     └───┘         └─┬─┘
  original   mutat           │ ▲ -20px
             50px→           │
                           ┌─┴─┐
                           │ X │
                           └───┘
                           original
```

### Scale — Mărește sau micșorează

```css
.element:hover {
    transform: scale(1.1);           /* 110% din dimensiune — mai mare */
    transform: scale(0.9);           /* 90% — mai mic */
    transform: scaleX(1.5);          /* mai lat, înălțimea la fel */
}
```

### Rotate — Rotește

```css
.element:hover {
    transform: rotate(45deg);        /* rotește 45 de grade */
    transform: rotate(-90deg);       /* rotește 90° în sens invers */
    transform: rotate(360deg);       /* rotație completă */
}
```

```
  rotate(0deg)    rotate(45deg)     rotate(90deg)
  
  ┌────────┐       ╱╲                  │
  │        │      ╱  ╲                 │
  │   😀   │     │ 😀 │            ────┤ 😀 ├────
  │        │      ╲  ╱                 │
  └────────┘       ╲╱                  │
```

### Combinarea transformărilor

Poți aplica **mai multe** transformări simultan:

```css
.card:hover {
    transform: translateY(-10px) scale(1.02) rotate(1deg);
    /* Se ridică, devine puțin mai mare, se înclină ușor */
}
```

> ⚠️ **Atenție!**
> **Nu** poți pune două proprietăți `transform` separate — a doua o suprascrie pe prima:
> ```css
> /* ❌ GREȘIT — doar rotate se aplică */
> .element {
>     transform: translateX(50px);
>     transform: rotate(45deg);      /* ← suprascrie translateX! */
> }
> 
> /* ✅ CORECT — ambele într-o singură declarație */
> .element {
>     transform: translateX(50px) rotate(45deg);
> }
> ```

### `transform-origin` — Punctul de referință

Implicit, transformările se fac în jurul **centrului** elementului. Poți schimba asta:

```css
.element {
    transform-origin: top left;      /* rotește din colțul stânga-sus */
    transform-origin: center;        /* implicit — centru */
    transform-origin: bottom right;  /* din colțul dreapta-jos */
}
```

---

## 9.4 Exerciții practice cu tranziții

Creează un fișier `tranzitii.html` și încearcă fiecare efect:

### Efect 1: Card care „plutește" la hover

```html
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exerciții Animații</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: "Segoe UI", sans-serif;
            background-color: #F0F4F8;
            padding: 40px;
            display: flex;
            flex-wrap: wrap;
            gap: 30px;
            justify-content: center;
        }

        .card-float {
            width: 250px;
            background: white;
            border-radius: 16px;
            padding: 30px;
            text-align: center;
            border: 1px solid #E2E8F0;

            /* Tranziția — pe starea NORMALĂ */
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .card-float:hover {
            transform: translateY(-12px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        }

        .card-float .icon { font-size: 48px; margin-bottom: 12px; }
        .card-float h3 { color: #2D3748; margin-bottom: 8px; }
        .card-float p { color: #718096; font-size: 14px; }
    </style>
</head>
<body>

    <div class="card-float">
        <div class="icon">🎨</div>
        <h3>Design</h3>
        <p>Creează interfețe frumoase și intuitive.</p>
    </div>

    <div class="card-float">
        <div class="icon">⚡</div>
        <h3>Performanță</h3>
        <p>Site-uri rapide și optimizate.</p>
    </div>

    <div class="card-float">
        <div class="icon">🔒</div>
        <h3>Securitate</h3>
        <p>Protejează datele utilizatorilor.</p>
    </div>

</body>
</html>
```

### Efect 2: Buton cu efect de umplere

```css
.btn-fill {
    position: relative;
    padding: 14px 36px;
    font-size: 16px;
    font-weight: 600;
    color: #5A67D8;
    background: transparent;
    border: 2px solid #5A67D8;
    border-radius: 50px;
    cursor: pointer;
    overflow: hidden;         /* ascunde ce iese din buton */
    z-index: 1;
    transition: color 0.4s ease;
}

/* Pseudo-elementul care „umple" butonul */
.btn-fill::before {
    content: "";
    position: absolute;
    top: 0;
    left: -100%;              /* începe în afara butonului (stânga) */
    width: 100%;
    height: 100%;
    background-color: #5A67D8;
    z-index: -1;
    transition: left 0.4s ease;
}

.btn-fill:hover {
    color: white;
}

.btn-fill:hover::before {
    left: 0;                  /* alunecă înăuntru */
}
```

```
  Normal:                    Hover:
  ┌────────────────────┐     ┌████████████████████┐
  │     Apasă-mă      │     │█████ Apasă-mă █████│
  │   (text indigo)    │     │   (text alb)       │
  └────────────────────┘     └████████████████████┘
  border indigo              fundal indigo umplut
```

### Efect 3: Imagine cu zoom la hover

```css
.img-container {
    width: 300px;
    height: 200px;
    border-radius: 12px;
    overflow: hidden;          /* esențial — taie ce iese */
}

.img-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.img-container:hover img {
    transform: scale(1.15);    /* zoom 115% */
}
```

Trucul: containerul are `overflow: hidden`, deci imaginea mărită nu „iese" din cadru. Efectul pare profesional, dar e incredibil de simplu!

---

## 9.5 `@keyframes` — Animații cu mai mulți pași

Tranzițiile sunt simple: de la starea A la starea B. Dar ce faci când vrei o animație cu **mai mulți pași**? Aici intră `@keyframes`.

### Metafora: Flipbook (carte cu desene animate)

```
  Tranziție:           @keyframes:
  ───────────          ────────────
  
  Pagina 1  →  Pagina 2       Pagina 1 → Pagina 2 → Pagina 3 → Pagina 4
  (start)      (final)        (0%)       (33%)       (66%)       (100%)
  
  Doar 2 stări                 Oricâte stări intermediare!
```

### Cum funcționează

**Pasul 1:** Definești animația cu `@keyframes`:

```css
@keyframes alunecare {
    from {
        transform: translateX(-100px);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 1;
    }
}
```

**Pasul 2:** Aplici animația pe un element:

```css
.element {
    animation: alunecare 0.6s ease forwards;
    /*         ────────  ───  ────  ────────
               numele    cât  cum   păstrează
               animației durează    starea finală */
}
```

### Procente — Control total

Cu `from/to` ai doar 2 stări. Cu procente, ai **control total**:

```css
@keyframes pulsare {
    0% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.1);
    }
    100% {
        transform: scale(1);
    }
}

.inima {
    animation: pulsare 1.5s ease infinite;    /* se repetă la infinit */
}
```

```
  0%          25%         50%          75%         100%
  ┌───┐                 ┌─────┐                  ┌───┐
  │ ♥ │      ┌────┐     │  ♥  │     ┌────┐      │ ♥ │
  └───┘      │ ♥  │     │     │     │ ♥  │      └───┘
  normal     └────┘     └─────┘     └────┘      normal
              crește     maxim       scade
  
  ... și se repetă la infinit (infinite)
```

### Proprietățile animației

```css
.element {
    animation-name: numeleAnimatiei;
    animation-duration: 1s;
    animation-timing-function: ease;
    animation-delay: 0.5s;             /* așteaptă 0.5s înainte de start */
    animation-iteration-count: infinite; /* de câte ori: 1, 3, infinite */
    animation-direction: alternate;     /* du-te și vino */
    animation-fill-mode: forwards;      /* păstrează starea finală */
}

/* Sau pe scurt: */
.element {
    animation: numeleAnimatiei 1s ease 0.5s infinite alternate forwards;
}
```

| Proprietate | Valori comune | Ce face |
|---|---|---|
| `animation-name` | numele din `@keyframes` | Ce animație se aplică |
| `animation-duration` | `0.5s`, `1s`, `2s` | Cât durează un ciclu |
| `animation-timing-function` | `ease`, `linear`, `ease-in-out` | Curba de viteză |
| `animation-delay` | `0s`, `0.3s`, `1s` | Întârziere la start |
| `animation-iteration-count` | `1`, `3`, `infinite` | De câte ori se repetă |
| `animation-direction` | `normal`, `reverse`, `alternate` | Direcția animației |
| `animation-fill-mode` | `none`, `forwards`, `backwards` | Ce se întâmplă la final |

### Exemple practice

**Fade in (apariție treptată):**

```css
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.fade-in {
    animation: fadeIn 0.6s ease forwards;
}
```

**Shake (tremur — util pentru erori):**

```css
@keyframes shake {
    0%, 100% { transform: translateX(0); }
    20%      { transform: translateX(-10px); }
    40%      { transform: translateX(10px); }
    60%      { transform: translateX(-6px); }
    80%      { transform: translateX(6px); }
}

.eroare {
    animation: shake 0.5s ease;
}
```

**Spinner de încărcare:**

```css
@keyframes rotire {
    from { transform: rotate(0deg); }
    to   { transform: rotate(360deg); }
}

.spinner {
    width: 40px;
    height: 40px;
    border: 4px solid #E2E8F0;
    border-top-color: #5A67D8;
    border-radius: 50%;
    animation: rotire 0.8s linear infinite;
}
```

```
  Spinner de încărcare:
  
     ╭───╮       ╭───╮       ╭───╮       ╭───╮
    ╱█    ╲     ╱  █  ╲     ╱    █╲     ╱    ╲
   │      │    │      │    │      │    │█     │
    ╲    ╱      ╲    ╱      ╲    ╱      ╲    ╱
     ╰───╯       ╰───╯       ╰───╯       ╰───╯
   0°           90°          180°         270°
   
   Se rotește continuu (infinite) cu viteză constantă (linear)
```

**Bounce (săritură):**

```css
@keyframes bounce {
    0%, 100% {
        transform: translateY(0);
        animation-timing-function: ease-out;
    }
    40% {
        transform: translateY(-30px);
        animation-timing-function: ease-in;
    }
    70% {
        transform: translateY(-15px);
        animation-timing-function: ease-in;
    }
}

.bounce {
    animation: bounce 1s infinite;
}
```

---

## 9.6 Animații cu întârziere — Efect de cascadă

Un efect spectaculos și simplu: elementele apar unul câte unul, cu o mică întârziere între ele.

```css
@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.card {
    opacity: 0;     /* invizibil inițial */
    animation: slideUp 0.5s ease forwards;
}

/* Fiecare card are o întârziere diferită */
.card:nth-child(1) { animation-delay: 0.1s; }
.card:nth-child(2) { animation-delay: 0.2s; }
.card:nth-child(3) { animation-delay: 0.3s; }
.card:nth-child(4) { animation-delay: 0.4s; }
```

```
  Timp:  0.0s     0.1s     0.2s     0.3s     0.4s     0.5s     0.6s
  
  Card 1:         ╭── apare ──╮
  Card 2:                  ╭── apare ──╮
  Card 3:                           ╭── apare ──╮
  Card 4:                                    ╭── apare ──╮
  
  Fiecare card „alunecă" în sus cu o întârziere de 0.1s
  Efectul vizual: o cascadă, ca domino-urile
```

O variantă cu JavaScript care funcționează cu oricâte elemente:

```javascript
let carduri = document.querySelectorAll(".card");

for (let i = 0; i < carduri.length; i++) {
    carduri[i].style.animationDelay = `${i * 0.1}s`;
}
```

---

## 9.7 Animații controlate de JavaScript

CSS-ul e perfect pentru animații predefinite. Dar când ai nevoie de **logică** (animează doar dacă..., animează la click..., animează în funcție de scor...), JavaScript preia controlul.

### Metoda 1: Adaugă/elimină clase CSS

Cea mai elegantă abordare — definești animația în CSS, iar JavaScript decide **când** o pornește:

```css
/* CSS — definim animațiile */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes shake {
    0%, 100% { transform: translateX(0); }
    25%      { transform: translateX(-8px); }
    75%      { transform: translateX(8px); }
}

.anim-fadeIn {
    animation: fadeIn 0.5s ease forwards;
}

.anim-shake {
    animation: shake 0.4s ease;
}
```

```javascript
// JavaScript — declanșăm animațiile la momentul potrivit
let mesaj = document.querySelector("#mesaj");
let input = document.querySelector("#input");

function arataSucces() {
    mesaj.textContent = "✅ Salvat cu succes!";
    mesaj.classList.add("anim-fadeIn");
}

function arataEroare() {
    input.classList.add("anim-shake");
    
    // Elimină clasa după ce animația se termină (ca să o poți re-declanșa)
    setTimeout(function() {
        input.classList.remove("anim-shake");
    }, 400);
}
```

> 💡 **De ce eliminăm clasa după animație?**
> Dacă adaugi o clasă cu animație dar nu o elimini, adăugarea clasei a doua oară nu face nimic — clasa e deja acolo. Eliminând-o și readăugând-o, re-declanșezi animația.

### Metoda 2: Modifică stilul direct

Pentru valori **dinamice** (calculate de JavaScript):

```javascript
let bara = document.querySelector("#bara-progres");

function actualizeazaBara(procent) {
    bara.style.width = `${procent}%`;
    // transition din CSS face ca schimbarea să fie animată
}

actualizeazaBara(75);    // bara alunecă la 75%
```

### Metoda 3: `requestAnimationFrame` — Animații cadru cu cadru

Pentru animații **continue** (jocuri, particule, mișcări complexe), JavaScript oferă `requestAnimationFrame` — funcția care îți spune „execută asta la fiecare cadru de animație" (~60 cadre/secundă):

```javascript
let pozitieX = 0;
let minge = document.querySelector("#minge");

function animeaza() {
    pozitieX += 2;     // mișcă 2px la fiecare cadru
    minge.style.transform = `translateX(${pozitieX}px)`;
    
    if (pozitieX < 500) {
        requestAnimationFrame(animeaza);    // continuă animația
    }
}

// Pornește animația
requestAnimationFrame(animeaza);
```

```
  requestAnimationFrame:
  
  Cadru 1    Cadru 2    Cadru 3    Cadru 4    ...
  (16ms)     (16ms)     (16ms)     (16ms)
  
  x = 0      x = 2      x = 4      x = 6     ...
  ●          ●          ●          ●
  │──────────│──────────│──────────│──────────
  
  ~60 cadre pe secundă = mișcare fluidă!
```

De ce nu `setInterval`? `requestAnimationFrame` este **sincronizat cu rata de reîmprospătare a ecranului** (de obicei 60fps) și se oprește automat când tab-ul nu e vizibil, economisind resurse.

---

## 9.8 Animații la scroll — Elemente care apar

Unul dintre cele mai populare efecte pe web: elementele **apar cu animație** pe măsură ce derulezi pagina.

### Cum funcționează

```
  Viewport (ce vezi pe ecran):
  ┌─────────────────────────────┐
  │  Element 1 (vizibil) ✅    │
  │                             │
  │  Element 2 (vizibil) ✅    │
  │                             │
  ├─────────────────────────────┤ ← marginea ecranului
  │  Element 3 (invizibil) ❌  │
  │  Element 4 (invizibil) ❌  │
  │                             │
  
  Când scrollezi în jos și Element 3 intră în viewport → animează-l!
```

### Implementare cu `IntersectionObserver`

```css
/* CSS — elementele sunt invizibile inițial */
.reveal {
    opacity: 0;
    transform: translateY(40px);
    transition: opacity 0.6s ease, transform 0.6s ease;
}

/* Când devin vizibile */
.reveal.vizibil {
    opacity: 1;
    transform: translateY(0);
}
```

```javascript
// JavaScript — observă când elementele intră în viewport
let elementsToReveal = document.querySelectorAll(".reveal");

let observer = new IntersectionObserver(function(entries) {
    for (let i = 0; i < entries.length; i++) {
        if (entries[i].isIntersecting) {
            entries[i].target.classList.add("vizibil");
        }
    }
}, {
    threshold: 0.2     // declanșează când 20% din element e vizibil
});

// Observă fiecare element
for (let i = 0; i < elementsToReveal.length; i++) {
    observer.observe(elementsToReveal[i]);
}
```

Explicație:

```
  IntersectionObserver = un „paznic" care stă și observă
  
  1. Creezi paznicul: new IntersectionObserver(...)
  2. Îi spui CE să observe: observer.observe(element)
  3. Când elementul intră în viewport, paznicul raportează:
     "Elementul X este acum vizibil!" → isIntersecting = true
  4. Tu reacționezi: adaugi clasa "vizibil"
  5. CSS-ul face tranziția: opacity 0→1, translateY 40px→0
```

### Efect de cascadă la scroll

Combină IntersectionObserver cu delay-ul CSS:

```html
<div class="reveal" style="transition-delay: 0s">Card 1</div>
<div class="reveal" style="transition-delay: 0.1s">Card 2</div>
<div class="reveal" style="transition-delay: 0.2s">Card 3</div>
```

Sau calculează delay-ul din JavaScript:

```javascript
let elementsToReveal = document.querySelectorAll(".reveal");

let observer = new IntersectionObserver(function(entries) {
    let delay = 0;
    for (let i = 0; i < entries.length; i++) {
        if (entries[i].isIntersecting) {
            entries[i].target.style.transitionDelay = `${delay}s`;
            entries[i].target.classList.add("vizibil");
            delay += 0.1;
        }
    }
}, { threshold: 0.2 });

for (let i = 0; i < elementsToReveal.length; i++) {
    observer.observe(elementsToReveal[i]);
}
```

---

## 9.9 Proiect practic: Landing page animată 🚀

Hai să construim o pagină completă cu animații profesionale. Fiecare secțiune va folosi tehnici diferite.

Creează structura:

```
  📁 landing-animat/
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
    <title>SpaceCode — Învață să codezi 🚀</title>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="stil.css">
</head>
<body>

    <!-- NAV -->
    <nav class="navbar">
        <div class="container nav-interior">
            <div class="logo">🚀 Space<span>Code</span></div>
            <ul class="meniu">
                <li><a href="#hero">Acasă</a></li>
                <li><a href="#features">Funcții</a></li>
                <li><a href="#stats">Statistici</a></li>
                <li><a href="#cta">Start</a></li>
            </ul>
        </div>
    </nav>

    <!-- HERO cu animații la încărcare -->
    <header id="hero" class="hero">
        <div class="container hero-interior">
            <h1 class="hero-titlu">
                Învață să codezi.<br>
                <span class="gradient-text">Construiește viitorul.</span>
            </h1>
            <p class="hero-sub">Platformă interactivă de programare web 
            pentru tinerii aventurieri digitali.</p>
            <div class="hero-butoane">
                <a href="#features" class="btn btn-primar">Descoperă ✨</a>
                <a href="#cta" class="btn btn-secundar">Începe gratis</a>
            </div>
        </div>
        <!-- Elemente decorative animate -->
        <div class="particula particula-1">✦</div>
        <div class="particula particula-2">◆</div>
        <div class="particula particula-3">●</div>
        <div class="particula particula-4">✦</div>
    </header>

    <!-- FEATURES cu reveal la scroll -->
    <section id="features" class="features">
        <div class="container">
            <h2 class="sectiune-titlu reveal">Ce oferim?</h2>
            <div class="features-grid">
                <div class="feature-card reveal">
                    <div class="feature-icon">📚</div>
                    <h3>Lecții pas cu pas</h3>
                    <p>HTML, CSS și JavaScript explicate simplu, cu exemple vizuale.</p>
                </div>
                <div class="feature-card reveal">
                    <div class="feature-icon">🎮</div>
                    <h3>Proiecte reale</h3>
                    <p>Construiești jocuri, quiz-uri și site-uri web complete.</p>
                </div>
                <div class="feature-card reveal">
                    <div class="feature-icon">🏆</div>
                    <h3>Provocări zilnice</h3>
                    <p>Testează-ți cunoștințele și urcă în clasament.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- STATISTICI cu numere animate -->
    <section id="stats" class="stats">
        <div class="container">
            <div class="stats-grid">
                <div class="stat-item reveal">
                    <span class="stat-numar" data-target="1250">0</span>
                    <span class="stat-label">Elevi activi</span>
                </div>
                <div class="stat-item reveal">
                    <span class="stat-numar" data-target="48">0</span>
                    <span class="stat-label">Lecții interactive</span>
                </div>
                <div class="stat-item reveal">
                    <span class="stat-numar" data-target="12">0</span>
                    <span class="stat-label">Proiecte practice</span>
                </div>
                <div class="stat-item reveal">
                    <span class="stat-numar" data-target="98">0</span>
                    <span class="stat-label">% recomandă</span>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA (Call to Action) -->
    <section id="cta" class="cta">
        <div class="container cta-interior reveal">
            <h2>Gata să începi aventura?</h2>
            <p>Alătură-te miilor de tineri programatori. E gratuit!</p>
            <button class="btn btn-primar btn-cta" id="btn-cta">
                Începe acum 🚀
            </button>
        </div>
    </section>

    <!-- FOOTER -->
    <footer class="footer">
        <div class="container">
            <p>Creat cu ❤️ — Constructorul de Site-uri, Capitolul 9</p>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

### `stil.css`:

```css
/* ══════════════════════════════
   RESET ȘI BAZĂ
   ══════════════════════════════ */
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: "Nunito", sans-serif;
    color: #2D3748;
    line-height: 1.7;
    overflow-x: hidden;
}

.container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 0 20px;
}

/* ══════════════════════════════
   NAVBAR (cu transition)
   ══════════════════════════════ */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background-color: rgba(255, 255, 255, 0.95);
    border-bottom: 1px solid #E2E8F0;
    padding: 12px 0;
    z-index: 100;
    backdrop-filter: blur(10px);
}

.nav-interior {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-family: "Fredoka", sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #2D3748;
}

.logo span { color: #5A67D8; }

.meniu {
    display: flex;
    gap: 6px;
    list-style: none;
}

.meniu a {
    text-decoration: none;
    color: #4A5568;
    font-weight: 600;
    font-size: 15px;
    padding: 8px 16px;
    border-radius: 8px;
    transition: color 0.2s, background-color 0.2s;
}

.meniu a:hover {
    color: #5A67D8;
    background-color: #EBF4FF;
}

/* ══════════════════════════════
   BUTOANE
   ══════════════════════════════ */
.btn {
    display: inline-block;
    font-family: "Fredoka", sans-serif;
    font-weight: 600;
    font-size: 16px;
    padding: 14px 32px;
    border-radius: 50px;
    border: none;
    cursor: pointer;
    text-decoration: none;
    transition: transform 0.2s, box-shadow 0.2s, background-color 0.2s;
}

.btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.12);
}

.btn:active {
    transform: translateY(-1px);
}

.btn-primar {
    background-color: #5A67D8;
    color: white;
}

.btn-primar:hover { background-color: #434190; }

.btn-secundar {
    background-color: transparent;
    color: white;
    border: 2px solid rgba(255,255,255,0.5);
}

.btn-secundar:hover {
    background-color: rgba(255,255,255,0.1);
    border-color: white;
}

/* ══════════════════════════════
   HERO — animații la încărcare
   ══════════════════════════════ */
.hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    color: white;
    padding: 100px 20px 60px;
    position: relative;
    overflow: hidden;
}

/* Animații de intrare pentru elementele hero */
@keyframes heroFadeUp {
    from {
        opacity: 0;
        transform: translateY(40px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.hero-titlu {
    font-family: "Fredoka", sans-serif;
    font-size: 48px;
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 18px;
    animation: heroFadeUp 0.8s ease forwards;
}

.gradient-text {
    background: linear-gradient(90deg, #667eea, #a78bfa, #ec4899);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-sub {
    font-size: 18px;
    color: rgba(255,255,255,0.7);
    max-width: 500px;
    margin: 0 auto 30px;
    opacity: 0;
    animation: heroFadeUp 0.8s ease 0.2s forwards;
}

.hero-butoane {
    display: flex;
    gap: 15px;
    justify-content: center;
    flex-wrap: wrap;
    opacity: 0;
    animation: heroFadeUp 0.8s ease 0.4s forwards;
}

/* Particule decorative animate */
@keyframes float {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50%      { transform: translateY(-25px) rotate(180deg); }
}

.particula {
    position: absolute;
    color: rgba(255,255,255,0.1);
    font-size: 30px;
    animation: float 6s ease-in-out infinite;
}

.particula-1 { top: 15%; left: 10%; animation-delay: 0s; font-size: 24px; }
.particula-2 { top: 60%; right: 12%; animation-delay: 1.5s; font-size: 18px; }
.particula-3 { bottom: 20%; left: 20%; animation-delay: 3s; font-size: 14px; }
.particula-4 { top: 30%; right: 25%; animation-delay: 4.5s; font-size: 20px; }

/* ══════════════════════════════
   FEATURES
   ══════════════════════════════ */
.features {
    padding: 80px 0;
    background-color: #F7FAFC;
}

.sectiune-titlu {
    font-family: "Fredoka", sans-serif;
    font-size: 32px;
    text-align: center;
    color: #2D3748;
    margin-bottom: 40px;
}

.features-grid {
    display: flex;
    gap: 25px;
    flex-wrap: wrap;
}

.feature-card {
    flex: 1;
    min-width: 250px;
    background-color: white;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 35px 25px;
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 16px 32px rgba(0,0,0,0.08);
}

.feature-icon {
    font-size: 48px;
    margin-bottom: 15px;
}

.feature-card h3 {
    font-family: "Fredoka", sans-serif;
    font-size: 20px;
    color: #5A67D8;
    margin-bottom: 10px;
}

.feature-card p {
    color: #718096;
    font-size: 15px;
}

/* ══════════════════════════════
   STATISTICI
   ══════════════════════════════ */
.stats {
    padding: 70px 0;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
}

.stats-grid {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 30px;
}

.stat-item {
    text-align: center;
    min-width: 150px;
}

.stat-numar {
    display: block;
    font-family: "Fredoka", sans-serif;
    font-size: 48px;
    font-weight: 700;
}

.stat-label {
    font-size: 15px;
    color: rgba(255,255,255,0.75);
    margin-top: 4px;
}

/* ══════════════════════════════
   CTA
   ══════════════════════════════ */
.cta {
    padding: 80px 0;
}

.cta-interior {
    text-align: center;
    background: linear-gradient(135deg, #1a1a2e, #16213e);
    color: white;
    padding: 55px 35px;
    border-radius: 24px;
}

.cta-interior h2 {
    font-family: "Fredoka", sans-serif;
    font-size: 30px;
    margin-bottom: 12px;
}

.cta-interior p {
    color: rgba(255,255,255,0.7);
    margin-bottom: 28px;
    font-size: 17px;
}

.btn-cta {
    font-size: 20px;
    padding: 18px 44px;
}

/* ══════════════════════════════
   FOOTER
   ══════════════════════════════ */
.footer {
    background-color: #1a1a2e;
    color: rgba(255,255,255,0.4);
    text-align: center;
    padding: 25px 20px;
    font-size: 13px;
}

/* ══════════════════════════════
   ANIMAȚII REVEAL (scroll)
   ══════════════════════════════ */
.reveal {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.6s ease, transform 0.6s ease;
}

.reveal.vizibil {
    opacity: 1;
    transform: translateY(0);
}

/* ══════════════════════════════
   RESPONSIVE
   ══════════════════════════════ */
@media (max-width: 768px) {
    .hero-titlu { font-size: 32px; }
    .hero-sub { font-size: 16px; }
    .sectiune-titlu { font-size: 26px; }
    .stat-numar { font-size: 36px; }
    .meniu { gap: 2px; }
    .meniu a { padding: 6px 10px; font-size: 13px; }
}
```

### `script.js`:

```javascript
// ══════════════════════════════════════════════
// 🚀 SPACECODE LANDING PAGE — ANIMAȚII
// ══════════════════════════════════════════════


// ── 1. REVEAL LA SCROLL (IntersectionObserver) ──

const elemReveal = document.querySelectorAll(".reveal");

const observerReveal = new IntersectionObserver(function(entries) {
    for (let i = 0; i < entries.length; i++) {
        if (entries[i].isIntersecting) {
            // Adaugă un delay în cascadă pentru elementele din același grup
            entries[i].target.style.transitionDelay = `${i * 0.1}s`;
            entries[i].target.classList.add("vizibil");
        }
    }
}, {
    threshold: 0.15
});

for (let i = 0; i < elemReveal.length; i++) {
    observerReveal.observe(elemReveal[i]);
}


// ── 2. NUMERE ANIMATE (Count Up) ──

function animateNumber(element, target, duration) {
    let start = 0;
    let startTime = null;
    
    function updateNumber(currentTime) {
        if (!startTime) startTime = currentTime;
        let progress = (currentTime - startTime) / duration;
        
        if (progress > 1) progress = 1;
        
        // Funcție ease-out: pornește rapid, încetinește
        let easeOut = 1 - Math.pow(1 - progress, 3);
        
        let current = Math.round(easeOut * target);
        element.textContent = current;
        
        if (progress < 1) {
            requestAnimationFrame(updateNumber);
        }
    }
    
    requestAnimationFrame(updateNumber);
}

// Observă când secțiunea de statistici devine vizibilă
const statSection = document.querySelector(".stats");
let statsAnimated = false;     // semafor: animează o singură dată

const observerStats = new IntersectionObserver(function(entries) {
    if (entries[0].isIntersecting && !statsAnimated) {
        statsAnimated = true;
        
        let statNrs = document.querySelectorAll(".stat-numar");
        for (let i = 0; i < statNrs.length; i++) {
            let target = Number(statNrs[i].dataset.target);
            animateNumber(statNrs[i], target, 2000);
        }
    }
}, { threshold: 0.3 });

observerStats.observe(statSection);


// ── 3. SMOOTH SCROLL ──

const linkuriMeniu = document.querySelectorAll('.meniu a[href^="#"]');

for (let i = 0; i < linkuriMeniu.length; i++) {
    linkuriMeniu[i].addEventListener("click", function(e) {
        e.preventDefault();     // oprește comportamentul normal al linkului
        
        let targetId = this.getAttribute("href");
        let targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            targetElement.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        }
    });
}


// ── 4. EFECT BUTON CTA ──

const btnCta = document.querySelector("#btn-cta");

btnCta.addEventListener("click", function() {
    // Schimbă textul cu o animație
    this.textContent = "🎉 Bine ai venit!";
    this.style.backgroundColor = "#48BB78";
    
    setTimeout(() => {
        this.textContent = "Începe acum 🚀";
        this.style.backgroundColor = "#5A67D8";
    }, 2000);
});
```

### Ce tehnici de animație folosește proiectul

```
  TEHNICA                     UNDE E FOLOSITĂ
  ──────────────────────      ──────────────────────────────
  @keyframes heroFadeUp       Titlu, subtitlu, butoane hero
  @keyframes float            Particule decorative
  transition (hover)          Carduri features, butoane, linkuri nav
  classList + transition      Reveal la scroll (fade-in + slide-up)
  requestAnimationFrame       Numere animate (count up)
  IntersectionObserver        Declanșare animații la scroll
  scrollIntoView              Smooth scroll pentru meniu
  setTimeout                  Feedback buton CTA
  animation-delay             Cascadă particule, cascadă reveal
  transform                   translateY, scale (hover carduri)
  linear-gradient             Text gradient (hero), fundal stats
  backdrop-filter             Navbar semi-transparent
```

---

## 9.10 Performanță — Reguli de aur ⚡

Nu toate proprietățile CSS se animează la fel de bine. Unele sunt rapide, altele lente:

```
  RAPID (GPU-accelerate) ✅        LENT (recalculate layout) ❌
  ─────────────────────            ───────────────────────────
  transform                        width, height
  opacity                          top, left, right, bottom
                                   margin, padding
                                   font-size
  
  Regulă: Animează doar TRANSFORM și OPACITY ori de câte ori poți!
```

De ce? `transform` și `opacity` sunt gestionate de **GPU** (placa grafică), care e specializată în mișcare. Proprietăți ca `width` sau `margin` forțează browserul să **recalculeze layout-ul** întregii pagini la fiecare cadru — mult mai lent.

### Exemplu: Mișcă un element

```css
/* ❌ LENT — browserul recalculează layout-ul */
.element {
    position: relative;
    transition: left 0.3s;
}
.element:hover {
    left: 50px;
}

/* ✅ RAPID — GPU face toată munca */
.element {
    transition: transform 0.3s;
}
.element:hover {
    transform: translateX(50px);
}
```

### Exemplu: Ascunde un element

```css
/* ❌ LENT — display: none nu se poate anima */
.element {
    transition: display 0.3s;    /* NU FUNCȚIONEAZĂ! */
}

/* ✅ RAPID — opacity se animează perfect */
.element {
    opacity: 1;
    transition: opacity 0.3s;
}
.element.ascuns {
    opacity: 0;
    pointer-events: none;    /* nu mai interceptează click-uri */
}
```

### Proprietatea `will-change`

Dacă știi că un element va fi animat, poți „avertiza" browserul:

```css
.element-animat {
    will-change: transform, opacity;
}
```

Atenție: folosește-o doar pe elementele care chiar vor fi animate, nu pe toate.

---

## 9.11 Greșeli frecvente (și cum le repari) 🔧

### ❌ Greșeala 1: Tranziție pusă pe `:hover` în loc de starea normală

```css
/* ❌ Animația funcționează la hover, dar SARE BRUSC înapoi la mouse-out */
.card:hover {
    transform: translateY(-10px);
    transition: transform 0.3s;
}

/* ✅ Pune transition pe starea NORMALĂ — animează ȘI la intrare ȘI la ieșire */
.card {
    transition: transform 0.3s;
}
.card:hover {
    transform: translateY(-10px);
}
```

### ❌ Greșeala 2: Animezi proprietăți „imposibile"

```css
/* ❌ display: none → block NU se poate anima */
.element {
    display: none;
    transition: display 0.3s;    /* nu are efect */
}

/* ✅ Folosește opacity + visibility */
.element {
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.3s, visibility 0.3s;
}
.element.vizibil {
    opacity: 1;
    visibility: visible;
}
```

### ❌ Greșeala 3: Animații prea lungi

```css
/* ❌ 2 secunde pentru un hover e O ETERNITATE */
.buton {
    transition: background-color 2s;
}

/* ✅ 200-400ms e zona perfectă */
.buton {
    transition: background-color 0.25s;
}
```

Ghid de durată:

```
  Hover, click, focus:      150-300ms   (rapid, responsiv)
  Apariție element:         300-600ms   (suficient să se vadă)
  Tranziție pagină/ecran:   400-800ms   (fluid dar nu lent)
  Animații decorative:      1-6s        (fundal, particule)
```

### ❌ Greșeala 4: Re-declanșarea animației nu funcționează

```javascript
// ❌ A doua apelare nu face nimic — clasa e deja acolo!
element.classList.add("anim-shake");
// ... mai târziu ...
element.classList.add("anim-shake");    // niciun efect!

// ✅ Elimină clasa, apoi re-adaugă
element.classList.remove("anim-shake");
// Forțează browser-ul să „vadă" schimbarea
void element.offsetWidth;   // „flush" — truc de re-render
element.classList.add("anim-shake");
```

### ❌ Greșeala 5: Prea multe animații simultan

```
  ❌ Totul se mișcă, sclipește, rotește, pulează simultan
     → Utilizatorul e dezorientat, nu știe unde să se uite
     → Performanță slabă pe dispozitive vechi
  
  ✅ Animații subtile, pe elemente importante
     → Ghidează privirea utilizatorului
     → Performanță bună peste tot
  
  Regula: Dacă nu poți justifica DE CE un element e animat,
          probabil că nu trebuie animat.
```

---

## 9.12 Mini-quiz — Verifică ce ai învățat! ✅

**1.** Care e diferența dintre `transition` și `@keyframes`?

**2.** Ce face `transform: translateY(-20px) scale(1.05)`?

**3.** De ce punem `transition` pe starea normală a elementului, nu pe `:hover`?

**4.** Ce funcție JavaScript e optimă pentru animații continue (cadru cu cadru)?

**5.** Ce face `IntersectionObserver`?

**6.** De ce e mai bine să animezi `transform` decât `margin-left`?

**7.** Cât ar trebui să dureze o tranziție la hover?

---

<details>
<summary>🔑 Click aici pentru răspunsuri</summary>

1. **`transition`** animează schimbarea **între 2 stări** (ex: hover → normal) — e simplă și automată. **`@keyframes`** definește animații cu **mai mulți pași** (0%, 25%, 50%, 100%) — oferă control total și poate rula fără interacțiune.

2. Mută elementul **20 pixeli în sus** (`translateY(-20px)`) și îl mărește la **105%** din dimensiunea originală (`scale(1.05)`). Ambele se aplică simultan.

3. Dacă pui `transition` pe `:hover`, animația funcționează doar la **intrare** (mouse-over). La ieșirea mouse-ului, elementul **sare brusc** înapoi. Pe starea normală, animația funcționează **și la intrare, și la ieșire**.

4. **`requestAnimationFrame()`** — este sincronizat cu rata de reîmprospătare a ecranului (~60fps), se oprește automat când tab-ul nu e vizibil, și e mai eficient decât `setInterval`.

5. Observă dacă un element **intră sau iese din viewport** (zona vizibilă a ecranului). Se folosește pentru a declanșa animații la scroll — de exemplu, fade-in când un card devine vizibil.

6. `transform` este gestionat de **GPU** (placa grafică), deci e foarte rapid. `margin-left` forțează browserul să **recalculeze layout-ul** întregii pagini la fiecare cadru, ceea ce e mult mai lent.

7. Între **150 și 300 de milisecunde** (0.15s–0.3s). Sub 150ms poate fi greu de perceput, peste 400ms pare lent și neresponsiv.

</details>

---

## 9.13 Știai că? — Curiozități din lumea tech 🤓

🎬 **Animațiile la 60fps** (frames per second) sunt standardul industriei. La 60fps, fiecare cadru durează doar **16.6 milisecunde**. Dacă codul tău de animație durează mai mult de 16ms per cadru, animația „saccadează" (jank). De aceea performanța contează atât de mult — fiecare milisecundă e prețioasă!

🎨 **Disney's 12 Principles of Animation** (cele 12 principii de animație ale Disney), create în anii 1930, se aplică și pe web! Principii ca „anticipare" (un mic pas înapoi înainte de mișcarea principală), „ease in/out" (accelerare și decelerare naturală) și „squash and stretch" (deformarea în mișcare) sunt folosite de designerii web pentru a crea interfețe care par „vii".

⚡ **CSS Houdini** este un proiect experimental care va permite programatorilor să creeze propriile proprietăți CSS și animații la nivel de browser — practic, poți „programa" CSS-ul. Numele vine de la celebrul magician Harry Houdini, pentru că această tehnologie face „magie" cu CSS!

🌐 **`prefers-reduced-motion`** este o media query CSS care respectă preferințele utilizatorului pentru animații reduse. Unii oameni suferă de sensibilitate la mișcare (motion sickness) și își setează sistemul de operare să reducă animațiile. Un web developer responsabil adaugă: `@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }`.

---

## Recapitulare — Ce ai învățat în Capitolul 9

```
  TRANZIȚII CSS:
  ✅ transition: proprietate durată funcție delay
  ✅ Funcții de timing: ease, ease-in, ease-out, linear
  ✅ Tranziții pe hover, focus, active
  ✅ Tranziții pe mai multe proprietăți (sau "all")
  
  TRANSFORM:
  ✅ translate(X, Y) — mișcă elementul
  ✅ scale() — mărește / micșorează
  ✅ rotate() — rotește (în grade)
  ✅ Combinarea transformărilor într-o singură declarație
  ✅ transform-origin — punctul de referință
  
  @KEYFRAMES:
  ✅ Animații cu mai mulți pași (from/to sau procente)
  ✅ animation: name duration timing delay count direction fill
  ✅ Animații infinite, alternate, cu delay
  ✅ Fade-in, shake, spinner, bounce, slide-up
  ✅ Cascadă cu animation-delay (staggering)
  
  JAVASCRIPT + ANIMAȚII:
  ✅ classList.add/remove pentru a declanșa animații CSS
  ✅ requestAnimationFrame() — animații cadru cu cadru
  ✅ IntersectionObserver — animații la scroll
  ✅ Numere animate (count up) cu requestAnimationFrame
  ✅ Smooth scroll cu scrollIntoView()
  
  PERFORMANȚĂ:
  ✅ Animează doar transform și opacity (GPU-accelerate)
  ✅ Evită animarea width, height, margin, top/left
  ✅ Durată ideală: 200-500ms pentru interacțiuni
  ✅ will-change pentru a optimiza animații
  
  PROIECT:
  ✅ Landing page animată cu 6+ tehnici diferite! 🚀
```

---

## Ce urmează?

În **Capitolul 10: Proiectul 2 — Catch the Stars 🌟**, vei construi un joc 2D real folosind elementul HTML `<canvas>`! Stele vor cădea din cer, iar tu vei mișca un coș pentru a le prinde. Vei învăța elementul `<canvas>`, desenarea cu JavaScript, game loop-uri, detecția coliziunilor și mai multe concepte de programare avansată.

Pregătește-te — devii game developer! 🎮

---

> *„Animația poate explica orice mintea omului poate concepe."*
> — Walt Disney
