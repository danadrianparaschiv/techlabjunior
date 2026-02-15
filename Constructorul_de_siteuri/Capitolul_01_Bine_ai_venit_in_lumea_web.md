# Capitolul 1: Bine ai venit în lumea web! 🌍

> *„Orice tehnologie suficient de avansată este indistinctă de magie."*
> — Arthur C. Clarke

---

## Ce vei învăța în acest capitol

- Ce este internetul și cum funcționează (pe înțelesul tău!)
- Cum ajunge o pagină web pe ecranul tău
- Ce sunt HTML, CSS și JavaScript — și de ce ai nevoie de toate trei
- Cum să îți instalezi „atelierul" de programare
- Cum să creezi **prima ta pagină web**

---

## 1.1 Povestea internetului — Cel mai mare sistem poștal din lume

Imaginează-ți că ai un prieten în Japonia. Vrei să îi trimiți o scrisoare. Ce faci?

1. **Scrii scrisoarea** (conținutul)
2. **O pui într-un plic** decorat frumos
3. **Scrii adresa** pe plic
4. **O duci la poștă**
5. Scrisoarea **călătorește** prin avioane, camioane, trenuri...
6. Ajunge la **oficiul poștal** din orașul prietenului
7. **Poștașul** o livrează la ușa lui

**Internetul funcționează exact la fel**, doar că totul se întâmplă în câteva milisecunde, nu în câteva zile!

Hai să traducem:

| 📬 Lumea reală | 💻 Lumea web |
|---|---|
| Scrisoarea ta | Pagina web (fișierele HTML, CSS, JS) |
| Oficiul poștal unde se păstrează scrisorile | **Serverul** — un computer puternic care păstrează site-urile |
| Adresa de pe plic | **Adresa web (URL)** — ex: `www.google.com` |
| Poștașul care livrează | **Browserul** tău (Chrome, Firefox, Edge) |
| Drumurile și avioanele | **Cablurile de internet** (inclusiv submarine!) |

### Cum funcționează, pas cu pas

Când scrii `www.youtube.com` în browser și apeși Enter, se întâmplă asta:

```
    TU (browserul tău)                         SERVERUL (computerul YouTube)
    ┌──────────────┐                           ┌──────────────────┐
    │  Chrome /    │  ── "Vreau pagina!" ──►   │  Computerul care │
    │  Firefox /   │                           │  păstrează toate │
    │  Edge        │  ◄── "Poftim!" ────────   │  fișierele site- │
    │              │      (HTML+CSS+JS)         │  ului YouTube    │
    └──────────────┘                           └──────────────────┘
          │                                            │
          │          ═══════════════════════            │
          └─────────  Cabluri de internet  ────────────┘
                     ═══════════════════════
```

1. **Browserul trimite o cerere**: „Hei, server! Vreau pagina `www.youtube.com`!"
2. **Cererea călătorește** prin cabluri (uneori chiar pe fundul oceanului — da, există cabluri submarine!)
3. **Serverul primește cererea** și caută fișierele necesare
4. **Serverul trimite înapoi** fișierele: HTML, CSS și JavaScript
5. **Browserul primește fișierele** și le „citește"
6. **Browserul desenează pagina** pe ecranul tău — asta vezi tu!

> 💡 **Știai că?**
> Există peste 500 de cabluri submarine care conectează continentele. Unele sunt lungi de peste 20.000 km! Dacă ar fi întinse, ar putea înconjura Pământul de aproape 3 ori. Rechinii uneori le mușcă — da, serios! De aceea sunt protejate cu armură specială.

---

## 1.2 Cele trei super-puteri ale web-ului: HTML, CSS și JavaScript

Fiecare pagină web este construită cu trei „ingrediente" diferite. Gândește-te la ele ca la construirea unei case:

