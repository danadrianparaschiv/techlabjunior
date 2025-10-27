# Capitolul 3: Condiții și comparații

Una dintre fundamentele oricărui limbaj de programare este capacitatea de a efectua operații condiționale – de a schimba fluxul programului în funcție de rezultatul unui test.

În acest capitol, vom analiza cum testați condițiile în programele dvs. C și cum folosiți rezultatele pentru a determina ce se întâmplă în continuare.

## Instrucțiunea if-else

În C, mecanismul pentru controlul fluxului bazat pe testarea unei condiții este instrucțiunea `if-else`. Iată un exemplu simplu:

```c
#include <stdio.h>

void main (void) 
{ 
  int a = 0;
  
  if (a == 0) 
  { 
    printf ("a este egal cu 0\n"); 
  } 
  else 
  { 
    printf ("a nu este egal cu 0\n"); 
  } 
}
```

Aici, cuvântul cheie `if` este urmat de un test inclus în paranteze rotunde, în acest caz `(a == 0)`. Dacă testul evaluează ca adevărat, operațiile incluse în acoladele de după test sunt executate.

Acest exemplu arată și utilizarea unei clauze `else`. La sfârșitul acoladelor din jurul operațiilor pe care doriți să le executați dacă testul este adevărat, există un `else` urmat de un alt set de acolade; acestea conțin operațiile pe care doriți să le executați dacă testul original a fost evaluat ca fals.

Încercați să compilați codul de mai sus și schimbați valoarea cu care este inițializat a pentru a vă asigura că face ceea ce vă așteptați.

> **ACOLADE**
> 
> Acoladele sunt folosite pentru a grupa împreună un set de instrucțiuni care se execută întotdeauna împreună. Dacă bucla sau instrucțiunea if trebuie să execute doar o singură instrucțiune, puteți omite acoladele după test, dar acest lucru poate face scopul codului mai puțin evident pentru om!

## = sau ==?

Totul e bine, dar despre ce este vorba cu acest `a == 0`? Sigur, dacă vrem să știm dacă a este egal cu 0, punem doar `a = 0`? De ce două semne de egalitate? Ei bine, încercați să înlocuiți semnul dublu de egalitate cu un singur semn de egalitate și vedeți ce se întâmplă.

Acesta este un aspect foarte important al sintaxei C și o sursă comună de bug-uri. Semnul egal este folosit pentru două lucruri diferite: unul este pentru a atribui o valoare unei variabile, în timp ce celălalt este pentru a testa dacă o variabilă este egală cu o valoare. Un singur semn egal (`=`) atribuie o variabilă; un semn dublu egal (`==`) testează o variabilă.

Deci instrucțiunea...

```c
if (a == 0)
```

...testează pentru a vedea dacă a este egal cu 0. Dacă este, atunci testul evaluează ca adevărat, și codul imediat după `if` este executat.

Dar instrucțiunea...

```c
if (a = 0)
```

...nu compară deloc a cu 0: doar setează a la 0. Deci cum decide compilatorul ce să facă în continuare? În acest caz, se uită doar la valoarea a ceea ce este în paranteze; ați setat a la 0, deci valoarea din interiorul parantezelor este 0.

În C, o valoare de 0 este echivalentă cu fals, iar o valoare diferită de zero este echivalentă cu adevărat. Deci, înlocuind dubla egalitate cu o singură egalitate, ați schimbat valoarea lui a, și apoi vă uitați pentru a vedea dacă valoarea la care ați setat a este echivalentă cu adevărat sau fals; niciunul dintre acestea nu era ceea ce doreați să faceți! Dacă un program C se comportă ciudat, verificați cu atenție că toate testele dvs. sunt de fapt teste și nu atribuiri: aceasta este o greșeală foarte ușor de făcut.

> **ATENȚIE!**
> 
> Asigurați-vă că folosiți un semn dublu egal în parantezele după if, nu unul singur!

## Operatori de comparație

Deci `==` este testul pentru a vedea dacă o valoare este egală cu alta. Există alte simboluri utile care pot fi folosite într-un test. Simbolul `!=`, de exemplu, înseamnă „nu este egal cu".

Operatorii matematici `>` și `<` sunt folosiți pentru a testa „este mai mare decât" și „este mai mic decât", respectiv, și pot fi, de asemenea, combinați cu un semn egal pentru a da `>=` și `<=`, testele pentru „este mai mare sau egal cu" și „este mai mic sau egal cu".

