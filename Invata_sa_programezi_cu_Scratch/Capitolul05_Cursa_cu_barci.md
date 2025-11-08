# Capitolul 5: CURSĂ CU BĂRCI

*Creează propriul tău joc de curse cu bărci, complet cu control prin mouse, detectare a coliziunilor și cronometru pe ecran*

---

## Creează un joc de curse captivant!

În acest capitol, vei crea propriul tău joc arcade în care jucătorul încearcă să ghideze o barcă în siguranță printr-un traseu în formă de labirint – inclusiv o poartă care se rotește – până la finish, în cel mai scurt timp posibil. Poți chiar să proiectezi propriul tău traseu personalizat dacă vrei!

Pe lângă mișcarea unui sprite către cursorul mouse-ului, acest proiect implică detectarea coliziunilor, folosind blocul Sensing `touching color` (atinge culoare) pentru a determina dacă barca a lovit ceva. 

Hai să ne scufundăm și să începem programarea...

---

## 📥 **DESCARCĂ SPRITE-URILE**

Sprite-urile pentru acest proiect nu sunt în biblioteca Scratch 1.4, dar le poți descărca de la:
**magpi.cc/scratch_art**

---

## **PASUL 01: Pregătește-ți grafica**

Mai întâi, șterge pisica! Apoi ar trebui să imporți cele două sprite-uri, pentru barcă și poartă.

### **Importă sprite-urile:**
1. Apasă pe iconița stea/folder deasupra Listei de Sprite-uri
2. Navighează la folderul unde ai salvat grafica descărcată
3. Importă sprite-urile **Boat** (Barcă) și **Gate** (Poartă)

### **Importă sau creează fundalul traseului:**

**Opțiunea A - Folosește traseul nostru:**
1. Apasă pe **Stage** în Lista de Sprite-uri
2. Selectează fila **Backgrounds**
3. Apasă pe **Import** și navighează la folder
4. Selectează imaginea **Course**

**Opțiunea B - Creează propriul traseu:**
Citește instrucțiunile de la Pasul 02 mai jos!

---

## **PASUL 02: Proiectează un traseu (Opțional)**

Dacă vrei să creezi propriul traseu:

1. Apasă pe **Stage** în Lista de Sprite-uri
2. Apasă pe fila **Backgrounds**
3. Apasă pe **Paint**

### **Instrucțiuni de desenare:**

**1. Umplu fundalul cu apă albastră:**
   - Folosește instrumentul **paint bucket** (găleată cu vopsea)
   - Alege o culoare albastră
   - Umple tot canvasul

**2. Desenează pereții traseului cu maro:**
   - Folosește culoarea **maro** – trebuie să fie **aceeași culoare** ca în sprite-ul Gate!
   - Desenează pereții labirintului tău
   - Fă traseu cât de complicat vrei!

**3. Desenează linia de finish cu galben:**
   - Folosește culoarea **galbenă**
   - Desenează nisip pentru finish

**4. Adaugă săgeți albe pentru boostere de viteză:**
   - Folosește culoarea **albă**
   - Desenează săgeți care vor acționa ca boostere de viteză

---

## **PASUL 03: Fă poarta să se rotească**

Hai să facem sprite-ul Gate să se rotească. Selectează-l în Lista de Sprite-uri și adaugă acest cod simplu:

```scratch
when [flag] clicked
forever
    turn (1) degrees
```

**Ce face:** Poarta se va roti continuu cu 1 grad pe fiecare iterație, creând o barieră care se mișcă!

---

## **PASUL 04: Controlează barca**

Acum vine partea distractivă – să facem barca să se miște! Apasă pe sprite-ul Boat în Lista de Sprite-uri și adaugă acest cod:

```scratch
when [flag] clicked
switch costume to [normal]
point in direction (0)
go to x: (-190) y: (-150)
forever
    if <(distance to [mouse-pointer]) > [5]>
        point towards [mouse-pointer]
        move (1) steps
```

**Ce face acest cod:**

1. **Setare inițială:**
   - Schimbă la costumul 'normal'
   - Pointează în sus (direcție 0)
   - Plasează barca la poziția de start (x: -190, y: -150)

2. **Control cu mouse-ul:**
   - În buclă `forever`, verifică dacă distanța până la cursorul mouse-ului este mai mare de 5
   - Dacă da, pointează barca spre cursor și o mișcă cu 1 pas
   - Acest lucru oprește barca din a se mișca când este foarte aproape de cursor

**Testează codul și ghidează barca!** Momentan, trece direct prin bariere.

---

## **PASUL 05: Fă-o să se ciocnească!**

Avem nevoie de detectare a coliziunilor pentru a verifica dacă barca a lovit un pericol. În interiorul buclei tale `forever`, adaugă acest cod sub codul de control al bărcii:

```scratch
forever
    if <(distance to [mouse-pointer]) > [5]>
        point towards [mouse-pointer]
        move (1) steps
    
    if <touching color [brown]?>
        switch costume to [hit]
        say [Noooooo!] for (1) secs
        switch costume to [normal]
        point in direction (0)
        go to x: (-190) y: (-150)
```

**Ce face acest cod:**

1. **Detectează coliziunea:**
   - Folosește blocul Sensing `touching color` pentru a vedea dacă barca atinge ceva maro
   - Apasă pe pătratul de culoare pentru a obține o unealtă pipetă
   - Apoi apasă pe o parte maro a traseului pentru a selecta culoarea exactă

2. **Când se ciocnește:**
   - Schimbă costumul bărcii (pentru a arăta avariată)
   - Spune "Noooooo!" timp de 1 secundă
   - O plasează înapoi la punctul de start (în costumul normal)

