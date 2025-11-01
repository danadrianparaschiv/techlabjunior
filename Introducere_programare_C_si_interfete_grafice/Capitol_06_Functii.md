# Capitolul 6: Funcții

Până acum, toate exemplele pe care le-am analizat au avut o singură funcție, `main`, cu tot codul în ea. Acest lucru este perfect valid pentru programe mici și simple, dar nu este foarte practic odată ce aveți mai mult de câteva zeci de linii și este o pierdere de spațiu dacă trebuie să faceți același lucru de mai multe ori. Împărțirea codului în funcții separate îl face mai lizibil și permite reutilizarea ușoară.

Am văzut deja funcții folosite; funcția main este o funcție C standard, deși cu un nume special. Am văzut, de asemenea, funcția printf apelată de exemplele noastre. Deci cum creăm și folosim o funcție proprie? Iată un exemplu:

```c
#include <stdio.h>

int sum (int a, int b) 
{ 
  int res; 
  res = a + b; 
  return res; 
}

void main (void) 
{ 
  int y = 2; 
  int z = sum (5, y);
  printf ("The sum of 5 and %d is %d\n", y, z); 
}
```

Aceasta include atât funcția main, cât și o a doua funcție numită sum. În ambele cazuri, structura funcției este aceeași: o linie care definește valoarea returnată de funcție, numele funcției și argumentele funcției, urmată de un bloc de cod inclus în acolade, care este ceea ce face de fapt funcția.

## Ce conține o funcție?

Să analizăm funcția sum:

```c
int sum (int a, int b)
```

Definiția unei funcții are trei părți:

1. **Tipul valorii returnate** de funcție: în acest caz, un `int`
2. **Numele funcției**: în acest caz, `sum`
3. **Argumentele funcției**: în paranteze rotunde, separate prin virgule, fiecare cu tipul său: în acest caz, două argumente întregi, `a` și `b`

Restul funcției este între acolade.

```c
int res;
```

Aceasta declară o variabilă **locală** pentru funcție, un întreg numit res. Aceasta este o variabilă care poate fi folosită doar local, în interiorul funcției în sine. Variabilele declarate în interiorul unei definiții de funcție pot fi folosite doar în cadrul acelei funcții; dacă încercați să citiți sau să scrieți res în interiorul funcției main, veți obține o eroare.

> **NOTĂ**: Ați putea declara un alt int numit res în funcția main, dar aceasta ar fi o variabilă diferită numită res de cea din interiorul funcției sum, și ar deveni foarte confuz, deci nu este recomandat!

```c
res = a + b;
```

Acest lucru ar trebui să fie evident! Observați că a și b sunt cele două argumente definite ale funcției. Când o funcție este apelată, o copie locală a argumentelor este făcută și folosită în cadrul funcției. Dacă schimbați valorile lui a sau b în interiorul funcției (ceea ce este perfect valid), aceasta afectează doar valoarea lui a și b în cadrul acestei funcții; nu schimbă valorile pe care argumentele le aveau în funcția din care a fost apelată.

```c
return res;
```

În cele din urmă, trebuie să returnăm rezultatul. Funcția a fost definită să returneze un întreg, deci trebuie să apeleze instrucțiunea `return` cu o valoare întreagă care să fie returnată funcției apelante.

O funcție nu trebuie să returneze o valoare; dacă tipul de returnare este setat la `void`, nu returnează nimic. Nu este nevoie de o instrucțiune return într-o funcție cu un tip de returnare void: funcția va returna când ajunge la ultima linie; totuși, dacă doriți să returnați devreme (în cazul unei erori, de exemplu), doar apelați return fără nicio valoare după ea.

> **ARGUMENTE**
> 
> O funcție poate avea orice număr de argumente, de la zero până la sute. Dacă nu aveți nevoie de argumente, listați argumentele ca `(void)` în definiția funcției (la fel ca în funcția main); când apelați funcția, puneți doar o pereche de paranteze rotunde goale `()` după numele funcției.

> **DOMENIUL DE VIZIBILITATE AL VARIABILELOR (SCOPE)**
> 
> Dacă declarați o variabilă în interiorul unei funcții, aceasta este utilizabilă doar în cadrul acelei funcții, nu în cadrul niciunor funcții care apelează funcția sau în cadrul funcțiilor apelate de funcție. Aceasta este cunoscută sub numele de **domeniul de vizibilitate (scope)** al unei variabile: părțile de cod în care este validă.

**Notă:** Funcția main tipărește valorile returnate de funcția sum.

## Apelarea unei funcții

Să ne uităm la modul în care apelăm funcția din main:

```c
int z = sum (5, y);
```

Funcția sum returnează un întreg, deci setăm o variabilă întreagă egală cu ea. Argumentele pe care le furnizăm funcției sunt în paranteze rotunde și în aceeași ordine ca în definiția funcției; deci în acest caz, a este 5, iar b este valoarea lui y.

## Returnarea mai multor valori

Puteți returna mai mult de un rezultat dintr-o funcție? Puteți returna doar o singură valoare, dar puteți folosi și pointeri pentru a transmite mai multe elemente de date înapoi la funcția apelantă. Luați în considerare acest exemplu:

```c
#include <stdio.h>

int sum_and_diff (int a, int b, int *res) 
{ 
  int sum; 
  sum = a + b; 
  *res = a - b; 
  return sum; 
}

void main (void) 
{ 
  int b = 2; 
  int diff;
  
  printf ("The sum of 5 and %d is %d\n", b,  
      sum_and_diff (5, b, &diff)); 
  printf ("The difference of 5 and %d is %d\n", b, diff); 
}
```

