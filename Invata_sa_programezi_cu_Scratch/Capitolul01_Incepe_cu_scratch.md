# Capitolul 1: ÎNCEPE CU SCRATCH

*Îți place Disney sau Miyamoto? Fie că inspirația ta este Mickey Mouse sau Mario, Scratch te ajută să îți aduci creațiile la viață...*

---

## Să punem lucrurile în mișcare cu Scratch!

În câteva minute, poți construi primul tău program pentru a mișca pisica Scratch pe ecran folosind tastele săgeată sus, jos, stânga și dreapta. Când vei învăța mai mult mai târziu, vei putea dezvolta acest program simplu într-un pachet de desen cu pisica ca stilou, un joc (unde trebuie să meargă pisica?), sau orice altceva care necesită mișcare controlată de tastatură.

Pe măsură ce lucrezi prin acest capitol, vei învăța cum este organizat ecranul Scratch, astfel încât să găsești ușor ce ai nevoie pentru a construi celelalte proiecte din această carte.

Dacă ești nerăbdător să scrii propriile tale jocuri sau să începi să construiești propriile tale proiecte electronice, Scratch este locul perfect pentru a începe.

Simplitatea sa vine din modul în care selectezi comenzile dintr-un meniu și le îmbini ca pe niște piese de puzzle. Pentru că Scratch vine cu o colecție de imagini și sunete, poți începe să faci primul tău program în câteva minute.

Puterea Scratch vine din multele moduri creative în care poți combina comenzile pentru a-ți face propriul program.

---

## Găsește-ți drumul prin Scratch

Ecranul este împărțit în mai multe panouri, evidențiate în diagrama noastră de mai jos.

### **Scena** (The Stage)
Aici îți vei vedea sprite-urile (personajele) mișcându-se și interacționând. Este ca un teatru unde se întâmplă acțiunea!

### **Lista de Sprite-uri** (Sprite List)
Selectează sprite-urile aici pentru a le schimba scripturile sau costumele. Apasă pe Scenă în Lista de Sprite-uri pentru a adăuga scripturi sau pentru a schimba fundalul.

### **Paleta de Blocuri** (Blocks Palette)
Aici găsești comenzile pentru a controla sprite-urile tale. Apasă pe butoanele rotunjite de sus pentru a comuta între diferitele tipuri de blocuri.

### **Zona de Scripturi** (Scripts Area)
Asamblează-ți programele aici trăgând blocuri din Paleta de Blocuri și îmbinându-le între ele.

### **File** (Tabs)
Apasă pe file pentru a alege între modificarea scripturilor, costumelor sau sunetelor unui sprite.

---

## Imagini pe care le poți controla în Scratch se numesc **sprite-uri**

Poți să le faci să se miște, să deseneze pe ecran, să răspundă la clicuri, să își schimbe aspectul și să interacționeze între ele. Un joc spațial ar putea avea un sprite extraterestru, un sprite navă spațială și un sprite rachetă, de exemplu.

Multe proiecte au mai mult de un sprite, și poți alege între ele apăsând pe ele în Lista de Sprite-uri, în colțul din dreapta jos. Fiecare proiect nou Scratch include pisica Scratch.

Când testezi programul tău, vei urmări sprite-urile tale pe Scenă, în partea dreaptă sus a ecranului. Jocurile tale sunt mai plăcute când ocupă tot ecranul, așa că atunci când ești gata să te joci cum trebuie, apasă pe iconița cu șevalet din dreapta deasupra Scenei pentru a mări imaginea.

---

## Să faci sprite-urile să facă ceva

Pentru a face sprite-urile să facă ceva, trebuie să le dai instrucțiuni care să le spună exact ce să facă și când. Aceste instrucțiuni vin sub forma unor blocuri care se îmbină între ele. Blocurile sunt sortate în opt categorii:

### 🔵 **Motion** (Mișcare)
Folosite pentru a mișca sprite-urile pe Scenă.

### 🟣 **Looks** (Aspect)
Folosite pentru animarea sprite-urilor, pentru a le da baloane de vorbire, și pentru a le schimba dimensiunea și aspectul.

### 🟣 **Sound** (Sunet)
Folosite pentru a reda înregistrări sau note muzicale.

### 🟢 **Pen** (Stilou)
Folosite pentru a desena pe măsură ce un sprite se mișcă pe Scenă. Grozav pentru a face artă aleatorie și pentru efecte speciale în jocuri.

### 🟡 **Control** (Control)
Folosite pentru a descrie ce se întâmplă când, și pentru a face părți din programul tău să se repete.

### 🔵 **Sensing** (Senzori)
Folosite pentru a testa dacă sprite-ul tău atinge un alt sprite sau o altă culoare, sau pentru a obține informații despre alte sprite-uri. Poți folosi și blocurile cu valori ale senzorilor în propriile tale proiecte electronice pe Raspberry Pi.