```
  🏗️ HTML               🎨 CSS                ⚡ JavaScript
  ═══════════          ═══════════           ═══════════════
  STRUCTURA            STILUL                COMPORTAMENTUL
  
  Pereții, ușile,      Vopseaua, tapetul,    Soneria, liftul,
  ferestrele,          culorile, mobilierul  sistemul de alarmă,
  acoperișul                                 ușile automate
  
  "Ce există           "Cum arată            "Ce se întâmplă
   pe pagină?"          pagina?"              când interacționezi?"
```

### 🧱 HTML — Scheletul

**HTML** (HyperText Markup Language) este „scheletul" paginii. El spune browserului **ce** elemente există: titluri, paragrafe, imagini, butoane, linkuri.

Fără HTML, nu ar exista nimic pe ecran.

### 🎨 CSS — Hainele

**CSS** (Cascading Style Sheets) este garderoba paginii. El spune browserului **cum arată** elementele: ce culori au, cât de mari sunt, unde sunt poziționate, ce fonturi folosesc.

Fără CSS, pagina ar arăta ca un document Word din anii '90 — text negru pe fundal alb, fără personalitate.

### ⚡ JavaScript — Creierul

**JavaScript** (prescurtat **JS**) este creierul paginii. El face pagina **interactivă**: butoanele funcționează, jocurile se mișcă, formularele verifică ce scrii.

Fără JavaScript, pagina ar fi ca o poză — frumoasă, dar nemișcată.

### Împreună, sunt imbatabile

Iată cum colaborează cele trei pentru un simplu buton:

| Limbaj | Ce face pentru buton |
|---|---|
| **HTML** | Creează butonul pe pagină: „Aici există un buton cu textul *Click pe mine*" |
| **CSS** | Îl face frumos: fundal albastru, colțuri rotunjite, text alb, umbră |
| **JavaScript** | Îi dă viață: când apeși pe el, apare un mesaj „Salut!" |

> ⚠️ **Atenție!**
> JavaScript și Java sunt **două limbaje complet diferite**! Nu le confunda. E ca diferența dintre „car" (mașină) și „carpet" (covor) în engleză — sună similar, dar nu au legătură. JavaScript s-a numit așa din motive de marketing, în anii '90.

---

## 1.3 Cum „vede" browserul o pagină web

Când browserul primește fișierele de la server, le citește într-o ordine specifică:

```
  ┌─────────────────────────────────────────────────────────┐
  │                    BROWSERUL                            │
  │                                                         │
  │   Pasul 1          Pasul 2           Pasul 3           │
  │  ┌─────────┐     ┌──────────┐     ┌────────────┐      │
  │  │  HTML   │────►│   CSS    │────►│ JavaScript │      │
  │  │         │     │          │     │            │      │
  │  │ Citește │     │ Aplică   │     │ Adaugă     │      │
  │  │ structu-│     │ stiluri  │     │ interacti- │      │
  │  │ ra      │     │ și culori│     │ vitate     │      │
  │  └─────────┘     └──────────┘     └────────────┘      │
  │       │                │                │              │
  │       ▼                ▼                ▼              │
  │  ┌─────────────────────────────────────────────┐      │
  │  │          PAGINA COMPLETĂ PE ECRAN           │      │
  │  │     (ce vezi tu când navighezi pe web)       │      │
  │  └─────────────────────────────────────────────┘      │
  │                                                         │
  └─────────────────────────────────────────────────────────┘
```

Gândește-te la asta ca la pregătirea unui actor pentru un spectacol:
- **HTML** = actorul în sine (corpul, fața, mâinile)
- **CSS** = costumul și machiajul (haine, culori, accesorii)
- **JavaScript** = regizorul care îi spune ce să facă pe scenă (mișcări, replici, reacții)

---

## 1.4 Pregătirea atelierului — Instalează-ți uneltele! 🛠️

Înainte să construiești ceva, ai nevoie de unelte. Vestea bună? **Toate sunt gratuite!**

Ai nevoie de doar două lucruri:

### 1. Un editor de cod — Visual Studio Code (VS Code)

**Ce este?** Un program special în care scrii cod. Este ca un Microsoft Word, dar pentru programatori. Are super-puteri: colorează codul diferit pentru a-l face mai ușor de citit, te avertizează când faci greșeli și îți sugerează completări.

