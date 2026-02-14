# Capitolul 7: DOM — JavaScript învață să atingă pagina 👀

> *„Nu-mi spune, arată-mi."*
> — proverb adaptat

---

## Ce vei învăța în acest capitol

- Ce este **DOM-ul** și cum vede browserul pagina ta
- Cum **selectezi** elemente HTML din JavaScript
- Cum **schimbi** textul, culorile și stilurile din cod
- Cum **adaugi** și **ștergi** elemente de pe pagină
- Ce sunt **evenimentele** și cum reacționezi la click, tastare, mouse
- Cum construiești componente **interactive** reale

---

## 7.1 De ce contează acest capitol?

În capitolele 5 și 6, JavaScript a lucrat doar în consolă — invizibil pentru utilizator. A fost ca un bucătar care gătește în bucătărie dar nu servește niciodată mâncarea.

Acum, JavaScript **iese din bucătărie** și începe să interacționeze cu pagina. Poate schimba titluri, colora butoane, face elemente să apară sau să dispară, și reacționa la fiecare mișcare a utilizatorului.

```
  CAPITOLELE 5-6                     CAPITOLUL 7
  ─────────────                      ──────────
  
  ┌──────────────┐                   ┌──────────────┐
  │   Consola    │                   │  PAGINA WEB  │
  │              │                   │              │
  │  > "Salut!"  │                   │  ┌────────┐  │
  │  > 42        │                   │  │ Titlul │  │ ← JS schimbă asta!
  │  > true      │                   │  └────────┘  │
  │              │                   │  ┌────────┐  │
  │  Invizibil   │                   │  │ Buton  │  │ ← JS ascultă click!
  │  pentru      │                   │  └────────┘  │
  │  utilizator  │                   │              │
  └──────────────┘                   │  Vizibil și  │
                                     │  interactiv! │
                                     └──────────────┘
```

---

## 7.2 Ce este DOM-ul?

**DOM** = **D**ocument **O**bject **M**odel (Modelul Obiect al Documentului).

Când browserul citește fișierul tău HTML, nu păstrează textul brut. Îl transformă într-un **arbore de obiecte** — o structură organizată în care fiecare element HTML devine un „obiect" pe care JavaScript îl poate atinge, modifica sau șterge.

### Metafora: Telecomanda și televizorul 📺

Gândește-te așa:
- **HTML** = programul TV (conținutul)
- **DOM** = televizorul care afișează programul (structura pe care o vezi)
- **JavaScript** = **telecomanda** (controlează ce se vede pe ecran)

Cu telecomanda (JavaScript) poți:
- Schimba canalul (modifica conținutul)
- Regla volumul (modifica stilurile)
- Porni/opri subtitrările (adăuga/șterge elemente)
- Pune pe pauză (reacționa la evenimente)

### Arborele DOM

Acest HTML:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Pagina mea</title>
</head>
<body>
    <h1 id="titlu">Salut!</h1>
    <p class="text">Un paragraf.</p>
    <button id="btn">Click</button>
</body>
</html>
```

Devine acest arbore în memorie:

```
                        document
                           │
                         <html>
                        ┌──┴───┐
                    <head>    <body>
                      │      ┌──┼────────┐
                  <title>  <h1>  <p>    <button>
                      │      │    │        │
                  "Pagina" "Salut!" "Un    "Click"
                   mea"            paragraf."
                   
  Fiecare dreptunghi este un NOD (obiect) în DOM.
  JavaScript poate accesa orice nod și îl poate modifica!
