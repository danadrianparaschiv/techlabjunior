# Capitolul 2: ARICI SĂLTĂREȚ

*Spike ariciul adoră să se joace pe trambulină, dar e un pic stângaci. Poți mișca trambutina la stânga și la dreapta pentru a-l prinde și a-l face să sară?*

---

## Creează primul tău joc!

În acest capitol, vei crea primul tău joc Scratch, în care folosești tastele săgeată pentru a mișca trambutina stânga-dreapta și a prinde o țintă care sare. Acest proiect îți arată cum să aduci sprite-uri și fundaluri noi, și cum să folosești blocurile cu paranteze și blocurile diamant în proiectele tale. Vei găsi aceste abilități utile pe măsură ce construiești celelalte proiecte din această carte.

Pornește un proiect nou Scratch și pregătește-te să sari! Amintește-ți că te poți întoarce la capitolul anterior dacă ai nevoie de ajutor pentru a găsi elementele pe ecran.

---

## **PASUL 01: Pregătește-ți grafica**

Pentru acest proiect Scratch, nu ai nevoie de pisică, așa că dă click dreapta pe ea în Lista de Sprite-uri și apoi alege Delete (Șterge).

Pentru a adăuga un sprite nou, apasă pe iconița deasupra Listei de Sprite-uri care arată un folder și o stea. 

**Adaugă:**
- Sprite-ul **trampoline** din folderul Things
- Sprite-ul **fantasy11** din folderul Fantasy

Hai să schimbăm și fundalul:
1. Apasă pe Scenă în Lista de Sprite-uri
2. Fila Costumes se schimbă într-o filă Backgrounds
3. Apasă pe filă și folosește butonul Import pentru a aduce fundalul ales de tine
4. Noi folosim imaginea **atom-playground** din folderul Outdoors

---

## **PASUL 02: Adaugă controale pentru jucător**

Apasă pe trambulină (care ar trebui să fie Sprite1) în Lista de Sprite-uri pentru a o selecta, apoi apasă pe fila Scripts deasupra Paletei de Blocuri.

**Adaugă aceste scripturi la sprite-ul trambulină:**

```scratch
when [flag] clicked
set size to (20) %
go to x: (0) y: (-120)

when [left arrow] key pressed
change x by (-10)

when [right arrow] key pressed
change x by (10)
```

**Ce face acest cod:**
- Când apeși steagul verde, trambutina devine mică (20% din dimensiunea normală)
- Se poziționează în partea de jos a ecranului (y: -120)
- Când apeși săgeata stânga, trambutina se mișcă cu 10 pași la stânga
- Când apeși săgeata dreapta, trambutina se mișcă cu 10 pași la dreapta

**Testează-ți jocul până acum!** Trambutina ar trebui să se miște când apeși tastele săgeată.

---

## **PASUL 03: Pregătește ariciul**

Apasă pe Sprite2 în Lista de Sprite-uri (ariciul). Adaugă acest script:

```scratch
when [flag] clicked
set size to (40) %
point in direction (15)
go to x: (-200) y: (150)
wait (1) secs
```

**Ce face acest cod:**
- Pune sprite-ul în colțul din stânga sus când jocul începe
- Îi dă jucătorului o șansă să vadă unde este ariciul înainte să se miște

---

## **PASUL 04: Adaugă o buclă repeat (repetă până când)**

Vom extinde acel script acum adăugând mai multe blocuri în partea de jos.

Trage un bloc `repeat until` (repetă până când) în Zona de Scripturi și îmbină-l la scriptul tău de până acum. *(Asigură-te că nu folosești blocul repeat cu un număr în el!)*

Apoi, trebuie să plasezi un bloc `<` (mai mic decât) în găușa în formă de diamant:
1. Apasă pe butonul Operators deasupra Paletei de Blocuri pentru a-l găsi
2. Scrie -120 în căsuța din dreapta
3. Apasă pe butonul Motion și trage blocul `y position` (poziția y) în căsuța din stânga

**Ce face acest bloc:**

Acum, orice vom pune înăuntrul parantezei `repeat until` va fi repetat până când poziția y a sprite-ului (cât de sus sau jos pe ecran este) este mai mică de -120. În jocul nostru, asta înseamnă că a ratat trambutina și a lovit podeaua!

---

## **PASUL 05: Fă ariciul să se miște**