---

## **PASUL 06: Adaugă finish-ul și boosterele**

Hai să adăugăm încă două blocuri `if touching color` la bucla noastră `forever`:

```scratch
if <touching color [yellow]?>
    say [YEAH!] for (1) secs
    stop all

if <touching color [white]?>
    move (3) steps
```

**Ce face acest cod:**

**1. Detectează finish-ul (galben):**
   - Când barca atinge nisipul galben, a câștigat!
   - Spune "YEAH!" și oprește toate scripturile (jocul se termină)

**2. Boostere de viteză (alb):**
   - Când barca atinge o săgeată albă, primește un boost!
   - Se mișcă cu 3 pași în loc de 1 (este mai rapidă temporar)

---

## **PASUL 07: Adaugă un cronometru**

Pentru a face jocul mai captivant, avem nevoie de un cronometru!

### **Creează variabila pentru timp:**
1. Apasă pe **Stage** în Lista de Sprite-uri
2. Du-te la fila **Scripts**
3. În **Variables**, creează o variabilă nouă numită **time** (timp)
4. Asigură-te că este **bifată** pentru a fi vizibilă pe scenă

### **Adaugă scriptul cronometrului:**

```scratch
when [flag] clicked
set [time] to (0)
forever
    wait (0.1) secs
    change [time] by (0.1)
```

**Ce face acest cod:**

- Setează timpul la 0 când jocul începe
- La fiecare 0.1 secunde, crește timpul cu 0.1
- Acest lucru creează un cronometru care numără în sus!

Timpul va fi afișat pe scenă și se va opri când barca ajunge la finish.

---

## 🎮 **Scripturile complete**

### Poartă (Gate):
```scratch
when [flag] clicked
forever
    turn (1) degrees
```

### Barcă (Boat):
```scratch
when [flag] clicked
switch costume to [normal]
point in direction (0)
go to x: (-190) y: (-150)
forever
    if <(distance to [mouse-pointer]) > [5]>
        point towards [mouse-pointer]
        move (1) steps
    
    if <touching color [brown]?>
        switch costume to [hit]
        say [Noooooo!] for (1) secs
        switch costume to [normal]
        point in direction (0)
        go to x: (-190) y: (-150)
    
    if <touching color [yellow]?>
        say [YEAH!] for (1) secs
        stop all
    
    if <touching color [white]?>
        move (3) steps
```

### Scenă (Stage) - Cronometru:
```scratch
when [flag] clicked
set [time] to (0)
forever
    wait (0.1) secs
    change [time] by (0.1)
```

---

## 🎯 **Cum să joci**

1. Apasă steagul verde pentru a începe
2. Mișcă mouse-ul pentru a controla barca
3. Ghidează barca prin traseu, evitând pereții maroni și poarta care se rotește
4. Treci prin săgețile albe pentru boostere de viteză
5. Ajunge la nisipul galben în cel mai scurt timp!
6. Dacă lovești un perete, vei fi trimis înapoi la start!

---

## 🌟 **Mergi mai departe!**

**Îmbunătățiri pe care le poți adăuga:**

1. **Efecte sonore:**
   - Adaugă un sunet când barca se lovește
   - Adaugă muzică de fundal folosind blocuri Sound

2. **Cel mai bun timp:**
   Poți stoca cel(e) mai bun(e) timp(uri) într-o variabilă sau listă:
   ```scratch
   if <(time) < (best time)>
       set [best time] to (time)
   ```

3. **Niveluri de dificultate:**
   - Creează trasee multiple cu diferite grade de dificultate
   - Fă poarta să se rotească mai repede pe niveluri mai grele

4. **Efecte vizuale:**
   - Adaugă un efect de stropi când barca se mișcă
   - Schimbă culoarea bărcii când trece prin boostere

5. **Multipli jucători:**
   - Adaugă o a doua barcă controlată de tastatură
   - Vezi cine termină primul!

6. **Power-ups:**
   - Adaugă sprite-uri pentru power-ups speciale
   - De exemplu: invincibilitate temporară, viteză extra, etc.

---

## 💡 **Ce ai învățat**

În acest capitol ai învățat:

- ✅ Cum să controlezi sprite-uri cu mouse-ul
- ✅ Cum să folosești `touching color` pentru detectarea coliziunilor
- ✅ Cum să creezi și să modifici fundaluri personalizate
- ✅ Cum să folosești variabile pentru cronometrare
- ✅ Cum să creezi diferite zone pe scenă cu funcții diferite
- ✅ Cum să combini mai multe mecanici de joc într-un proiect complet

---

## 🎨 **Sfaturi pentru proiectarea traseului**

Când creezi propriul traseu:

1. **Începe simplu:** Fă mai întâi un traseu ușor pentru a testa
2. **Adaugă varietate:** Combină secțiuni largi cu secțiuni înguste
3. **Testează-l:** Asigură-te că este posibil dar provocator
4. **Folosește culori clare:** Asigură-te că culorile sunt distincte
5. **Adaugă detalii:** Poți adăuga decorațiuni care nu afectează jocul

---

## 🏆 **Provocări**

1. **Creează un traseu cu 3 niveluri de dificultate**
2. **Adaugă 5 boostere de viteză în locuri strategice**
3. **Fă 2 porți rotitoare în loc de una**
4. **Adaugă un sistem de viți (3 lovituri înainte de game over)**
5. **Creează un meniu de start cu butoane pentru a începe jocul**

---

**Felicitări!** 🚤 Ai creat un joc complet de curse cu bărci! Acesta demonstrează multe concepte importante de programare și game design!

**Continuă să experimentezi și să creezi trasee și mai interesante!** 🌊
