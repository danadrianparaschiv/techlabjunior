# Capitolul 10: Proiectul 2 — Catch the Stars 🌟

> *„Jocurile sunt cea mai elevată formă de cercetare."*
> — Albert Einstein

---

## Ce vei construi în acest capitol

Un **joc 2D complet** în care stele cad din cer, iar tu miști un coș pentru a le prinde. Cu cât prinzi mai multe stele, cu atât scorul crește, nivelul avansează și jocul devine mai rapid!

```
  ┌─────────────────────────────────────────────┐
  │  ⭐ Scor: 12          Nivel: 3    ❤️ ❤️ ❤️  │
  │                                             │
  │          ✦                                  │
  │                    ⭐                       │
  │     💣                        ✦             │
  │                                             │
  │                ⭐                           │
  │        ✦                                    │
  │                         💣                  │
  │                                             │
  │                                             │
  │              ┌─────────┐                    │
  │              │  🧺     │  ← tu controlezi  │
  │              └─────────┘                    │
  └─────────────────────────────────────────────┘
  
  ⭐ Stea       = +1 punct
  ✦  Stea mică  = +2 puncte (mai rară, mai rapidă)
  💣 Bombă      = -1 viață (evit-o!)
```

### Ce vei învăța:

- Elementul HTML **`<canvas>`** — pânza pe care desenezi
- **Desenarea** cu JavaScript: dreptunghiuri, cercuri, text, culori
- **Game loop** — ciclul infinit care face jocul să meargă
- **Mișcarea** obiectelor pe ecran
- **Detecția coliziunilor** — când două obiecte se ating
- **Niveluri** progresive de dificultate
- Organizarea codului unui joc

---

## 10.1 Ce este Canvas?

Până acum ai construit pagini din elemente HTML: div-uri, paragrafe, butoane. Canvas este diferit — este o **pânză goală** pe care desenezi **pixel cu pixel** din JavaScript.

```
  HTML normal:                    Canvas:
  ──────────────                  ───────
  ┌──────────────┐                ┌──────────────┐
  │ <h1>Titlu</h1>│                │              │
  │ <p>Text</p>  │                │  Tu desenezi │
  │ <button>     │                │  ORICE vrei  │
  │              │                │  cu cod JS   │
  │  Elemente    │                │              │
  │  predefinite │                │  Cercuri,    │
  │              │                │  linii, text │
  └──────────────┘                │  imagini...  │
                                  └──────────────┘
  
  HTML = construiești din         Canvas = pictezi
  cărămizi LEGO                   pe o pânză albă
```

### Metafora: Tabloul alb și pensula

Gândește-te la Canvas ca la un **tablou alb** pe un perete:
- **HTML** = tabloul (pânza)
- **JavaScript** = mâna ta cu pensula
- **Contextul 2D** = setul de pensule și vopsele

```html
<!-- Creează pânza în HTML -->
<canvas id="joc" width="600" height="400"></canvas>
```

```javascript
// Pregătește pensula în JavaScript
let canvas = document.querySelector("#joc");
let ctx = canvas.getContext("2d");    // "contextul" = setul de instrumente

// Acum poți desena!
ctx.fillStyle = "red";               // alege culoarea
ctx.fillRect(50, 50, 100, 80);       // desenează un dreptunghi
```

```
  Canvas (600 x 400 pixeli):
  
  (0,0)───────────────────────────────────► X (600)
    │
    │    (50,50)
    │      ┌──────────┐
    │      │          │ 80px
    │      │  ROȘU    │ înălțime
    │      └──────────┘
    │        100px lățime
    │
    ▼
    Y (400)
    
  Atenție: Y crește în JOS, nu în sus!
  (0,0) e colțul STÂNGA-SUS.
```

> ⚠️ **Atenție!**
> Sistemul de coordonate pe Canvas e **inversat pe verticală** față de matematică. `Y = 0` este **sus**, iar Y crește în **jos**. Asta confuză la început, dar te obișnuiești rapid.

---

## 10.2 Desenarea pe Canvas — Instrumente de bază

### Dreptunghiuri

```javascript
// Dreptunghi plin (umplut cu culoare)
ctx.fillStyle = "#5A67D8";
ctx.fillRect(x, y, lățime, înălțime);

// Dreptunghi contur (doar marginile)
ctx.strokeStyle = "#E53E3E";
ctx.lineWidth = 3;
ctx.strokeRect(x, y, lățime, înălțime);

// Șterge o zonă (face-o transparentă)
ctx.clearRect(x, y, lățime, înălțime);
```

### Cercuri

Cercurile se desenează cu `arc()`:

```javascript
ctx.beginPath();                           // începe o formă nouă
ctx.arc(x, y, raza, 0, Math.PI * 2);     // cerc complet
ctx.fillStyle = "#F6E05E";                // galben
ctx.fill();                               // umple cu culoare

// Math.PI * 2 = un cerc complet (360°)
// Math.PI     = jumătate de cerc (180°)
```

```
  ctx.arc(centruX, centruY, raza, unghi_start, unghi_final)
  
        unghi_start = 0
             │
             ▼
         ╭───────╮
        ╱    r    ╲     r = raza
       │  (x,y)   │    (x,y) = centrul
        ╲         ╱
         ╰───────╯
             ▲
             │
       unghi_final = Math.PI * 2
       (cerc complet = 360°)
```

### Text

```javascript
ctx.fillStyle = "white";
ctx.font = "bold 24px Fredoka";
ctx.textAlign = "center";
ctx.fillText("Salut, lume!", 300, 50);     // textul, x, y
```