```

> 💡 **Ideea cheie:**
> DOM-ul nu e HTML-ul. HTML-ul este textul pe care l-ai scris. DOM-ul este **reprezentarea live** a paginii în memorie. Când JavaScript modifică DOM-ul, pagina se actualizează **instant** pe ecran — fără a reîncărca pagina!

---

## 7.3 Selectarea elementelor — Găsește-le pe pagină

Primul pas: trebuie să „prinzi" elementul pe care vrei să-l modifici. JavaScript oferă mai multe metode:

### `getElementById()` — Găsește după ID

Cel mai direct mod — selectezi un element unic prin ID-ul său:

```html
<h1 id="titlu-principal">Salut, lume!</h1>
```

```javascript
let titlu = document.getElementById("titlu-principal");
console.log(titlu);           // <h1 id="titlu-principal">Salut, lume!</h1>
console.log(titlu.textContent); // "Salut, lume!"
```

```
  document.getElementById("titlu-principal")
  ────────  ──────────────  ────────────────
      │           │                │
  documentul   metoda de       ID-ul elementului
  (pagina      selecție        căutat (fără #)
   întreagă)
```

### `querySelector()` — Găsește cu selectori CSS ⭐

Aceasta este metoda **cea mai versatilă** — folosește exact aceiași selectori pe care i-ai învățat la CSS:

```javascript
// Selectează după element
let primulParagraf = document.querySelector("p");

// Selectează după clasă (cu punct!)
let textImportant = document.querySelector(".important");

// Selectează după ID (cu diez!)
let titlu = document.querySelector("#titlu-principal");

// Selectori complecși — exact ca în CSS!
let linkDinNav = document.querySelector("nav a");
let primulItem = document.querySelector("ul li:first-child");
```

### `querySelectorAll()` — Găsește TOATE elementele

`querySelector` returnează doar **primul** element găsit. `querySelectorAll` le returnează pe **toate**:

```html
<ul>
    <li>Element 1</li>
    <li>Element 2</li>
    <li>Element 3</li>
</ul>
```

```javascript
// Doar primul <li>
let primul = document.querySelector("li");
console.log(primul.textContent);    // "Element 1"

// TOATE elementele <li>
let toateLi = document.querySelectorAll("li");
console.log(toateLi.length);       // 3

// Parcurge-le cu o buclă
for (let i = 0; i < toateLi.length; i++) {
    console.log(toateLi[i].textContent);
}
// "Element 1"
// "Element 2"
// "Element 3"
```

### Referință rapidă

| Metodă | Selectează | Returnează | Exemplu |
|---|---|---|---|
| `getElementById("x")` | Un element cu ID-ul `x` | Un element | `getElementById("titlu")` |
| `querySelector("x")` | Primul element care se potrivește cu selectorul CSS | Un element | `querySelector(".card")` |
| `querySelectorAll("x")` | Toate elementele care se potrivesc | O listă | `querySelectorAll("li")` |

> 💡 **Sfat de profesionist!**
> `querySelector` și `querySelectorAll` sunt cele mai folosite în practică. Ele folosesc aceeași sintaxă ca CSS, deci nu trebuie să memorezi reguli noi. Dacă știi CSS, știi și cum să selectezi în JavaScript!

---

## 7.4 Modificarea conținutului — Schimbă ce scrie pe pagină

Odată ce ai „prins" un element, poți schimba ce conține:

### `textContent` — Schimbă textul

```html
<h1 id="titlu">Text vechi</h1>
```

```javascript
let titlu = document.querySelector("#titlu");

// Citește textul curent
console.log(titlu.textContent);    // "Text vechi"

// Schimbă textul
titlu.textContent = "Text nou și mai bun!";
// Acum pe pagină scrie "Text nou și mai bun!"
```

### `innerHTML` — Schimbă conținutul HTML

Diferența față de `textContent`: poți include **tag-uri HTML**:

```javascript
let container = document.querySelector("#info");

// textContent — tratează totul ca text simplu
container.textContent = "<strong>Bold</strong>";
// Afișează literal: "<strong>Bold</strong>"

// innerHTML — interpretează tag-urile HTML
container.innerHTML = "<strong>Bold</strong>";
// Afișează: Bold (cu bold aplicat)
```

```
  textContent = "Pun text simplu"
  innerHTML   = "Pun HTML complet (cu tag-uri)"
  
  ┌─────────────────────────────────────────────┐
  │  textContent = "<em>test</em>"              │
  │  Rezultat pe ecran: <em>test</em>           │
  │  (tag-urile apar ca text!)                  │
  │                                             │
  │  innerHTML = "<em>test</em>"                │
  │  Rezultat pe ecran: test (italic)           │
  │  (tag-urile sunt interpretate!)             │
  └─────────────────────────────────────────────┘
```

### Exemplu practic — Actualizare dinamică

```html
<p>Ai <span id="scor">0</span> puncte.</p>
<p>Nivel: <span id="nivel">1</span></p>
```

```javascript
let scorElement = document.querySelector("#scor");
let nivelElement = document.querySelector("#nivel");

// Simulăm câștigarea de puncte
let scor = 0;

scor += 100;
scorElement.textContent = scor;    // Pagina afișează acum "100"

scor += 250;
scorElement.textContent = scor;    // Pagina afișează acum "350"

nivelElement.textContent = 2;      // Nivelul se schimbă în "2"
```

---

## 7.5 Modificarea stilurilor — CSS din JavaScript

### Proprietatea `style` — Stiluri individuale

Poți schimba orice proprietate CSS direct din JavaScript:

```javascript
let titlu = document.querySelector("#titlu");

titlu.style.color = "tomato";
titlu.style.fontSize = "48px";
titlu.style.textAlign = "center";
titlu.style.backgroundColor = "#F0F4F8";
titlu.style.padding = "20px";
titlu.style.borderRadius = "12px";
```

> ⚠️ **Atenție la sintaxă!**
> În CSS scrii `font-size` (cu cratimă). În JavaScript scrii `fontSize` (camelCase). Regula: elimini cratima și faci litera următoare MAJUSCULĂ.
>
> ```
>   CSS                  →    JavaScript
>   ───                       ──────────
>   font-size            →    fontSize
>   background-color     →    backgroundColor
>   text-align           →    textAlign
>   border-radius        →    borderRadius
>   margin-top           →    marginTop
> ```

### `classList` — Adaugă și elimină clase CSS ⭐

Metoda profesională: în loc de a schimba stiluri individuale, definești **clase CSS** și le adaugi/elimini cu JavaScript:

```css
/* În stil.css */
.ascuns {
    display: none;
}

.evidențiat {
    background-color: #FEFCBF;
    border: 2px solid #F6E05E;
    padding: 10px;
    border-radius: 8px;
}

.eroare {
    color: #E53E3E;
    font-weight: bold;
}
```

```javascript
let mesaj = document.querySelector("#mesaj");

// Adaugă o clasă
mesaj.classList.add("evidențiat");

// Elimină o clasă
mesaj.classList.remove("evidențiat");

// Toggle — adaugă dacă nu există, elimină dacă există
mesaj.classList.toggle("ascuns");

// Verifică dacă are o clasă
if (mesaj.classList.contains("eroare")) {
    console.log("Mesajul are clasa eroare!");
}
```

```
  classList.add("x")        →  Adaugă clasa "x"
  classList.remove("x")     →  Elimină clasa "x"
  classList.toggle("x")     →  Adaugă/elimină alternativ
  classList.contains("x")   →  Verifică dacă există (true/false)
```

De ce `classList` e mai bun decât `style`?

```
  style.color = "red"              classList.add("eroare")
  ─────────────────                ─────────────────────
  • Schimbă un singur stil         • Aplică un SET de stiluri
  • Stilul e „prins" în JS         • Stilurile rămân în CSS
  • Greu de întreținut             • Ușor de întreținut
  • Amestecă JS cu CSS             • Separă JS de CSS ✅
```

> 💡 **Regulă de aur:**
> Folosește `classList` pentru orice schimbare de aspect. Folosește `style` doar pentru valori **dinamice** calculate în JavaScript (de exemplu, o poziție calculată matematic).

---

## 7.6 Modificarea atributelor

Poți citi și schimba atributele HTML:

```html
<img id="poza" src="pisica.jpg" alt="O pisică">
<a id="link" href="https://google.com">Google</a>
```

```javascript
let poza = document.querySelector("#poza");

// Citește un atribut
console.log(poza.src);        // "pisica.jpg"
console.log(poza.alt);        // "O pisică"

// Schimbă atribute
poza.src = "catel.jpg";
poza.alt = "Un cățel drăguț";

// Schimbă href-ul unui link
let link = document.querySelector("#link");
link.href = "https://youtube.com";
link.textContent = "YouTube";
```

### `setAttribute()` și `getAttribute()`

O alternativă mai explicită:

```javascript
let poza = document.querySelector("#poza");

poza.setAttribute("src", "catel.jpg");
poza.setAttribute("alt", "Un cățel drăguț");

let sursa = poza.getAttribute("src");
console.log(sursa);    // "catel.jpg"
```

---

## 7.7 Evenimente — Pagina ascultă și reacționează 🎧

Evenimentele sunt **cel mai important concept** din acest capitol. Ele sunt ceea ce face paginile web interactive.

Un **eveniment** este ceva ce se întâmplă pe pagină: un click, o tastă apăsată, mouse-ul care se mișcă, pagina care se încarcă. JavaScript poate **asculta** aceste evenimente și **reacționa**.

### Metafora: Soneria casei 🔔

```
  EVENIMENTUL = cineva apasă soneria     (click, tastare, scroll)
  ASCULTĂTORUL = urechea ta              (addEventListener)
  REACȚIA = te duci să deschizi ușa      (funcția care se execută)
  
  ┌───────────┐      ┌──────────────┐      ┌───────────────┐
  │  🔔 Click │ ───► │ 👂 Ascultă   │ ───► │ 🏃 Reacție!   │
  │ (eveniment)│      │ (listener)   │      │ (funcția ta)  │
  └───────────┘      └──────────────┘      └───────────────┘
```

### `addEventListener()` — Pune urechea la pândă

```html
<button id="btn">Apasă-mă!</button>
```

```javascript
let buton = document.querySelector("#btn");

buton.addEventListener("click", function() {
    alert("Ai apăsat butonul! 🎉");
});
```

Anatomia:

```
  buton.addEventListener( "click" ,  function() { ... } );
  ─────  ────────────────  ──────    ──────────────────
    │          │              │              │
  elementul  "adaugă un    CE EVENIMENT   CE SE ÎNTÂMPLĂ
  pe care    ascultător    asculți?       când evenimentul
  asculți    de                           are loc?
             eveniment"                   (funcția callback)
```

### Evenimentele cele mai comune

| Eveniment | Când se declanșează | Exemplu |
|---|---|---|
| `"click"` | Utilizatorul face click | Buton apăsat |
| `"dblclick"` | Dublu-click | Zoom pe imagine |
| `"mouseover"` | Mouse-ul intră pe element | Hover pe card |
| `"mouseout"` | Mouse-ul părăsește elementul | Ieșire din card |
| `"keydown"` | O tastă este apăsată | Joc cu tastatura |
| `"keyup"` | O tastă este eliberată | Căutare live |
| `"input"` | Textul dintr-un câmp se schimbă | Formular în timp real |
| `"submit"` | Un formular este trimis | Login, înregistrare |
| `"load"` | Pagina s-a încărcat complet | Animație de start |

### Exemplu pas cu pas: Buton care schimbă culoarea

```html
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Schimbă culoarea</title>
    <style>
        body {
            font-family: "Segoe UI", sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            transition: background-color 0.5s;
        }
        h1 { margin-bottom: 20px; }
        .btn {
            padding: 14px 32px;
            font-size: 18px;
            border: none;
            border-radius: 50px;
            background-color: #5A67D8;
            color: white;
            cursor: pointer;
            font-weight: 600;
        }
        .btn:hover {
            background-color: #434190;
        }
    </style>
</head>
<body>

    <h1 id="titlu">Apasă butonul!</h1>
    <button class="btn" id="btn-culoare">Schimbă culoarea 🎨</button>

    <script>
        // Lista de culori
        const culori = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", 
                        "#FFEAA7", "#DDA0DD", "#98D8C8", "#F7DC6F"];
        let indexCuloare = 0;

        // Selectăm elementele
        let buton = document.querySelector("#btn-culoare");
        let titlu = document.querySelector("#titlu");

        // Ascultăm click-ul
        buton.addEventListener("click", function() {
            // Schimbă culoarea de fundal
            document.body.style.backgroundColor = culori[indexCuloare];
            
            // Actualizează titlul
            titlu.textContent = `Culoarea #${indexCuloare + 1}! 🎨`;
            
            // Treci la culoarea următoare (cu wrap-around)
            indexCuloare++;
            if (indexCuloare >= culori.length) {
                indexCuloare = 0;     // revino la prima culoare
            }
        });
    </script>

