# Capitolul 12: Fișiere antet și preprocesorul

Toate exemplele pe care le-am văzut până acum au pus tot codul pentru un program într-un singur fișier C. Dar odată ce programele devin mari, are mai mult sens să le împărțiți în fișiere separate, grupând funcții similare împreună. Pentru a înțelege cum funcționează acest lucru, trebuie să analizăm mai în detaliu ce face de fapt compilatorul.

## Procesul de compilare

În toate exemplele de până acum, am apelat gcc pe un singur fișier sursă și a creat un singur program executabil. Acest lucru ascunde faptul că gcc face de fapt două lucruri:

1. **Compilează** fișierul sursă C într-un așa-numit **fișier obiect** (object file)
2. **Leagă** (link) fișierul obiect cu toate funcțiile de bibliotecă pentru a crea executabilul

Acest al doilea pas este efectuat de un program numit **linker** (editor de legături); gcc face de fapt ambele operații.

### Compilarea cu multiple fișiere

Dacă creați un program cu mai multe fișiere sursă, trebuie doar să includeți numele tuturor fișierelor sursă în apelul la gcc. Va crea apoi un fișier obiect pentru fiecare fișier sursă, și apoi va lega toate fișierele dvs. obiect împreună pentru a crea executabilul.

## Problema și soluția - Fișiere antet

Există o problemă, totuși. Dacă ați separat codul în fișiere separate (de obicei numite **module**), veți avea unele fișiere care fac apeluri la funcții din alte fișiere pentru a funcționa. Aceste fișiere nu află unul de celălalt până când linker-ul operează asupra lor; fișierele sunt compilate individual, iar compilatorul se va plânge dacă folosiți funcții într-un fișier despre care nu știe.

Rezolvăm acest lucru folosind **fișiere antet** (header files). Acestea sunt fișiere cu extensia `.h` care conțin **declarațiile** funcțiilor (și variabilelor globale) definite într-un modul, astfel încât compilatorul să poată fi informat despre ele când sunt folosite de un alt modul.

Am văzut deja acest lucru de multe ori; amintiți-vă de linia `#include <stdio.h>` din partea de sus a exemplelor? Acesta este exact acest proces; spune compilatorului că funcțiile declarate în fișierul antet de sistem `stdio.h` sunt folosite în acest modul.

> **MENȚINEȚI NUME CONSISTENTE**
> 
> Deși puteți numi fișierele antet cum doriți – nu există nimic magic în nume – este o bună practică să dați fișierului antet pentru funcțiile dintr-un anumit fișier C același nume ca fișierul C în sine, cu extensia `.h` în loc de `.c`. Acest lucru face mai ușor pentru cineva care citește codul dvs. să găsească fișierele unde sunt definite funcțiile.

## Împărțirea codului în mai multe fișiere

Să ne uităm la un exemplu despre cum funcționează acest lucru. Creați trei fișiere, două cu extensia `.c` și unul cu extensia `.h`, după cum urmează:

### function.c
```c
int add_vals (int a, int b, int c) 
{ 
  return a + b + c; 
}
```

### function.h
```c
extern int add_vals (int a, int b, int c);
```

### main.c
```c
#include <stdio.h> 
#include "function.h"

void main (void) 
{ 
  printf ("The total is %d\n", add_vals (1, 2, 3)); 
}
```

Puneți toate cele trei fișiere în același director și rulați gcc, dându-i numele ambelor fișiere `.c`:

```bash
gcc -o myprog main.c function.c
```

Programul rezultat va rula funcția main din `main.c`, care apelează funcția `add_vals` din `function.c`.

**Notă:** Funcția add_vals este apelată din funcția main – linker-ul conectează apelul din main.c la definiția funcției din function.c.

### Lucruri importante de observat:

1. **Cuvântul cheie `extern`:**
   ```c
   extern int add_vals (int a, int b, int c);
   ```
   În interiorul fișierului antet declarăm funcția cu cuvântul `extern` la începutul declarației. Aceasta îi spune compilatorului că această funcție urmează să fie găsită **extern** fișierului, adică într-un alt fișier C.

2. **Ghilimele vs. Paranteze unghiulare:**
   - `#include <stdio.h>` - Paranteze unghiulare `<>` pentru fișiere sistem
   - `#include "function.h"` - Ghilimele `""` pentru fișiere locale

