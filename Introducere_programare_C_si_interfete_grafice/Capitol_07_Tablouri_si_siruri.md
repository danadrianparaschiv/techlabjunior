# Capitolul 7: Tablouri și șiruri de caractere

Variabilele pe care le-am analizat până acum sunt toate valori numerice singulare. În acest capitol, vom analiza cum gestionează C listele de valori, iar acest lucru duce la folosirea listelor de litere pentru a stoca și manipula șiruri de text.

## Ce este un tablou?

Un **tablou** este o singură variabilă care stochează mai multe valori diferite de același tip; valorile individuale sunt accesate prin indexarea tabloului. Un tablou poate avea una sau mai multe dimensiuni:
- Un tablou unidimensional este o simplă listă de valori
- Un tablou bidimensional este o listă de liste de valori, și așa mai departe

## Declararea tablourilor

Un tablou este declarat în C prin punarea dimensiunii fiecărei dimensiuni în paranteze pătrate după numele variabilei. Deci:

```c
int a[10];
```

...este o listă de zece întregi, în timp ce:

```c
int b[5][6];
```

...este o listă de cinci liste, fiecare dintre ele conținând șase întregi.

## Indexarea tablourilor

Când accesați elementele dintr-un tablou, **indexul tabloului** – numărul din interiorul parantezei – începe de la **0**. Deci cele zece întregi conținute în tabloul `a` de mai sus sunt numite `a[0]`, `a[1]`, `a[2]`, și așa mai departe până la `a[9]`.

> **⚠️ ATENȚIE CRITICĂ!**
> 
> Compilatorul vă va permite să citiți sau să scrieți `a[10]`, `a[11]`, sau într-adevăr `a[orice număr doriți]`, dar toate acestea sunt în afara memoriei care a fost alocată când tabloul a fost declarat, deci scrierea în ele este o **idee foarte proastă**!

> **RĂMÂNEȚI ÎN INTERIORUL TABLOULUI**
> 
> Una dintre cele mai neplăcute surse de crash-uri și bug-uri în C este crearea unui tablou și apoi scrierea dincolo de sfârșitul acestuia. Compilatorul nu vă va opri să scrieți în memoria de la sfârșitul unui tablou, iar acest lucru poate avea consecințe grave. Asigurați-vă întotdeauna că indicii tabloului dvs. se încadrează în tabloul dvs.

## Tablouri și pointeri

Acest lucru ne aduce la relația dintre pointeri și tablouri. **Numele unui tablou este efectiv un pointer la primul element al tabloului.** Amintiți-vă că un pointer este adresa unei variabile în memorie? Ei bine, un tablou este un bloc contiguu de memorie care conține toate elementele tabloului în ordine, deci puteți folosi un pointer pentru a-l accesa.

De fapt, chiar dacă folosiți valori în paranteze pătrate pentru a-l accesa, compilatorul le tratează oricum ca pe un pointer. Iată un exemplu:

```c
#include <stdio.h>

void main (void) 
{ 
  int a[10]; 
  int count;
  
  for (count = 0; count < 10; count++) 
  { 
    a[count] = count * 10 + count; 
  } 
  
  printf ("The first and second elements of a are %d and %d\n",  
      a[0], a[1]); 
  printf ("Or, as pointers, %d and %d\n", *a, *(a+1)); 
}
```

Aceasta umple cele zece valori ale lui `a` cu numerele 0, 11, 22, 33 și așa mai departe, și apoi citește `a[0]` și `a[1]`. Apoi citește aceleași valori folosind `a` ca pointer, și puteți vedea, dacă rulați codul, că sunt identice.

> **NUMELE SUNT POINTERI**
> 
> Amintiți-vă că numele unui tablou sau al unui șir este doar un pointer la primul element al tabloului sau șirului în cauză și poate fi folosit în același mod ca orice alt pointer; poate fi incrementat și decrementat, sau dereferențiat pentru a găsi valoarea la care indică.

## Tablouri multidimensionale

Cu un tablou bidimensional (sau mai multe dimensiuni), trebuie să luați în considerare modul în care compilatorul aranjează dimensiunile în memorie; face acest lucru prin gruparea elementelor de la cel mai din dreapta index al tabloului împreună.

Cu tabloul `b[5][6]`:
- `b` în sine indică la `b[0][0]`
- `b+1` indică la `b[0][1]`
- `b+5` indică la `b[0][5]`
- `b+6` indică la `b[1][0]`

**Notă:** Elementele tabloului sunt stocate secvențial în memorie, cu numele tabloului ca pointer la primul element. Elementele tabloului multidimensional sunt stocate cu elementele cu valori învecinate în indexul cel mai din dreapta una lângă alta.

## Inițializarea tablourilor

Puteți inițializa un tablou în același timp cu declararea acestuia prin punerea valorilor în acolade:

```c
int a[10] = { 0, 11, 22, 33, 44, 55, 66, 77, 88, 99 };
```

Dar **observați** că acest lucru funcționează doar când tabloul este declarat pentru prima dată; odată ce există, nu puteți folosi această scurtătură și va trebui să iterați prin indicii tabloului, setând fiecare valoare pe rând.

## Șiruri de caractere (Strings)

În C, un șir este doar un alt tablou; este un tablou de caractere individuale. După cum am văzut în capitolul 2, un caracter este un tip specific în C, numit `char`; acesta deține un singur byte, ceea ce este suficient pentru a deține un caracter alfanumeric.

Deci un șir cu zece caractere ar fi:

```c
char mystring[10];
```

