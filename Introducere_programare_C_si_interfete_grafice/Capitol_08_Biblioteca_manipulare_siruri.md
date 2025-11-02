# Capitolul 8: Biblioteca de șiruri

În capitolul anterior, am văzut cum să accesăm șiruri folosind pointeri. Acest lucru funcționează perfect, și vă oferă o bună înțelegere a modului în care funcționează pointerii, dar este destul de lung. Din fericire, C oferă o bibliotecă de funcții utile pentru șiruri, care economisesc multă tastare!

În ultimul capitol, am văzut cum să unim două șiruri împreună folosind pointeri. Vom face același lucru folosind biblioteca de gestionare a șirurilor. Iată codul rescris folosind funcții din biblioteca de șiruri:

```c
#include <stdio.h> 
#include <string.h>

void main (void) 
{ 
  char str1[10] = "first"; 
  char str2[10] = "second"; 
  char str3[20];
  
  strcpy (str3, str1); 
  strcat (str3, str2);
  
  printf ("%s + %s = %s\n", str1, str2, str3); 
}
```

E mult mai scurt! Observați `#include <string.h>` la început, care îi spune compilatorului că vrem să folosim funcții din biblioteca de șiruri.

> **RĂMÂNEȚI ÎN INTERIORUL ȘIRULUI**
> 
> Funcțiile bibliotecii de șiruri, în general, nu vă vor împiedica să scrieți dincolo de sfârșitul unui șir; la fel ca atunci când folosiți pointeri, când folosiți funcții de bibliotecă tot trebuie să vă asigurați că variabilele șir sunt suficient de mari pentru valorile pe care le scrieți în ele.

## Funcțiile strcpy și strcat

Acest cod ne arată două funcții pentru șiruri:

### strcpy - Copierea șirurilor

**`strcpy`** ('string copy' - copiază șir) copiază șirul de la al doilea argument la începutul șirului de la primul argument.

```c
strcpy (destinatie, sursa);
```

### strcat - Concatenarea șirurilor

**`strcat`** ('string concatenate' - concatenează șir) face același lucru, dar în loc să copieze la începutul primului argument, găsește zero-ul de terminare al primului argument și începe să copieze la locația acestuia, unind astfel cele două șiruri împreună.

```c
strcat (destinatie, sursa);
```

> **NU SUPRASCRIEȚI**
> 
> Pare că ar trebui să fie posibil să folosiți `strcpy` și `strcat` pentru a copia o parte a unui șir peste el însuși – `strcpy (a + 1, a)`, de exemplu. Nu încercați! Zonele de memorie sursă și destinație pentru `strcpy` și `strcat` trebuie să fie complet separate; dacă nu, comportamentul lor este imprevizibil.

## Compararea șirurilor

O altă cerință comună este să puteți compara două șiruri pentru a vedea dacă sunt la fel. După cum am văzut deja, putem compara valori numerice cu operatorul `==`, dar acest lucru nu funcționează cu șirurile.

Amintiți-vă că numele unui șir este de fapt doar un pointer la o locație în memorie care conține șirul, deci folosirea `==` pentru a compara două șiruri vă va spune doar dacă sunt în același loc în memorie, nu dacă două șiruri de la locații diferite sunt la fel.

### Comparare manuală

Puteți folosi `==` pentru a compara două variabile char, iar un șir este un tablou de char-uri, deci este posibil să scrieți o bucată simplă de cod care compară fiecare caracter dintr-un șir pe rând:

```c
#include <stdio.h>

void main (void) 
{ 
  char str1[10] = "first"; 
  char str2[10] = "fire"; 
  char *ptr1 = str1, *ptr2 = str2;
  
  while (*ptr1 != 0 && *ptr2 != 0) 
  { 
    if (*ptr1 != *ptr2) 
    { 
      break; 
    } 
    ptr1++; 
    ptr2++; 
  }
  
  if (*ptr1 == 0 && *ptr2 == 0) 
  { 
    printf ("The two strings are identical.\n"); 
  } 
  else 
  { 
    printf ("The two strings are different.\n"); 
  } 
}
```

### strcmp - Comparare simplificată

