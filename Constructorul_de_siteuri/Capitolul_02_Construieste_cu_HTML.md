# Capitolul 2: Construiește cu HTML — Scheletul paginii 🦴

> *„Roma nu a fost construită într-o zi, dar au început cu prima cărămidă."*
> — Proverb adaptat

---

## Ce vei învăța în acest capitol

- Ce sunt **tag-urile** HTML și cum funcționează
- Cum să formatezi text: **bold**, *italic*, titluri, paragrafe
- Cum să creezi **liste** (numerotate și cu buline)
- Cum să adaugi **imagini** pe pagina ta
- Cum să creezi **linkuri** către alte pagini
- Ce sunt **atributele** HTML și de ce sunt importante

---

## 2.1 HTML este scheletul paginii tale

În capitolul trecut am spus că HTML este ca **structura unei case** — pereții, ușile, ferestrele. Dar hai să folosim o metaforă și mai bună:

**HTML este ca scheletul uman.**

```
         🧠 <head>
         ┌───┐
         │   │  ← Creierul (informații invizibile)
         └─┬─┘
           │
     ┌─────┴─────┐
     │   <body>   │
     │            │  ← Trunchiul (conținutul vizibil)
     │  ┌──────┐  │
     │  │ <h1> │  │  ← Inima (titlul principal)
     │  └──────┘  │
     │  ┌──────┐  │
     │  │ <p>  │  │  ← Coastele (paragrafele)
     │  │ <p>  │  │
     │  └──────┘  │
     │  ┌──────┐  │
     │  │ <img>│  │  ← Mâinile (imaginile)
     │  └──────┘  │
     │  ┌──────┐  │
     │  │ <a>  │  │  ← Picioarele (linkurile — te duc în altă parte!)
     │  └──────┘  │
     └────────────┘
```

Fiecare „os" din schelet este un **element HTML** — o piesă cu un rol specific. Unele sunt mari și importante (coloana vertebrală = `<body>`), altele sunt mici dar esențiale (degetele = `<span>`).

**Fără schelet**, corpul ar fi o grămadă informă. La fel, **fără HTML**, nu ar exista nimic pe ecran — niciun text, nicio imagine, nimic.

---

## 2.2 Anatomia unui tag HTML

Înainte de orice, trebuie să înțelegi cum arată un tag HTML. Este piesa fundamentală — ca o **cărămidă LEGO** din care construiești totul.

### Tag simplu (cu conținut)

```
    tag de deschidere       tag de închidere
          │                       │
          ▼                       ▼
        ┌───┐                  ┌────┐
        │   │                  │    │
        <h1> Salut, lume!      </h1>
              ─────────────
                    │
                conținutul
                (ce apare pe ecran)
```

**Regula de aur:** Ce deschizi, trebuie să închizi!

Este exact ca o **cutie**: o deschizi (`<h1>`), pui ceva înăuntru (textul), apoi o închizi (`</h1>`).

### Tag gol (fără conținut)

Câteva tag-uri nu au conținut — sunt „de sine stătătoare", ca un sticker pe care îl lipești:

```html
<img src="pisica.jpg" alt="O pisică drăguță">
<br>
<hr>
```

Aceste tag-uri nu au nevoie de `</...>` pentru că nu „conțin" nimic — ele **sunt** conținutul.

### Regula cutiilor (nesting)

Tag-urile pot fi puse unele **în interiorul** altora, exact ca niște cutii:

```
  ┌─────────── <body> ──────────────┐
  │                                  │
  │  ┌──────── <h1> ──────────┐     │
  │  │  Titlul meu            │     │
  │  └────────────────────────┘     │
  │                                  │
  │  ┌──────── <p> ───────────┐     │
  │  │  Un text cu un cuvânt  │     │
  │  │  ┌── <strong> ──┐      │     │
  │  │  │  important   │      │     │
  │  │  └──────────────┘      │     │
  │  └────────────────────────┘     │
  │                                  │
  └──────────────────────────────────┘
```

**Regula:** Cutia interioară trebuie să fie **complet** în interiorul cutiei exterioare. Nu se pot suprapune parțial.

```html
<!-- ✅ CORECT — strong este complet în interiorul lui p -->
<p>Un text cu un cuvânt <strong>important</strong> aici.</p>

<!-- ❌ GREȘIT — tag-urile se încrucișează -->
<p>Un text cu un cuvânt <strong>important</p></strong>
```

---

## 2.3 Tag-uri pentru text — Spune-ți povestea

Hai să învățăm cele mai folosite tag-uri, pas cu pas. Creează un fișier nou numit `text.html` și scrie:

```html
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Învăț tag-uri HTML</title>
</head>
<body>

    <h1>Jurnalul meu de programator</h1>
    <h2>Ziua 1 — Am descoperit HTML</h2>
    
    <p>Astăzi am învățat că HTML este scheletul paginilor web. 
    Fiecare element are un tag de deschidere și unul de închidere.</p>
    
    <p>Cel mai important lucru pe care l-am reținut: 
    <strong>ce deschizi, trebuie să închizi!</strong></p>

</body>
</html>
```

Salvează și deschide în browser. Vei vedea un titlu mare, un subtitlu și două paragrafe. Acum hai să adăugăm mai multe!

### Titluri: `<h1>` până la `<h6>`

HTML are **6 nivele de titluri**. Gândește-te la ele ca la cuprinsul unei cărți:

```html
<h1>Cartea mea</h1>              <!-- Titlul cărții (1 singur pe pagină!) -->
<h2>Capitolul 1</h2>             <!-- Capitol -->
<h3>Prima lecție</h3>            <!-- Subcapitol -->
<h4>Un detaliu important</h4>    <!-- Secțiune -->
<h5>O notă mică</h5>            <!-- Sub-secțiune -->
<h6>Cel mai mic titlu</h6>      <!-- Detaliu minor -->
```

Pe ecran, arată cam așa (dimensiunile sunt aproximative):

```
  ██  Cartea mea                          ← h1: MARE și bold
  
  █  Capitolul 1                          ← h2: mare și bold
  
  █ Prima lecție                          ← h3: mediu-mare
  
    Un detaliu important                  ← h4: mediu
    
    O notă mică                           ← h5: mic
    
    Cel mai mic titlu                     ← h6: cel mai mic
```

> ⚠️ **Atenție!**
> Nu folosi `<h1>` de mai multe ori pe o pagină! Este ca titlul unei cărți — o carte are un singur titlu principal. Dacă ai nevoie de mai multe secțiuni, folosește `<h2>`, `<h3>` etc.

> 💡 **Știai că?**
> Motoarele de căutare (Google, Bing) citesc titlurile tale HTML ca să înțeleagă despre ce e pagina ta. Un `<h1>` bun ajută pagina ta să apară mai sus în rezultatele căutării!

### Paragrafe: `<p>`

Fiecare bloc de text merge într-un `<p>`:

```html
<p>Aceasta este prima propoziție a paragrafului meu. 
Poate continua pe mai multe linii în cod, dar browserul 
le va afișa ca un singur bloc de text.</p>

<p>Acesta este al doilea paragraf. Browserul pune automat 
un spațiu între paragrafe.</p>
```

> ⚠️ **Atenție!**
> Dacă apeși Enter în codul HTML, browserul **nu** va face o linie nouă pe ecran! Browserul ignoră spațiile și enter-urile multiple. Dacă vrei un paragraf nou, folosește un nou `<p>`. Dacă vrei doar o linie nouă fără paragraf, folosește `<br>` (break).

```html
<!-- ❌ Asta NU funcționează cum crezi -->
<p>Linia 1
Linia 2
Linia 3</p>
<!-- Browserul afișează: "Linia 1 Linia 2 Linia 3" pe ACEEAȘI linie -->

<!-- ✅ Cu <br> forțezi linii noi -->
<p>Linia 1<br>Linia 2<br>Linia 3</p>

<!-- ✅ Sau folosește paragrafe separate -->
<p>Linia 1</p>
<p>Linia 2</p>
<p>Linia 3</p>
```

### Formatare text: bold, italic și altele

```html
<p>Pot face text <strong>bold (gras)</strong> pentru lucruri importante.</p>
<p>Pot face text <em>italic (înclinat)</em> pentru accent.</p>
<p>Pot face <strong><em>bold ȘI italic</em></strong> în același timp!</p>
<p>Pot <mark>evidenția</mark> text ca un marker galben.</p>
<p>Pot scrie H<sub>2</sub>O (apă) sau E = mc<sup>2</sup> (fizică).</p>
```

Iată ce face fiecare:

| Tag | Ce face | Exemplu | Rezultat |
|---|---|---|---|
| `<strong>` | Text **bold** (gras) | `<strong>important</strong>` | **important** |
| `<em>` | Text *italic* (înclinat) | `<em>accent</em>` | *accent* |
| `<mark>` | Text evidențiat (marker) | `<mark>atenție</mark>` | atenție (cu galben) |
| `<sub>` | Text jos (subscript) | `H<sub>2</sub>O` | H₂O |
| `<sup>` | Text sus (superscript) | `x<sup>2</sup>` | x² |
| `<del>` | Text ~~tăiat~~ | `<del>greșit</del>` | ~~greșit~~ |
| `<br>` | Linie nouă | `linia 1<br>linia 2` | (linie nouă) |
| `<hr>` | Linie orizontală | `<hr>` | ————————— |