**Cum îl instalezi:**

1. Deschide browserul și mergi la: **`https://code.visualstudio.com`**
2. Apasă butonul mare **„Download"**
3. Deschide fișierul descărcat și urmează pașii de instalare (Next → Next → Install)
4. Deschide VS Code — felicitări, ai primul tău instrument de programator!

> 💡 **Știai că?**
> VS Code este folosit de **milioane** de programatori profesioniști din toată lumea. Același program pe care îl vei folosi tu este cel pe care îl folosesc inginerii de la Google, Microsoft sau NASA. Ești în companie bună!

### 2. Un browser modern

Deja ai unul! Chrome, Firefox, Edge sau Safari — oricare funcționează. Noi vom folosi **Chrome** în exemple, dar poți folosi ce preferi.

**Truc util:** În Chrome, apasă tasta `F12` (sau `Ctrl + Shift + I`) pentru a deschide **Instrumentele pentru Dezvoltatori** (Developer Tools). Aici vei vedea „în spatele scenei" oricărei pagini web. Vom folosi des acest instrument!

---

## 1.5 Extensii recomandate pentru VS Code

După ce instalezi VS Code, adaugă aceste extensii care te vor ajuta enorm:

| Extensie | Ce face | De ce ai nevoie |
|---|---|---|
| **Live Server** | Deschide pagina ta web într-un browser și o actualizează automat când salvezi | Nu mai trebuie să apeși refresh manual! |
| **Prettier** | Aranjează codul frumos și ordonat automat | Codul tău va arăta mereu profesionist |
| **Auto Rename Tag** | Când schimbi un tag HTML de deschidere, îl schimbă automat și pe cel de închidere | Economisești timp și eviți greșeli |

**Cum instalezi o extensie:**

1. Deschide VS Code
2. Apasă pe iconița cu pătrate din bara din stânga (Extensions) sau `Ctrl + Shift + X`
3. Scrie numele extensiei în bara de căutare
4. Apasă **Install** pe extensia corectă

```
  ┌──────────────────────────────────┐
  │  VS Code                   _ □ X │
  ├────┬─────────────────────────────┤
  │    │                             │
  │ 📄 │   Aici vei scrie codul...   │
  │ 🔍 │                             │
  │ 🔀 │                             │
  │ 🧩◄── Apasă aici pentru         │
  │ ▶️ │   extensii (Extensions)     │
  │    │                             │
  │    │                             │
  ├────┴─────────────────────────────┤
  │ Terminal                         │
  └──────────────────────────────────┘
```

---

## 1.6 Prima ta pagină web — „Salut, lume!" 🎉

Acesta este momentul cel mare. Ești pregătit? Hai să creăm prima ta pagină web!

### Pasul 1: Creează un folder pentru proiect

1. Creează undeva pe computer un folder nou numit `prima-pagina`
2. Deschide VS Code
3. Mergi la **File → Open Folder** și selectează folderul `prima-pagina`

### Pasul 2: Creează fișierul HTML

1. În VS Code, apasă pe iconița de **fișier nou** (sau `Ctrl + N`)
2. Salvează fișierul (`Ctrl + S`) cu numele: **`index.html`**

> 💡 **Știai că?**
> De ce `index.html`? Acesta este numele „magic" pe care serverele web îl caută automat. Când cineva vizitează un site, serverul caută mai întâi `index.html` — este ca ușa de intrare a casei tale digitale.

### Pasul 3: Scrie codul

Scrie (sau copiază) următorul cod în fișierul `index.html`:

```html
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prima mea pagină web</title>
</head>
<body>
    <h1>Salut, lume! 🌍</h1>
    <p>Aceasta este prima mea pagină web.</p>
    <p>Am creat-o eu, cu mâinile mele (și cu tastatura)!</p>
</body>
</html>
```

### Pasul 4: Deschide pagina în browser