Am modificat funcția sum pentru a calcula atât suma, cât și diferența argumentelor. Suma este returnată ca înainte, dar transmitem și diferența înapoi folosind un pointer. Amintiți-vă că argumentele unei funcții sunt variabile locale; chiar dacă schimbați una în funcție, nu are niciun efect asupra valorii transmise de funcția apelantă. Acesta este motivul pentru care pointerii sunt utili: prin transmiterea unui pointer, funcția nu schimbă valoarea pointerului în sine, dar poate schimba valoarea variabilei la care indică.

Deci apelăm funcția cu aceleași două argumente ca înainte, dar adăugăm un al treilea, un pointer la variabila în care dorim să scriem diferența calculată de funcție. În funcție, avem această linie:

```c
*res = a - b;
```

Diferența este scrisă în variabila la care res este un pointer.

În funcția main, apelăm funcția sum_and_diff astfel:

```c
sum_and_diff (5, b, &diff)
```

Furnizăm adresa întregului diff ca argument pointer pentru funcția sum_and_diff; când diferența este calculată, este scrisă în variabila diff din funcția main.

> **RETURNAREA VALORILOR**
> 
> O funcție poate returna o singură valoare sau deloc. Dacă definiți funcția ca returnând void, nu este nevoie să folosiți o instrucțiune return în ea, dar veți primi o eroare dacă nu includeți un return de tipul corect într-o funcție non-void.

> **MODIFICAREA ARGUMENTELOR**
> 
> Argumentele sunt variabile locale în cadrul unei funcții. Dacă doriți ca o funcție să modifice argumentele pe care le dați, faceți fiecare argument pe care doriți să îl modificați un pointer la o variabilă; puteți apoi citi valoarea la care se indică în cadrul funcției și scrie valoarea modificată înapoi la același pointer.

**Notă:** Prin folosirea unui pointer ca argument, funcția sum_and_diff poate returna atât suma, cât și diferența argumentelor.

## Ordinea contează

Un lucru de avut în vedere când definiți funcții este că compilatorul citește fișierele de sus în jos, și trebuie să îi spuneți despre o funcție înainte de a o putea folosi. În exemplele de mai sus, acest lucru este automat, deoarece definiția funcțiilor sum și sum_and_diff este înaintea primului apel la ele în main.

Dar în fișiere mai mari, când mai multe funcții apelează mai multe alte funcții, acest lucru devine complicat; nu este întotdeauna ușor să vă asigurați că definițiile funcțiilor sunt toate în ordinea corectă. Pentru a evita acest lucru, C vă permite să **declarați** funcții înainte de a fi folosite.

## Declararea funcțiilor

O declarație de funcție este doar definiția funcției, minus codul funcției din interiorul acoladelor. Deci pentru funcția sum_and_diff, declarația ar fi:

```c
int sum_and_diff (int a, int b, int *res);
```

Observați punct și virgula de la sfârșit! Declarațiile de funcții sunt incluse în partea de sus a fișierului; când compilatorul găsește o declarație de funcție, știe că la un moment dat o funcție cu acest nume, argumente și tip de returnare va fi definită, deci știe cum să gestioneze un apel la ea, chiar dacă nu a văzut încă definiția în sine.

## Exemplu complet cu declarații

```c
#include <stdio.h>

// Declarații de funcții
int sum (int a, int b);
int sum_and_diff (int a, int b, int *res);

// Funcția main
void main (void) 
{ 
  int y = 2;
  int z = sum (5, y);
  int diff;
  
  printf ("The sum of 5 and %d is %d\n", y, z);
  
  printf ("The sum of 5 and %d is %d\n", y,  
      sum_and_diff (5, y, &diff));
  printf ("The difference of 5 and %d is %d\n", y, diff);
}

// Definiții de funcții
int sum (int a, int b) 
{ 
  return a + b; 
}

int sum_and_diff (int a, int b, int *res) 
{ 
  *res = a - b; 
  return a + b; 
}
```

**Notă:** Puteți folosi un apel de funcție oriunde ar putea fi folosită o variabilă de același tip cu valoarea returnată de funcție – în codul de aici, un apel la sum_and_diff înlocuiește o valoare întreagă în argumentele lui printf.

## Rezumat

Punctele cheie despre funcții în C:

### Structura unei funcții:
```c
tip_returnare nume_functie (tip_arg1 arg1, tip_arg2 arg2, ...) 
{
  // cod local
  return valoare; // dacă tip_returnare != void
}
```

### Avantajele funcțiilor:
- ✅ **Reutilizare cod** - Scrie o dată, folosește de multe ori
- ✅ **Lizibilitate** - Cod mai curat și organizat
- ✅ **Modularitate** - Împarte probleme mari în părți mici
- ✅ **Debugging** - Mai ușor de testat și corectat
- ✅ **Colaborare** - Fiecare programator poate lucra pe funcții separate

### Reguli importante:
1. Declarați funcția înainte de a o folosi (sau definiți-o înaintea apelului)
2. Argumentele sunt copii locale - modificările nu afectează variabilele originale
3. Folosiți pointeri pentru a returna multiple valori
4. Variabilele locale există doar în funcția lor
5. O funcție `void` nu returnează nimic
6. O funcție non-void TREBUIE să returneze o valoare

### Exemple de utilizare:
```c
// Funcție simplă
int double_value(int x) {
    return x * 2;
}

// Funcție fără returnare
void print_message(void) {
    printf("Hello!\n");
}

// Funcție cu pointer pentru rezultat suplimentar
int divide_with_remainder(int a, int b, int *remainder) {
    *remainder = a % b;
    return a / b;
}
```

În capitolul următor, vom învăța despre array-uri și șiruri de caractere, care vor face funcțiile noastre și mai puternice și mai flexibile!
