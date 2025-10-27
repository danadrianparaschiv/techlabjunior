# Capitolul 4: Control avansat al fluxului

Instrucțiunea `if` și bucla `while` descrise în capitolul anterior sunt structuri de control destul de simple. În acest capitol, vom analiza câteva structuri mai complexe care pot ajuta la scurtarea codului și la reducerea cantității de tastare pe care trebuie să o faceți...

## Bucla for

Deși bucla `while` pe care am văzut-o în articolul anterior este foarte utilă, bucla `for` tinde să fie preferată de mulți programatori, deoarece pune toată logica care controlează bucla într-un singur loc. Iată un exemplu:

```c
#include <stdio.h>

void main (void) 
{ 
  int a;
  
  for (a = 0; a < 5; a++) 
  { 
    printf ("a is equal to %d\n", a); 
  } 
  
  printf ("a is equal to %d and I've finished\n", a); 
}
```

Aceasta nu este atât de diferită de o buclă while, dar tot controlul pentru buclă trăiește în parantezele rotunde după cuvântul cheie `for`. Aceasta conține trei instrucțiuni, separate prin punct și virgulă: în ordine, acestea sunt condiția inițială, testul și incrementul.

- `a = 0` este condiția inițială; variabila a este inițializată la 0 la începutul buclei.
- `a < 5` este testul, exact ca într-o buclă while. Acesta este verificat la fiecare iterație a buclei, și codul buclei este executat doar dacă testul evaluează ca adevărat; de îndată ce testul este fals, execuția continuă după acolada de la sfârșitul codului buclei.
- `a++` este incrementul; acesta este codul care este executat la sfârșitul fiecărei iterații a buclei, înainte ca testul să fie evaluat din nou. În acest caz, adaugă 1 la a.

Deci, când această buclă for rulează, ce se întâmplă? Mai întâi, a este setat la 0. Testul este apoi verificat: este a (care este 0) mai mic decât 5? Da, este, deci codul din interiorul acoladelor este executat, și valoarea lui a este tipărită. În cele din urmă, incrementul este aplicat, ceea ce înseamnă că 1 este adăugat la a.

Testul este apoi repetat. Dacă este adevărat, codul buclei este executat din nou, și incrementul este din nou aplicat; acest lucru se repetă iar și iar până când testul este fals, moment în care execuția continuă după acolada de închidere.

**Notă:** Ieșirea când bucla for rulează este identică cu cea a buclei while din capitolul anterior – ambele fac exact același lucru.

În ceea ce privește ceea ce fac, buclele for și buclele while sunt destul de mult identice; ambele împachetează o secțiune de cod pe care doriți să o rulați de mai multe ori într-o logică care controlează de câte ori rulează. Puteți folosi pe oricare are cel mai mult sens sau pe oricare arată cel mai ordonat pentru dvs.!

> **INIȚIALIZĂRI MULTIPLE**
> 
> Puteți inițializa mai multe variabile într-o buclă for – doar separați-le prin virgule. Deci, dacă doriți să setați două variabile la începutul buclei, puteți folosi:
> ```c
> for (a = 0, b = 1; <test>; <increment>)
> ```

> **INCREMENTE MULTIPLE**
> 
> La fel ca în cazul inițializărilor multiple, puteți avea incremente multiple într-o buclă for, de asemenea separate prin virgule – `for (a = 0, b = 1; <test>; a++, b *= 2)`. Acest lucru este util dacă există două sau mai multe variabile care se schimbă în mod constant în timp ce bucla rulează.

## Instrucțiuni switch

Un lucru pe care destul de des doriți să-l faceți este să testați o variabilă față de mai multe valori și să faceți lucruri diferite pe baza fiecăreia dintre ele. Puteți face acest lucru cu un set de instrucțiuni if imbricate:

```c
#include <stdio.h>

void main (void) 
{ 
  unsigned int a = 0;
  
  if (a == 0) 
  { 
    printf ("a is equal to 0\n"); 
  } 
  else if (a == 1) 
  { 
    printf ("a is equal to 1\n"); 
  } 
  else 
  { 
    printf ("a is greater than 1\n"); 
  } 
}
```

Totuși, acest lucru începe să devină destul de lung, așa că C oferă o modalitate mai ordonată de a face acest lucru, numită instrucțiune `switch`.

```c
#include <stdio.h>

void main (void) 
{ 
  unsigned int a = 0;
  
  switch (a) 
  { 
    case 0 :    printf ("a is equal to 0\n"); 
                break; 
    case 1 :    printf ("a is equal to 1\n"); 
                break; 
    default :   printf ("a is greater than 1\n");             
  } 
}
```

