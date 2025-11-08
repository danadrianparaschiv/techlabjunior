# Capitolul 4: CHATBOT

*Nano, robotul drăguț, adoră să vorbească. El va răspunde la răspunsurile tale, și chiar va sări în sus și în jos dacă îl rogi!*

---

## Creează un prieten robot vorbăreț!

Pentru acest proiect, vei crea propriul tău robot vorbitor care răspunde la ceea ce scrii. De asemenea, îi vom schimba expresia alternând între diferite costume. Vom folosi comenzi `ask` (întreabă), blocuri `if/else` (dacă/altfel), și operatorul `join` (îmbină). Vom crea și o variabilă pentru a stoca numele utilizatorului – variabilele sunt foarte utile pentru a reține informații pe care le folosim mai târziu.

Suficient cu vorbăria – hai să pornim un proiect nou Scratch și să începem!

---

## 📥 **DESCARCĂ SPRITE-URILE**

Sprite-urile pentru acest proiect nu sunt în biblioteca Scratch 1.4, dar le poți descărca de la:
**magpi.cc/scratch_art**

---

## **PASUL 01: Pregătește-ți grafica**

După ce ștergi pisica (click dreapta și selectează Delete), e timpul să imporți un nou fundal pentru scenă și sprite-ul personajului nostru.

### **Schimbă fundalul:**
1. Apasă pe **Stage** în Lista de Sprite-uri (colț dreapta jos)
2. Selectează fila **Backgrounds** (sus la mijloc)
3. Apasă pe **Import** și navighează la folderul unde ai salvat grafica descărcată pentru acest proiect
4. Selectează fundalul dorit

### **Importă sprite-ul Nano:**
1. Apasă pe iconița stea/folder deasupra Listei de Sprite-uri
2. Navighează la același folder și importă sprite-ul **Nano**

**Observă costumele:** Dacă apeși pe fila Costumes, vei vedea că Nano are patru costume diferite. Le vom alterna pentru a-l anima pe micul nostru prieten robot!

---

## **PASUL 02: Cere un nume**

Mai întâi, vom face robotul nostru să ceară numele utilizatorului și apoi să îl folosească într-un răspuns.

Cu sprite-ul Nano selectat, apasă pe fila **Scripts** (sus la mijloc) și adaugă următorul cod:

### **Creează o variabilă pentru nume:**

1. Selectează **Variables** din partea stângă sus
2. Apasă pe **'Make a variable'** (Creează o variabilă)
3. Alege **'For this sprite only'** (Doar pentru acest sprite)
4. Introdu **'name'** (nume) în câmpul text
5. **Dezactivează** căsuța de lângă blocul name pentru a-l ascunde de pe scenă

### **Scriptul pentru a întreba numele:**

```scratch
when Nano clicked
switch costume to [nano-b]
ask [What's your name?] and wait
set [name] to (answer)
say (join [Hi ] (name)) for (2) secs
```

**Ce face acest cod:**

1. **Când Nano este apăsat cu mouse-ul:**
   - Schimbă costumul la nano-b
   - Întreabă "Care este numele tău?" și așteaptă răspunsul utilizatorului

2. **Stochează și folosește numele:**
   - Setează variabila `name` la `answer` (răspunsul utilizatorului)
   - Spune "Salut [numele]" timp de 2 secunde

**IMPORTANT:** Blocul `join` (îmbină) din Operatori este folosit pentru a combina "Hi " cu numele. Asigură-te că pui un spațiu după "Hi" pentru a evita să fie lipite împreună!

---

## **PASUL 03: Adaugă o întrebare**

Acum, vom adăuga mai multe blocuri în partea de jos a acestui script:

```scratch
ask (join [Are you OK ] (name)) and wait
if <(answer) = [yes]>
    switch costume to [nano-c]
    say [That's great to hear!] for (2) secs
else
    switch costume to [nano-d]
    say [Oh no!] for (2) secs
```

**Ce face acest cod:**

1. **Întreabă dacă utilizatorul e bine:**
   - Folosește din nou blocul `ask` (Sensing)
   - Folosește variabila `name` pentru a se adresa utilizatorului pe nume
   - "Ești bine [nume]?"

2. **Răspunde diferit în funcție de răspuns:**
   - Folosește un bloc `if...else` (Control) pentru a decide răspunsul lui Nano bazat pe ce scrie utilizatorul
   - **Dacă răspunsul e 'yes'** (folosim operatorul `=` pentru a testa):
     - Schimbă costumul lui Nano la nano-c (fericit)
     - Spune "That's great to hear!" (Mă bucur să aud asta!)
   - **Altfel (în partea else):**
     - Schimbă costumul lui Nano la nano-d (supărat)
     - Spune "Oh no!" (Oh nu!)

---

## **PASUL 04: Altfel aceasta...**

În partea `else` a blocului `if...else`, determinăm ce se întâmplă dacă input-ul utilizatorului nu este 'yes'.

În acest caz:
- Schimbăm costumul lui Nano la nano-d care se încruntă
- Îl facem să spună 'Oh no!'