Pentru a face sprite-ul să se miște, adaugă aceste două blocuri Motion înăuntrul blocului `repeat until` din scriptul tău:

```scratch
repeat until <(y position) < (-120)>
    move (6) steps
    if on edge, bounce
```

Apasă pe steagul verde deasupra Scenei pentru a testa până aici. Ar trebui să vezi ariciul mergând în colțul din stânga sus, căzând în jos și oprind-se când ajunge jos.

---

## **PASUL 06: Fă trambutina elastică!**

Trebuie să facem ariciul să sară înapoi în sus dacă atinge trambutina.

Apasă pe butonul Control și trage un bloc `if` (dacă) în scriptul tău. **Atenție unde îl pui:** el aparține înăuntrul parantezei tale `repeat until`!

```scratch
repeat until <(y position) < (-120)>
    move (6) steps
    if on edge, bounce
    if <touching [Sprite1]?>
        point in direction (pick random (-45) to (45))
```

**Ce face acest cod:**

Apasă pe butonul Sensing și trage un bloc `touching` (atinge) pentru găușa în formă de diamant din blocul tău `if`. Apasă pe meniul din blocul touching pentru a alege Sprite1 (trambutina).

Înăuntrul parantezei blocului tău `if`, pune un bloc Motion `point in direction 90`. În loc să pui un număr în găușa lui, de data aceasta vom folosi `pick random` (alege aleatoriu) cu valori de -45 și 45. Îl vei găsi în secțiunea Operators din Paleta de Blocuri.

Acum sprite-ul va pointa într-o direcție aleatorie în sus (între 45 de grade la stânga și 45 de grade la dreapta) dacă atinge trambutina.

În final, adaugă un bloc `say` la sfârșitul scriptului tău, în afara tuturor parantezelor. Acesta este afișat când jocul se termină:

```scratch
say [Ouch!] for (2) secs
```

---

## 🎮 **Scripturile complete**

### Script pentru Trambulină (Sprite1):
```scratch
when [flag] clicked
set size to (20) %
go to x: (0) y: (-120)

when [left arrow] key pressed
change x by (-10)

when [right arrow] key pressed  
change x by (10)
```

### Script pentru Arici (Sprite2):
```scratch
when [flag] clicked
set size to (40) %
point in direction (15)
go to x: (-200) y: (150)
wait (1) secs
repeat until <(y position) < (-120)>
    move (6) steps
    if on edge, bounce
    if <touching [Sprite1]?>
        point in direction (pick random (-45) to (45))
say [Ouch!] for (2) secs
```

---

## 🎯 **Testează jocul!**

1. Apasă steagul verde pentru a porni jocul
2. Folosește tastele săgeată stânga și dreapta pentru a mișca trambutina
3. Încearcă să prinzi ariciul când cade!
4. Dacă reușești, el va sări înapoi în sus
5. Dacă îl ratezi, el va spune "Ouch!" și jocul se termină

---

## 🌟 **Fă jocul mai interesant!**

Iată câteva idei pentru a-ți îmbunătăți jocul:

1. **Schimbă viteza:** Modifică numărul din blocul `move 6 steps` pentru a face ariciul să cadă mai repede sau mai încet

2. **Adaugă sunete:** Folosește blocuri Sound pentru a adăuga efecte sonore când ariciul sare sau când cade

3. **Ține scorul:** Creează o variabilă numită "scor" și mărește-o de fiecare dată când prinzi ariciul

4. **Adaugă mai multe sprite-uri:** Poate ariciul să aibă prieteni care cad și ei?

5. **Schimbă dificultatea:** Fă trambutina mai mică sau ariciul să cadă mai repede pe măsură ce jocul avansează

---

## 💡 **Ce ai învățat**

În acest capitol ai învățat:

- ✅ Cum să adaugi și să ștergi sprite-uri
- ✅ Cum să schimbi fundalul
- ✅ Cum să folosești tastele săgeată pentru a controla un sprite
- ✅ Cum să folosești blocuri `if` pentru a lua decizii
- ✅ Cum să folosești blocuri `repeat until` pentru a repeta acțiuni
- ✅ Cum să detectezi când sprite-urile se ating
- ✅ Cum să folosești numere aleatorii

**Felicitări!** 🎊 Ai creat primul tău joc Scratch! Continuă să experimentezi și să te distrezi!