Dar este destul de plictisitor să scrieți acest lucru de fiecare dată, deci biblioteca de șiruri poate face acest lucru pentru dvs. cu funcția **`strcmp`** (pentru 'string compare' - compară șiruri). Iată cum o folosiți:

```c
#include <stdio.h> 
#include <string.h>

void main (void) 
{ 
  char str1[10] = "first"; 
  char str2[10] = "fire"; 
  
  if (strcmp (str1, str2) == 0) 
  { 
    printf ("The two strings are identical.\n"); 
  } 
  else 
  { 
    printf ("The two strings are different.\n"); 
  } 
}
```

`strcmp` primește două șiruri ca argumente și returnează **0** dacă sunt la fel; returnează o valoare diferită de zero dacă nu sunt.

### strncmp - Comparare parțială

Ce se întâmplă dacă doriți să comparați doar primele câteva caractere ale unui șir, nu întregul șir? Există o funcție de bibliotecă și pentru asta: **`strncmp`** (pentru 'string numbered compare' - compară șiruri numărând).

Aceasta funcționează exact în același mod ca `strcmp`, dar primește un al treilea argument, un întreg care indică numărul de caractere de comparat.

Deci:
- `strncmp ("first", "fire", 4)` ar returna o valoare diferită de zero
- `strncmp ("first", "fire", 3)` ar returna 0

> **IGNORAREA MAJUSCULELOR**
> 
> Există versiuni ale `strcmp` și `strncmp` care ignoră majusculele literelor din șirurile comparate; se numesc `strcasecmp` și `strncasecmp`, respectiv. Primesc aceleași argumente și returnează aceleași valori.

## Citirea valorilor dintr-un șir

Am văzut în capitolul anterior că putem folosi `sprintf` pentru a scrie variabile într-un șir; ce zici de a putea citi variabilele înapoi dintr-un șir? Funcția **`sscanf`** ('string scan formatted' - scanează șir formatat) face asta pentru dvs. Iată cum funcționează:

```c
#include <stdio.h>

void main (void) 
{ 
  int val; 
  char string[10] = "250";
  
  sscanf (string, "%d", &val); 
  printf ("The value in the string is %d\n", val); 
}
```

`sscanf` folosește exact aceiași specificatori de format ca `printf`. O diferență importantă, totuși, este că argumentele pentru `sscanf` trebuie să fie toate **pointeri** la variabile, mai degrabă decât variabilele în sine. Ca întotdeauna, o funcție nu poate niciodată să schimbe valorile variabilelor furnizate ca argumente, dar poate scrie la destinațiile lor dacă sunt pointeri.

**Notă:** Funcția bibliotecii sscanf este folosită aici cu specificatorul de format %d pentru a citi valoarea zecimală 250 dintr-un șir.

### Verificarea succesului

Puteți verifica dacă `sscanf` a putut potrivi specificatorii de format cu șirul furnizat prin analizarea valorii pe care o returnează; `sscanf` returnează **numărul de valori** pe care le-a citit cu succes.

Deci, de exemplu:
- Dacă un specificator de format `%d` este furnizat dar șirul furnizat nu începe cu un număr zecimal, `sscanf` va scrie nimic în pointerul furnizat și va returna 0
- Dacă șirul furnizat începe cu un număr zecimal, `sscanf` va returna 1

### Format string complex

Șirul de format furnizat pentru `sscanf` poate conține mai mulți specificatori de format și chiar alt text:

```c
#include <stdio.h>

void main (void) 
{ 
  int val; 
  char result[10]; 
  char string[25] = "The first number is 1";
  
  if (sscanf (string, "The %s number is %d", result, &val) == 2) 
  { 
    printf ("String : %s Value : %d\n", result, val); 
  } 
  else 
  { 
    printf ("I couldn't find two values in that string.\n"); 
  } 
}
```

Observați că, puțin inconsecvent, specificatorul de format `%s` denotă un pointer la un șir atât în `printf`, cât și în `sscanf`, în timp ce specificatorul `%d` denotă o variabilă în `printf`, dar un pointer în `sscanf`.