**Testează codul cu diferite input-uri** pentru a verifica că funcționează cum te aștepți.

**NOTĂ IMPORTANTĂ:** În timp ce input-ul text al utilizatorului nu este sensibil la majuscule/minuscule, trebuie să fie exact 'yes', fără nimic adăugat, pentru a fi recunoscut ca atare.

---

## **PASUL 05: Sări în sus și în jos**

În final, vom adăuga o altă întrebare folosind `ask`, folosind un bloc standard `if` pentru a face Nano să sară în sus și în jos sau nu:

```scratch
ask [Would like to see me jump?] and wait
if <(answer) = [yes]>
    switch costume to [nano-c]
    repeat (4)
        change y by (10)
        wait (0.1) secs
        change y by (-10)
        wait (0.1) secs
```

**Ce face acest cod:**

1. **Întreabă despre sărit:**
   - "Ai vrea să mă vezi sărind?"

2. **Dacă răspunsul e 'yes':**
   - Schimbă la costumul nano-c (să nu fie încruntat în timp ce sare!)
   - Folosește o buclă `repeat` pentru a face Nano să se miște repetat în sus și în jos pentru o animație de săritură:
     - Mută în sus cu 10 (change y by 10)
     - Așteaptă puțin
     - Mută în jos cu 10 (change y by -10)
     - Așteaptă puțin
   - Repetă de 4 ori pentru o săritură completă!

---

## 🎭 **Scriptul complet**

```scratch
when Nano clicked

switch costume to [nano-b]
ask [What's your name?] and wait
set [name] to (answer)
say (join [Hi ] (name)) for (2) secs

ask (join [Are you OK ] (name)) and wait
if <(answer) = [yes]>
    switch costume to [nano-c]
    say [That's great to hear!] for (2) secs
else
    switch costume to [nano-d]
    say [Oh no!] for (2) secs

ask [Would like to see me jump?] and wait
if <(answer) = [yes]>
    switch costume to [nano-c]
    repeat (4)
        change y by (10)
        wait (0.1) secs
        change y by (-10)
        wait (0.1) secs
```

---

## **PASUL 06: Mergi mai departe!**

Poți modifica întrebările din exemplu sau să adaugi orice întrebări suplimentare dorești, chiar poți face Nano să spună o glumă!

**Idei pentru îmbunătățiri:**

1. **Adaugă mai multe întrebări:**
   - "Care este culoarea ta preferată?"
   - "Ce îți place să faci?"
   - "Vrei să auzi o glumă?"

2. **Creează mai multe costume:**
   Poți adăuga costume suplimentare copiindu-le și editându-le în Paint Editor, sau chiar să proiectezi un sprite complet nou cu diverse costume!

3. **Adaugă sunete:**
   Folosește blocuri Sound pentru a face Nano să facă zgomote când vorbește sau sare

4. **Fă-l mai inteligent:**
   Poți adăuga mai multe verificări pentru diferite răspunsuri:
   ```scratch
   if <(answer) = [yes]>
       say [Great!]
   else
       if <(answer) = [no]>
           say [OK, maybe later]
       else
           say [I didn't understand that]
   ```

5. **Creează o conversație mai lungă:**
   Poți face Nano să pună mai multe întrebări care se bazează pe răspunsurile anterioare

---

## 💡 **Ce ai învățat**

În acest capitol ai învățat:

- ✅ Cum să folosești blocul `ask` pentru a obține input de la utilizator
- ✅ Cum să creezi și să folosești variabile pentru a stoca informații
- ✅ Cum să folosești blocul `join` pentru a combina text
- ✅ Cum să folosești blocuri `if...else` pentru a lua decizii
- ✅ Cum să schimbi între costume pentru a anima sprite-uri
- ✅ Cum să creezi animații simple de mișcare
- ✅ Cum să verifici dacă răspunsurile sunt egale cu anumite valori

---

## 🎯 **Provocări**

1. **Fă Nano să pună 5 întrebări diferite**
2. **Creează un costume nou pentru Nano când este surprins**
3. **Fă Nano să danseze dacă îi ceri**
4. **Adaugă un sistem de puncte – dacă utilizatorul răspunde corect la întrebări, primește puncte!**

---

## 🌟 **Sfat de programare**

Când lucrezi cu text în Scratch, amintește-ți:
- `answer` este mereu ultimul răspuns pe care l-a dat utilizatorul
- Variabilele pot stoca text, numere sau orice altceva
- Blocul `join` este perfect pentru a combina bucăți de text
- Testează mereu codul cu diferite input-uri pentru a vedea ce se întâmplă!

**Felicitări!** 🤖 Ai creat propriul ChatBot! Nano este acum gata să vorbească cu toată lumea!

---

## 🎨 **Idee creativă**

De ce nu creezi o familie întreagă de roboți? Fiecare ar putea avea personalitatea sa:
- Un robot timid care vorbește încet
- Un robot vesel care râde mult
- Un robot înțelept care dă sfaturi
- Un robot glumeț care spune glume

**Distrează-te programând!** 🚀