</body>
</html>
```

### Evenimentul ca obiect — Informații despre ce s-a întâmplat

Funcția de callback primește automat un obiect `event` (pe scurt `e`) cu detalii:

```javascript
// Unde a dat click utilizatorul?
document.addEventListener("click", function(e) {
    console.log(`Click la coordonatele: ${e.clientX}, ${e.clientY}`);
    console.log(`Element apăsat: ${e.target.tagName}`);
});

// Ce tastă a apăsat?
document.addEventListener("keydown", function(e) {
    console.log(`Tasta apăsată: ${e.key}`);
    
    if (e.key === "Enter") {
        console.log("Ai apăsat Enter!");
    }
    if (e.key === "Escape") {
        console.log("Ai apăsat Escape!");
    }
});
```

`e.target` este elementul **exact** pe care s-a făcut acțiunea. Este extrem de util:

```javascript
// Orice buton de pe pagină, într-un singur listener
document.addEventListener("click", function(e) {
    // Verifică dacă elementul apăsat are clasa "btn"
    if (e.target.classList.contains("btn")) {
        console.log(`Butonul "${e.target.textContent}" a fost apăsat!`);
    }
});
```

---

## 7.8 Crearea și ștergerea elementelor

Nu doar modifici ce există — poți **crea** elemente noi și le poți **adăuga** pe pagină!

### Creează un element nou

```javascript
// Pasul 1: Creează elementul (încă nu e pe pagină!)
let paragrafNou = document.createElement("p");