### 🟢 **Operators** (Operatori)
Folosite pentru matematică, numere aleatorii și pentru a face lucruri cu text. Există și blocuri aici pentru a combina blocurile folosite în luarea deciziilor.

### 🟠 **Variables** (Variabile)
Folosite pentru a reține informații, cum ar fi scoruri, valori de temporizator sau numele jucătorilor.

---

## Găsești toate blocurile în Paleta de Blocuri

Paleta de Blocuri este în stânga ecranului. Blocurile sunt codificate prin culori, deci când copiezi programe din cărți sau reviste, poți găsi blocurile de care ai nevoie mai ușor.

În mijlocul ecranului este **Zona de Scripturi**. Aici îți faci listele de instrucțiuni (sau 'scripturi') pentru sprite-urile tale.

---

## 📌 **SFAT: ȚINE-TE LA ZI!**

Obține cea mai recentă versiune de Scratch actualizându-ți sistemul de operare folosind:
```bash
sudo apt-get update && sudo apt-get upgrade
```

---

## 📌 **ATENȚIE: CE VERSIUNE?**

Dacă folosești tutoriale online, verifică dacă sunt compatibile cu Scratch 1.4. Scratch 2.0 mai nou pentru PC-uri și Mac-uri este bazat pe Flash și nu va funcționa pe Pi. Totuși, principiile de bază sunt aceleași!

---

## 🎩 **Blocurile PĂLĂRIE (Hat Blocks)**

Blocurile cu un vârf curbat, cum ar fi `when space key pressed` (când tasta spațiu este apăsată), se numesc blocuri pălărie. Ele pot fi îmbinate doar în partea de sus a unui script. Acestea sunt folosite pentru a porni scripturile tale!

**Exemple de blocuri pălărie:**
- `when [flag] clicked` - când steagul verde este apăsat
- `when [space] key pressed` - când tasta spațiu este apăsată  
- `when Sprite1 clicked` - când Sprite1 este apăsat cu mouse-ul
- `when I receive [message]` - când primesc un mesaj

---

## Crearea primului tău Script Scratch

Ți-am promis că poți face primul tău script Scratch în câteva minute, așa că hai să o facem!

### **PASUL 01: Mișcă 10 pași**

Când deschizi Scratch (este listat sub Programming în meniul Start), acesta arată blocurile Motion în Paleta de Blocuri. Apasă pe blocul `move 10 steps` de aici și vei vedea pisica mișcându-se pe Scenă. 

De fiecare dată când apeși, se mișcă o singură dată. Asta pentru că '10 pași' înseamnă cât de departe se mișcă, nu de câte ori. Poți apăsa pe 10 și să tastezi un număr diferit pentru a face pisica să meargă mai departe sau mai puțin cu fiecare clic. 

Trage și plasează blocul `move 10 steps` în Zona de Scripturi.

### **PASUL 02: Combinarea blocurilor**

Trage blocul `point in direction 90` în Zona de Scripturi. Dacă îl plasezi chiar deasupra blocului `move 10 steps`, acestea se vor închide împreună ca piesele unui puzzle. Caută linia albă care arată că sunt pe cale să se îmbine înainte de a elibera butonul mouse-ului.

Dacă apeși pe oricare dintre blocuri, Scratch va executa instrucțiunile în ordine, mai întâi pointând în direcția 90 (îndreptându-se spre dreapta) și apoi mișcându-se 10 pași. 

Apasă pe butonul Control deasupra Paletei de Blocuri. Trage blocul `when space key pressed` și îmbină-l în partea de sus a celorlalte două blocuri tale. Sprite-ul tău se va mișca spre dreapta (direcția 90) când apeși bara de spațiu.

### **PASUL 03: Crearea controalelor de tastatură**

Dă click dreapta pe scriptul tău și alege Duplicate (Duplică). Apasă pe un spațiu gol în Zona de Scripturi pentru a plasa scriptul tău copiat. Repetă până când ai patru scripturi identice.

Hai să le transformăm în controale pentru tastele săgeată:
- Apasă pe 'space' în primul bloc pentru a deschide meniul și alege 'up arrow' (săgeată sus)
- În blocul `point in direction` de dedesubt, apasă pe '90' și alege '0' (sus)
- Acum, când apeși săgeata sus, pisica se mișcă în sus pe ecran

Editează celelalte scripturi pentru a adăuga controale pentru stânga, dreapta și jos.

**Direcțiile sunt:**
- Sus = 0
- Dreapta = 90
- Jos = 180
- Stânga = -90

---

## 🎨 **DEVINO ARTISTIC!**

Poți adăuga controale pentru `pen up` (stilou sus) și `pen down` (stilou jos) astfel încât să poți folosi acest program pentru a desena pe Scenă?

---

## Felicitări! 🎉

Tocmai ai creat primul tău program Scratch! În capitolele următoare, vei învăța să creezi jocuri complete, animații și proiecte și mai interesante.

**Continuă să explorezi și să te distrezi programând!**