**Varianta A — Cu Live Server (recomandat):**
- Click dreapta pe fișierul `index.html` în VS Code
- Alege **„Open with Live Server"**
- Browserul se deschide automat cu pagina ta!

**Varianta B — Manual:**
- Găsește fișierul `index.html` pe computer
- Dublu-click pe el — se va deschide în browser

### 🎉 Felicitări!

Dacă vezi pe ecran textul „Salut, lume! 🌍" — ai reușit! **Tocmai ai creat prima ta pagină web!**

Știi ce au în comun aproape toți programatorii din lume? Primul lor program a fost mereu un „Hello, World!" (Salut, lume!). Este o tradiție care datează din 1972. Acum faci și tu parte din această familie!

---

## 1.7 Să înțelegem codul — Linie cu linie

Hai să vedem ce face fiecare parte. Nu trebuie să memorezi totul acum — le vom repeta de multe ori!

```html
<!DOCTYPE html>
```
📌 **Ce face:** Spune browserului „Hei, acest fișier este HTML5!" (versiunea modernă de HTML).
🏠 **Metaforă:** Este ca plăcuța de la intrarea în casă care spune „Aceasta este o casă, nu un magazin sau o școală."

---

```html
<html lang="ro">
```
📌 **Ce face:** Deschide „cutia" mare care conține TOT. `lang="ro"` spune că limba paginii este româna.
🏠 **Metaforă:** Este fundația casei — totul se construiește înăuntru.

---

```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prima mea pagină web</title>
</head>
```
📌 **Ce face:**
- `<head>` = secțiunea „invizibilă" — informații **despre** pagină (nu apar pe ecran)
- `charset="UTF-8"` = permite caractere speciale (ă, î, ș, ț, emoji-uri 🎉)
- `viewport` = face pagina să arate bine pe telefoane
- `<title>` = textul din tab-ul browserului (sus, pe bara de titlu)

🏠 **Metaforă:** `<head>` este ca „creierul" casei — nu îl vezi din exterior, dar controlează lucruri importante (electricitate, apă, încălzire). `<title>` este ca numele scris pe cutia poștală.

---

```html
<body>
    <h1>Salut, lume! 🌍</h1>
    <p>Aceasta este prima mea pagină web.</p>
    <p>Am creat-o eu, cu mâinile mele (și cu tastatura)!</p>
</body>
```
📌 **Ce face:**
- `<body>` = tot ce este **vizibil** pe pagină
- `<h1>` = heading (titlu) de nivel 1 — cel mai mare și mai important
- `<p>` = paragraph (paragraf) — text normal

🏠 **Metaforă:** `<body>` este interiorul casei — tot ce văd oaspeții când intră. `<h1>` este panoul mare de bun venit, iar `<p>` sunt foile de pe masă cu informații.

### Structura generală — mereu aceeași

```
<!DOCTYPE html>          ← "Aceasta e o pagină HTML5"
<html>                   ← Începutul a tot
  ┌─────────────────┐
  │  <head>         │    ← Informații invizibile
  │    <title>      │
  │  </head>        │
  ├─────────────────┤
  │  <body>         │    ← Conținutul vizibil
  │    <h1>         │
  │    <p>          │
  │  </body>        │
  └─────────────────┘
</html>                  ← Sfârșitul a tot
```

> ⚠️ **Atenție!**
> Observi cum fiecare tag care se **deschide** (`<body>`) trebuie să se **închidă** (`</body>`)? E ca parantezele în matematică: dacă deschizi una, trebuie s-o închizi. Uiți să închizi un tag? Browserul se confuzează și pagina poate arăta ciudat!

---

## 1.8 Experimentează! Modifică pagina ta 🧪

Acum vine partea distractivă. Modifică codul și vezi ce se întâmplă!

### Provocare 1: Schimbă textul

Înlocuiește `Salut, lume! 🌍` cu propriul tău mesaj. Poate:
- `Bine ați venit pe site-ul meu! 🚀`
- `Sunt [numele tău] și iubesc programarea! 💻`
- `Aceasta este cea mai tare pagină din univers! ✨`

