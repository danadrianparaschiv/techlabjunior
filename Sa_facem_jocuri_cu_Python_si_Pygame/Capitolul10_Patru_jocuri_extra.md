# 🎮 Capitolul 10 – Patru Jocuri Extra

> **Din cartea:** *Making Games with Python and Pygame* de Al Sweigart
> **Tradus în română** – într-un stil prietenos, pentru tineri programatori! 🐍

---

## 👋 Despre ce e vorba în acest capitol?

Felicitări că ai ajuns până aici! 🎉

În acest capitol vei găsi **codul sursă** pentru patru jocuri super tari. Nu vom explica fiecare linie de cod în detaliu ca în capitolele anterioare — dar nu te speria! Până acum ai învățat destul de multe lucruri încât poți **să te joci** cu aceste jocuri și **să descoperi singur** cum funcționează codul, citindu-l și urmărind comentariile.

### 🕹️ Cele patru jocuri sunt:

| Joc | Ce fel de joc este? | Descriere scurtă |
|-----|---------------------|-------------------|
| **Flippy** | Un joc de tip „Othello" | Încerci să întorci piesele adversarului (computerul) pe tabla de joc |
| **Ink Spill** | Un joc de tip „Flood It" | Folosește un algoritm special numit *flood fill* (umplere prin inundare) |
| **Four in a Row** | Un joc de tip „Connect Four" | Joci contra computerului — cine pune 4 într-un rând câștigă! |
| **Gemgem** | Un joc de tip „Bejeweled" | Schimbi pietrele prețioase între ele ca să faci rânduri de trei |

> 💡 **Sfat:** Dacă ai întrebări despre codul sursă din această carte, poți trimite un email autorului la adresa **al@inventwithpython.com**.

### 🐛 Vrei să exersezi găsirea de bug-uri?

Există și versiuni **cu bug-uri** ale acestor programe, ca să poți exersa repararea lor — exact ca un adevărat detectiv al codului! 🔍

- 🔗 `http://invpy.com/buggy/flippy`
- 🔗 `http://invpy.com/buggy/inkspill`
- 🔗 `http://invpy.com/buggy/fourinarow`
- 🔗 `http://invpy.com/buggy/gemgem`

---

## 🟤⚪ Flippy — Un joc de tip „Othello"

### Ce este Othello?

**Othello** (cunoscut și sub numele de **Reversi**) este un joc care se joacă pe o tablă de **8 x 8** cu piese care sunt **negre pe o parte** și **albe pe cealaltă**.

La începutul jocului, tabla arată cam așa: sunt două piese albe și două piese negre în centru.

### 🎯 Cum se joacă?

1. Fiecare jucător își pune, pe rând, o piesă nouă de culoarea lui pe tablă.
2. Toate piesele adversarului care se află **între** piesa ta nouă și o altă piesă a ta se **întorc** și devin de culoarea ta! 🔄
3. Scopul jocului este să ai **cât mai multe piese** de culoarea ta pe tablă.

### 📖 Un exemplu pas cu pas

Imaginează-ți că jucătorul cu piese **albe** pune o piesă nouă pe poziția 5, 6:

- Piesa neagră de la poziția 5, 5 se află între piesa albă nouă și piesa albă existentă de la 5, 4.
- Aceasta se **întoarce** și devine albă! ✨

Apoi jucătorul cu piese **negre** face o mutare similară: pune o piesă neagră pe 4, 6, ceea ce întoarce piesa albă de la 4, 5.

Piesele se pot întoarce **în toate direcțiile** — sus, jos, stânga, dreapta și chiar pe diagonală — atâta timp cât sunt prinse între piesa nouă și una existentă de aceeași culoare.

### ⚠️ Reguli importante

- Jucătorii **trebuie** să facă întotdeauna o mutare care capturează cel puțin o piesă.
- Jocul se termină când un jucător **nu mai poate face nicio mutare** sau când tabla este **complet plină**.
- Câștigă cel care are **cele mai multe piese** de culoarea sa!