### Separarea secțiunilor cu `<hr>`

`<hr>` (horizontal rule) desenează o linie pe ecran, utilă pentru a separa secțiuni:

```html
<h2>Secțiunea 1</h2>
<p>Conținutul primei secțiuni...</p>

<hr>

<h2>Secțiunea 2</h2>
<p>Conținutul celei de-a doua secțiuni...</p>
```

---

## 2.4 Liste — Pune lucrurile în ordine

Listele sunt peste tot pe web: meniuri, rețete, instrucțiuni, clasamente. HTML oferă două tipuri principale.

### Lista neordonată (cu buline): `<ul>`

**ul** = *unordered list* (listă neordonată)
**li** = *list item* (element din listă)

```html
<h2>Lucruri de care am nevoie:</h2>
<ul>
    <li>Un computer</li>
    <li>VS Code instalat</li>
    <li>Un browser modern</li>
    <li>Curiozitate!</li>
</ul>
```

Rezultat pe ecran:
```
  Lucruri de care am nevoie:
  • Un computer
  • VS Code instalat
  • Un browser modern
  • Curiozitate!
```

### Lista ordonată (numerotată): `<ol>`

**ol** = *ordered list* (listă ordonată)

```html
<h2>Pașii pentru a face o pagină web:</h2>
<ol>
    <li>Deschide VS Code</li>
    <li>Creează un fișier .html</li>
    <li>Scrie codul HTML</li>
    <li>Salvează fișierul</li>
    <li>Deschide în browser</li>
</ol>
```

Rezultat pe ecran:
```
  Pașii pentru a face o pagină web:
  1. Deschide VS Code
  2. Creează un fișier .html
  3. Scrie codul HTML
  4. Salvează fișierul
  5. Deschide în browser
```

### Liste în liste (nesting)

Poți pune o listă **în interiorul** altei liste! Este ca un cuprins detaliat:

```html
<h2>Ce voi învăța în această carte:</h2>
<ol>
    <li>HTML — Scheletul
        <ul>
            <li>Tag-uri de text</li>
            <li>Imagini și linkuri</li>
            <li>Liste și tabele</li>
        </ul>
    </li>
    <li>CSS — Stilul
        <ul>
            <li>Culori și fonturi</li>
            <li>Layout cu Flexbox</li>
        </ul>
    </li>
    <li>JavaScript — Creierul
        <ul>
            <li>Variabile și funcții</li>
            <li>Evenimente</li>
        </ul>
    </li>
</ol>
```

Rezultat:
```
  Ce voi învăța în această carte:
  1. HTML — Scheletul
     • Tag-uri de text
     • Imagini și linkuri
     • Liste și tabele
  2. CSS — Stilul
     • Culori și fonturi
     • Layout cu Flexbox
  3. JavaScript — Creierul
     • Variabile și funcții
     • Evenimente
```

> 💡 **Sfat!**
> Cum alegi între `<ul>` și `<ol>`? Simplu: dacă **ordinea contează** (pași, clasament, instrucțiuni), folosește `<ol>`. Dacă **ordinea NU contează** (ingrediente, hobby-uri, caracteristici), folosește `<ul>`.

---

## 2.5 Atribute HTML — Instrucțiuni suplimentare

Până acum, tag-urile noastre au fost simple: `<h1>`, `<p>`, `<li>`. Dar unele tag-uri au nevoie de **informații în plus**. Acestea se numesc **atribute**.

Gândește-te la un tag ca la un **verb**, și la atribute ca la **detalii suplimentare**:

```
  Verbul:  „Afișează o imagine"          →  <img>
  Detalii: „Care imagine? pisica.jpg"    →  src="pisica.jpg"
           „Descriere? O pisică"         →  alt="O pisică"

  Rezultat complet:
  <img src="pisica.jpg" alt="O pisică">
```

### Cum arată un atribut

```
       numele          valoarea
     atributului      atributului
         │                │
         ▼                ▼
  ┌─────────────────────────────┐
  │                             │
  │  <tag  nume="valoare">     │
  │                             │
  └─────────────────────────────┘
          │         │
          ▼         ▼
      fără spațiu   mereu între
      între tag     ghilimele!
      și atribut    
```

Reguli simple:
1. Atributele se scriu **în tag-ul de deschidere** (niciodată în cel de închidere!)
2. Formatul este mereu `nume="valoare"`
3. Valoarea e mereu **între ghilimele** (`"..."`)
4. Poți avea **mai multe atribute** pe același tag, separate prin spații