Aceasta face exact același lucru ca exemplul de mai sus cu multiple instrucțiuni if, dar este mult mai scurt. Deci cum funcționează?

Linia de deschidere constă din cuvântul cheie `switch`, cu numele unei variabile în paranteze rotunde. Aceasta este variabila care va fi testată față de diferitele cazuri.

Corpul instrucțiunii switch este un număr de instrucțiuni `case`. Variabila a este comparată cu fiecare caz la rândul său; dacă se potrivește cu valoarea imediat după cuvântul case, atunci liniile de cod după două puncte sunt executate.

Cazul final este doar numit `default` – fiecare instrucțiune switch ar trebui să includă un caz default ca ultim în listă, și acesta este codul care este executat dacă niciunul dintre celelalte cazuri nu se potrivește.

Observați că ultima linie din fiecare secțiune de caz este cuvântul `break` – acest lucru este foarte important. Cuvântul cheie break îi spune compilatorului că doriți să „ieșiți" din instrucțiunea switch în acest punct; adică, să opriți executarea codului din interiorul switch-ului și să reluați execuția după acolada de închidere.

> **ATENȚIE!**
> 
> Nu uitați instrucțiunile break la sfârșitul fiecărui caz în instrucțiunile dvs. switch!

Dacă uitați să includeți instrucțiunile break, fiecare caz de după cel pe care l-ați dorit se va executa, precum și cel pe care l-ați dorit. Încercați compilând codul de mai sus și rulându-l – veți vedea următoarele în terminal:

```
a is equal to 0
```

Acum eliminați cele două instrucțiuni break, astfel încât switch-ul să arate astfel:

```c
switch (a) 
{ 
  case 0 :    printf ("a is equal to 0\n"); 
  case 1 :    printf ("a is equal to 1\n"); 
  default :   printf ("a is greater than 1\n"); 
}
```

...și rulați-l din nou – veți vedea acum:

```
a is equal to 0
a is equal to 1
a is greater than 1
```

Nu este ceea ce v-ați așteptat! Aceasta este o altă eroare comună în codul C – uitarea instrucțiunilor break în cazurile dvs. poate duce la un comportament foarte neașteptat. Dar acest lucru poate fi, de asemenea, util; programatorii vor structura uneori o instrucțiune switch cu cod pe care doresc să-l execute în mai multe cazuri diferite și vor omite în mod deliberat instrucțiunile break.

> **BUCLA DVS. PREFERATĂ...**
> 
> Toate cele trei tipuri de bucle în C – while, do-while și for – pot fi folosite în destul de multe situații în care este nevoie de o buclă; alegeți pe oricare vă place. Unii oameni preferă să folosească un tip de buclă pentru tot; alții aleg în funcție de care arată cel mai ordonat pentru fiecare circumstanță. Nu există alegeri greșite!

## Ieșirea dintr-o buclă în avans

Instrucțiunea break are o altă utilizare: poate fi folosită în interiorul buclelor while și for pentru a ieși din ele. Uitați-vă la acest exemplu:

```c
#include <stdio.h>

void main (void) 
{ 
  int a = 0;
  
  while (1) 
  { 
    printf ("a is equal to %d\n", a); 
    a++; 
    
    if (a == 5)  
    { 
      break; 
    } 
  } 
  
  printf ("a is equal to %d and I've finished\n", a); 
}
```

Deci avem o buclă while în care testul este doar valoarea 1; aceasta este o valoare diferită de zero și, prin urmare, este întotdeauna adevărată. Dacă includeți cod în interiorul acoladelor după o instrucțiune `while (1)`, bucla nu se va termina niciodată; va continua să ruleze pentru totdeauna.

Dar în acest caz am furnizat o modalitate alternativă de a termina bucla; testăm valoarea lui a în interiorul buclei în sine într-o instrucțiune if și, dacă a este egal cu 5, apelăm break. Acest lucru face ca bucla să se termine și execuția să continue cu instrucțiunea de după buclă. O instrucțiune break ca aceasta poate fi utilă pentru a părăsi o buclă în avans în cazul unei erori, de exemplu.

> **CONTINUE**
> 
> Cuvântul cheie `continue` poate fi folosit într-o buclă în loc de break, dar în loc să iasă din buclă, sare peste tot restul codului din iterația curentă și revine la cazul de test de la începutul buclei. Printre altele, acest lucru poate fi util pentru a accelera codul dvs.

Asta este cam tot ce trebuie să știți despre controlul fluxului în C; în capitolul următor, vom analiza pointerii, care sunt una dintre cele mai utile și puternice caracteristici ale lui C.