Salvează (`Ctrl + S`) și privește browserul — dacă ai Live Server, pagina se actualizează singură!

### Provocare 2: Adaugă mai mult conținut

Adaugă mai multe elemente în `<body>`. Încearcă:

```html
<body>
    <h1>Blogul lui [numele tău]</h1>
    <h2>Despre mine</h2>
    <p>Mă numesc [numele tău] și am [vârsta] ani.</p>
    <p>Îmi place să [hobby-ul tău] și tocmai învăț programare web!</p>
    
    <h2>Lucruri care îmi plac</h2>
    <p>Culoarea mea preferată este [culoarea].</p>
    <p>Jocul meu preferat este [jocul].</p>
    <p>Mâncarea mea preferată este [mâncarea].</p>

    <h2>Ce vreau să construiesc</h2>
    <p>Vreau să învăț să fac jocuri și site-uri web cool!</p>
</body>
```

### Provocare 3: Experimentează cu heading-urile

HTML are 6 nivele de titluri. Încearcă-le pe toate:

```html
<h1>Titlu nivel 1 — Cel mai mare</h1>
<h2>Titlu nivel 2</h2>
<h3>Titlu nivel 3</h3>
<h4>Titlu nivel 4</h4>
<h5>Titlu nivel 5</h5>
<h6>Titlu nivel 6 — Cel mai mic</h6>
```

Gândește-te la ele ca la un cuprins de carte:
- `<h1>` = Titlul cărții (folosești **o singură dată** pe pagină)
- `<h2>` = Capitolele
- `<h3>` = Subcapitolele
- `<h4>` până la `<h6>` = Secțiuni tot mai mici

---

## 1.9 Greșeli frecvente (și cum le repari) 🔧

Toată lumea face greșeli la început. Iată cele mai comune:

### ❌ Greșeala 1: Tag neînchis

```html
<!-- ❌ GREȘIT — lipsește </h1> -->
<h1>Titlul meu
<p>Un paragraf</p>

<!-- ✅ CORECT -->
<h1>Titlul meu</h1>
<p>Un paragraf</p>
```

**Simptom:** Textul arată ciudat — poate totul e bold sau mare.
**Regulă:** Fiecare `<tag>` are nevoie de `</tag>`.

### ❌ Greșeala 2: Tag-uri încurcate (overlapping)

```html
<!-- ❌ GREȘIT — se încrucișează -->
<h1>Titlul <p>meu</h1></p>

<!-- ✅ CORECT — se închid în ordine inversă -->
<h1>Titlul meu</h1>
<p>Un paragraf separat</p>
```

**Regulă:** Tag-urile sunt ca niște cutii — o cutie mai mică e complet **în interiorul** cutiei mai mari. Nu se pot suprapune parțial.

```
  ✅ CORECT:               ❌ GREȘIT:
  ┌─── html ───────┐       
  │ ┌─── body ───┐ │       Tag-urile se 
  │ │ ┌── h1 ──┐ │ │       suprapun ca 
  │ │ └────────┘ │ │       niște inele
  │ │ ┌── p ───┐ │ │       înlănțuite
  │ │ └────────┘ │ │       
  │ └────────────┘ │       Nu face asta! 🚫
  └────────────────┘       
```

### ❌ Greșeala 3: Conținut în afara lui `<body>`

```html
<!-- ❌ GREȘIT — textul e în afara body-ului -->
<html>
<head>
    <title>Test</title>
</head>
<p>Acest text e rătăcit!</p>
<body>
    <p>Acest text e ok.</p>
</body>
</html>

<!-- ✅ CORECT — tot conținutul vizibil e în body -->
<html>
<head>
    <title>Test</title>
</head>
<body>
    <p>Acest text e ok.</p>
    <p>Și acesta la fel!</p>
</body>
</html>
```

**Regulă:** Tot ce vrei să fie vizibil pe pagină merge **obligatoriu** în `<body>`.

