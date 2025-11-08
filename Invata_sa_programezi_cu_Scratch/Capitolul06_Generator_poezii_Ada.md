# Capitolul 6: GENERATOR DE POEZII ADA

*Ada Lovelace dezvăluie Motorul Analitic! Acest computer timpuriu arată puțin primitiv, dar poate genera poezii aleatorii*

---

## Creează poezii aleatorii cu Scratch!

În acest capitol, vei crea un generator de poezii care combină aleatoriu cuvinte din liste diferite pentru a crea versuri amuzante și uneori surprinzător de bune! Vei învăța cum să folosești **liste** în Scratch – o abilitate foarte utilă pentru multe tipuri de proiecte.

Ada Lovelace a fost prima programatoare din lume, lucrând cu Charles Babbage la Motorul Analitic în anii 1800. Deși acest computer timpuriu nu a fost niciodată construit complet în timpul vieții lor, ideile lor au fost cu mult înaintea timpului lor!

Hai să creăm ceva de care Ada ar fi mândră!

---

## 📥 **DESCARCĂ SPRITE-URILE**

Sprite-urile pentru acest proiect nu sunt în biblioteca Scratch 1.4, dar le poți descărca de la:
**magpi.cc/scratch_art**

---

## **PASUL 01: Pregătește-ți scena**

După ce ștergi pisica (click dreapta și Delete), importă sprite-urile și fundalul pentru acest proiect.

### **Importă fundalul:**
1. Apasă pe **Stage** în Lista de Sprite-uri
2. Selectează fila **Backgrounds**
3. Apasă pe **Import** și selectează fundalul potrivit pentru proiectul tău
4. Poți folosi orice fundal care arată ca un atelier sau laborator din secolul 19!

### **Importă sprite-ul Ada:**
1. Apasă pe iconița stea/folder deasupra Listei de Sprite-uri
2. Navighează la folderul cu sprite-urile descărcate
3. Importă sprite-ul **Ada Lovelace**

---

## **PASUL 02: Creează listele de cuvinte**

Acum vine partea distractivă – să creăm liste cu cuvinte pe care le vom combina pentru poezii!

### **Cum se creează o listă:**

1. Apasă pe **Variables** în Paleta de Blocuri
2. Apasă pe **Make a List** (Creează o listă)
3. Dă-i un nume listei
4. Alege **For all sprites** (Pentru toate sprite-urile)

### **Creează aceste 4 liste:**

**Lista 1: `verbs` (verbe)**
- dances (dansează)
- sleeps (doarme)
- thinks (gândește)
- laughs (râde)
- codes (programează)
- jumps (sare)
- runs (aleargă)
- sings (cântă)

**Lista 2: `nouns` (substantive)**
- cat (pisică)
- dog (câine)
- computer (computer)
- robot (robot)
- moon (lună)
- star (stea)
- flower (floare)
- tree (copac)

**Lista 3: `adjectives` (adjective)**
- happy (fericit)
- silly (prostănac)
- bright (strălucitor)
- funny (amuzant)
- clever (deștept)
- gentle (blând)
- swift (rapid)
- magical (magic)

**Lista 4: `places` (locuri)**
- in the garden (în grădină)
- on the moon (pe lună)
- under the sea (sub mare)
- in the clouds (în nori)
- by the river (lângă râu)
- in the forest (în pădure)
- on the mountain (pe munte)
- in the city (în oraș)

### **Cum să adaugi cuvinte în liste:**

După ce creezi o listă, aceasta va apărea pe scenă. Vei vedea un **+** la baza listei. Apasă pe el și scrie fiecare cuvânt, apoi apasă Enter!

---

## **PASUL 03: Scriptul pentru generarea poeziilor**

Acum hai să creăm scriptul care va genera poeziile! Selectează sprite-ul Ada și adaugă acest cod:

```scratch
when [space] key pressed
say (join (item (random) of [adjectives]) (join [ ] (item (random) of [nouns]))) for (2) secs
say (join (item (random) of [verbs]) (join [ ] (item (random) of [places]))) for (2) secs
say (join [A ] (join (item (random) of [adjectives]) (join [ ] (join (item (random) of [nouns]) (join [ ] (item (random) of [verbs])))))) for (2) secs
say (join (item (random) of [places]) [!]) for (2) secs
```

**Wow, asta arată complicat!** Hai să-l desfacem pas cu pas...

---

## **PASUL 04: Înțelege cum funcționează**

### **Blocul de bază: `item (random) of [list]`**

Acest bloc alege un element aleatoriu dintr-o listă. De exemplu:
- `item (random) of [nouns]` ar putea returna "cat", "dog", sau "robot"

### **Blocul `join` - îmbină text**

Blocul `join` lipește două bucăți de text împreună:
- `join [happy] [cat]` devine "happycat"
- `join [happy] (join [ ] [cat])` devine "happy cat" (cu spațiu!)

### **Să construim o linie pas cu pas:**

**Linia 1: Un substantiv cu adjectiv**
```
join (item (random) of [adjectives]) 
     (join [ ] 
           (item (random) of [nouns]))
```
Rezultat: "happy cat" sau "silly robot"

**Linia 2: Un verb cu un loc**
```
join (item (random) of [verbs]) 
     (join [ ] 
           (item (random) of [places]))
```
Rezultat: "dances in the garden" sau "sleeps on the moon"

