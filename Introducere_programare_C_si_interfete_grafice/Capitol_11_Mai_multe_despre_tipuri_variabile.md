# Capitolul 11: Mai multe despre tipuri și variabile

În acest capitol, vom analiza unele dintre subiectele mai avansate legate de utilizarea variabilelor și tipurilor, inclusiv diferența dintre variabile locale și globale, definirea de tipuri noi și utilizarea enumerărilor și structurilor de date.

Când am folosit variabile în exemplele din această carte, le-am pus întotdeauna în interiorul definițiilor de funcții. Acestea sunt prin urmare **variabile locale**; adică variabile care sunt locale pentru acele funcții și nu au semnificație în afara funcției.

## Variabile globale

C permite, de asemenea, **variabile globale**; adică variabile care sunt definite în afara tuturor funcțiilor. Acestea au **domeniu global** (global scope), ceea ce înseamnă că pot fi citite și scrise din orice funcție din cadrul programului. Să ne uităm la un exemplu:

```c
#include <stdio.h>

int result;

void add (int a, int b) 
{ 
  result = a + b; 
}

void main (void) 
{ 
  add (3, 4); 
  printf ("The result is %d\n", result); 
}
```

În acest exemplu, variabila `result` este globală. Prin urmare, poate fi citită sau scrisă atât în funcția `add`, cât și în funcția `main`; după cum puteți vedea, scriem o valoare în ea în `add` și o citim înapoi în `main`, și astfel nu trebuie să returnăm o valoare din `add`.

### De ce să nu folosim variabile globale peste tot?

În unele privințe, acest lucru pare mai ușor decât să transmiteți valori peste tot, nu-i așa? Deci de ce să nu facem asta tot timpul? Răspunsul este **memoria**. 

- **Variabilele locale** în funcții sunt alocate temporar spațiu în timp ce funcția rulează, iar memoria este eliberată de îndată ce funcția se termină
- **Variabilele globale** sunt alocate spațiu când programul pornește, și acel spațiu nu este eliberat până când programul se termină
- Dacă alocați suficient de multe variabile globale, puteți rămâne fără memorie pe unele sisteme

Există o metodă mai bună de a face o mulțime de date disponibile pentru fiecare funcție, la care vom ajunge puțin mai târziu...

> **FOLOSIȚI NUME DIFERITE**
> 
> Deși este perfect valid să dați unei variabile locale același nume ca unei variabile globale în același program, nu faceți asta! Dacă aveți o variabilă globală și una locală cu același nume, versiunea locală este folosită în funcția în care este declarată, iar cea globală este folosită peste tot – acest lucru poate duce la comportament neașteptat.

## Definiții de tipuri (typedef)

În capitolul 2, am analizat gama de tipuri de variabile în C: `char`, `int`, `float`, și așa mai departe. C vă permite, de asemenea, să definiți propriile tipuri, cu ceea ce este cunoscut ca un **typedef**.

### Sintaxa typedef

Un typedef este o linie de format:

```c
typedef <tip_existent> <nume_nou>;
```

De obicei, este pus la începutul unui program. De exemplu:

```c
typedef unsigned char BYTE;
```

Aceasta definește un tip nou numit `BYTE`, care este un alt nume pentru un `unsigned char`.

> **NOTĂ:** Prin convenție, tipurile definite de utilizator primesc de obicei nume cu litere mari. Nu este obligatoriu, dar ajută la distingerea lor de variabile atunci când citiți codul.

### De ce să folosim typedef?

Când spunem că aceasta definește un tip nou, ceea ce face de fapt este să creeze un **alias** la un tip existent. Acest lucru pare oarecum inutil, dar poate ajuta în două moduri:

1. **Claritate** - Poate face mai evident ce face codul dvs. dacă faceți numele tipurilor specifice datelor programului dvs.
2. **Siguranță** - Prin definirea tipurilor specifice, puteți determina compilatorul să vă avertizeze dacă folosiți tipul greșit pentru un argument de funcție sau o variabilă