```html
<!-- Un singur atribut -->
<html lang="ro">

<!-- Mai multe atribute -->
<img src="pisica.jpg" alt="O pisică" width="300" height="200">
```

---

## 2.6 Imagini — O imagine face cât o mie de cuvinte 🖼️

Imaginile fac paginile web **mult** mai interesante. Tag-ul pentru imagini este `<img>`.

### Anatomia tag-ului `<img>`

```html
<img src="pisica.jpg" alt="O pisică portocalie dormind pe canapea">
```

| Atribut | Ce face | Obligatoriu? |
|---|---|---|
| `src` | **Source** (sursa) — calea către imagine. Unde se află fișierul imaginii? | ✅ Da! |
| `alt` | **Alternative text** — descriere textulă a imaginii. Apare dacă imaginea nu se încarcă. | ✅ Da! |
| `width` | Lățimea imaginii (în pixeli) | ❌ Opțional |
| `height` | Înălțimea imaginii (în pixeli) | ❌ Opțional |

### Pas cu pas: adaugă o imagine

**Pasul 1:** Găsește sau creează o imagine. Salvează-o în **același folder** cu fișierul HTML. Să zicem că ai o imagine numită `eu.jpg`.

```
  📁 proiectul-meu/
  ├── index.html
  └── eu.jpg          ← imaginea ta
```

**Pasul 2:** Adaugă tag-ul `<img>` în HTML:

```html
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pagina mea cu imagini</title>
</head>
<body>
    <h1>Despre mine</h1>
    <img src="eu.jpg" alt="O fotografie cu mine" width="300">
    <p>Aceasta sunt eu! Învăț programare web.</p>
</body>
</html>
```

### Organizare cu subfolder

Când ai multe imagini, e mai curat să le pui într-un folder separat:

```
  📁 proiectul-meu/
  ├── index.html
  └── 📁 imagini/
      ├── eu.jpg
      ├── pisica.jpg
      └── peisaj.png
```

În acest caz, calea se schimbă:

```html
<!-- Imaginea e în subfolderul "imagini" -->
<img src="imagini/eu.jpg" alt="O fotografie cu mine">
<img src="imagini/pisica.jpg" alt="Pisica mea, Felix">
<img src="imagini/peisaj.png" alt="Un peisaj de munte">
```

### Imagini de pe internet

Poți folosi și imagini de pe internet, folosind adresa lor completă (URL):

```html
<img src="https://placekitten.com/400/300" alt="O pisică drăguță" width="400">
```

> ⚠️ **Atenție!**
> Imaginile de pe internet pot dispărea oricând — dacă cineva șterge imaginea de pe serverul lor, pe pagina ta va apărea un pătrat gol. De aceea, pentru proiectele tale importante, descarcă imaginile și folosește-le local (din computerul tău).

> 💡 **Știai că?**
> Atributul `alt` nu e doar pentru când imaginea nu se încarcă. Este esențial pentru **accesibilitate** — persoanele cu deficiențe de vedere folosesc programe speciale (screen readers) care citesc cu voce tare textul `alt`. Când scrii un `alt` bun, ajuți pe cineva să „vadă" imaginea prin cuvinte!

---

## 2.7 Linkuri — Poduri între pagini 🔗

Linkurile (legăturile) sunt **superputerea** web-ului. Ele conectează paginile între ele, creând o rețea imensă — de aici vine și numele *World Wide Web* (Pânza Mondială).

Gândește-te la linkuri ca la **poduri** sau **uși**: faci click și ajungi în altă parte.

### Tag-ul `<a>` (anchor = ancoră)

```html
<a href="https://www.google.com">Mergi la Google</a>
```

Descompunere:

```
      atributul href
      (unde te duce linkul)
            │
            ▼
  <a href="https://www.google.com">Mergi la Google</a>
                                   ────────────────
                                         │
                                   textul vizibil
                                   (ce vede utilizatorul)
```

| Parte | Ce înseamnă |
|---|---|
| `<a>` | Tag-ul de link (anchor = ancoră) |
| `href` | **Hypertext Reference** — adresa destinației |
| Textul dintre tag-uri | Ce vede și pe ce face click utilizatorul |

### Tipuri de linkuri

**1. Link extern** — către alt site:

```html
<p>Motorul meu de căutare preferat este 
<a href="https://www.google.com">Google</a>.</p>
```

**2. Link intern** — către altă pagină din site-ul tău:

```html
<!-- Dacă ai un fișier "despre.html" în același folder -->
<a href="despre.html">Despre mine</a>
```