### Gradient

```javascript
let gradient = ctx.createLinearGradient(0, 0, 600, 0);
gradient.addColorStop(0, "#667eea");
gradient.addColorStop(1, "#764ba2");

ctx.fillStyle = gradient;
ctx.fillRect(0, 0, 600, 400);
```

### Exercițiu rapid — Desenează o scenă

```javascript
let canvas = document.querySelector("#joc");
let ctx = canvas.getContext("2d");

// Cerul (gradient)
let cer = ctx.createLinearGradient(0, 0, 0, 400);
cer.addColorStop(0, "#0f0c29");
cer.addColorStop(0.5, "#302b63");
cer.addColorStop(1, "#24243e");
ctx.fillStyle = cer;
ctx.fillRect(0, 0, 600, 400);

// Stele (cercuri mici galbene)
ctx.fillStyle = "#F6E05E";
for (let i = 0; i < 30; i++) {
    let x = Math.random() * 600;
    let y = Math.random() * 300;
    let r = Math.random() * 2 + 0.5;
    ctx.beginPath();
    ctx.arc(x, y, r, 0, Math.PI * 2);
    ctx.fill();
}

// Pământul
ctx.fillStyle = "#2D3748";
ctx.fillRect(0, 360, 600, 40);

// Mesaj
ctx.fillStyle = "white";
ctx.font = "bold 20px sans-serif";
ctx.textAlign = "center";
ctx.fillText("🌟 Catch the Stars!", 300, 200);
```

---

## 10.3 Game Loop — Bătaia inimii jocului

Un joc nu e o singură imagine. E o **serie de imagini** afișate rapid, una după alta — exact ca un film. Fiecare imagine se numește **cadru** (frame).

### Metafora: Flipbook-ul

```
  Cadru 1       Cadru 2       Cadru 3       Cadru 4
  ┌───────┐     ┌───────┐     ┌───────┐     ┌───────┐
  │  ⭐   │     │       │     │       │     │       │
  │       │     │  ⭐   │     │       │     │       │
  │       │     │       │     │  ⭐   │     │       │
  │ ┌───┐ │     │ ┌───┐ │     │ ┌───┐ │     │ ┌⭐┐ │
  └───────┘     └───────┘     └───────┘     └───────┘
  
  La ~60 cadre pe secundă, steaua pare că „cade" lin!
```

### Ciclul unui game loop

La fiecare cadru (de ~60 ori pe secundă), jocul face 3 lucruri:

```
  ┌─────────────────────────────────────────────┐
  │               GAME LOOP                      │
  │                                              │
  │   ┌──────────┐                               │
  │   │1. ȘTERGE │  Curăță pânza (clearRect)    │
  │   └────┬─────┘                               │
  │        │                                     │
  │   ┌────▼─────┐                               │
  │   │2. UPDATE │  Mișcă obiectele,             │
  │   │          │  verifică coliziuni,          │
  │   │          │  actualizează scorul          │
  │   └────┬─────┘                               │
  │        │                                     │
  │   ┌────▼─────┐                               │
  │   │3. DESENEZ│  Redesenează totul            │
  │   │          │  în pozițiile noi             │
  │   └────┬─────┘                               │
  │        │                                     │
  │        └───────── requestAnimationFrame ──►  │
  │                   (repetă la infinit)         │
  └─────────────────────────────────────────────┘
```

```javascript
function gameLoop() {
    sterge();         // 1. Curăță ecranul
    actualizeaza();   // 2. Mișcă totul, verifică coliziuni
    deseneaza();      // 3. Redesenează totul
    
    requestAnimationFrame(gameLoop);    // Repetă!
}

// Pornește jocul
requestAnimationFrame(gameLoop);
```

---

## 10.4 Construim jocul — Pas cu pas

Creează structura:

```
  📁 catch-the-stars/
  ├── index.html
  ├── stil.css
  └── joc.js
```

### Pas 1: Structura HTML și CSS

#### `index.html`:

```html
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Catch the Stars 🌟</title>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="stil.css">
</head>
<body>

    <div class="joc-container">
        
        <!-- Ecranul de start -->
        <div id="ecran-start" class="overlay">
            <div class="overlay-continut">
                <div class="overlay-icon">🌟</div>
                <h1>Catch the Stars</h1>
                <p>Prinde stelele care cad din cer!<br>
                Evită bombele! 💣</p>
                <div class="instructiuni">
                    <span>⬅️ ➡️ Săgeți</span> sau <span>🖱️ Mouse</span>
                </div>
                <button id="btn-start" class="btn-joc">▶ Joacă!</button>
            </div>
        </div>

        <!-- Ecranul de game over -->
        <div id="ecran-gameover" class="overlay ascuns">
            <div class="overlay-continut">
                <div class="overlay-icon" id="go-icon">💫</div>
                <h1 id="go-titlu">Game Over</h1>
                <p id="go-scor">Scor final: 0</p>
                <p id="go-nivel">Nivel atins: 1</p>
                <p id="go-mesaj" class="go-mesaj">Mesaj...</p>
                <button id="btn-restart" class="btn-joc">🔄 Joacă din nou</button>
            </div>
        </div>

        <!-- Canvas-ul jocului -->
        <canvas id="canvas-joc" width="600" height="500"></canvas>

    </div>

    <script src="joc.js"></script>
</body>
</html>
```

#### `stil.css`:

```css
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: "Nunito", sans-serif;
    background-color: #0a0a1a;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    color: white;
}

.joc-container {
    position: relative;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 0 60px rgba(90, 103, 216, 0.3);
}

canvas {
    display: block;
    background-color: #0f0c29;
}

/* Overlay (start / game over) */
.overlay {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background-color: rgba(10, 10, 26, 0.92);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10;
    backdrop-filter: blur(6px);
}

.overlay.ascuns { display: none; }

.overlay-continut {
    text-align: center;
    padding: 30px;
}

.overlay-icon {
    font-size: 64px;
    margin-bottom: 10px;
}

.overlay-continut h1 {
    font-family: "Fredoka", sans-serif;
    font-size: 36px;
    margin-bottom: 10px;
    background: linear-gradient(90deg, #F6E05E, #ECC94B);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.overlay-continut p {
    color: rgba(255,255,255,0.7);
    font-size: 16px;
    margin-bottom: 8px;
    line-height: 1.6;
}

.instructiuni {
    color: rgba(255,255,255,0.4);
    font-size: 14px;
    margin-bottom: 25px;
}

.instructiuni span {
    background-color: rgba(255,255,255,0.1);
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 13px;
}

.go-mesaj {
    font-style: italic;
    color: rgba(255,255,255,0.5);
    margin-bottom: 15px;
}

.btn-joc {
    font-family: "Fredoka", sans-serif;
    font-size: 20px;
    font-weight: 600;
    padding: 16px 44px;
    background: linear-gradient(135deg, #667eea, #5A67D8);
    color: white;
    border: none;
    border-radius: 50px;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
}

.btn-joc:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(90, 103, 216, 0.4);
}

@media (max-width: 640px) {
    .joc-container { border-radius: 0; }
    canvas { width: 100vw; height: 80vh; }
}
```

---

### Pas 2: JavaScript — Creierul jocului

#### `joc.js`:

```javascript
// ══════════════════════════════════════════════
// 🌟 CATCH THE STARS — JOCUL COMPLET
// ══════════════════════════════════════════════


// ── SETUP CANVAS ──

const canvas = document.querySelector("#canvas-joc");
const ctx = canvas.getContext("2d");
const W = canvas.width;       // 600
const H = canvas.height;      // 500


// ── ELEMENTE UI ──

const ecranStart = document.querySelector("#ecran-start");
const ecranGameOver = document.querySelector("#ecran-gameover");
const btnStart = document.querySelector("#btn-start");
const btnRestart = document.querySelector("#btn-restart");
const goIcon = document.querySelector("#go-icon");
const goTitlu = document.querySelector("#go-titlu");
const goScor = document.querySelector("#go-scor");
const goNivel = document.querySelector("#go-nivel");
const goMesaj = document.querySelector("#go-mesaj");


// ══════════════════════════════════════════════
// STAREA JOCULUI
// ══════════════════════════════════════════════

let joc = {
    activ: false,
    scor: 0,
    nivel: 1,
    vieti: 3,
    obiecte: [],              // stelele și bombele care cad
    steleFundal: [],          // stelele statice de fundal
    timpUltimObiect: 0,       // când a apărut ultimul obiect
    intervalObiect: 1200,     // la câte ms apare un obiect nou
    animFrameId: null         // ID-ul animației (pentru a o opri)
};

// Jucătorul (coșul)
let jucator = {
    x: W / 2 - 40,
    y: H - 60,
    latime: 80,
    inaltime: 35,
    viteza: 6,
    culoare: "#F6E05E"
};

// Input (ce taste sunt apăsate)
let taste = {
    stanga: false,
    dreapta: false
};

// Poziția mouse-ului (alternativ la taste)
let mouseX = W / 2;
let useazaMouse = false;


// ══════════════════════════════════════════════
// FUNCȚII UTILITARE
// ══════════════════════════════════════════════

// Număr aleatoriu între min și max
function random(min, max) {
    return Math.random() * (max - min) + min;
}

// Număr întreg aleatoriu
function randomInt(min, max) {
    return Math.floor(random(min, max + 1));
}

// Verifică dacă două dreptunghiuri se suprapun (coliziune)
function coliziune(a, b) {
    return a.x < b.x + b.latime &&
           a.x + a.latime > b.x &&
           a.y < b.y + b.inaltime &&
           a.y + a.inaltime > b.y;
}


// ══════════════════════════════════════════════
// CREAREA OBIECTELOR
// ══════════════════════════════════════════════

// Creează steluțele statice de fundal
function creeazaSteleFundal() {
    joc.steleFundal = [];
    for (let i = 0; i < 60; i++) {
        joc.steleFundal.push({
            x: random(0, W),
            y: random(0, H),
            raza: random(0.3, 1.8),
            opacitate: random(0.2, 0.7),
            vitezaPalpaiere: random(0.005, 0.02)
        });
    }
}

// Creează un obiect care cade (stea, stea specială sau bombă)
function creeazaObiect() {
    let tip;
    let sansa = Math.random();
    
    if (sansa < 0.15) {
        tip = "bomba";         // 15% șansă de bombă
    } else if (sansa < 0.30) {
        tip = "steaSpeciala";  // 15% șansă de stea specială (+2 puncte)
    } else {
        tip = "stea";          // 70% stea normală
    }
    
    // Viteza crește cu nivelul
    let vitezaBaza = 1.5 + (joc.nivel - 1) * 0.3;
    
    let obiect = {
        x: random(20, W - 40),
        y: -30,
        latime: 28,
        inaltime: 28,
        vitezaY: vitezaBaza + random(0, 1),
        tip: tip,
        rotatie: 0,
        vitezaRotatie: random(-0.03, 0.03)
    };
    
    if (tip === "steaSpeciala") {
        obiect.latime = 22;
        obiect.inaltime = 22;
        obiect.vitezaY += 0.5;     // mai rapidă
    }
    
    if (tip === "bomba") {
        obiect.latime = 30;
        obiect.inaltime = 30;
    }
    
    joc.obiecte.push(obiect);
}


// ══════════════════════════════════════════════
// ACTUALIZARE (LOGICĂ)
// ══════════════════════════════════════════════

function actualizeaza(timestamp) {
    // ── Mișcă jucătorul ──
    if (useazaMouse) {
        // Mișcare cu mouse-ul — jucătorul urmărește cursorul
        let targetX = mouseX - jucator.latime / 2;
        jucator.x += (targetX - jucator.x) * 0.12;    // mișcare lină
    } else {
        // Mișcare cu tastele
        if (taste.stanga) jucator.x -= jucator.viteza;
        if (taste.dreapta) jucator.x += jucator.viteza;
    }
    
    // Limitează jucătorul în canvas
    if (jucator.x < 0) jucator.x = 0;
    if (jucator.x > W - jucator.latime) jucator.x = W - jucator.latime;
    
    // ── Creează obiecte noi periodic ──
    if (timestamp - joc.timpUltimObiect > joc.intervalObiect) {
        creeazaObiect();
        joc.timpUltimObiect = timestamp;
    }
    
    // ── Mișcă obiectele și verifică coliziuni ──
    for (let i = joc.obiecte.length - 1; i >= 0; i--) {
        let obj = joc.obiecte[i];
        
        // Mișcă în jos
        obj.y += obj.vitezaY;
        obj.rotatie += obj.vitezaRotatie;
        
        // Verifică coliziunea cu jucătorul
        if (coliziune(obj, jucator)) {
            if (obj.tip === "stea") {
                joc.scor += 1;
            } else if (obj.tip === "steaSpeciala") {
                joc.scor += 2;
            } else if (obj.tip === "bomba") {
                joc.vieti--;
                if (joc.vieti <= 0) {
                    gameOver();
                    return;
                }
            }
            // Elimină obiectul prins
            joc.obiecte.splice(i, 1);
            continue;
        }
        
        // Dacă a ieșit din ecran (în jos)
        if (obj.y > H + 40) {
            // Steaua pierdută — fără penalizare
            joc.obiecte.splice(i, 1);
        }
    }
    
    // ── Verifică avansarea de nivel ──
    // La fiecare 10 puncte, avansezi un nivel
    let nivelCalculat = Math.floor(joc.scor / 10) + 1;
    if (nivelCalculat > joc.nivel) {
        joc.nivel = nivelCalculat;
        // Crește dificultatea: obiecte mai frecvente
        joc.intervalObiect = Math.max(400, 1200 - (joc.nivel - 1) * 100);
    }
    
    // ── Palpâie stelele de fundal ──
    for (let i = 0; i < joc.steleFundal.length; i++) {
        let s = joc.steleFundal[i];
        s.opacitate += s.vitezaPalpaiere;
        if (s.opacitate > 0.8 || s.opacitate < 0.1) {
            s.vitezaPalpaiere *= -1;    // inversează direcția
        }
    }
}


// ══════════════════════════════════════════════
// DESENARE (GRAFICĂ)
// ══════════════════════════════════════════════

function deseneaza() {
    // ── 1. Fundalul (cerul nopții) ──
    let gradient = ctx.createLinearGradient(0, 0, 0, H);
    gradient.addColorStop(0, "#0f0c29");
    gradient.addColorStop(0.5, "#302b63");
    gradient.addColorStop(1, "#24243e");
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, W, H);
    
    // ── 2. Stelele de fundal (decorative) ──
    for (let i = 0; i < joc.steleFundal.length; i++) {
        let s = joc.steleFundal[i];
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.raza, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(255, 255, 255, ${s.opacitate})`;
        ctx.fill();
    }
    
    // ── 3. Obiectele care cad ──
    for (let i = 0; i < joc.obiecte.length; i++) {
        let obj = joc.obiecte[i];
        deseneazaObiect(obj);
    }
    
    // ── 4. Jucătorul (coșul) ──
    deseneazaJucator();
    
    // ── 5. Interfața (HUD) ──
    deseneazaHUD();
}