### ❌ Greșeala 4: Fișierul nu are extensia .html

Dacă salvezi fișierul ca `index.txt` sau doar `index`, browserul nu va ști că e o pagină web. **Numele trebuie să se termine cu `.html`**.

---

## 1.10 Mini-quiz — Verifică ce ai învățat! ✅

Răspunde la aceste întrebări (răspunsurile sunt mai jos, dar încearcă singur mai întâi!):

**1.** Ce rol are serverul în „sistemul poștal" al internetului?

**2.** Care sunt cele trei limbaje principale folosite pentru a crea pagini web?

**3.** Care limbaj se ocupă de **structură** (ce există pe pagină)?

**4.** Care limbaj se ocupă de **stil** (cum arată)?

**5.** Ce conținut din HTML este vizibil pe pagină — ce e în `<head>` sau ce e în `<body>`?

**6.** De ce se numește fișierul principal `index.html`?

**7.** Ce se întâmplă dacă uiți să închizi un tag HTML?

---

<details>
<summary>🔑 Click aici pentru răspunsuri</summary>

1. Serverul este computerul care **păstrează fișierele** site-ului web și le trimite browserului când acesta le cere (ca un oficiu poștal).

2. **HTML**, **CSS** și **JavaScript**.

3. **HTML** — definește structura: titluri, paragrafe, imagini, butoane etc.

4. **CSS** — definește stilul: culori, fonturi, mărimi, poziții.

5. Ce e în **`<body>`** — conținutul din `<head>` nu este vizibil pe pagină (doar informații pentru browser, ca titlul din tab).

6. Pentru că serverele web caută automat un fișier numit `index.html` — este „ușa de intrare" a site-ului.

7. Browserul se poate confuza și pagina poate arăta ciudat — texte prea mari, formatare greșită etc.

</details>

---

## 1.11 Știai că? — Curiozități din lumea tech 🤓

🌐 **Prima pagină web din lume** a fost creată în 1991 de Tim Berners-Lee, un cercetător britanic de la CERN (laboratorul de fizică din Elveția). Pagina încă există online! Era foarte simplă — doar text și linkuri, fără imagini sau culori.

📱 **Câte site-uri web există?** Peste **1,9 miliarde** de site-uri sunt înregistrate, dar doar aproximativ 400 de milioane sunt active. Asta înseamnă că peste un miliard de site-uri sunt „abandonate" — ca niște case goale pe internet.

👶 **Cel mai tânăr programator** certificat avea doar 6 ani! Se numește Kautilya Katariya și era din Marea Britanie. Deci la vârsta ta, ești la momentul perfect pentru a începe.

⚡ **Viteza internetului:** Când apeși Enter pe o adresă web, semnalul poate călători cu aproape viteza luminii prin cablurile de fibră optică. O pagină web poate face ocolul Pământului în doar 0,1 secunde!

---

## Recapitulare — Ce ai învățat în Capitolul 1

Hai să facem un inventar:

```
  ✅ Ce este internetul (sistemul poștal digital)
  ✅ Rolul serverului, browserului și al cablurilor
  ✅ HTML = structura, CSS = stilul, JavaScript = interactivitate
  ✅ Ai instalat VS Code (editorul de cod)
  ✅ Ai instalat extensii utile (Live Server, Prettier)
  ✅ Ai creat prima ta pagină web! 🎉
  ✅ Înțelegi structura de bază: DOCTYPE, html, head, body
  ✅ Știi să folosești <h1>-<h6> și <p>
  ✅ Cunoști greșelile frecvente și cum să le eviți
```

---

## Ce urmează?

În **Capitolul 2: Construiește cu HTML — Scheletul paginii**, vei învăța mult mai multe tag-uri: liste, imagini, linkuri, tabele și altele. Vei putea să construiești pagini web mult mai interesante!

Dar mai întâi, ia o pauză bine meritată. Ai făcut un pas important astăzi. 🚀

---

> *„Fiecare expert a fost cândva un începător."*
> — Helen Hayes