**Linia 3: O propoziție mai lungă**
```
join [A ] 
     (join (item (random) of [adjectives]) 
           (join [ ] 
                 (join (item (random) of [nouns]) 
                       (join [ ] 
                             (item (random) of [verbs])))))
```
Rezultat: "A bright star jumps" sau "A clever dog runs"

**Linia 4: Sfârșitul cu un loc**
```
join (item (random) of [places]) [!]
```
Rezultat: "in the clouds!" sau "under the sea!"

---

## **PASUL 05: Versiunea simplificată (pentru început)**

Dacă construccia de mai sus pare prea complicată, începe cu ceva mai simplu!

```scratch
when [space] key pressed
set [line1] to (join (item (random) of [adjectives]) (join [ ] (item (random) of [nouns])))
set [line2] to (join (item (random) of [verbs]) (join [ ] (item (random) of [places])))

say (line1) for (2) secs
say (line2) for (2) secs
```

Aceasta creează o poezie cu două linii folosind variabile!

---

## **PASUL 06: Fă-o și mai bună!**

### **Adaugă un buton pentru poezie nouă:**

```scratch
when this sprite clicked
clear
say [Click space for a new poem!] for (2) secs
```

### **Adaugă animație:**

```scratch
when [space] key pressed
repeat (3)
    turn (15) degrees
    wait (0.1) secs
    turn (-15) degrees
    wait (0.1) secs
say (join (item (random) of [adjectives]) (join [ ] (item (random) of [nouns]))) for (2) secs
[... restul codului ...]
```

Aceasta face Ada să se legene înainte de a spune poezia!

---

## 🎨 **Idei pentru îmbunătățiri**

1. **Mai multe liste:**
   - Adaugă o listă cu `colors` (culori)
   - Adaugă o listă cu `emotions` (emoții)
   - Adaugă o listă cu `actions` (acțiuni)

2. **Poezii mai lungi:**
   - Creează poezii cu 6, 8 sau chiar 10 linii!
   - Folosește un pattern care rimează

3. **Salvează poeziile favorite:**
   - Creează o listă numită `favorite_poems`
   - Adaugă un buton pentru a salva poezia curentă

4. **Diferite stiluri:**
   - Creează butoane pentru diferite tipuri de poezii (fericite, triste, amuzante)
   - Folosește liste diferite pentru fiecare stil

5. **Afișare mai frumoasă:**
   - Folosește efecte vizuale când se generează poezia
   - Adaugă un sprite pentru a afișa poezia în baloane de text frumoase

---

## 💡 **Exemple de poezii generate**

Iată câteva exemple de poezii pe care le-ar putea genera programul tău:

```
Happy robot
Dances in the garden
A bright star jumps
In the clouds!

Silly moon
Sleeps under the sea
A clever cat thinks
On the mountain!

Magical flower
Sings by the river
A gentle dog codes
In the forest!
```

---

## 🎯 **Provocări**

1. **Creează 20 de cuvinte în fiecare listă**
2. **Adaugă o listă cu peste 15 locuri diferite**
3. **Fă poezia să aibă 6 linii în loc de 4**
4. **Creează un buton pentru a afișa toate poeziile generate într-o listă**
5. **Adaugă sunete când se generează poezia**

---

## 📚 **Ce ai învățat**

În acest capitol ai învățat:

- ✅ Cum să creezi și să folosești **liste** în Scratch
- ✅ Cum să alegi elemente **aleatorii** din liste
- ✅ Cum să **îmbini** (join) text pentru a crea propoziții
- ✅ Cum să folosești **variabile** pentru a stoca text temporar
- ✅ Cum să creezi **generatoare** de conținut aleatoriu
- ✅ Cum să combini mai multe blocuri `join` pentru structuri complexe

---

## 🌟 **De ce sunt listele importante?**

Listele sunt unul dintre cele mai puternice instrumente în programare! Le poți folosi pentru:

- 📝 **Stocarea scorurilor** în jocuri
- 👥 **Păstrarea numelor** jucătorilor
- 🎨 **Colecții de culori** sau imagini
- 📚 **Inventare** în jocuri de aventură
- 🎵 **Secvențe de note** muzicale
- 🎲 **Întrebări și răspunsuri** pentru quiz-uri

Odată ce înveți să folosești liste, poți crea proiecte mult mai complexe și interesante!

---

## 🎓 **Despre Ada Lovelace**

**Știai că?**

Ada Lovelace (1815-1852) este considerată prima programatoare din lume! Ea a lucrat cu Charles Babbage la Motorul Analitic, un computer mecanic timpuriu. Ada a fost prima persoană care și-a dat seama că computerele ar putea face mult mai mult decât să calculeze numere – ar putea crea muzică, artă și poezie!

Generatorul nostru de poezii este o mică omagiere pentru viziunea ei!

---

## 🚀 **Pasul următor**

Acum că ai învățat să folosești liste, poți crea:

- **Un generator de povești** cu personaje, locații și acțiuni aleatorii
- **Un generator de nume** pentru personaje de joc
- **Un creator de propoziții** pentru a învăța limbi străine
- **Un joc de ghicește cuvântul** cu o listă de cuvinte
- **Un sistem de inventar** pentru un joc de aventură

**Posibilitățile sunt nelimitate!** 🌈

---

**Felicitări!** 🎊 Ai terminat Capitolul 6 și ai creat un generator de poezii funcțional! Ada Lovelace ar fi mândră de tine!

**Continuă să programezi și să creezi lucruri uimitoare!** 💻✨