Există câteva cazuri specifice în care typedef-urile sunt deosebit de utile: acestea sunt **tipurile enumerate** și **structurile de date**.

## Tipuri enumerate (enum)

Adesea, există nevoie de o variabilă care poate lua doar una dintre câteva valori posibile. C oferă un tip numit `enum` în acest scop, care definește un întreg cu un set fix de valori denumite.

Iată un exemplu:

```c
#include <stdio.h>

typedef enum { 
  false, 
  true 
} BOOLEAN;

void main (void) 
{ 
  BOOLEAN b_var;
  
  b_var = false; 
  if (b_var == true) 
  { 
    printf ("TRUE\n"); 
  } 
  else 
  { 
    printf ("FALSE\n"); 
  } 
}
```

După cum puteți vedea, valorile denumite ale tipului enumerat sunt folosite în loc de numere pentru atribuiri și comparații. Acest lucru poate face codul mult mai ușor de înțeles și este o modalitate foarte bună de a preveni erorile, deoarece o variabilă enumerată poate fi setată doar la o valoare validă.

> **ENUM-URI NUMEROTATE**
> 
> Când creați un enum, compilatorul atribuie o valoare numerică fiecăreia dintre valorile posibile. În mod implicit, numerotează prima din listă ca 0 și contorizează în sus de acolo. Puteți suprascrie acest lucru punând un semn egal după fiecare valoare denumită și setând-o la valoarea pe care o doriți.

### Exemplu de enum cu valori personalizate:

```c
typedef enum {
  LUNI = 1,
  MARTI = 2,
  MIERCURI = 3,
  JOI = 4,
  VINERI = 5,
  SAMBATA = 6,
  DUMINICA = 7
} ZI_SAPTAMANA;
```

## Structuri de date (struct)

Celălalt lucru foarte util pe care îl puteți face cu un typedef este să îl folosiți pentru a defini o **structură de date**. Aceasta este o colecție de variabile individuale care sunt grupate împreună, permițându-vă să transmiteți structura între funcții în loc de variabilele individuale.

Iată un exemplu:

```c
#include <stdio.h>

typedef struct { 
  int inval1; 
  int inval2; 
  int outval; 
} MY_DATA;

void add (MY_DATA *d) 
{ 
  d->outval = d->inval1 + d->inval2; 
}

void main (void) 
{ 
  MY_DATA data;
  
  data.inval1 = 5; 
  data.inval2 = 7; 
  add (&data);
  
  printf ("The sum of %d and %d is %d\n", data.inval1,  
      data.inval2, data.outval); 
}
```

### Explicația structurii:

Deci aici folosim un typedef pentru a crea un tip de date numit `MY_DATA`. Definiția structurii constă din:
- Cuvântul cheie `struct`
- O listă de variabile închise în acolade
- În acest caz, structura constă din trei variabile întregi

**Notă:** O instanță a structurii MY_DATA este folosită pentru a transmite cele trei întregi la funcția add.

### Accesarea elementelor structurii

În funcția `main`, declarăm o **instanță** a structurii ca variabilă numită `data` de tip `MY_DATA`. Apoi accesăm elementele individuale ale structurii prin:

```c
nume_structura.nume_element
```

De exemplu:
- `data.inval1 = 5` - setează valoarea elementului `inval1` din `data` la 5

### Accesarea prin pointeri

Funcția `add` primește un **pointer** la o structură `MY_DATA` ca singur argument; ca întotdeauna, o funcție nu poate schimba valorile argumentelor sale, dar poate schimba valorile la care indică argumentele sale, deci transmitem un pointer în loc de structura în sine.

Pentru a accesa elementele unei structuri dintr-un pointer la ea, înlocuim punctul (`.`) cu o **săgeată** formată dintr-un semn minus și un semn mai mare (`->`).