Semnele `<>` spun compilatorului să caute fișierul în directorul unde sunt stocate fișierele include ale sistemului; semnele `""` indică faptul că fișierul este local și se află în același director cu fișierele `.c` pe care le construiți.

> **Dacă creați propriile fișiere antet, folosiți întotdeauna ghilimele duble în jurul numelui când le includeți.**

> **MAKEFILE-URI**
> 
> După cum vă puteți imagina, dacă aveți un proiect cu zeci sau sute de fișiere C, tastarea tuturor numelor lor în apelul la gcc de fiecare dată ar fi puțin plictisitoare! Proiectele mari sunt construite cu un instrument numit 'make', care stochează instrucțiuni de construire într-un 'Makefile'. Makefile-urile depășesc domeniul de aplicare al acestei cărți, dar există multe informații despre ele online.

## Preprocesorul

Deci ce face de fapt `#include`? Este o instrucțiune pentru **preprocesor** (preprocessor), care este prima etapă a compilării; substituie text în fișierele sursă înainte de a le transmite compilatorului în sine.

Preprocesorul este controlat cu ceea ce se numesc **directive**; acestea sunt ușor de identificat, deoarece toate încep cu un semn `#`.

### Directiva #include

Directiva `#include` instruiește preprocesorul să înlocuiască linia cu fișierul pe care îl include. Deci în exemplul nostru de mai sus, linia `#include "function.h"` din fișierul `.c` este înlocuită cu conținutul fișierului `function.h`, ceea ce înseamnă că ceea ce este transmis compilatorului arată astfel:

```c
#include <stdio.h> 
extern int add_vals (int a, int b, int c);

void main (void) 
{ 
  printf ("The total is %d\n", add_vals (1, 2, 3)); 
}
```

> **NU INCLUDEȚI FIȘIERE C**
> 
> `#include` va funcționa pe orice fișier; doar substituie linia include cu conținutul fișierului. Ocazional veți vedea acest lucru fiind abuzat; unii programatori ocolesc utilizarea fișierelor antet prin a include doar celelalte fișiere C în sine. Deși acest lucru funcționează, este o practică proastă; nu fiți tentați să o încercați!

## Directiva #define

O altă directivă utilă este `#define`, care poate fi folosită pentru a defini **valori constante**. Uitați-vă la acest exemplu:

```c
#include <stdio.h>
#define PI 3.14159

void main (void) 
{ 
  float rad = 3; 
  float circ = rad * 2 * PI; 
  float area = rad * rad * PI; 
  
  printf ("The circumference of a circle radius %f is %f\n",   
      rad, circ); 
  printf ("The area of a circle radius %f is %f\n", rad, area); 
}
```

Directiva `#define` este folosită pentru a seta valoarea lui pi. Lucrul important de reținut este că `PI` nu este o variabilă; este **text care va fi substituit de preprocesor**.

Linia `#define` îi spune preprocesorului să parcurgă fișierul și să înlocuiască fiecare instanță a textului `PI` cu cifrele `3.14159` înainte de a-l transmite compilatorului.

### De ce este util #define?

De ce să nu declarăm doar o variabilă float numită PI și să o setăm la 3.14159? O variabilă în virgulă mobilă necesită alocarea de memorie în care să o stocheze; folosirea `#define` economisește acea memorie, ceea ce este util dacă memoria este limitată.

### #define pentru funcții

Puteți, de asemenea, `#define` funcții:

```c
#include <stdio.h> 
#define ADD(a,b) (a+b)

void main (void) 
{ 
  printf ("The sum of %d and %d is %d\n", 5, 2, ADD(5,2)); 
  printf ("The sum of %d and %d is %d\n", 3, 7, ADD(3,7)); 
}
```

Din nou, aceasta face o substituție de text; ori de câte ori `ADD(a,b)` apare în cod, este înlocuit cu `(a+b)`, cu valorile lui a și b înlocuite de argumentele la ADD.

> **#DEFINE PENTRU TEXT**
> 
> Dacă folosiți #define pentru șiruri de text, acestea ar trebui să fie incluse în ghilimele duble, altfel textul înlocuit se va termina la primul spațiu. Deci folosiți:
> ```c
> #define MY_TEXT "This is some text to replace."
> ```
> Ghilimelele duble sunt incluse în înlocuire, deci apoi puteți apela doar:
> ```c
> printf(MY_TEXT);
> ```