**3. Link care se deschide în tab nou:**

```html
<a href="https://www.google.com" target="_blank">Deschide Google în tab nou</a>
```

Atributul `target="_blank"` spune browserului: „Nu pleca de pe pagina mea, deschide linkul într-un tab nou!"

**4. Link pe o imagine** — imaginea devine „buton":

```html
<a href="https://www.youtube.com">
    <img src="imagini/youtube-logo.png" alt="Mergi la YouTube" width="100">
</a>
```

**5. Link de email:**

```html
<a href="mailto:numele.meu@email.com">Trimite-mi un email</a>
```

### Linkuri în context

Linkurile se pun de obicei **în interiorul** altor elemente:

```html
<p>Am învățat HTML de pe 
<a href="https://developer.mozilla.org" target="_blank">MDN Web Docs</a>, 
un site excelent pentru programatori.</p>

<ul>
    <li><a href="pagina1.html">Prima pagină</a></li>
    <li><a href="pagina2.html">A doua pagină</a></li>
    <li><a href="pagina3.html">A treia pagină</a></li>
</ul>
```

---

## 2.8 Arborele HTML — Cum vede browserul pagina ta

Acum că știi mai multe tag-uri, hai să vedem **imaginea de ansamblu**. Browserul vede pagina ta ca un **arbore** — exact ca un arbore genealogic:

```
                          <html>
                        ┌───┴───┐
                     <head>    <body>
                       │      ┌──┼──────┐
                   <title>  <h1>  <p>    <ul>
                              │    │    ┌──┼──┐
                          "Salut" │  <li> <li> <li>
                                  │
                           ┌──────┴──────┐
                        "Text "    <strong>
                                      │
                                 "important"
```

### Terminologie de familie

Exact ca într-o familie, elementele HTML au relații între ele:

```
  <body>                    ← PĂRINTE
    ├── <h1>                ← COPIL al body, FRATE cu p și ul
    ├── <p>                 ← COPIL al body, FRATE cu h1 și ul
    │     └── <strong>      ← COPIL al p, NEPOT al body
    └── <ul>                ← COPIL al body, FRATE cu h1 și p
          ├── <li>          ← COPIL al ul
          ├── <li>
          └── <li>
```

| Termen | Înseamnă | Exemplu |
|---|---|---|
| **Părinte** (parent) | Elementul care conține alt element | `<body>` este părintele lui `<h1>` |
| **Copil** (child) | Elementul conținut direct de altul | `<h1>` este copilul lui `<body>` |
| **Frați** (siblings) | Elemente cu același părinte | `<h1>`, `<p>` și `<ul>` sunt frați |
| **Descendent** | Orice element conținut (direct sau nu) | `<strong>` este descendent al lui `<body>` |

> 💡 **De ce contează asta?**
> Când vei învăța CSS (capitolul următor!), vei folosi aceste relații pentru a stiliza elementele. De exemplu, vei putea spune: „Fă bold toate paragrafele care sunt **copii** ai body-ului" sau „Schimbă culoarea tuturor **descendenților** lui `<ul>`".

---

## 2.9 Proiect practic: Pagina „Despre mine" 🚀

Hai să punem totul cap la cap! Vom construi o pagină completă „Despre mine" care folosește **toate** tag-urile învățate.

Creează un folder `despre-mine` cu structura:

```
  📁 despre-mine/
  ├── index.html
  └── 📁 imagini/
      └── (adaugă o poză cu tine sau un avatar)
```

Acum scrie acest cod în `index.html`:

```html
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Despre Mine — Pagina mea personală</title>
</head>
<body>

    <h1>Bun venit pe pagina mea! 👋</h1>
    <hr>

    <!-- ===== SECȚIUNEA: Despre mine ===== -->
    <h2>Despre mine</h2>
    <img src="imagini/avatar.jpg" alt="Fotografia mea" width="200">
    <p>Salut! Mă numesc <strong>[Numele tău]</strong> și am 
    <strong>[vârsta] ani</strong>.</p>
    <p>Sunt elev/ă în clasa <em>[clasa ta]</em> și 
    tocmai am început să învăț <strong>programare web</strong>!</p>

    <!-- ===== SECȚIUNEA: Hobby-uri ===== -->
    <h2>Lucrurile mele preferate</h2>
    
    <h3>🎮 Hobby-uri</h3>
    <ul>
        <li>Programare (evident!)</li>
        <li>[Hobby-ul tău 1]</li>
        <li>[Hobby-ul tău 2]</li>
        <li>[Hobby-ul tău 3]</li>
    </ul>

    <h3>📚 Materii preferate la școală</h3>
    <ol>
        <li>[Materia ta preferată]</li>
        <li>[A doua materie]</li>
        <li>[A treia materie]</li>
    </ol>

    <h3>🎬 Top 3 filme</h3>
    <ol>
        <li><strong>[Filmul #1]</strong> — <em>cel mai tare!</em></li>
        <li>[Filmul #2]</li>
        <li>[Filmul #3]</li>
    </ol>

    <!-- ===== SECȚIUNEA: Ce am învățat ===== -->
    <h2>Ce știu deja în HTML</h2>
    <p>Am învățat să folosesc aceste tag-uri:</p>
    <ul>
        <li><strong>Titluri</strong> — h1 până la h6</li>
        <li><strong>Paragrafe</strong> — pentru text</li>
        <li><strong>Bold și italic</strong> — pentru a evidenția cuvinte</li>
        <li><strong>Liste</strong> — ordonate și neordonate</li>
        <li><strong>Imagini</strong> — cu src și alt</li>
        <li><strong>Linkuri</strong> — pentru a conecta pagini</li>
    </ul>

    <!-- ===== SECȚIUNEA: Linkuri utile ===== -->
    <h2>Resurse care mă ajută</h2>
    <p>Iată câteva site-uri de unde învăț:</p>
    <ul>
        <li><a href="https://developer.mozilla.org" target="_blank">MDN Web Docs</a> 
            — documentația oficială pentru web</li>
        <li><a href="https://www.w3schools.com" target="_blank">W3Schools</a> 
            — tutoriale interactive</li>
    </ul>

    <hr>

    <!-- ===== FOOTER ===== -->
    <p><em>Creat cu ❤️ de [Numele tău] — Constructorul de Site-uri, Capitolul 2</em></p>

</body>
</html>
```

### Ce am folosit în acest proiect

Verifică — ai reușit să folosești toate acestea:

```
  ✅ Structura completă (DOCTYPE, html, head, body)
  ✅ Titluri pe mai multe nivele (h1, h2, h3)
  ✅ Paragrafe (p) cu text formatat
  ✅ Bold (strong) și italic (em)
  ✅ Linie orizontală (hr) ca separator
  ✅ Imagine (img) cu src și alt
  ✅ Lista neordonată (ul > li)
  ✅ Lista ordonată (ol > li)
  ✅ Linkuri (a) cu href și target
  ✅ Comentarii HTML (<!-- -->)
```

---

## 2.10 Comentariile HTML — Note invizibile

Ai observat în codul de mai sus linii ca aceasta?

```html
<!-- ===== SECȚIUNEA: Despre mine ===== -->
```

Acestea sunt **comentarii**. Browserul le **ignoră complet** — nu apar pe ecran. Sunt note doar pentru tine, programatorul.

```html
<!-- Acesta este un comentariu. Browserul nu-l afișează. -->

<p>Acest text APARE pe ecran.</p>

<!-- 
    Comentariile pot fi 
    și pe mai multe linii.
    Sunt utile pentru a explica ce face codul.
-->
```

Gândește-te la comentarii ca la **biletelele lipicioase** (post-it-uri) pe care le pui în manual — te ajută să înțelegi codul când te întorci la el peste câteva zile sau săptămâni.

