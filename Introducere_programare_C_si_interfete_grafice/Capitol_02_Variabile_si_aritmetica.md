# Capitolul 2: Variabile și operații aritmetice

În unele limbaje, puteți crea variabile pe parcurs și puteți pune orice date doriți în ele. C nu este așa: pentru a folosi o variabilă în C, trebuie să o fi creat mai întâi, și în momentul în care o creați, trebuie să stabiliți ce tip de valoare va stoca. Făcând acest lucru, un bloc de memorie de dimensiunea corectă poate fi alocat de compilator pentru a păstra variabila. Acest proces de creare a unei variabile este cunoscut sub numele de **declarare**.

## Numere întregi (Integer)

Există mai multe tipuri fundamentale de date în C, dar vom începe prin a analiza unul dintre cele mai utilizate: tipul `int`, folosit pentru a stoca o valoare întreagă.

```c
#include <stdio.h>

void main (void) 
{ 
  int a; 
  int b = 3; 
  int c;
  
  a = 2; 
  c = a + b; 
  printf ("The sum of adding %d and %d is %d\n", a, b, c); 
}
```

Primele trei linii din interiorul funcției main sunt declarații. Acestea îi spun compilatorului că ne-ar plăcea să folosim variabile numite a, b și c, respectiv, și că fiecare este de tip `int`, adică un număr întreg.

În a doua linie, vedem un exemplu de **inițializare** în același timp cu o declarare: aceasta stochează o valoare inițială de 3 în variabila b. Observați că valorile lui a și c în acest moment sunt nedefinite; ați putea presupune că o variabilă care nu a avut o valoare stocată în ea este întotdeauna 0, dar acesta nu este cazul în C. Înainte de a citi valoarea dintr-o variabilă sau de a o folosi într-un calcul, trebuie să stocați o valoare în ea; citirea unei variabile înainte de a o inițializa este o eroare comună în C.

Următoarele două linii fac ceva efectiv cu variabilele pe care le-am declarat.

```c
a = 2;
```

Aceasta stochează o valoare de 2 în variabila a, care va avea acum această valoare până când este schimbată. Motivul pentru care a este numită variabilă este că poate varia: puteți schimba valoarea ei ori de câte ori doriți, dar doar la un alt număr întreg. Valoarea unei variabile poate schimba, dar tipul său este fixat când este declarată.

```c
c = a + b;
```

Această linie adaugă a la b și stochează rezultatul în c.

```c
printf ("The sum of adding %d and %d is %d\n", a, b, c);
```

Aceasta este o altă utilizare a funcției de tipărire formatată pe care am văzut-o în capitolul anterior. Observați cele trei simboluri `%d` din interiorul șirului: acestea sunt **specificatori de format**, și sunt modul în care afișați numere în C. Când funcția printf este executată, fiecare `%d` este înlocuit cu o reprezentare zecimală (d pentru decimal integer) a variabilei în poziția corespunzătoare din lista de după șir. Deci primul `%d` va fi înlocuit cu valoarea lui a, al doilea cu valoarea lui b și al treilea cu valoarea lui c.

Compilați programul de mai sus și apoi rulați-l. Ar trebui să vedeți acest lucru în terminal:

```
The sum of adding 2 and 3 is 5
```

> **DECLARAȚII MULTIPLE**
> 
> Puteți declara mai multe variabile de același tip pe o singură linie, separate prin virgule. Pentru exemplul de aici, în loc de trei declarații int separate, ați putea scrie `int a, b = 3, c;` pe o singură linie.

## Numere în virgulă mobilă (Floating-point)

Deci putem aduna două numere întregi împreună; ce altceva putem face? Un lucru pe care am putea dori să-l facem este să folosim numere în virgulă mobilă: numere cu virgulă zecimală. Acestea au un tip diferit, numit `float`. Încercați să schimbați codul de mai sus astfel încât, în loc de:

```c
int a;
```

...să aveți:

```c
float a;
```

Aceasta îi spune compilatorului că a este acum o valoare în virgulă mobilă, mai degrabă decât un număr întreg. Compilați și rulați programul. Ce se întâmplă?

Hopa! Asta nu arată bine, nu-i așa? Ceea ce s-a întâmplat este că, în timp ce calculele matematice sunt încă corecte, instrucțiunea printf este acum greșită; îi spuneți să tipărească a, care este o valoare în virgulă mobilă, ca un număr întreg zecimal. Pentru a remedia asta, schimbați primul `%d` din funcția printf în `%f`, care este specificatorul de format pentru un număr în virgulă mobilă, astfel:

```c
printf ("The sum of adding %f and %d is %d\n", a, b, c);
```