Sau, pentru a-l inițializa în același timp:

```c
char mystring[10] = "thestring";
```

### Terminatorul de șir

Un lucru important de reținut este că un șir în C trebuie să se termine întotdeauna cu un byte setat la zero, și că memoria necesară pentru a deține acest zero final (numit **terminator de șir**) trebuie să fie alocată când declarați șirul.

Deci `mystring`, care este declarat ca un tablou de zece char-uri, poate deține de fapt doar text de **nouă sau mai puține litere**.

**Notă:** Șirurile sunt stocate ca un tablou de caractere individuale, cu elementul de după ultimul caracter setat la zero.

> **TERMINAREA ȘIRURILOR**
> 
> Amintiți-vă întotdeauna că memoria pe care o alocați pentru un șir trebuie să fie suficient de lungă pentru a deține toate caracterele, **plus unul suplimentar** pentru a stoca terminatorul zero. Dacă manipulați șirurile singur cu pointeri, asigurați-vă că vă amintiți să scrieți zero la sfârșitul oricărui șir pe care îl creați.

## Manipularea șirurilor cu pointeri

Puteți folosi indexul în paranteze pătrate pentru a accesa caractere individuale într-un șir, sau puteți folosi un pointer. Iată un exemplu de folosire a pointerilor pentru a uni două șiruri împreună:

```c
#include <stdio.h>

void main (void) 
{ 
  char str1[10] = "first"; 
  char str2[10] = "second";  
  char str3[20]; 
  char *src, *dst;
  
  src = str1; 
  dst = str3; 
  while (*src != 0) 
  { 
    *dst = *src; 
    src++; 
    dst++;  
  } 
  
  src = str2; 
  while (*src != 0) 
  { 
    *dst = *src; 
    src++; 
    dst++;  
  } 
  *dst = 0;
  
  printf ("%s + %s = %s\n", str1, str2, str3); 
}
```

### Explicația codului:

1. Mai întâi, creăm două șiruri – `str1` este 'first' și `str2` este 'second' – și alocăm un șir gol, `str3`, pentru a pune rezultatul.

2. Apoi creăm o pereche de pointeri char și indicăm `src` la începutul lui `str1` (la 'f' din 'first') și `dst` la începutul lui `str3` gol.

3. Apoi facem o buclă, copiind ce este la `src` la `dst`, și apoi mutând ambii pointeri înainte cu unu, până când găsim zero-ul care termină `str1`.

4. Apoi indicăm `src` la `str2` și facem același lucru din nou, până când găsim zero-ul de la sfârșitul lui `str2`.

5. În cele din urmă, scriem un zero la sfârșitul lui `str3` pentru a-l termina.

### Format specifiers pentru șiruri

Observați noul specificator de format folosit pentru a tipări șiruri:
- **`%s`** este folosit pentru a tipări un șir și va afișa fiecare caracter de la pointerul furnizat ca argument, până la primul zero de terminare pe care îl găsește
- **`%c`** poate fi folosit pentru a tipări un singur caracter

## Scrierea în șiruri

Deoarece numele unei variabile șir este doar un pointer la primul caracter al șirului, **nu puteți folosi doar un semn egal pentru a seta valoarea unui șir complet**. Puteți inițializa o variabilă șir în momentul în care o declarați, ca mai sus, dar ce se întâmplă dacă doriți să o setați sau să o schimbați mai târziu?

### Funcția sprintf

Există câteva moduri de a face acest lucru, dar cel mai util este funcția `sprintf`; aceasta este o versiune a funcției `printf` pe care am văzut-o deja, care scrie text arbitrar în variabile șir. Singura diferență este că primul argument pe care îl ia este numele unei variabile șir, și scrie în aceea în loc de terminal:

```c
#include <stdio.h>

void main (void) 
{ 
  int val = 12; 
  char string[50];
  
  sprintf (string, "The value of val is %d\n", val); 
  printf ("%s", string); 
}
```

Funcția `sprintf` va adăuga automat terminatorul zero la sfârșitul oricărui șir pe care îl creați cu ea.

## Rezumat

### Tablouri:
```c
// Declarare
int numbers[5];              // Tablou de 5 întregi
int matrix[3][4];            // Tablou 2D: 3 rânduri × 4 coloane

// Inițializare
int values[5] = {1, 2, 3, 4, 5};

// Accesare
numbers[0] = 10;             // Primul element (indexul 0)
numbers[4] = 50;             // Ultimul element (indexul 4)
```

### Șiruri de caractere:
```c
// Declarare și inițializare
char name[20] = "John";      // Șir de max 19 caractere + '\0'

// Accesare caractere individuale
name[0] = 'J';               // Primul caracter
name[1] = 'o';               // Al doilea caracter

// Scriere în șir
sprintf(name, "Hello %s", "World");

// Afișare
printf("%s\n", name);        // Afișează întregul șir
printf("%c\n", name[0]);     // Afișează primul caracter
```

### Puncte cheie:
- ✅ Tablourile încep de la indexul 0
- ✅ Numele tabloului este un pointer la primul element
- ✅ Șirurile sunt tablouri de char terminate cu '\0'
- ✅ Alocați întotdeauna spațiu pentru terminatorul '\0'
- ✅ Nu scrieți niciodată dincolo de limitele tabloului
- ✅ Folosiți `sprintf()` pentru a scrie în șiruri

În capitolul următor, vom analiza unele dintre funcțiile furnizate în biblioteca de gestionare a șirurilor din C pentru a face munca cu șirurile mai ușoară.