// Desenează un obiect individual (stea sau bombă)
function deseneazaObiect(obj) {
    ctx.save();     // salvează starea curentă a canvas-ului
    ctx.translate(obj.x + obj.latime / 2, obj.y + obj.inaltime / 2);
    ctx.rotate(obj.rotatie);
    
    let size = obj.latime;
    
    if (obj.tip === "stea") {
        // Stea galbenă
        deseneazaStea(0, 0, size / 2, "#F6E05E", "#ECC94B");
    } else if (obj.tip === "steaSpeciala") {
        // Stea mică albastră-strălucitoare
        deseneazaStea(0, 0, size / 2, "#90CDF4", "#63B3ED");
        // Efect de strălucire
        ctx.beginPath();
        ctx.arc(0, 0, size / 2 + 4, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(144, 205, 244, 0.15)";
        ctx.fill();
    } else if (obj.tip === "bomba") {
        // Bombă roșie
        ctx.beginPath();
        ctx.arc(0, 0, size / 2, 0, Math.PI * 2);
        ctx.fillStyle = "#2D3748";
        ctx.fill();
        ctx.strokeStyle = "#E53E3E";
        ctx.lineWidth = 2;
        ctx.stroke();
        // Fitilul
        ctx.beginPath();
        ctx.moveTo(0, -size / 2);
        ctx.lineTo(3, -size / 2 - 8);
        ctx.strokeStyle = "#A0AEC0";
        ctx.lineWidth = 2;
        ctx.stroke();
        // Scânteia
        ctx.beginPath();
        ctx.arc(3, -size / 2 - 8, 3, 0, Math.PI * 2);
        ctx.fillStyle = "#FC8181";
        ctx.fill();
    }
    
    ctx.restore();  // restaurează starea canvas-ului
}


// Desenează o stea cu 5 colțuri
function deseneazaStea(cx, cy, raza, culoare1, culoare2) {
    let colturi = 5;
    let razaInterior = raza * 0.45;
    
    ctx.beginPath();
    for (let i = 0; i < colturi * 2; i++) {
        let r = i % 2 === 0 ? raza : razaInterior;
        let unghi = (i * Math.PI / colturi) - Math.PI / 2;
        let x = cx + r * Math.cos(unghi);
        let y = cy + r * Math.sin(unghi);
        
        if (i === 0) {
            ctx.moveTo(x, y);
        } else {
            ctx.lineTo(x, y);
        }
    }
    ctx.closePath();
    ctx.fillStyle = culoare1;
    ctx.fill();
    ctx.strokeStyle = culoare2;
    ctx.lineWidth = 1;
    ctx.stroke();
}


// Desenează jucătorul (coșul)
function deseneazaJucator() {
    let x = jucator.x;
    let y = jucator.y;
    let w = jucator.latime;
    let h = jucator.inaltime;
    
    // Corpul coșului (trapez)
    ctx.beginPath();
    ctx.moveTo(x + 8, y);                 // colțul stânga sus
    ctx.lineTo(x + w - 8, y);             // colțul dreapta sus
    ctx.lineTo(x + w, y + h);             // colțul dreapta jos
    ctx.lineTo(x, y + h);                 // colțul stânga jos
    ctx.closePath();
    
    let gradientCos = ctx.createLinearGradient(x, y, x, y + h);
    gradientCos.addColorStop(0, "#F6E05E");
    gradientCos.addColorStop(1, "#D69E2E");
    ctx.fillStyle = gradientCos;
    ctx.fill();
    ctx.strokeStyle = "#B7791F";
    ctx.lineWidth = 2;
    ctx.stroke();
    
    // Liniile decorative ale coșului
    ctx.strokeStyle = "rgba(255,255,255,0.3)";
    ctx.lineWidth = 1;
    for (let i = 1; i < 4; i++) {
        let offsetX = i * (w / 4);
        ctx.beginPath();
        ctx.moveTo(x + offsetX + 2, y + 3);
        ctx.lineTo(x + offsetX, y + h - 3);
        ctx.stroke();
    }
}


// Desenează interfața (scor, nivel, vieți)
function deseneazaHUD() {
    // Fundal semi-transparent pentru text
    ctx.fillStyle = "rgba(0, 0, 0, 0.3)";
    ctx.fillRect(0, 0, W, 42);
    
    ctx.font = "bold 16px Fredoka, sans-serif";
    
    // Scor (stânga)
    ctx.fillStyle = "#F6E05E";
    ctx.textAlign = "left";
    ctx.fillText(`⭐ Scor: ${joc.scor}`, 15, 28);
    
    // Nivel (centru)
    ctx.fillStyle = "#90CDF4";
    ctx.textAlign = "center";
    ctx.fillText(`Nivel ${joc.nivel}`, W / 2, 28);
    
    // Vieți (dreapta)
    ctx.textAlign = "right";
    let vietiText = "";
    for (let i = 0; i < 3; i++) {
        vietiText += i < joc.vieti ? "❤️ " : "🖤 ";
    }
    ctx.fillText(vietiText, W - 15, 28);
}


// ══════════════════════════════════════════════
// GAME LOOP
// ══════════════════════════════════════════════

function gameLoop(timestamp) {
    if (!joc.activ) return;
    
    actualizeaza(timestamp);
    deseneaza();
    
    joc.animFrameId = requestAnimationFrame(gameLoop);
}


// ══════════════════════════════════════════════
// START / GAME OVER / RESTART
// ══════════════════════════════════════════════

function startJoc() {
    // Resetează starea
    joc.activ = true;
    joc.scor = 0;
    joc.nivel = 1;
    joc.vieti = 3;
    joc.obiecte = [];
    joc.timpUltimObiect = 0;
    joc.intervalObiect = 1200;
    
    jucator.x = W / 2 - jucator.latime / 2;
    
    creeazaSteleFundal();
    
    // Ascunde overlay-urile
    ecranStart.classList.add("ascuns");
    ecranGameOver.classList.add("ascuns");
    
    // Pornește game loop-ul
    requestAnimationFrame(gameLoop);
}


function gameOver() {
    joc.activ = false;
    
    if (joc.animFrameId) {
        cancelAnimationFrame(joc.animFrameId);
    }
    
    // Afișează ecranul de game over
    goScor.textContent = `Scor final: ${joc.scor}`;
    goNivel.textContent = `Nivel atins: ${joc.nivel}`;
    
    if (joc.scor >= 50) {
        goIcon.textContent = "🏆";
        goTitlu.textContent = "Legendă!";
        goMesaj.textContent = "Scor incredibil! Ești maestrul stelelor!";
    } else if (joc.scor >= 30) {
        goIcon.textContent = "🌟";
        goTitlu.textContent = "Impresionant!";
        goMesaj.textContent = "Ai prins stele ca un profesionist!";
    } else if (joc.scor >= 15) {
        goIcon.textContent = "👏";
        goTitlu.textContent = "Foarte bine!";
        goMesaj.textContent = "Ești pe drumul cel bun. Mai exersează!";
    } else {
        goIcon.textContent = "💫";
        goTitlu.textContent = "Game Over";
        goMesaj.textContent = "Nu renunța! Fiecare încercare te face mai bun!";
    }
    
    ecranGameOver.classList.remove("ascuns");
}


// ══════════════════════════════════════════════
// EVENIMENTE (INPUT)
// ══════════════════════════════════════════════

// Tastatura
document.addEventListener("keydown", function(e) {
    if (e.key === "ArrowLeft" || e.key === "a") taste.stanga = true;
    if (e.key === "ArrowRight" || e.key === "d") taste.dreapta = true;
    useazaMouse = false;
});

document.addEventListener("keyup", function(e) {
    if (e.key === "ArrowLeft" || e.key === "a") taste.stanga = false;
    if (e.key === "ArrowRight" || e.key === "d") taste.dreapta = false;
});

// Mouse
canvas.addEventListener("mousemove", function(e) {
    let rect = canvas.getBoundingClientRect();
    mouseX = (e.clientX - rect.left) * (W / rect.width);
    useazaMouse = true;
});

// Touch (pentru telefoane)
canvas.addEventListener("touchmove", function(e) {
    e.preventDefault();
    let rect = canvas.getBoundingClientRect();
    mouseX = (e.touches[0].clientX - rect.left) * (W / rect.width);
    useazaMouse = true;
}, { passive: false });

// Butoanele de start / restart
btnStart.addEventListener("click", startJoc);
btnRestart.addEventListener("click", startJoc);
```

---

## 10.5 Cum funcționează — Anatomia jocului

### Obiectul `joc` — Starea centralizată

Toate datele jocului sunt grupate într-un singur obiect:

```javascript
let joc = {
    activ: false,           // jocul rulează?
    scor: 0,                // punctele jucătorului
    nivel: 1,               // nivelul curent
    vieti: 3,               // câte vieți mai are
    obiecte: [],            // lista de stele/bombe active
    intervalObiect: 1200    // frecvența aparițiilor
};
```

Avantajul: totul e într-un loc. Când resetezi jocul, resetezi un singur obiect.

### Array-ul de obiecte active

Fiecare stea sau bombă este un obiect în array-ul `joc.obiecte`:

```
  joc.obiecte = [
      { x: 120, y: 80,  tip: "stea",    vitezaY: 2.1, ... },
      { x: 340, y: 200, tip: "bomba",   vitezaY: 1.8, ... },
      { x: 500, y: 50,  tip: "steaSpeciala", vitezaY: 2.5, ... }
  ];
  
  La fiecare cadru:
  1. Fiecare obiect se mișcă în jos (y += vitezaY)
  2. Dacă atinge jucătorul → coliziune!
  3. Dacă iese din ecran → se elimină din array
  4. Obiecte noi se adaugă periodic
```

### Detecția coliziunilor — AABB

Funcția `coliziune()` verifică dacă două dreptunghiuri se suprapun. Aceasta se numește **AABB** (Axis-Aligned Bounding Box) — cea mai simplă și rapidă formă de detecție a coliziunilor:

```
  Coliziune AABB:
  
  Două dreptunghiuri se suprapun DACĂ ȘI NUMAI DACĂ
  toate cele 4 condiții sunt adevărate:
  
  ┌─────────┐
  │    A     │
  │   ┌─────┼────┐
  │   │/////│////│    Zona de
  └───┼─────┘    │    suprapunere
      │     B    │
      └──────────┘
  
  A.stânga < B.dreapta    ȘI
  A.dreapta > B.stânga    ȘI
  A.sus < B.jos           ȘI
  A.jos > B.sus
```

```javascript
function coliziune(a, b) {
    return a.x < b.x + b.latime &&          // stânga A < dreapta B
           a.x + a.latime > b.x &&          // dreapta A > stânga B
           a.y < b.y + b.inaltime &&         // sus A < jos B
           a.y + a.inaltime > b.y;           // jos A > sus B
}
```

### Bucla inversă la ștergere din array

```javascript
// De ce parcurgem de la FINAL la ÎNCEPUT?
for (let i = joc.obiecte.length - 1; i >= 0; i--) {
    // ...
    if (trebuieSters) {
        joc.obiecte.splice(i, 1);    // șterge elementul la indexul i
    }
}
```

Dacă parcurgi de la 0 la length și ștergi un element, indexurile se schimbă și poți sări peste un element. Parcurgând invers, ștergerea nu afectează elementele neprocesate încă.

```
  De la 0 la n (PROBLEMATIC):
  Index:  0  1  2  3  4
  Array: [A, B, C, D, E]
  Șterge B (index 1) → [A, C, D, E]
  i devine 2 → sare peste C!
  
  De la n la 0 (CORECT):
  Index:  0  1  2  3  4
  Array: [A, B, C, D, E]
  Procesează E(4), D(3), C(2)
  Șterge B (index 1) → [A, C, D, E]
  i devine 0 → procesează A normal ✅
```

### Sistemul de niveluri

```javascript
let nivelCalculat = Math.floor(joc.scor / 10) + 1;
// Scor  0-9  → Nivel 1
// Scor 10-19 → Nivel 2
// Scor 20-29 → Nivel 3
// ...

joc.intervalObiect = Math.max(400, 1200 - (joc.nivel - 1) * 100);
// Nivel 1: 1200ms (un obiect la fiecare 1.2 secunde)
// Nivel 2: 1100ms
// Nivel 5: 800ms
// Nivel 9+: 400ms (minimul — nu scade mai mult)
```

### `ctx.save()` și `ctx.restore()` — Izolarea transformărilor

Când rotești un obiect cu `ctx.rotate()`, rotația afectează **tot** ce desenezi după. `save()` și `restore()` izolează transformările:

```javascript
ctx.save();                    // 📸 salvează starea curentă
ctx.translate(100, 100);       // mută „originea" la (100, 100)
ctx.rotate(0.5);               // rotește
// ... desenează obiectul rotit ...
ctx.restore();                 // 🔄 revine la starea salvată
// Tot ce desenezi acum e din nou normal (nerotit)
```

---

## 10.6 Provocări — Extinde jocul! 🚀

### 🟢 Ușor: Schimbă culorile și dimensiunile

Modifică culorile stelelor, mărimea coșului, viteza de bază. Experimentează!

### 🟡 Mediu: Adaugă power-up-uri

Creează un nou tip de obiect — un power-up (de exemplu 🛡️) care dă o viață bonus:

```javascript
// În creeazaObiect(), adaugă un nou tip:
if (sansa < 0.05) {
    tip = "viata";    // 5% șansă — foarte rară!
}

// În actualizeaza(), la coliziune:
if (obj.tip === "viata") {
    joc.vieti = Math.min(joc.vieti + 1, 5);    // max 5 vieți
}
```

### 🟡 Mediu: Efecte sonore

Folosește Web Audio API pentru sunete simple:

```javascript
function sunetPrindere() {
    let audioCtx = new AudioContext();
    let osc = audioCtx.createOscillator();
    let gain = audioCtx.createGain();
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.frequency.value = 800;
    gain.gain.value = 0.1;
    osc.start();
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.15);
    osc.stop(audioCtx.currentTime + 0.15);
}
```

### 🔴 Avansat: High score persistent

Salvează cel mai mare scor în `localStorage`:

```javascript
function salveazaHighScore() {
    let highScore = localStorage.getItem("catchStarsHigh") || 0;
    if (joc.scor > highScore) {
        localStorage.setItem("catchStarsHigh", joc.scor);
    }
}
```

---

## 10.7 Greșeli frecvente (și cum le repari) 🔧

### ❌ Greșeala 1: Uitai `clearRect` → totul lasă „urme"

```javascript
// ❌ Fără ștergere — obiectele lasă urme
function gameLoop() {
    actualizeaza();
    deseneaza();          // desenează PESTE cadrul anterior!
    requestAnimationFrame(gameLoop);
}