// Pasul 2: Adaugă conținut și stiluri
paragrafNou.textContent = "Sunt un paragraf nou, creat de JavaScript!";
paragrafNou.classList.add("text-nou");

// Pasul 3: Adaugă-l pe pagină (în interiorul unui container)
let container = document.querySelector("#continut");
container.appendChild(paragrafNou);
```

```
  Pasul 1:  createElement("p")     → <p></p>  (în memorie, invizibil)
  Pasul 2:  .textContent = "..."   → <p>Sunt un paragraf nou...</p>
  Pasul 3:  .appendChild(...)      → elementul APARE pe pagină! ✨
```

### Adaugă mai multe elemente

```javascript
// Creează 5 elemente dinamic
let lista = document.querySelector("#lista-dinamica");

for (let i = 1; i <= 5; i++) {
    let item = document.createElement("li");
    item.textContent = `Element generat #${i}`;
    lista.appendChild(item);
}
```

### `innerHTML` — Modalitate mai rapidă (dar cu grijă)

```javascript
let container = document.querySelector("#carduri");

container.innerHTML = `
    <div class="card">
        <h3>Card nou</h3>
        <p>Creat cu innerHTML!</p>
    </div>
`;
```

> ⚠️ **Atenție!**
> `innerHTML` **înlocuiește** tot conținutul existent. Dacă containerul avea deja conținut, acesta dispare! Folosește `innerHTML +=` pentru a **adăuga** fără a pierde ce exista:
>
> ```javascript
> container.innerHTML += `<p>Paragraf adăugat</p>`;  // adaugă la final
> ```
>
> Totuși, pentru adăugări frecvente (în bucle), `createElement` + `appendChild` este mai eficient.

### Șterge un element

```javascript
// Metoda modernă — simplu
let element = document.querySelector("#de-sters");
element.remove();

// Metoda alternativă — din perspectiva părintelui
let parinte = document.querySelector("#container");
let copil = document.querySelector("#de-sters");
parinte.removeChild(copil);
```

---

## 7.9 Proiect practic: Lista de sarcini (To-Do List) 🚀

Acesta este un proiect clasic care pune cap la cap tot ce ai învățat. Vom construi o aplicație completă de „to-do list" — o listă interactivă de sarcini.

Creează structura:

```
  📁 todo-list/
  ├── index.html
  ├── stil.css
  └── script.js
```

### HTML (`index.html`):

```html
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista mea de sarcini ✅</title>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="stil.css">
</head>
<body>

    <div class="container">
        <h1>Lista mea de sarcini ✅</h1>
        
        <div class="input-zona">
            <input type="text" id="input-sarcina" placeholder="Ce ai de făcut?">
            <button id="btn-adauga">Adaugă</button>
        </div>

        <div class="statistici">
            <span id="total">Total: 0</span>
            <span id="completate">Completate: 0</span>
        </div>

        <ul id="lista-sarcini">
            <!-- Sarcinile vor fi adăugate aici de JavaScript -->
        </ul>

        <p id="mesaj-gol" class="mesaj-gol">
            Nicio sarcină încă. Adaugă prima ta sarcină! 📝
        </p>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

### CSS (`stil.css`):