## Directiva #if - Compilare condițională

Preprocesorul poate, de asemenea, evalua condiții cu directiva `#if`:

```c
#include <stdio.h>

void main (void) 
{ 
#if 0 
  printf ("Some code\n"); 
#else 
  printf ("Some other code\n"); 
#endif 
}
```

Cu un `0` după `#if`, codul dintre `#if` și `#else` nu este apelat, dar codul dintre `#else` și `#endif` este apelat.

Dacă schimbați valoarea după `#if` la `1`, codul dintre `#if` și `#else` este apelat, dar codul dintre `#else` și `#endif` nu este.

Acesta este un truc foarte util pentru a elimina sau înlocui temporar o bucată de cod când depanați.

**Notă:** Cea mai comună utilizare a #if este pentru eliminarea temporară a codului – doar înfășurați-l între un #if 0 și un #endif. #else este opțional, dar uneori doriți să substituiți codul pe care l-ați eliminat cu cod diferit.

## Rezumat

### Directivele preprocesorului:

| Directivă | Descriere | Exemplu |
|-----------|-----------|---------|
| `#include` | Include un fișier | `#include "myfile.h"` |
| `#define` | Definește o constantă | `#define MAX 100` |
| `#if` | Compilare condițională | `#if DEBUG` |
| `#else` | Alternativă pentru #if | `#else` |
| `#endif` | Închide bloc #if | `#endif` |
| `#ifdef` | Verifică dacă este definit | `#ifdef DEBUG` |
| `#ifndef` | Verifică dacă NU este definit | `#ifndef MYHEADER_H` |

### Structura unui proiect multi-fișier:

```
proiect/
├── main.c          (funcția main)
├── functii.c       (implementări funcții)
├── functii.h       (declarații funcții)
└── constante.h     (definiri constante)
```

### Exemplu complet de proiect:

**constante.h:**
```c
#ifndef CONSTANTE_H
#define CONSTANTE_H

#define MAX_SIZE 100
#define PI 3.14159

#endif
```

**calcule.h:**
```c
#ifndef CALCULE_H
#define CALCULE_H

extern float calculeaza_arie_cerc(float raza);
extern float calculeaza_circumferinta(float raza);

#endif
```

**calcule.c:**
```c
#include "constante.h"
#include "calcule.h"

float calculeaza_arie_cerc(float raza) {
    return PI * raza * raza;
}

float calculeaza_circumferinta(float raza) {
    return 2 * PI * raza;
}
```

**main.c:**
```c
#include <stdio.h>
#include "calcule.h"

int main(void) {
    float raza = 5.0;
    
    printf("Aria: %.2f\n", calculeaza_arie_cerc(raza));
    printf("Circumferința: %.2f\n", calculeaza_circumferinta(raza));
    
    return 0;
}
```

**Compilare:**
```bash
gcc -o program main.c calcule.c
```

### Protecție pentru includere multiplă:

```c
#ifndef MYHEADER_H
#define MYHEADER_H

// Conținutul fișierului antet

#endif
```

Acest model previne includerea multiplă a aceluiași fișier antet.

### Puncte cheie:

- ✅ Folosiți fișiere `.h` pentru declarații
- ✅ Folosiți fișiere `.c` pentru implementări
- ✅ Marcați declarațiile cu `extern` în fișiere antet
- ✅ Folosiți `""` pentru fișiere locale, `<>` pentru fișiere sistem
- ✅ `#define` pentru constante și macrocomenzi
- ✅ `#if` pentru debugging și compilare condițională
- ✅ Protejați fișierele antet împotriva includerii multiple
- ✅ Mențineți nume consistente între `.c` și `.h`

### Avantajele organizării în module:

- 🎯 **Claritate** - Cod mai ușor de înțeles
- 🎯 **Reutilizare** - Funcții reutilizabile în alte proiecte
- 🎯 **Colaborare** - Mai mulți dezvoltatori pot lucra simultan
- 🎯 **Întreținere** - Mai ușor de găsit și reparat bug-uri
- 🎯 **Compilare** - Recompilare selectivă doar a fișierelor modificate

**Felicitări! Ați finalizat Partea I - Programare în C!** 🎉

În capitolul următor, vom începe Partea a II-a despre programarea GUI cu GTK!