// ✅ Cu ștergere — fiecare cadru e curat
function deseneaza() {
    ctx.clearRect(0, 0, W, H);    // ← sau redesenează fundalul
    // ... desenează totul
}
```

### ❌ Greșeala 2: Coordonate Y inversate

```javascript
// ❌ „De ce steaua merge în sus, nu în jos??"
obj.y -= obj.vitezaY;      // Y scade = merge în SUS pe canvas

// ✅ Pe canvas, Y crește în JOS
obj.y += obj.vitezaY;      // Y crește = merge în JOS ✅
```

### ❌ Greșeala 3: Game loop-ul continuă după game over

```javascript
// ❌ Jocul se blochează — loop-ul continuă dar starea e inconsistentă
function gameOver() {
    // ... afișează ecranul de game over
    // Am uitat să opresc loop-ul!
}

// ✅ Oprește loop-ul
function gameOver() {
    joc.activ = false;     // flag-ul verificat la începutul gameLoop()
    cancelAnimationFrame(joc.animFrameId);
    // ...
}
```

### ❌ Greșeala 4: Ștergerea din array în buclă normală

```javascript
// ❌ Sare peste elemente!
for (let i = 0; i < joc.obiecte.length; i++) {
    if (conditie) {
        joc.obiecte.splice(i, 1);    // schimbă indexurile!
    }
}