```css
/* ── RESET ȘI BAZĂ ── */
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
    justify-content: center;
    padding: 40px 20px;
}

.container {
    width: 100%;
    max-width: 550px;
}

h1 {
    font-family: "Fredoka", sans-serif;
    font-size: 30px;
    text-align: center;
    margin-bottom: 25px;
    color: #5A67D8;
}

/* ── ZONA DE INPUT ── */
.input-zona {
    display: flex;
    gap: 10px;
    margin-bottom: 15px;
}

#input-sarcina {
    flex: 1;
    padding: 14px 18px;
    font-size: 16px;
    font-family: "Nunito", sans-serif;
    border: 2px solid #E2E8F0;
    border-radius: 12px;
    outline: none;
}

#input-sarcina:focus {
    border-color: #5A67D8;
}

#btn-adauga {
    padding: 14px 24px;
    font-size: 16px;
    font-family: "Fredoka", sans-serif;
    font-weight: 600;
    background-color: #5A67D8;
    color: white;
    border: none;
    border-radius: 12px;
    cursor: pointer;
}

#btn-adauga:hover {
    background-color: #434190;
}

/* ── STATISTICI ── */
.statistici {
    display: flex;
    justify-content: space-between;
    font-size: 14px;
    color: #718096;
    margin-bottom: 20px;
    padding: 0 5px;
}

/* ── LISTA ── */
#lista-sarcini {
    list-style: none;
}

.sarcina {
    display: flex;
    align-items: center;
    gap: 12px;
    background-color: white;
    padding: 14px 18px;
    margin-bottom: 8px;
    border-radius: 10px;
    border: 1px solid #E2E8F0;
}

.sarcina:hover {
    border-color: #CBD5E0;
}

.sarcina-text {
    flex: 1;
    font-size: 16px;
}

.sarcina.completata .sarcina-text {
    text-decoration: line-through;
    color: #A0AEC0;
}

.btn-check {
    width: 26px;
    height: 26px;
    border-radius: 50%;
    border: 2px solid #CBD5E0;
    background-color: transparent;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    color: transparent;
}

.btn-check:hover {
    border-color: #68D391;
}

.sarcina.completata .btn-check {
    background-color: #68D391;
    border-color: #68D391;
    color: white;
}

.btn-sterge {
    background: none;
    border: none;
    color: #E2E8F0;
    font-size: 20px;
    cursor: pointer;
    padding: 2px 6px;
    border-radius: 6px;
}

.btn-sterge:hover {
    color: #E53E3E;
    background-color: #FFF5F5;
}

/* ── MESAJ GOL ── */
.mesaj-gol {
    text-align: center;
    color: #A0AEC0;
    padding: 30px;
    font-size: 15px;
}

.ascuns {
    display: none;
}
```

### JavaScript (`script.js`):

```javascript
// ══════════════════════════════════════════════
// ✅ LISTA MEA DE SARCINI — SCRIPT PRINCIPAL
// ══════════════════════════════════════════════

// ── SELECTĂM ELEMENTELE ──
const inputSarcina = document.querySelector("#input-sarcina");
const btnAdauga = document.querySelector("#btn-adauga");
const listaSarcini = document.querySelector("#lista-sarcini");
const mesajGol = document.querySelector("#mesaj-gol");
const totalElement = document.querySelector("#total");
const completateElement = document.querySelector("#completate");


// ── FUNCȚII ──

// Actualizează statisticile afișate
function actualizeazaStatistici() {
    let toateSarcinile = document.querySelectorAll(".sarcina");
    let sarcinileComplete = document.querySelectorAll(".sarcina.completata");
    
    totalElement.textContent = `Total: ${toateSarcinile.length}`;
    completateElement.textContent = `Completate: ${sarcinileComplete.length}`;
    
    // Arată/ascunde mesajul "nicio sarcină"
    if (toateSarcinile.length === 0) {
        mesajGol.classList.remove("ascuns");
    } else {
        mesajGol.classList.add("ascuns");
    }
}


// Creează un element de sarcină nouă
function creeazaSarcina(text) {
    // Creează <li> cu clasa "sarcina"
    let li = document.createElement("li");
    li.classList.add("sarcina");
    
    // Construiește conținutul interior
    li.innerHTML = `
        <button class="btn-check">✓</button>
        <span class="sarcina-text">${text}</span>
        <button class="btn-sterge">✕</button>
    `;
    
    // Adaugă la listă
    listaSarcini.appendChild(li);
    
    // Actualizează statisticile
    actualizeazaStatistici();
}


// Adaugă o sarcină nouă (apelată la click sau Enter)
function adaugaSarcina() {
    let text = inputSarcina.value.trim();    // .trim() elimină spațiile
    
    // Verifică dacă textul nu e gol
    if (text === "") {
        inputSarcina.style.borderColor = "#E53E3E";  // chenar roșu
        setTimeout(function() {
            inputSarcina.style.borderColor = "#E2E8F0";  // revine la normal
        }, 1500);
        return;       // oprește funcția, nu adăuga nimic
    }
    
    // Creează sarcina
    creeazaSarcina(text);
    
    // Golește câmpul de input
    inputSarcina.value = "";
    inputSarcina.focus();     // pune cursorul înapoi în input
}


// ── EVENIMENTE ──

// Click pe butonul "Adaugă"
btnAdauga.addEventListener("click", adaugaSarcina);

// Apasă Enter în câmpul de input
inputSarcina.addEventListener("keydown", function(e) {
    if (e.key === "Enter") {
        adaugaSarcina();
    }
});

// Click pe lista de sarcini (delegare de evenimente)
listaSarcini.addEventListener("click", function(e) {
    
    // Dacă s-a apăsat butonul de check → toggle completare
    if (e.target.classList.contains("btn-check")) {
        let sarcina = e.target.closest(".sarcina");
        sarcina.classList.toggle("completata");
        actualizeazaStatistici();
    }
    
    // Dacă s-a apăsat butonul de ștergere → elimină sarcina
    if (e.target.classList.contains("btn-sterge")) {
        let sarcina = e.target.closest(".sarcina");
        sarcina.remove();
        actualizeazaStatistici();
    }
});
```