> 🚀 **Provocare!**
> Deschide orice pagină web (de exemplu google.com), apasă `Ctrl + U` (sau click dreapta → „View Page Source"). Vei vedea codul HTML din spatele paginii! Caută comentarii `<!-- ... -->`. Multe site-uri profesionale au comentarii care explică secțiunile.

---

## 2.11 Caractere speciale — Entități HTML

Ce faci dacă vrei să scrii simbolul `<` pe pagină? Nu poți pur și simplu scrie `<`, pentru că browserul crede că începi un tag!

Soluția: **entități HTML** — coduri speciale care reprezintă caractere:

| Ce vrei | Ce scrii | Cum se numește |
|---|---|---|
| < | `&lt;` | less than |
| > | `&gt;` | greater than |
| & | `&amp;` | ampersand |
| " | `&quot;` | quote |
| spațiu suplimentar | `&nbsp;` | non-breaking space |
| © | `&copy;` | copyright |
| ♥ | `&hearts;` | hearts |

Exemplu practic:

```html
<p>În HTML, un tag arată așa: &lt;numeTag&gt;</p>
<p>&copy; 2025 Numele Meu. Toate drepturile rezervate.</p>
<p>Eu &hearts; programarea!</p>
```

Pe ecran:
```
  În HTML, un tag arată așa: <numeTag>
  © 2025 Numele Meu. Toate drepturile rezervate.
  Eu ♥ programarea!
```

---

## 2.12 Tabel rezumativ — Toate tag-urile din acest capitol

Iată un „cheat sheet" cu tot ce ai învățat:

| Tag | Nume | Ce face | Exemplu |
|---|---|---|---|
| `<h1>`–`<h6>` | Heading | Titluri (6 nivele) | `<h1>Titlu</h1>` |
| `<p>` | Paragraph | Paragraf de text | `<p>Text...</p>` |
| `<strong>` | Strong | Text **bold** | `<strong>bold</strong>` |
| `<em>` | Emphasis | Text *italic* | `<em>italic</em>` |
| `<mark>` | Mark | Text evidențiat | `<mark>evidențiat</mark>` |
| `<del>` | Delete | Text ~~tăiat~~ | `<del>tăiat</del>` |
| `<sub>` | Subscript | Text jos | `H<sub>2</sub>O` |
| `<sup>` | Superscript | Text sus | `x<sup>2</sup>` |
| `<br>` | Break | Linie nouă | `linia 1<br>linia 2` |
| `<hr>` | Horizontal Rule | Linie separatoare | `<hr>` |
| `<ul>` | Unordered List | Listă cu buline | `<ul><li>...</li></ul>` |
| `<ol>` | Ordered List | Listă numerotată | `<ol><li>...</li></ol>` |
| `<li>` | List Item | Element din listă | `<li>element</li>` |
| `<img>` | Image | Imagine | `<img src="x.jpg" alt="...">` |
| `<a>` | Anchor | Link | `<a href="url">text</a>` |
| `<!-- -->` | Comment | Comentariu (invizibil) | `<!-- notă -->` |

---

## 2.13 Greșeli frecvente (și cum le repari) 🔧

### ❌ Greșeala 1: Alt-ul lipsă la imagini

```html
<!-- ❌ GREȘIT — fără alt -->
<img src="pisica.jpg">

<!-- ✅ CORECT — cu alt descriptiv -->
<img src="pisica.jpg" alt="Pisica mea Felix dormind pe canapea">
```

**De ce contează:** Fără `alt`, persoanele cu deficiențe de vedere nu vor ști ce conține imaginea. În plus, dacă imaginea nu se încarcă, utilizatorul vede `alt` în loc de un pătrat gol.

### ❌ Greșeala 2: `<li>` în afara listei

```html
<!-- ❌ GREȘIT — li fără ul sau ol -->
<li>Element 1</li>
<li>Element 2</li>

<!-- ✅ CORECT — li în interiorul unei liste -->
<ul>
    <li>Element 1</li>
    <li>Element 2</li>
</ul>
```

### ❌ Greșeala 3: Calea greșită către imagine

```html
<!-- Structura folderului: -->
<!-- 📁 proiect/ -->
<!--   ├── index.html -->
<!--   └── 📁 imagini/ -->
<!--       └── pisica.jpg -->

<!-- ❌ GREȘIT — fișierul nu e în același folder -->
<img src="pisica.jpg" alt="Pisica">

<!-- ✅ CORECT — calea include folderul -->
<img src="imagini/pisica.jpg" alt="Pisica">
```

**Sfat:** Dacă imaginea nu apare, verifică:
1. Numele fișierului este scris **exact** la fel? (pisica.jpg ≠ Pisica.jpg ≠ pisica.JPG)
2. Fișierul este în **locul corect**?
3. Ai scris **calea corectă** în `src`?

### ❌ Greșeala 4: Ghilimele lipsă la atribute

```html
<!-- ❌ GREȘIT — fără ghilimele -->
<img src=pisica.jpg alt=O pisică>

<!-- ✅ CORECT — cu ghilimele -->
<img src="pisica.jpg" alt="O pisică">
```

### ❌ Greșeala 5: Paragraf în paragraf

```html
<!-- ❌ GREȘIT — nu poți pune <p> în <p> -->
<p>Un text <p>altul</p> și continuare</p>

<!-- ✅ CORECT — paragrafe separate -->
<p>Un text</p>
<p>Altul</p>
<p>Și continuare</p>
```

**Regulă:** `<p>` nu poate conține alt `<p>`. Paragrafele sunt mereu la același nivel.

---

## 2.14 Mini-quiz — Verifică ce ai învățat! ✅

**1.** Ce tip de listă folosești pentru o rețetă (unde ordinea pașilor contează)?

**2.** Ce atribut este **obligatoriu** la `<img>` pe lângă `src`?

**3.** Ce face atributul `target="_blank"` la un link?

**4.** Care este diferența dintre `<strong>` și `<h1>`? Ambele fac text mare și bold, nu?

**5.** De ce e important `alt` la imagini?

**6.** Ce se întâmplă dacă scrii `<li>` fără `<ul>` sau `<ol>` în jurul lor?

**7.** Cum scrii simbolul `<` într-un text HTML fără ca browserul să creadă că e un tag?

---

<details>
<summary>🔑 Click aici pentru răspunsuri</summary>

1. **`<ol>`** (ordered list) — lista ordonată, pentru că pașii trebuie urmați în ordine.

2. **`alt`** — textul alternativ care descrie imaginea. Este esențial pentru accesibilitate și apare când imaginea nu se poate încărca.

3. **Deschide linkul într-un tab nou** în browser, în loc să părăsească pagina curentă.

4. Sunt complet diferite! **`<h1>`** este un titlu de secțiune — definește structura paginii. **`<strong>`** marchează text ca fiind important în interiorul unui paragraf, fără a crea o secțiune nouă. Este ca diferența dintre titlul unui capitol (h1) și un cuvânt subliniat într-o propoziție (strong).

5. Este important pentru: (a) **accesibilitate** — programele de citire a ecranului citesc `alt` pentru persoanele cu deficiențe de vedere; (b) **fallback** — dacă imaginea nu se încarcă, utilizatorul vede textul; (c) **SEO** — motoarele de căutare înțeleg ce conține imaginea.

6. Codul este **invalid**. Browserul va încerca să-l afișeze, dar comportamentul este imprevizibil. `<li>` trebuie să fie mereu copilul direct al unui `<ul>` sau `<ol>`.

7. Folosind entitatea HTML **`&lt;`** (care înseamnă „less than").

</details>

---

## 2.15 Știai că? — Curiozități din lumea tech 🤓

🏷️ **HTML a fost inventat în 1991** de Tim Berners-Lee. Prima versiune avea doar **18 tag-uri**! Azi, HTML5 are peste **110 tag-uri** diferite. Nu trebuie să le știi pe toate — chiar și programatorii profesioniști folosesc zilnic doar 20–30 dintre ele.

🌍 **Cele mai vizitate pagini web** (Google, YouTube, Facebook) folosesc exact aceleași tag-uri pe care tocmai le-ai învățat: `<h1>`, `<p>`, `<img>`, `<a>`. Diferența este că au **foarte mult** CSS și JavaScript deasupra.

♿ **Peste 1 miliard de oameni** din lume au o formă de dizabilitate. Când scrii `alt` la imagini și folosești tag-uri corecte (nu doar `<div>` pentru tot), faci web-ul accesibil pentru toată lumea. Este ca și cum ai construi o rampă lângă scări — îi ajuți pe toți să intre.

🔤 **Cel mai folosit tag HTML** din lume este `<div>` (pe care îl vei învăța în curând). Pe un site mare, pot exista mii de div-uri! Este ca o cutie universală — poți pune orice în ea.

---

## Recapitulare — Ce ai învățat în Capitolul 2

```
  ✅ Tag-urile HTML au deschidere <tag> și închidere </tag>
  ✅ Regula cutiilor: tag-urile se pot imbrica, dar nu se suprapun
  ✅ Titluri (h1–h6) — structura ierarhică a paginii
  ✅ Paragrafe (p) — blocuri de text
  ✅ Formatare: strong (bold), em (italic), mark, del, sub, sup
  ✅ Liste neordonate (ul) și ordonate (ol) cu elemente (li)
  ✅ Liste imbricate (listă în listă)
  ✅ Atributele sunt informații suplimentare în tag-ul de deschidere
  ✅ Imagini (img) cu src și alt
  ✅ Linkuri (a) cu href — interne, externe, în tab nou
  ✅ Arborele HTML — relații părinte/copil/frate
  ✅ Comentarii (<!-- -->) — note invizibile
  ✅ Entități HTML (&lt; &gt; &amp;) pentru caractere speciale
  ✅ Ai construit o pagină completă "Despre mine"! 🎉
```

---

## Ce urmează?

În **Capitolul 3: Îmbracă-ți pagina cu CSS — Stilul contează!**, pagina ta „Despre mine" va primi culori, fonturi frumoase, spații armonioase și un design profesional. Vei vedea cum aceeași pagină HTML poate arăta complet diferit doar schimbând CSS-ul — ca un actor care schimbă costumul!

Pregătește-te — lucrurile încep să devină **colorate**! 🎨

---

> *„Web-ul este mai mult un instrument social decât unul tehnic. L-am proiectat pentru un efect social — să ajute oamenii să lucreze împreună."*
> — Tim Berners-Lee, inventatorul World Wide Web