```c
pointer_structura->nume_element
```

Deci funcția `add` citește valorile lui `inval1` și `inval2` din structura la care indică `d`, și apoi scrie rezultatul înapoi în `outval` din aceeași structură; funcția `main` apoi tipărește rezultatul din structură.

> **. VS ->**
> 
> Când accesați elementele unei structuri, asigurați-vă că folosiți simbolul corect:
> - Folosiți `.` dacă variabila dvs. este o **instanță** a structurii în sine
> - Folosiți `->` dacă variabila dvs. este un **pointer** la o instanță a structurii
> 
> Folosirea celui greșit va da de obicei o eroare.

> **TIPURI NOI ÎN INTERIORUL STRUCTURILOR**
> 
> O structură poate conține alte tipuri noi (tipuri simple, enum-uri sau chiar alte structuri); doar asigurați-vă că typedef-urile pentru acestea apar înaintea typedef-ului structurii în care doriți să le includeți.

## Avantajele structurilor

Structurile sunt foarte utile dacă trebuie să transmiteți o mulțime de date între funcții; pot fi mult mai eficiente din punct de vedere al memoriei decât să aveți un număr mare de variabile globale, deoarece trebuie să creați structura doar când aveți nevoie de ea, mai degrabă decât să ocupați memorie tot timpul.

## Rezumat

### Comparație între tipuri de variabile:

| Tip | Domeniu | Durată de viață | Memorie |
|-----|---------|-----------------|---------|
| **Locale** | În funcție | Timp de execuție funcție | Eliberată automat |
| **Globale** | Întregul program | Întreaga durată program | Ocupată permanent |

### Sintaxă typedef:

```c
// Tip simplu
typedef unsigned int UINT;

// Enumerare
typedef enum {
  VALOARE1,
  VALOARE2,
  VALOARE3
} NUME_ENUM;

// Structură
typedef struct {
  int camp1;
  float camp2;
  char camp3[20];
} NUME_STRUCT;
```

### Exemple practice:

```c
#include <stdio.h>

// Definiții de tipuri
typedef enum {
  ROSU,
  GALBEN,
  VERDE
} CULOARE_SEMAFOR;

typedef struct {
  char nume[50];
  int varsta;
  float salariu;
} ANGAJAT;

void proceseaza_angajat(ANGAJAT *a) {
  printf("Nume: %s\n", a->nume);
  printf("Varsta: %d\n", a->varsta);
  printf("Salariu: %.2f\n", a->salariu);
}

int main(void) {
  // Folosire enum
  CULOARE_SEMAFOR semafor = VERDE;
  
  if (semafor == VERDE) {
    printf("Mergi!\n");
  }
  
  // Folosire struct
  ANGAJAT ang;
  sprintf(ang.nume, "Ion Popescu");
  ang.varsta = 30;
  ang.salariu = 5000.50;
  
  proceseaza_angajat(&ang);
  
  return 0;
}
```

### Puncte cheie:

- ✅ **Variabile locale** - Preferați-le pentru economie de memorie
- ✅ **Variabile globale** - Folosiți cu moderație
- ✅ **typedef** - Face codul mai clar și mai sigur
- ✅ **enum** - Pentru valori cu opțiuni limitate
- ✅ **struct** - Pentru gruparea datelor înrudite
- ✅ **`.` pentru instanțe** - `data.camp`
- ✅ **`->` pentru pointeri** - `ptr->camp`

### Când să folosiți fiecare:

| Concept | Când să folosiți |
|---------|------------------|
| Variabile locale | Întotdeauna când este posibil |
| Variabile globale | Doar pentru date cu adevărat globale |
| typedef | Pentru claritate și siguranță tip |
| enum | Pentru valori din set finit |
| struct | Pentru date complexe înrudite |

În capitolul următor, vom învăța despre fișierele antet și preprocesorul, care ne vor ajuta să organizăm programe mai mari!