### Cum funcționează — Pas cu pas

```
  1. Utilizatorul scrie "Învață JavaScript" în input
  
  2. Apasă butonul "Adaugă" (sau Enter)
     │
     ▼
  3. addEventListener("click") se activează
     │
     ▼
  4. adaugaSarcina() se execută:
     ├── Citește textul din input: "Învață JavaScript"
     ├── Verifică dacă nu e gol ✅
     ├── Apelează creeazaSarcina("Învață JavaScript")
     │   ├── Creează un <li> nou
     │   ├── Adaugă butoane check și ștergere
     │   └── Îl pune în <ul>
     └── Golește input-ul
  
  5. Pe ecran apare sarcina nouă! ✨
  
  6. Utilizatorul apasă ✓ (check):
     ├── Event listener pe listă detectează click
     ├── Verifică: e.target are clasa "btn-check"? DA
     ├── Adaugă clasa "completata" pe <li>
     └── CSS-ul face text-ul tăiat și gri
  
  7. Utilizatorul apasă ✕ (ștergere):
     ├── Event listener pe listă detectează click
     ├── Verifică: e.target are clasa "btn-sterge"? DA
     └── element.remove() — sarcina dispare!
```

### Concept nou: Delegarea evenimentelor

Ai observat că nu punem `addEventListener` pe fiecare buton individual? În schimb, ascultăm click-urile pe **părintele** (`listaSarcini`) și verificăm **ce element exact** a fost apăsat cu `e.target`:

```javascript
// ❌ PROBLEMATIC — trebuie adăugat pe FIECARE buton nou creat
document.querySelector("#btn-1").addEventListener("click", ...);
document.querySelector("#btn-2").addEventListener("click", ...);
// Ce facem cu butoanele create DUPĂ ce pagina s-a încărcat?

// ✅ DELEGARE — un singur listener pe părinte
listaSarcini.addEventListener("click", function(e) {
    if (e.target.classList.contains("btn-check")) {
        // ... acțiune pentru butonul check
    }
});
```

Metafora: În loc să angajezi un portar la FIECARE cameră a hotelului, angajezi unul singur la **intrarea principală** care redirecționează vizitatorii. Delegarea este exact acest principiu — un singur ascultător la „intrare" care gestionează totul.

### Ce am folosit

```
  ✅ querySelector / querySelectorAll — selectarea elementelor
  ✅ textContent / innerHTML — modificarea conținutului
  ✅ classList.add / remove / toggle / contains
  ✅ createElement + appendChild — crearea elementelor dinamice
  ✅ element.remove() — ștergerea elementelor
  ✅ addEventListener pentru click și keydown
  ✅ e.target — elementul exact pe care s-a făcut click
  ✅ e.target.closest() — găsește părintele cel mai apropiat
  ✅ Delegarea evenimentelor — un listener pentru mai multe butoane
  ✅ .value, .trim(), .focus() — lucrul cu input-uri
  ✅ setTimeout() — acțiune întârziată (preview!)
  ✅ Funcții organizate: creeazaSarcina(), adaugaSarcina(),
     actualizeazaStatistici()
```

---

## 7.10 Lucrul cu formulare și input-uri

Formularele și câmpurile de input sunt esențiale pentru orice site interactiv.

### Citirea valorii unui input

```html
<input type="text" id="nume" placeholder="Scrie numele tău">
<button id="btn-salut">Salută-mă!</button>
<p id="rezultat"></p>
```

```javascript
let input = document.querySelector("#nume");
let buton = document.querySelector("#btn-salut");
let rezultat = document.querySelector("#rezultat");

buton.addEventListener("click", function() {
    let numeUtilizator = input.value;       // citește ce a scris
    rezultat.textContent = `Salut, ${numeUtilizator}! 👋`;
});
```

### Evenimentul `"input"` — Reacție în timp real

```javascript
let input = document.querySelector("#cautare");
let rezultat = document.querySelector("#rezultat-cautare");

// Se activează la FIECARE caracter tastat
input.addEventListener("input", function() {
    let text = input.value;
    rezultat.textContent = `Cauți: "${text}" (${text.length} caractere)`;
});
```

Diferența între evenimente pe input:

```
  "input"   → la FIECARE schimbare (cel mai frecvent folosit)
  "change"  → doar când utilizatorul TERMINĂ de editat (pierde focus)
  "keydown" → la FIECARE tastă apăsată (include Shift, Ctrl etc.)
  "keyup"   → când ELIBEREAZĂ o tastă
```

### Tipuri de input