// ✅ Parcurge INVERS
for (let i = joc.obiecte.length - 1; i >= 0; i--) {
    if (conditie) {
        joc.obiecte.splice(i, 1);    // sigur!
    }
}
```

---

## 10.8 Mini-quiz — Verifică ce ai învățat! ✅

**1.** Ce este `<canvas>` și cum diferă de elementele HTML normale?

**2.** Ce returnează `canvas.getContext("2d")`?

**3.** Care sunt cele 3 pași ai unui game loop?

**4.** De ce sistemul de coordonate al Canvas-ului are Y inversat?

**5.** Cum verifici dacă două dreptunghiuri se suprapun (coliziune AABB)?

**6.** De ce parcurgem array-ul invers când ștergem elemente din el?

**7.** Ce face `requestAnimationFrame()` și de ce e mai bun decât `setInterval()`?

---

<details>
<summary>🔑 Click aici pentru răspunsuri</summary>

1. `<canvas>` este o **pânză goală** pe care desenezi pixel cu pixel din JavaScript, spre deosebire de elementele HTML normale care au conținut și stil predefinit. E ca diferența dintre a construi cu LEGO (HTML) și a picta pe o pânză albă (Canvas).

2. Returnează **contextul de desenare 2D** — un obiect cu metode de desenare (`fillRect`, `arc`, `fillText` etc.). Este „setul de pensule și vopsele" cu care desenezi pe canvas.

3. **Șterge** (curăță pânza) → **Actualizează** (mișcă obiectele, verifică coliziuni, actualizează scorul) → **Desenează** (redesenează totul în pozițiile noi). Se repetă de ~60 ori pe secundă.

4. Este o convenție din primele zile ale computerelor grafice: ecranul se desenează de sus în jos, linie cu linie. Așa că (0,0) este colțul **stânga-sus**, iar Y crește **în jos**.

5. Două dreptunghiuri se suprapun dacă toate cele 4 condiții sunt adevărate: stânga A < dreapta B, dreapta A > stânga B, sus A < jos B, jos A > sus B. Dacă oricare condiție e falsă, nu există suprapunere.

6. Când ștergi un element din array cu `splice(i, 1)`, indexurile elementelor următoare se schimbă (scad cu 1). Parcurgând **invers** (de la final la început), elementele deja procesate nu sunt afectate de ștergere.

7. `requestAnimationFrame()` este **sincronizat cu rata de reîmprospătare a ecranului** (~60fps), se oprește automat când tab-ul nu e activ, și oferă un timestamp precis. `setInterval` nu e sincronizat cu ecranul și poate cauza animații sacadate.

</details>

---

## 10.9 Știai că? — Curiozități din lumea tech 🤓

🕹️ **Pong** (1972) este considerat primul joc video comercial de succes. Avea doar două „raclete" și o „minge" — forme geometrice simple, exact ca cele pe care le desenezi pe Canvas. Logica de bază (mișcare, coliziuni, scor) este identică cu cea din jocul tău Catch the Stars!

🎮 **HTML5 Canvas** a fost introdus în 2004 de Apple pentru browserul Safari. Inițial a fost criticat de unii ca fiind „prea simplu" pentru jocuri serioase. Astăzi, jocuri complexe ca **Angry Birds** (versiunea web), **Cut the Rope** și chiar emulatori de console vechi rulează pe Canvas!

🔢 **60 FPS** înseamnă că jocul tău redesenează ecranul complet de **60 de ori pe secundă**. Fiecare cadru are doar **16.6 milisecunde** disponibile. Dacă funcțiile tale de update + draw durează mai mult, jocul „saccadează". Optimizarea e crucială — și de aceea am folosit tehnici eficiente ca AABB în loc de detecție pixel-cu-pixel!

🏗️ **Game engines** profesionale ca Unity și Unreal Engine fac exact ce ai făcut tu, dar la o scară enormă. Game loop-ul? Identic. Detecția coliziunilor? Aceleași principii. Gestionarea obiectelor? Array-uri de entități, exact ca `joc.obiecte[]`. Diferența e în complexitate, nu în principii. Ai învățat bazele pe care se construiesc jocurile AAA!

---

## Recapitulare — Ce ai învățat în Capitolul 10

```
  CANVAS:
  ✅ <canvas> — pânza goală pentru desenare 2D
  ✅ getContext("2d") — contextul de desenare
  ✅ Sistemul de coordonate (0,0 = stânga-sus, Y crește în jos)
  ✅ fillRect, strokeRect, clearRect — dreptunghiuri
  ✅ beginPath, arc, fill — cercuri
  ✅ fillText, font, textAlign — text
  ✅ createLinearGradient — gradient-uri
  ✅ save() / restore() — izolarea transformărilor
  ✅ translate() + rotate() — rotirea obiectelor
  
  GAME DEVELOPMENT:
  ✅ Game Loop: Clear → Update → Draw → repeat
  ✅ requestAnimationFrame() la ~60fps
  ✅ Mișcarea obiectelor (x += viteza)
  ✅ Coliziuni AABB (Axis-Aligned Bounding Box)
  ✅ Ștergerea din array cu splice() în buclă inversă
  ✅ Spawning periodic cu timestamp
  ✅ Sistem de niveluri cu dificultate progresivă
  ✅ Input: tastatură (keydown/keyup) + mouse + touch
  ✅ Stare centralizată în obiectul „joc"
  ✅ Ecrane de start și game over (overlay)
  ✅ HUD (Heads-Up Display): scor, nivel, vieți
  
  FUNCȚII UTILITARE:
  ✅ random(min, max), randomInt(min, max)
  ✅ Math.random(), Math.floor(), Math.max(), Math.min()
  ✅ Desenarea unei stele cu 5 colțuri (trigonometrie)
  
  PROIECT COMPLET:
  ✅ Catch the Stars — joc 2D cu stele, bombe, niveluri! 🌟
```

---

## Ce urmează?

În **Capitolul 11: Proiectul 3 — Portofoliul meu 🌐**, vei construi un **site web personal complet** — portofoliul tău de programator! Va include: o pagină de prezentare, o galerie cu toate proiectele tale (Quiz Game, Catch the Stars), secțiuni „despre mine" și „contact", design responsive și animații. Va fi site-ul pe care îl poți arăta prietenilor, familiei și profesorilor!

Ești aproape de final — mai sunt doar 2 capitole! 🏁

---

> *„Jocurile sunt testul suprem al inteligenței artificiale, pentru că necesită toate abilitățile: percepție, raționament, planificare și învățare."*
> — adaptat după Stuart Russell