Puteți combina teste cu operatori logici. Simbolul `&&` este un AND Boolean (adică testează dacă ambele părți sunt adevărate), iar `||` este un OR Boolean (adică testează dacă oricare parte este adevărată). Deci, pentru a executa cod doar dacă atât a, cât și b sunt 0, ați folosi `if (a == 0 && b == 0)`. Pentru a testa dacă a sau b este 0, folosiți `if (a == 0 || b == 0)`.

Similar, puteți folosi operatorul `!` ca NOT Boolean pentru a inversa rezultatul unui test, deci `if (!(a == 0))` este același cu `if (a != 0)`.

> **ELSE-IF**
> 
> Puteți avea multiple instrucțiuni else într-un singur test. În loc de un simplu else pentru o alternativă, folosiți `else if ()` cu un nou test pentru fiecare alternativă pe care o doriți. Vom analiza mai multe despre acest lucru în capitolul următor.

## Bucle (Looping)

Instrucțiunea if este utilă pentru a lua o singură decizie, dar ce se întâmplă dacă doriți să faceți ceva în mod repetat până când un test este adevărat sau fals? Folosim o buclă `while` pentru aceasta, și iată un exemplu:

```c
#include <stdio.h>

void main (void) 
{ 
  int a = 0;
  
  while (a < 5) 
  { 
    printf ("a este  %d\n", a); 
    a++; 
  } 
  
  printf ("a este egal cu %d si am terminat\n", a); 
}
```

Aceasta este foarte asemănătoare cu o instrucțiune if, dar codul din acolade este executat în mod repetat atâta timp cât testul din parantezele rotunde este adevărat, nu doar o dată.

Deci în exemplul nostru de cod, a este inițializat la 0. Intrăm în bucla while și testăm pentru a vedea dacă a este mai mic decât 5, ceea ce este, deci codul din interiorul acoladelor este executat. Valoarea lui a este tipărită, apoi avem una dintre scurtăturile utile ale lui C pentru a economisi prea multă tastare...

`a++` este același lucru cu `a = a + 1`; dubla plus înseamnă „adaugă unu la această variabilă". Similar, `a--` înseamnă „scade unu din această variabilă"; acestea sunt folosite foarte frecvent pentru a număra timpii într-o buclă. Notația `a += 1` poate fi, de asemenea, folosită pentru a adăuga o valoare la o variabilă; aceasta funcționează și pentru alți operatori aritmetici, deci `a *= 3` înmulțește a cu 3, și așa mai departe.

În bucla while, de fiecare dată când codul din acolade a fost executat, testul din parantezele rotunde este repetat; dacă este încă adevărat, codul buclei este repetat din nou. De îndată ce testul este fals, execuția continuă cu linia de după acolada de închidere.

> **BUCLE INFINITE**
> 
> Asigurați-vă că buclele dvs. se termină întotdeauna! Dacă condiția pe care o testați într-o buclă while nu evaluează niciodată la fals, programul dvs. va sta în buclă pentru totdeauna și nu se va termina niciodată. Dacă un program pare să nu facă nimic când îl rulați, verificați testele buclei.

## Bucla do-while

Uneori, am putea dori o buclă care rulează întotdeauna cel puțin o dată înainte de a efectua un test. Facem acest lucru cu o mică modificare a sintaxei pentru a crea o buclă do-while:

```c
#include <stdio.h>

void main (void) 
{ 
  int a = 0;
  
  do 
  { 
    printf ("a este egal cu %d\n", a); 
    a++; 
  } while (a < 5); 
  
  printf ("a este egal cu %d si am terminat\n", a); 
}
```

Cuvântul cheie `do` merge acum înaintea acoladei, iar `while` și testul merg după acolada de închidere. Când aceasta rulează, codul din buclă se execută întotdeauna o dată înainte de test; puteți testa acest lucru rulând ambele exemple de buclă de mai sus cu a inițializat la 5 în loc de 0 și vedeți cum diferă comportamentul.

> **MAI MULTE DESPRE PUNCT ȘI VIRGULĂ**
> 
> Spre deosebire de testul dintr-o instrucțiune if sau o buclă while, trebuie să puneți un punct și virgulă după testul într-o buclă do-while. Aceasta indică sfârșitul codului buclei; într-o buclă while, codul buclei nu se termină până la ultima instrucțiune din interiorul acoladelor.

**Notă:** O buclă execută același cod de mai multe ori până când testul buclei este fals.

În capitolul următor, vom analiza câteva exemple mai complexe de buclare și control al fluxului.