> 📚 Poți afla mai multe despre Reversi pe Wikipedia: `http://en.wikipedia.org/wiki/Reversi`

> 📖 O versiune text a acestui joc (care folosește `print()` și `input()` în loc de Pygame) apare în **Capitolul 15** din *„Invent Your Own Computer Games with Python"*. Acolo poți citi cum funcționează algoritmul **inteligenței artificiale** (AI) al computerului.

### 🤖 Cât de deștept este computerul?

Computerul este **foarte bun** la acest joc! De ce? Pentru că poate simula (adică „se gândește la") **fiecare mutare posibilă** și o alege pe cea care întoarce cele mai multe piese. De obicei, computerul mă bate pe mine când joc! 😅

### 💻 Codul sursă pentru Flippy

Poți descărca codul sursă de la: `http://invpy.com/flippy.py`

Imaginile folosite de Flippy pot fi descărcate de la: `http://invpy.com/flippyimages.zip`

<details>
<summary>🔽 Click aici pentru a vedea codul sursă complet al jocului Flippy</summary>

> ⚠️ **Notă:** Codul sursă este în limba engleză, deoarece limbajele de programare folosesc cuvinte în engleză. Nu te îngrijora — comentariile te vor ajuta să înțelegi ce face fiecare bucată de cod!

```python
# Flippy (un joc de tip Othello sau Reversi)
# De Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Lansat sub licența "Simplified BSD"

# Bazat pe codul "reversi.py" din cartea
# "Invent Your Own Computer Games with Python", capitolul 15:
# http://inventwithpython.com/chapter15.html

import random, sys, pygame, time, copy
from pygame.locals import *

FPS = 10                # cadre pe secundă pentru actualizarea ecranului
WINDOWWIDTH = 640       # lățimea ferestrei în pixeli
WINDOWHEIGHT = 480      # înălțimea ferestrei în pixeli
SPACESIZE = 50          # dimensiunea fiecărui pătrat de pe tablă
BOARDWIDTH = 8          # câte coloane are tabla
BOARDHEIGHT = 8         # câte rânduri are tabla
WHITE_TILE = 'WHITE_TILE'
BLACK_TILE = 'BLACK_TILE'
EMPTY_SPACE = 'EMPTY_SPACE'
HINT_TILE = 'HINT_TILE'
ANIMATIONSPEED = 25     # viteză animație (1-100, mai mare = mai rapid)

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * SPACESIZE)) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * SPACESIZE)) / 2)

#              R    G    B
WHITE      = (255, 255, 255)
BLACK      = (  0,   0,   0)
GREEN      = (  0, 155,   0)
BRIGHTBLUE = (  0,  50, 255)
BROWN      = (174,  94,   0)

TEXTBGCOLOR1 = BRIGHTBLUE
TEXTBGCOLOR2 = GREEN
GRIDLINECOLOR = BLACK
TEXTCOLOR = WHITE
HINTCOLOR = BROWN
```

> 💡 **Ce observi aici?** Primele linii definesc **constante** — adică numere și culori care nu se schimbă niciodată pe parcursul jocului. E ca și cum ai spune: „Tabla mea are mereu 8 coloane și 8 rânduri."

*(Codul complet al jocului are sute de linii. Poți descărca versiunea completă de la linkul de mai sus!)*

</details>

---

## 🎨 Ink Spill — Un joc de tip „Flood It"

### Ce este „Flood It"?

**„Flood It"** este un joc care începe cu o tablă plină de **piese colorate** (diferite culori amestecate peste tot).

### 🎯 Cum se joacă?

1. La fiecare tură, alegi o **culoare nouă**.
2. Piesa din **colțul din stânga-sus** și toate piesele vecine care au aceeași culoare cu ea se **vopsesc** în culoarea aleasă de tine. 🖌️
3. Acest lucru funcționează folosind un algoritm magic numit **flood fill** (umplere prin inundare) — despre care am vorbit și în capitolul despre *Star Pusher*.
4. Scopul: să transformi **toată tabla** într-o singură culoare **înainte de a rămâne fără ture**! ⏰

### ⚙️ Setări personalizabile

Jocul are și un **ecran de setări** unde poți:

- Schimba **dimensiunea tablei** (mai mică = mai ușor, mai mare = mai greu)
- Schimba **dificultatea** jocului
- Alege **alte scheme de culori** dacă te-ai plictisit de culorile inițiale 🌈

### 💻 Codul sursă pentru Ink Spill

Poți descărca codul sursă de la: `http://invpy.com/inkspill.py`

Imaginile folosite de Ink Spill pot fi descărcate de la: `http://invpy.com/inkspillimages.zip`

---

## 🔴🟡 Four-In-A-Row — Un joc de tip „Connect Four"

### Ce este „Connect Four"?

**„Connect Four"** se joacă pe o tablă de **7 coloane x 6 rânduri**. Jucătorii **aruncă pe rând jetoane** (piese rotunde) din partea de sus a unei coloane. Jetonul **cade** până jos, oprindu-se pe fundul tablei sau deasupra ultimului jeton din acea coloană — exact ca în viața reală, datorită gravitației! 🪂

### 🎯 Cum câștigi?

Câștigi când reușești să pui **patru jetoane de-ale tale într-un rând** — fie pe orizontală ↔️, fie pe verticală ↕️, fie pe diagonală ↗️!

### 🧠 Cât de deștept este computerul?

AI-ul (inteligența artificială) pentru acest joc este **foarte inteligent**. Iată ce face:

1. Se gândește la **fiecare mutare posibilă** pe care o poate face.
2. Apoi se gândește la **fiecare mutare** pe care ai putea-o face **tu** ca răspuns.
3. Apoi se gândește la ce ar putea face **el** ca răspuns la mutarea ta.
4. Și apoi se gândește din nou la ce ai putea face **tu**!

Wow, asta e multă gândire! 🤯

### 📊 Câte mutări analizează?

Deoarece la fiecare tură poți face una dintre **7 mutări posibile** (una pentru fiecare coloană, dacă nu e plină), iar adversarul poate și el 7, iar tu alte 7, iar el alte 7... computerul analizează:

> **7 × 7 × 7 × 7 = 2.401 de mutări posibile!**

Asta e **foarte mult**! De aceea computerul este destul de greu de bătut. 💪

### ⚙️ Reglarea dificultății

Poți schimba cât de greu joacă computerul modificând constanta `DIFFICULTY` din cod:

| Valoare `DIFFICULTY` | Ce se întâmplă |
|:----:|------|
| **0** | Computerul face **mutări complet aleatoare** — e foarte ușor de bătut! 😄 |
| **1** | Computerul se gândește doar la mutarea lui și la răspunsul tău — nivel mediu |
| **2** | Computerul gândește **patru pași înainte** — greu de bătut! 😤 |
| **mai mult de 2** | Și mai greu, dar computerul va avea nevoie de **mult timp** să se gândească |

### 💻 Codul sursă pentru Four-In-A-Row

Poți descărca codul sursă de la: `http://invpy.com/fourinarow.py`

Imaginile folosite pot fi descărcate de la: `http://invpy.com/fourinarowimages.zip`

---

## 💎 Gemgem — Un joc de tip „Bejeweled"

### Ce este „Bejeweled"?

**„Bejeweled"** este un joc în care **pietrele prețioase** (gems) cad de sus și umplu o tablă.

### 🎯 Cum se joacă?

1. Poți **schimba** două pietre prețioase vecine între ele.
2. Scopul este să faci **rânduri de trei (sau mai multe) pietre identice** — pe orizontală sau pe verticală (nu pe diagonală).
3. Când faci un rând de pietre potrivite, ele **dispar** ✨ și pietre noi cad de sus pentru a le înlocui.
4. Dacă potrivești **mai mult de trei** pietre odată, sau dacă provoci o **reacție în lanț** (mai multe combinații una după alta), primești **mai multe puncte**! 🏆

### ⏰ Atenție la timp!

Scorul tău **scade încet** în timp, așa că trebuie să faci potriviri **tot timpul** — nu sta pe gânduri prea mult!

### 🏁 Când se termină jocul?

Jocul se termină când pe tablă **nu mai există nicio combinație posibilă**. Atunci e momentul să verifici ce scor ai reușit să strângi!

### 💻 Codul sursă pentru Gemgem

Poți descărca codul sursă de la: `http://invpy.com/gemgem.py`

Imaginile folosite de Gemgem pot fi descărcate de la: `http://invpy.com/gemgemimages.zip`

---

## 🌟 Rezumat

Sper că aceste jocuri ți-au dat **idei proprii** despre ce jocuri ai vrea să creezi și cum ai putea scrie codul pentru ele! 💡

Chiar dacă nu ai încă o idee originală, este o **practică excelentă** să încerci să programezi copii ale jocurilor la care te-ai jucat deja. Ia-ți un joc favorit și gândește-te: „Cum aș putea face asta cu Python și Pygame?" 🤔

### 📚 Site-uri utile pentru a învăța mai departe

Iată câteva locuri minunate unde poți continua să înveți programare:

| Site | Ce găsești acolo |
|------|------------------|
| **[pygame.org](http://pygame.org)** | Site-ul oficial Pygame — are codul sursă pentru **sute de jocuri** făcute de alți oameni! Poți învăța o grămadă citind codul altora. |
| **[python.org/doc](http://python.org/doc)** | Mai multe tutoriale Python și documentația pentru toate modulele și funcțiile Python. |
| **[pygame.org/docs](http://pygame.org/docs)** | Documentația completă pentru toate modulele și funcțiile Pygame. |
| **[reddit.com/r/learnpython](http://reddit.com/r/learnpython)** | O comunitate unde poți pune întrebări și găsi resurse pentru a învăța Python. |
| **[reddit.com/r/learnprogramming](http://reddit.com/r/learnprogramming)** | O comunitate utilă pentru a învăța programare în general. |
| **[inventwithpython.com/pygame](http://inventwithpython.com/pygame)** | Site-ul acestei cărți — include tot codul sursă și fișierele cu imagini și sunete. |
| **[inventwithpython.com](http://inventwithpython.com)** | Site-ul cărții *„Invent Your Own Computer Games with Python"* — acoperă bazele programării Python. |
| **[invpy.com/wiki](http://invpy.com/wiki)** | Un wiki cu concepte individuale de programare Python pe care le poți căuta oricând. |
| **[invpy.com/traces](http://invpy.com/traces)** | O aplicație web care te ajută să urmărești execuția programelor **pas cu pas**. Super util! |
| **[invpy.com/videos](http://invpy.com/videos)** | Videoclipuri care însoțesc programele din această carte. |
| **[gamedevlessons.com](http://gamedevlessons.com)** | Un site util despre cum să proiectezi și să programezi jocuri video. |

> 📧 Poți trimite întrebări autorului la: **al@inventwithpython.com**

Sau poți căuta pe internet expresii precum **„Python programming"** sau **„Python tutorials"** pentru a găsi și mai multe resurse.

---

## 🚀 Acum e rândul tău!

Acum ai toate cunoștințele de care ai nevoie. Du-te și **inventează-ți propriile jocuri**! 🎮

Și mult noroc! 🍀

---

> *Traducere realizată din cartea „Making Games with Python and Pygame" de Al Sweigart.*
> *Stilul a fost adaptat pentru a fi prietenos și accesibil tinerilor programatori.* 🐍✨
