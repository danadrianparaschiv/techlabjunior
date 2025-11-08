# Capitolul 3: PIERDUT ÎN SPAȚIU

*Programează propria ta animație a unei nave spațiale care se îndreaptă spre Pământ, folosind un efect de scalare pentru a face nava mai mică pe măsură ce se îndepărtează*

---

## Creează o animație spațială!

În acest capitol, vei crea o secvență de animație care, poate neașteptat, implică o maimuță spațială care se rotește! Acest proiect îți va arăta cum să miști, să rotești și să scalezi (să schimbi dimensiunea) sprite-urilor. Acestea sunt lucruri care îți vor fi foarte utile și pentru alte proiecte și jocuri.

Așa că pornește un proiect nou Scratch și pregătește-te să faci animație! Dacă ai nevoie de ajutor pentru a naviga prin meniurile Scratch, uită-te înapoi la capitolul 1.

---

## 📥 **DESCARCĂ SPRITE-URILE**

Sprite-urile folosite în acest proiect nu sunt în biblioteca Scratch 1.4, dar le poți descărca de la:
**magpi.cc/scratch_art**

---

## **PASUL 01: Pregătește-ți grafica**

După ce ștergi pisica (click dreapta și Delete), e timpul să imporți un nou fundal pentru scenă și sprite-uri.

### **Schimbă fundalul în stele:**
1. Apasă pe **Stage** în Lista de Sprite-uri (colț dreapta jos)
2. Selectează fila **Backgrounds** (sus la mijloc)
3. Apasă pe **Import** și navighează la **'stars'** în folderul Nature

### **Importă sprite-urile:**

Pentru că niciunul dintre sprite-urile folosite în acest proiect nu este în biblioteca Scratch 1.4, le poți descărca de la linkul de mai sus.

**Pentru fiecare sprite:**
1. Apasă pe iconița stea/folder deasupra Listei de Sprite-uri
2. Navighează la folderul unde ai salvat sprite-urile descărcate
3. Importă sprite-urile: **Earth** (Pământ), **Spaceship** (Navă spațială), **Monkey** (Maimuță), **Star** (Stea), **Rock** (Stâncă)

---

## **PASUL 02: Mișcă nava spațială**

Apasă pe sprite-ul Spaceship în Lista de Sprite-uri pentru a-l selecta, apoi apasă pe fila Scripts.

**Adaugă acest script pentru a face nava să se miște:**

```scratch
when [flag] clicked
set size to (100) %
clear graphic effects
point in direction (0)
go to x: (-150) y: (-150)
wait (1) secs
point towards [Earth]
repeat (200)
    move (2) steps
```

**Ce face acest cod:**

1. **Pornește nava:**
   - O face dimensiune normală (100%)
   - Îndreaptă nava în sus (direcția 0)
   - O plasează în colțul din stânga jos (x: -150, y: -150)

2. **Așteaptă și apoi:**
   - Așteaptă 1 secundă (ca jucătorul să vadă unde e nava)
   - Folosește blocul foarte util `point towards` (îndreptă-te spre) pentru a pointa spre sprite-ul Earth

3. **Se mișcă:**
   - Folosește o buclă `repeat` pentru a continua să miște nava spre Pământ, 2 pași de fiecare dată

**Testează-ți codul până acum!** Nava ar trebui să decoleze vertical și apoi să se întoarcă spre Pământ.

---

## **PASUL 03: Scalează nava**

Pentru a simula nava mișcându-se mai departe de noi, trebuie să reducem treptat dimensiunea ei pe măsură ce se mișcă spre Pământ. 

Acest lucru se realizează ușor adăugând un singur bloc suplimentar la scriptul existent:

```scratch
repeat (200)
    move (2) steps
    change size by (-0.5)
```

**Ce face acest bloc:**

Apasă pe butonul **Looks** în stânga sus și apoi trage un bloc `change size by` și plasează-l chiar sub blocul tău `move 2 steps`, înăuntrul buclei repeat.

Schimbă 10-ul din blocul `change size` la **-0.5**

Acum, încearcă să apeși steagul verde pentru a vedea nava ta spațială zburând spre Pământ, devenind mai mică tot timpul!

---

## **PASUL 04: Adaugă o maimuță spațială**

Acum hai să adăugăm câteva caracteristici suplimentare scenei noastre spațiale. Pentru puțină distracție, vom adăuga o maimuță care plutește, pierdută în spațiu.

1. Apasă din nou pe iconița stea/folder și navighează la folderul tău Lost in Space sprites
2. Selectează **Monkey**