Aceasta ar trebui să producă ceva mult mai sensibil când îl rulați. Aceasta este o lecție importantă despre C: va face exact ceea ce îi spuneți, chiar dacă nu are sens. I-ați spus să vă arate un număr în virgulă mobilă ca și cum ar fi un număr întreg zecimal, și compilatorul a presupus că asta este ceea ce doriți, chiar dacă rezultatul a fost absurd.

Când lucrați cu variabile, țineți întotdeauna evidența valorilor pe care le puneți în ce tipuri, deoarece este ușor să introduceți erori presupunând că o variabilă este de un tip când este de fapt de altul. O eroare comună este să puneți rezultatele unui calcul pe valori în virgulă mobilă într-un număr întreg.

Încercați acest lucru: faceți b un float de asemenea (nu uitați să schimbați specificatorul său de format în printf), dar lăsați c ca int, și setați cele două float-uri la valori cu virgule zecimale, astfel:

```c
float a; 
float b = 3.641; 
int c;

a = 2.897; 
c = a + b; 
printf ("The sum of adding %f and %f is %d\n", a, b, c);
```

Veți vedea un rezultat ca:

```
The sum of adding 2.897000 and 3.641000 is 6
```

6? Asta nu este corect! Dar este exact ceea ce ați cerut. Ceea ce a făcut compilatorul a fost să adauge cele două valori în virgulă mobilă împreună și a obținut răspunsul 6.538, dar apoi i-ați spus compilatorului să pună asta în c, o variabilă întreagă. Deci compilatorul a aruncat pur și simplu tot ce era după virgula zecimală! Dacă schimbați c în float și schimbați ultimul `%d` în `%f`, veți găsi că oferă răspunsul corect.

> **ATENȚIE!**
> 
> Nu uitați să folosiți `%f` în loc de `%d` ca specificator de tipărire când schimbați valorile int în valori float în exemplu.

> **ZECIMALE**
> 
> Puteți seta numărul de zecimale de afișat pentru un specificator de tip în virgulă mobilă în printf punând un punct zecimal și numărul de locuri între % și f – deci `%.3f` va afișa o valoare float cu trei cifre după virgula zecimală.

## Alte tipuri

Un alt tip comun de variabilă este `char`, o valoare de caracter. Aceasta este folosită, după cum sugerează și numele, pentru a stoca un singur caracter. Codificarea de caractere ASCII folosește o singură valoare între 0 și 127 pentru fiecare literă, număr și simbol de punctuație, deci un char este un singur byte; este de fapt doar o valoare întreagă care poate deține doar numere mici. Compilatorul alocă mai mulți bytes pentru a stoca un int sau un float, dar alocă doar un singur byte de memorie pentru a stoca un char.

Există și modificatori care pot fi aplicați tipurilor de variabile. Atât `char`, cât și `int` pot fi folosite pentru a stoca atât numere pozitive, cât și negative, dar prin aplicarea modificatorului `unsigned` când una este declarată, acestea pot fi restricționate pentru a stoca doar valori pozitive. Deci...

```c
char a;
```

...declară o variabilă care poate deține valori de la -128 la 127, în timp ce...

```c
unsigned char a;
```

...declară o variabilă care poate deține valori de la 0 la 255.

Când faceți operații aritmetice cu char-uri, este important să vă asigurați că răspunsurile la orice calcul se vor încadra în variabilă. Dacă, să zicem, aveți un char care conține valoarea 100 și adăugați 30 la el, v-ați aștepta să ajungeți cu rezultatul 130 – dar, după cum am văzut mai sus, un char poate deține doar valori până la 127. Deci valoarea pe care char-ul dvs. va ajunge efectiv să o conțină este -126, deoarece valorile peste 127 – cea mai mare valoare pe care un char o poate stoca – se înfășoară la cea mai mică valoare (-128) și încep să numere în sus de acolo. Acest comportament de „depășire" (overflow) este o cauză comună de bug-uri în programele C care efectuează operații aritmetice.

> **SCURTĂTURI ARITMETICE**
> 
> C permite scurtături pentru unele operații comune; de exemplu, în loc să tastați `a = a + 1`, puteți scrie doar `a++`. Sau pentru `a = a * 3`, puteți introduce `a *= 3`.

> **AMINTIȚI-VĂ PRECEDENȚA**
> 
> C respectă regulile comune pentru precedența operatorilor – deci `a = a + 2 * 3` evaluează mai întâi înmulțirea și apoi adaugă rezultatul, 6, la a. Puteți folosi paranteze rotunde pentru a schimba precedența – `a = (a + 2) * 3` dă `3a + 6`.

Aceasta vă oferă o idee despre cum C gestionează numerele și cum îl puteți folosi pentru operații aritmetice; în capitolul următor, vom analiza cum să folosim rezultatele calculelor pentru a lua decizii.