> **ȘIRURI SSCANF**
> 
> Specificatorul de format `%s` potrivește un set de caractere care nu sunt spații albe în sscanf; va extrage primul set de litere, numere sau punctuație până la primul spațiu, tab sau linie nouă pe care îl găsește în șirul scanat. Un spațiu în șirul de format potrivește unul sau mai multe caractere de spațiu alb, nu doar un singur spațiu.

Un lucru de remarcat despre `sscanf` este că se află în biblioteca standard I/O, nu în biblioteca de gestionare a șirurilor, deci nu aveți nevoie de `#include <string.h>` pentru a-l folosi.

**Notă:** sscanf citește valori numerice și cuvinte dintr-un șir formatat, permițându-vă să analizați text din altă parte. Amintiți-vă că toate argumentele pentru sscanf trebuie să fie pointeri.

## Lungimea unui șir

O ultimă funcție utilă de gestionare a șirurilor este **`strlen`** (pentru 'string length' - lungime șir); după cum sugerează numele, aceasta vă spune câte caractere sunt într-un șir, excluzând caracterul zero de terminare.

```c
#include <stdio.h> 
#include <string.h>

void main (void) 
{ 
  char str1[10] = "first";
  
  printf ("The length of the string '%s' is %d\n", str1, 
      strlen (str1)); 
}
```

## Rezumat

Toate operațiile pe care le-am analizat aici sunt posibile prin manipularea manuală a pointerilor; biblioteca de șiruri doar le face mai ușoare și vă va face codul mai scurt. Dacă vă găsiți mutând pointeri în jurul șirurilor într-un program, verificați întotdeauna biblioteca de șiruri pentru a vă asigura că nu reinventați roata!

### Funcții principale din biblioteca de șiruri:

| Funcție | Descriere | Exemplu |
|---------|-----------|---------|
| `strcpy(dest, src)` | Copiază șirul sursă în destinație | `strcpy(s1, "hello");` |
| `strcat(dest, src)` | Adaugă șirul sursă la sfârșitul destinației | `strcat(s1, " world");` |
| `strcmp(s1, s2)` | Compară două șiruri (returnează 0 dacă sunt egale) | `if (strcmp(s1, s2) == 0)` |
| `strncmp(s1, s2, n)` | Compară primele n caractere | `strncmp(s1, s2, 5)` |
| `strlen(s)` | Returnează lungimea șirului (fără '\0') | `len = strlen(s1);` |
| `sscanf(s, format, ...)` | Citește valori formatate dintr-un șir | `sscanf(s, "%d", &val);` |
| `sprintf(s, format, ...)` | Scrie valori formatate într-un șir | `sprintf(s, "%d", val);` |

### Variante suplimentare:

| Funcție | Descriere |
|---------|-----------|
| `strcasecmp(s1, s2)` | Compară ignorând majusculele |
| `strncasecmp(s1, s2, n)` | Compară n caractere ignorând majusculele |

### Puncte cheie de reținut:

- ✅ Includeți `<string.h>` pentru funcțiile de șiruri
- ✅ `strcmp` returnează 0 când șirurile sunt EGALE
- ✅ `sscanf` necesită pointeri ca argumente
- ✅ `strlen` NU include terminatorul '\0'
- ✅ Verificați întotdeauna că destinația are suficient spațiu
- ✅ Nu suprascrieți un șir peste el însuși
- ✅ `sscanf` returnează numărul de elemente citite cu succes

### Exemplu complet:

```c
#include <stdio.h>
#include <string.h>

void main (void) 
{
    char first[20] = "Hello";
    char second[20] = "World";
    char combined[40];
    
    // Copiază primul șir
    strcpy(combined, first);
    
    // Adaugă un spațiu
    strcat(combined, " ");
    
    // Adaugă al doilea șir
    strcat(combined, second);
    
    // Afișează rezultatul și lungimea
    printf("Result: %s\n", combined);
    printf("Length: %d\n", strlen(combined));
    
    // Compară șiruri
    if (strcmp(first, "Hello") == 0) 
    {
        printf("First string is 'Hello'\n");
    }
}
```

În capitolul următor, vom învăța cum să citim intrări de la utilizator, făcând programele noastre mai interactive!