Ca și cu orice sprite, poți ajusta dimensiunea folosind iconițele Grow/Shrink sprite (Mărește/Micșorează sprite) deasupra scenei.

### **Dă-i maimuței o cască spațială!**

1. Selecteaz-o în Lista de Sprite-uri
2. Apasă pe fila **Costumes** și butonul **Edit**
3. În Paint Editor:
   - Selectează instrumentul **Ellipse** (Elipsă)
   - Selectează opțiunea **outline** (contur) de jos
   - Alege o culoare galbenă din paletă
   - Desenează o elipsă galbenă în jurul capului maimuței pentru cască!

### **Fă maimuța să se rotească:**

```scratch
when [flag] clicked
forever
    turn (1) degrees
```

**Ce face acest cod:**

Adaugă acest script simplu în buclă pentru a face maimuța să se învârtă mereu!

---

## **PASUL 05: Adaugă strălucire și sărituri**

În final, vom adăuga o stea strălucitoare și o stâncă care sare. Importă-le pe ambele din folderul tău Lost In Space sprites, apoi poziționează-le și scalează-le pe scenă cum îți place.

### **Pentru Stea - efect de strălucire:**

```scratch
when [flag] clicked
forever
    repeat (20)
        change size by (2)
    repeat (20)
        change size by (-2)
```

**Ce face:** Două bucle `repeat` într-o buclă `forever` pentru a scala repetat steaua în sus și în jos, creând un efect de sclipire!

### **Pentru Stâncă - să sară prin spațiu:**

```scratch  
when [flag] clicked
point towards [Earth]
forever
    move (2) steps
    if on edge, bounce
```

**Ce face:** Adaugă acest cod stâncii pentru a o pune în mișcare, incluzând un bloc special (ca în capitolul 2) pentru a o face să sară înapoi ori de câte ori ajunge la marginea scenei.

---

## 🎬 **Scripturile complete**

### Navă Spațială:
```scratch
when [flag] clicked
set size to (100) %
clear graphic effects
point in direction (0)
go to x: (-150) y: (-150)
wait (1) secs
point towards [Earth]
repeat (200)
    move (2) steps
    change size by (-0.5)
```

### Maimuță:
```scratch
when [flag] clicked
forever
    turn (1) degrees
```

### Stea:
```scratch
when [flag] clicked
forever
    repeat (20)
        change size by (2)
    repeat (20)
        change size by (-2)
```

### Stâncă:
```scratch
when [flag] clicked
point towards [Earth]
forever
    move (2) steps
    if on edge, bounce
```

---

## **PASUL 06: Mergi mai departe!**

Animația ta ar trebui să arate destul de tare acum! Încearcă să te joci cu diferiți parametri pentru a vedea cum afectează viteza, mișcarea și scalarea obiectelor.

**Idei suplimentare:**

1. **Efecte de lumină disco:** 
   Poți adăuga și tu atingerea ta proprie, cum ar fi folosirea unui bloc `change color effect` pentru a da navei spațiale un efect de lumină disco fancy pe măsură ce se mișcă!

2. **Adaugă mai multe stele:** 
   Creează mai multe sprite-uri stea care sclipesc la viteze diferite

3. **Fă steaguri sau pancarte:**
   Maimuța ar putea ține o pancartă sau un steag

4. **Adaugă sunete:**
   Găsește sunete de navă spațială sau sunete spațiale pentru a face animația și mai captivantă

5. **Schimbă direcția:**
   În loc să meargă spre Pământ, poate nava să zboare în jurul planetei?

---

## 💡 **Ce ai învățat**

În acest capitol ai învățat:

- ✅ Cum să scalezi (să schimbi dimensiunea) sprite-urilor
- ✅ Cum să folosești blocul `point towards` pentru a întoarce un sprite spre altul
- ✅ Cum să creezi efecte de animație folosind bucle
- ✅ Cum să desenezi în Paint Editor pentru a modifica sprite-urile
- ✅ Cum să combini mai multe sprite-uri pentru a crea o scenă complexă
- ✅ Cum să faci sprite-uri să se rotească și să sară

**Felicitări!** 🚀 Ai creat o animație spațială impresionantă! Continuă să explorezi și să experimentezi!

---

## 🎨 **Provocare suplimentară**

Poți crea propria ta scenă spațială? Gândește-te la:
- Ce alte obiecte ar putea fi în spațiu?
- Cum s-ar putea mișca ele?
- Ce culori și efecte ar face scena ta unică?

**Fii creativ și distrează-te!** 🌟