```html
<input type="text" id="nume">          <!-- text simplu -->
<input type="number" id="varsta">      <!-- doar numere -->
<input type="email" id="email">        <!-- validare email -->
<input type="password" id="parola">    <!-- text ascuns -->
<input type="range" id="volum" min="0" max="100">  <!-- slider -->
<input type="color" id="culoare">      <!-- selector de culoare -->
<input type="checkbox" id="acord">     <!-- bifă -->
```

```javascript
// Câmpuri text, number, email, password
let valoareText = document.querySelector("#nume").value;          // string
let valoareNumar = Number(document.querySelector("#varsta").value); // convertit la number!

// Slider (range)
let volum = document.querySelector("#volum").value;

// Checkbox
let esteBifat = document.querySelector("#acord").checked;   // true sau false

// Color picker
let culoareAleasa = document.querySelector("#culoare").value;  // ex: "#ff6b6b"
```

---

## 7.11 `setTimeout` și `setInterval` — Timp în JavaScript ⏰

### `setTimeout` — Execută ceva DUPĂ un timp

```javascript
console.log("Start");

setTimeout(function() {
    console.log("Au trecut 3 secunde!");
}, 3000);     // 3000 milisecunde = 3 secunde

console.log("Codul continuă imediat...");

// Ordinea pe ecran:
// "Start"
// "Codul continuă imediat..."
// (3 secunde mai târziu) "Au trecut 3 secunde!"
```

### `setInterval` — Execută ceva la FIECARE interval

```javascript
let secunde = 0;

let timer = setInterval(function() {
    secunde++;
    console.log(`Au trecut ${secunde} secunde`);
    
    if (secunde >= 5) {
        clearInterval(timer);      // OPREȘTE intervalul
        console.log("Timer oprit!");
    }
}, 1000);     // la fiecare 1000ms = 1 secundă
```

```
  setTimeout:    "Fă ceva O SINGURĂ DATĂ, după X milisecunde"
                 Pui alarma la 7:00 → sună o dată → gata.
  
  setInterval:   "Fă ceva LA FIECARE X milisecunde"
                 Setezi timer de interval → sună la fiecare minut → 
                 trebuie oprit manual cu clearInterval()
```

### Exemplu practic — Cronometru simplu

```javascript
let display = document.querySelector("#cronometru");
let btnStart = document.querySelector("#btn-start");
let btnStop = document.querySelector("#btn-stop");

let secunde = 0;
let timerID = null;

btnStart.addEventListener("click", function() {
    // Pornește doar dacă nu rulează deja
    if (timerID === null) {
        timerID = setInterval(function() {
            secunde++;
            let min = Math.floor(secunde / 60);
            let sec = secunde % 60;
            display.textContent = `${min.toString().padStart(2, "0")}:${sec.toString().padStart(2, "0")}`;
        }, 1000);
    }
});

btnStop.addEventListener("click", function() {
    clearInterval(timerID);
    timerID = null;
});
```

---

## 7.12 Greșeli frecvente (și cum le repari) 🔧

### ❌ Greșeala 1: Script încărcat înainte de HTML

```html
<!-- ❌ Script în <head> — elementele nu există încă! -->
<head>
    <script src="script.js"></script>
</head>
<body>
    <h1 id="titlu">Salut</h1>
</body>
```

```javascript
// script.js
let titlu = document.querySelector("#titlu");
console.log(titlu);    // null! Elementul nu a fost creat încă.
```

```html
<!-- ✅ Script la final — elementele există deja -->
<body>
    <h1 id="titlu">Salut</h1>
    <script src="script.js"></script>
</body>
```

### ❌ Greșeala 2: Uiți `#` sau `.` în querySelector

```javascript
// ❌ GREȘIT — „titlu" nu e un tag HTML valid
let titlu = document.querySelector("titlu");       // null!

// ✅ CORECT — cu # pentru ID
let titlu = document.querySelector("#titlu");       // funcționează!

// ❌ GREȘIT — fără punct
let card = document.querySelector("important");     // null!

// ✅ CORECT — cu . pentru clasă
let card = document.querySelector(".important");    // funcționează!
```

### ❌ Greșeala 3: Confuzia `textContent` vs `value`

```javascript
// Pentru <p>, <h1>, <span> etc. → textContent
let paragraf = document.querySelector("p");
console.log(paragraf.textContent);     // ✅

// Pentru <input>, <textarea> → value
let input = document.querySelector("input");
console.log(input.value);              // ✅

// ❌ GREȘIT — input nu are textContent util
console.log(input.textContent);        // "" (mereu gol!)
```

### ❌ Greșeala 4: `addEventListener` cu paranteze la funcție

```javascript
function faSalut() {
    alert("Salut!");
}

// ❌ GREȘIT — apelează funcția IMEDIAT, nu la click!
buton.addEventListener("click", faSalut());

// ✅ CORECT — pasează REFERINȚA funcției (fără paranteze)
buton.addEventListener("click", faSalut);
```

### ❌ Greșeala 5: Schimbi stiluri neobservând camelCase

```javascript
// ❌ GREȘIT — CSS syntax nu merge în JS
element.style.font-size = "20px";          // SyntaxError!
element.style.background-color = "red";    // SyntaxError!

// ✅ CORECT — camelCase în JS
element.style.fontSize = "20px";
element.style.backgroundColor = "red";
```

---

## 7.13 Mini-quiz — Verifică ce ai învățat! ✅

