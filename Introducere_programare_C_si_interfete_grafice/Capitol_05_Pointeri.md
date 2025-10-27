# Capitolul 5: Pointeri

Termenul pointer a provocat frică în inima multor programatori C începători, dar odată ce ați înțeles conceptul, pointerii sunt o caracteristică foarte utilă a limbajului. Nu sunt de fapt atât de complicați în realitate, dar este ușor să vă confundați când îi folosiți, așa că să încercăm să evităm acest lucru...

Amintiți-vă când am analizat declararea variabilelor? Declararea unei variabile – spunând compilatorului ce tip este și cum se numește – înainte de a o putea folosi este necesară în C, deoarece declararea permite compilatorului să aloce un bloc de memorie pentru a stoca variabila. Deci, pentru fiecare variabilă pe care o declarați, există un bloc de memorie care este pus deoparte de compilator pentru acea variabilă, și compilatorul își amintește care anume bloc de memorie este folosit pentru fiecare variabilă.

## Ce este un pointer?

Un pointer este doar adresa unui bloc de memorie cu o variabilă în el; asta e tot. Deci, dacă declarați o variabilă și un pointer la acea variabilă, puteți accesa valoarea din acel bloc de memorie în două moduri: fie cu numele variabilei, fie cu pointerul.

Să ne uităm la un exemplu simplu:

```c
#include <stdio.h>

void main (void) 
{ 
  int a; 
  int *ptr_to_a;
  
  ptr_to_a = &a;
  
  a = 5; 
  printf ("The value of a is %d\n", a);
  
  *ptr_to_a = 6; 
  printf ("The value of a is %d\n", a);
  
  printf ("The value of ptr_to_a is %d\n", ptr_to_a); 
  printf ("It stores the value %d\n", *ptr_to_a); 
  printf ("The address of a is %d\n", &a); 
}
```

Analizând linie cu linie, prima linie este una cu care suntem deja familiarizați: declarăm o variabilă întreagă numită a. Dar ce este asta?

```c
int *ptr_to_a;
```

Pare că declară o altă variabilă întreagă, nu-i așa? Dar uitați-vă mai atent; asteriscul (`*`) de la începutul numelui variabilei indică faptul că aceasta nu declară o variabilă întreagă, ci un pointer la o variabilă întreagă.

Deci acum avem o variabilă întreagă numită a, și avem un pointer la o variabilă întreagă, numită ptr_to_a. Dar niciunul dintre acestea nu are încă o valoare în el: amândouă sunt neinițializate. E foarte bine să numim pointerul ptr_to_a, dar nu are nicio idee ce (sau unde) este a, așa că vom remedia acest lucru cu următoarea linie.

```c
ptr_to_a = &a;
```

Aceasta este partea importantă! În C, simbolul `&` înaintea unui nume de variabilă înseamnă **adresa variabilei**, deci `&a` înseamnă „adresa în memorie a variabilei a". Și după cum am spus mai sus, un pointer este adresa unei variabile. Deci această linie inițializează ptr_to_a să fie adresa lui a; ptr_to_a este acum un pointer valid la variabila a, deci acum îl putem folosi.

Următoarele două linii sunt familiare: setăm a să fie 5, și doar pentru a verifica că a funcționat, tipărim valoarea sa. Deci să încercăm să facem același lucru, dar cu pointerul.

```c
*ptr_to_a = 6;
```

Din nou asteriscul, dar folosit într-un mod ușor diferit de înainte. Când declarăm o variabilă, punerea unui asterisc înaintea numelui său indică că variabila este un pointer. Dar odată ce pointerul există, punerea unui asterisc în fața numelui său înseamnă **variabila la care indică acest pointer**; aceasta este cunoscută sub numele de **dereferențiere** a pointerului.

Deci această linie îi spune compilatorului să seteze variabila la care indică pointerul ptr_to_a la 6. Știm că variabila la care indică ptr_to_a este a; am stabilit asta cu câteva linii în urmă, și deci această linie este doar un alt mod de a seta a la 6; într-adevăr, dacă tipărim valoarea lui a, găsim că s-a schimbat în 6.

Următoarele linii vă vor ajuta, sperăm, să clarificați relația dintre pointeri, variabile și adrese în mintea dvs.

```c
printf ("The value of ptr_to_a is %d\n", ptr_to_a);
```

În această linie, tipărim valoarea lui ptr_to_a; nu valoarea la care indică, ci valoarea pointerului în sine. Aceasta tipărește un număr foarte mare, deoarece este adresa în memorie unde poate fi găsit a.

```c
printf ("It stores the value %d\n", *ptr_to_a);
```

În această linie, tipărim valoarea la care indică ptr_to_a; observați asteriscul înaintea numelui. Aceasta tipărește valoarea lui a.

```c
printf ("The address of a is %d\n", &a);
```

În cele din urmă, în această linie tipărim adresa lui a în sine; observați semnul `&` înaintea numelui. Din nou, aceasta tipărește un număr foarte mare, același cu valoarea lui ptr_to_a pe care am tipărit-o mai sus.

## Lucrul cu pointeri - Reguli importante

Lucrul crucial de reținut când lucrați cu pointeri este acesta: **nu puteți doar să declarați un pointer**, deoarece trebuie, de asemenea, să declarați și să asociați variabila la care doriți să indice. Când un pointer este creat, indică către o locație aleatorie în memorie; dacă încercați să scrieți ceva în el, puteți cauza tot felul de erori, până la și inclusiv blocarea completă a computerului! Asigurați-vă întotdeauna că pointerii dvs. indică către ceva înainte de a face orice cu ei.

> **MEMORIE**
> 
> Pointerii sunt una dintre modalitățile prin care C vă permite (sau în unele cazuri vă forțează) să gândiți despre ceea ce face de fapt hardware-ul computerului dvs. – o bună înțelegere a pointerilor vă oferă o bună înțelegere a modului în care compilatorul gestionează memoria.

> **\* ȘI &**
> 
> Când învățam pentru prima dată despre pointeri, mi-a fost util să spun cu voce tare ce făcea o linie de cod – un `*` este „ceea ce este indicat de", iar un `&` este „adresa lui". Odată ce ați fixat aceste două idei în cap, ați înțeles destul de mult pointerii!

## Rezumat

Pointerii pot părea intimidanți la început, dar sunt esențiali pentru:

- **Eficiență** - Transmiterea adreselor în loc de copii ale datelor
- **Flexibilitate** - Manipularea directă a memoriei
- **Structuri de date** - Crearea de liste înlănțuite, arbori, etc.
- **Funcții** - Modificarea variabilelor transmise ca argumente

Punctele cheie de reținut:

1. `int *ptr` - Declară un pointer la un întreg
2. `ptr = &var` - Atribuie adresa variabilei var la pointer
3. `*ptr` - Dereferențiază pointerul (accesează valoarea la care indică)
4. `&var` - Obține adresa variabilei var

În capitolul următor, vom vedea cum pointerii sunt folosiți în funcții pentru a face codul mai eficient și mai puternic.