**1.** Ce returnează `document.querySelector(".card")` dacă pe pagină sunt 5 elemente cu clasa `card`?

**2.** Care e diferența dintre `textContent` și `innerHTML`?

**3.** Cum adaugi clasa `activ` pe un element `btn`?

**4.** Ce eveniment folosești pentru a detecta când utilizatorul scrie într-un câmp de input?

**5.** Ce face `e.target` într-un event listener?

**6.** De ce punem `<script>` la finalul body-ului, nu în head?

**7.** Ce face acest cod?
```javascript
setTimeout(function() {
    alert("Surpriză!");
}, 5000);
```

---

<details>
<summary>🔑 Click aici pentru răspunsuri</summary>

1. Returnează doar **primul** element cu clasa `card`. Pentru a le obține pe **toate**, folosești `document.querySelectorAll(".card")`.

2. **`textContent`** schimbă doar textul simplu — tag-urile HTML sunt afișate ca text literal. **`innerHTML`** interpretează tag-urile HTML și le afișează stilizate. Ex: `innerHTML = "<strong>bold</strong>"` afișează **bold**, pe când `textContent` ar afișa literal `<strong>bold</strong>`.

3. ```javascript
   btn.classList.add("activ");
   ```

4. Evenimentul **`"input"`** — se declanșează la fiecare caracter tastat sau șters.

5. **`e.target`** este elementul exact pe care utilizatorul a făcut acțiunea (click, keydown etc.). Este util pentru delegarea evenimentelor — asculți pe părinte, dar identifici copilul exact.

6. Pentru că browserul citește pagina **de sus în jos**. Dacă JavaScript se execută înainte ca elementele HTML să existe, `querySelector` returnează `null` și codul dă erori.

7. Afișează un alert cu textul „Surpriză!" **după 5 secunde** (5000 milisecunde). Codul nu se blochează — restul programului continuă normal, iar alert-ul apare mai târziu.

</details>

---

## 7.14 Știai că? — Curiozități din lumea tech 🤓

🌳 **DOM-ul a fost standardizat în 1998** de W3C (World Wide Web Consortium). Înainte de standardizare, fiecare browser avea propriul mod de a manipula pagina, ceea ce era un coșmar pentru programatori. Mulți dezvoltatori web din anii '90 și 2000 erau nevoiți să scrie cod diferit pentru Internet Explorer, Netscape și Firefox!

⚡ **DOM-ul virtual** (Virtual DOM) este o inovație modernă popularizată de biblioteca React (creată de Facebook în 2013). În loc de a modifica DOM-ul real la fiecare schimbare (care e lent), React menține o copie „virtuală" în memorie, compară diferențele și actualizează doar ce s-a schimbat. Asta face aplicațiile mult mai rapide!

🎮 **Cele mai populare jocuri de browser** sunt făcute doar cu DOM manipulation și CSS. Jocuri simple ca `2048`, `Wordle` sau chiar `Cookie Clicker` nu folosesc Canvas — tot ce vezi sunt div-uri HTML stilizate cu CSS și manipulate cu JavaScript, exact ca în proiectul tău to-do list!

📱 **Aplicațiile mobile** de la Facebook, Instagram și multe altele sunt construite cu aceleași principii pe care tocmai le-ai învățat! React Native (bazat pe React) și alte framework-uri transformă cod JavaScript + DOM-manipulation în aplicații native pentru telefon. Practic, dacă știi DOM-ul, ești la un pas de a face aplicații mobile!

---

## Recapitulare — Ce ai învățat în Capitolul 7

```
  ✅ DOM = reprezentarea live a paginii HTML ca arbore de obiecte
  ✅ JavaScript = telecomanda care controlează DOM-ul
  ✅ querySelector() și querySelectorAll() — selectare cu sintaxă CSS
  ✅ getElementById() — selectare directă prin ID
  ✅ textContent — schimbă textul unui element
  ✅ innerHTML — schimbă conținutul HTML complet
  ✅ element.style.proprietate — schimbă stiluri individuale
  ✅ classList (add, remove, toggle, contains) — gestionează clase CSS
  ✅ setAttribute() / getAttribute() — modifică atribute HTML
  ✅ createElement() + appendChild() — creează elemente noi
  ✅ element.remove() — șterge elemente
  ✅ addEventListener() — ascultă evenimente
  ✅ Evenimente: click, keydown, input, mouseover
  ✅ e.target — elementul exact pe care s-a acționat
  ✅ Delegarea evenimentelor — un listener pe părinte
  ✅ Input: .value, .checked, tipuri de input
  ✅ setTimeout() și setInterval() — acțiuni programate în timp
  ✅ Ai construit o aplicație To-Do List completă! 📝
```

---

## Ce urmează?

În **Capitolul 8: Proiectul 1 — Quiz Game 🧠**, vei construi primul tău proiect major! Un joc de quiz complet cu întrebări, opțiuni de răspuns, scor, feedback vizual (corect/greșit), bară de progres și ecran de final. Vei folosi **tot** ce ai învățat în capitolele 1-7: HTML pentru structură, CSS pentru design, JavaScript pentru logică, DOM pentru interactivitate.

Pregătește-te — e timpul pentru primul tău joc web real! 🏆

---

> *„Cel mai bun mod de a prezice viitorul este să-l inventezi."*
> — Alan Kay, pionier al informaticii
