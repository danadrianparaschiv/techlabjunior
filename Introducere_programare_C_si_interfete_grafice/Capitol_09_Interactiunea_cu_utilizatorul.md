# Capitolul 9: Interactiunea cu utilizatorul

Am văzut funcția `printf` folosită mult în capitolele anterioare; este modul standard de scriere a textului formatat de ieșire dintr-un program la consolă, linia de comandă de unde rulați programul. Dar ce se întâmplă dacă doriți să obțineți intrări de la utilizator? Cum citim ceea ce utilizatorul tastează în consolă?

## Funcția scanf

În ultimul capitol, am analizat funcția `sscanf` care citește valori dintr-un șir. Există o funcție echivalentă numită `scanf`, care citește valori direct din consolă, ca în exemplul următor:

```c
#include <stdio.h>

void main (void) 
{ 
  char input[256]; 
  int age;    
  
  printf ("What is your name, user?\n"); 
  scanf ("%s", input);    
  
  printf ("Hello, %s. How old are you?\n", input); 
  scanf ("%d", &age);    
  
  printf ("Well, %s, you look young for %d...\n", input, age); 
}
```

`scanf` funcționează exact ca `sscanf`, dar are cu un argument mai puțin, deoarece citește din consolă în loc de dintr-un șir.

### Probleme cu scanf

Cu toate acestea, nu este într-adevăr cel mai bun mod de a obține intrări de la consolă; funcționează doar dacă aveți un utilizator care tastează exact ceea ce vă așteptați. Din păcate, utilizatorii au o tendință neplăcută de a tasta lucruri pe care nu le așteptați, iar `scanf` nu face față bine acestui lucru.

De exemplu, în codul de mai sus, dacă utilizatorul tastează 257 de caractere când i se cere numele, aceștia vor depăși spațiul alocat pentru șirul de intrare, și s-ar putea întâmpla lucruri rele...

> **SCANF**
> 
> La fel ca sscanf, scanf returnează un întreg care indică câte valori a citit cu succes, pe care îl puteți folosi pentru a verifica erorile. O problemă este că scanf elimină doar valorile potrivite din buffer-ul de intrare, deci dacă un scanf nu reușește să potrivească nimic, ceea ce utilizatorul a tastat va fi citit din nou la următorul apel la scanf. Chiar este mai ușor să folosiți fgets și sscanf!

## O metodă mai bună - fgets

O abordare mai bună este să citiți fiecare linie pe care utilizatorul o introduce într-un șir buffer, și apoi să folosiți `sscanf` pentru a citi valori din acel șir. Funcția din biblioteca C `fgets` este utilă pentru acest lucru. Aruncați o privire la acest exemplu:

```c
#include <stdio.h>

void main (void) 
{ 
  char input[256], name[256]; 
  int age;    
  
  printf ("What is your name, user?\n"); 
  fgets (input, 256, stdin); 
  sscanf (input, "%s", name);    
  
  printf ("Hello, %s. How old are you?\n", name); 
  while (1) 
  { 
    fgets (input, 256, stdin); 
    if (sscanf (input, "%d", &age) == 1) break; 
    printf ("I don't recognise that as an age - try again!\n"); 
  }    
  
  printf ("Well, %s, you look young for %d...\n", name, age); 
}
```

### Parametrii funcției fgets

`fgets` primește trei argumente:

1. **Buffer-ul** în care ar trebui să stocheze intrarea
2. **Numărul maxim de bytes** pe care îl va scrie în acel buffer; acest lucru este util pentru a preveni situația de depășire menționată mai sus
3. **Locația de unde să citească**; în acest caz, este setat la `stdin` (prescurtare pentru 'standard input'), care îi spune să citească din consolă

> **STDIN ȘI STDOUT**
> 
> Vorbim despre stdin în acest capitol, care este fluxul 'standard input': ceea ce utilizatorul tastează la consolă. Uneori veți vedea referințe la stdout, care este fluxul 'standard output' – așa cum v-ați putea aștepta, aceasta este ieșirea care este tipărită la consolă, de obicei prin printf.

### Avantajele acestei metode

Deci, de fiecare dată când cerem utilizatorului intrări, folosim `fgets` pentru a citi până la 256 de caractere din ceea ce tastează (până în punctul în care apasă tasta ENTER), și apoi folosim `sscanf` pentru a interpreta. În plus, când cerem vârsta utilizatorului, folosim valoarea returnată de `sscanf` (descrisă în capitolul anterior) pentru a verifica că utilizatorul a introdus ceea ce vă așteptați și facem o buclă până când dau un răspuns valid.

Puteți folosi această metodă pentru a interpreta aproape orice tastează un utilizator și pentru a gestiona în siguranță toate cazurile în care tastează ceva neașteptat!

## Citirea parametrilor din linia de comandă

Există o altă modalitate de a obține intrări pentru programul dvs., care este să le furnizați ca parametru când porniți programul din linia de comandă.

### Adevărata definiție a funcției main

La acest punct, trebuie să recunosc că nu am fost pe deplin sincer pentru ultimele opt capitole... Am arătat întotdeauna definiția funcției main ca:

```c
void main (void)
```

Acest lucru funcționează, așa cum ați văzut, dar nu este strict corect. Definiția strictă a main arată astfel:

```c
int main (int argc, char *argv[])
```

Dar să fim sinceri: dacă v-aș fi arătat asta în capitolul 1, ați fi fugit o milă, nu-i așa? Deci ce înseamnă toate acestea?

### Valoarea de returnare

În primul rând, putem vedea că main returnează un întreg; acesta este un cod de succes sau eșec pe care unele sisteme de operare îl pot folosi pentru procesare într-un script shell sau similar. În mod tradițional, dacă un program are succes, main returnează 0, iar dacă eșuează, returnează un cod de eroare diferit de zero. Pentru programele care rulează pe cont propriu, chiar nu trebuie să vă faceți griji pentru acest lucru!

> **VERIFICAREA VALORILOR DE RETURNARE**
> 
> În Linux, valoarea de returnare dintr-un program nu este afișată, dar este stocată și poate fi citită din linia de comandă. Dacă tastați `echo $?` imediat după rularea unui program, valoarea pe care programul a returnat-o va fi afișată. Valorile de returnare sunt utile în principal dacă apelați programe din script-uri.

### Argumentul argc

Ceea ce este mai util sunt celelalte două argumente. `argc` este un întreg, și acesta este **numărul de parametri** care au fost furnizați pe linia de comandă când programul a fost pornit.

Ciudat, numărul include numele programului în sine, deci această valoare este întotdeauna 1 sau mai mare; dacă au fost furnizați parametri, va fi 2 sau mai mare.

### Argumentul argv

`char *argv[]`; acum asta e confuz, nu-i așa? Acesta este de fapt un compozit din câteva lucruri pe care le-am văzut deja:
- Este un `*`, deci este un pointer
- Tipul este `char`, deci sunt caractere în el
- Sunt paranteze pătrate, deci este un tablou

Acesta este de fapt un **tablou de pointeri la caractere**; fiecare element al tabloului este un șir, și fiecare șir este unul dintre parametrii furnizați programului.

> **OBȚINEȚI NUMĂRUL CORECT**
> 
> Amintiți-vă că primul element din tabloul argv – argv[0] – este numele programului în sine, nu primul parametru. Parametrii reali încep de la argv[1].

### Exemplu practic

Este probabil mai ușor de înțeles în practică:

```c
#include <stdio.h>

int main (int argc, char *argv[]) 
{ 
  int param = 0; 
  
  while (param < argc) 
  { 
    printf ("Parameter %d is %s\n", param, argv[param]); 
    param++; 
  } 
  
  return 0; 
}
```

Încercați să rulați acest program ca înainte, doar tastând numele său. Apoi încercați să tastați alte lucruri după nume pe linia de comandă și vedeți ce tipărește programul.

**Notă:** Argumentele argc și argv ale funcției main pot fi folosite pentru a accesa parametrii tastați pe linia de comandă când programul este rulat.

## Calculator simplu cu parametri

Iată un exemplu de calculator (foarte) simplu scris folosind parametri de program:

```c
#include <stdio.h>

int main (int argc, char *argv[]) 
{ 
  int arg1, arg2; 
  
  if (argc == 4) 
  { 
    sscanf (argv[1], "%d", &arg1); 
    sscanf (argv[3], "%d", &arg2); 
    
    if (*argv[2] == '+') printf ("%d\n", arg1 + arg2); 
    if (*argv[2] == '-') printf ("%d\n", arg1 - arg2); 
    if (*argv[2] == 'x') printf ("%d\n", arg1 * arg2); 
    if (*argv[2] == '/') printf ("%d\n", arg1 / arg2); 
  } 
  
  return 0; 
}
```

### Explicație

Observați că folosim `*argv[2]` pentru a obține primul caracter al celui de-al doilea parametru. Acesta ar trebui să fie întotdeauna doar un singur caracter, dar deoarece fiecare dintre argumente poate fi un șir, `argv[2]` (fără asterisc) este un pointer la un caracter, nu caracterul singur necesar pentru o comparație folosind `==`.

Asigurați-vă că separați argumentele de operator cu spații astfel încât să fie identificate ca parametri separați:
- ✅ Corect: `<progname> 2 + 2`
- ❌ Greșit: `<progname> 2+2`

**Notă:** Calculatorul citește cele două valori și operatorul din tabloul argv și tipărește rezultatul.

## Rezumat

### Metode de citire a intrărilor:

| Metodă | Descriere | Când să folosiți |
|--------|-----------|------------------|
| `scanf()` | Citește direct din consolă | ⚠️ Nu este recomandat - nesigur |
| `fgets() + sscanf()` | Citește linie, apoi parseză | ✅ Recomandat - sigur și flexibil |
| `argc` și `argv` | Parametri din linia de comandă | ✅ Pentru utilitare și script-uri |

### Funcția fgets:

```c
fgets(buffer, dimensiune, stdin);
```

- **buffer** - unde să stocheze input-ul
- **dimensiune** - maximum bytes de citit
- **stdin** - citește din consolă

### Structura main corectă:

```c
int main (int argc, char *argv[])
{
    // argc = numărul de parametri (include numele programului)
    // argv[0] = numele programului
    // argv[1] = primul parametru
    // argv[2] = al doilea parametru, etc.
    
    return 0; // 0 = succes, != 0 = eroare
}
```

### Exemplu complet și sigur:

```c
#include <stdio.h>
#include <string.h>

int main (int argc, char *argv[]) 
{
    char input[256];
    int number;
    
    // Citirea sigură de la consolă
    printf("Enter a number: ");
    fgets(input, 256, stdin);
    
    if (sscanf(input, "%d", &number) == 1) 
    {
        printf("You entered: %d\n", number);
    } 
    else 
    {
        printf("That's not a valid number!\n");
    }
    
    // Afișarea parametrilor din linia de comandă
    printf("\nCommand line arguments:\n");
    for (int i = 0; i < argc; i++) 
    {
        printf("argv[%d] = %s\n", i, argv[i]);
    }
    
    return 0;
}
```

### Puncte cheie:

- ✅ Folosiți `fgets()` + `sscanf()` în loc de `scanf()`
- ✅ Verificați întotdeauna valorile de returnare
- ✅ Validați intrările utilizatorului
- ✅ `argv[0]` este numele programului
- ✅ `argc` include numele programului în număr
- ✅ Returnați 0 pentru succes, != 0 pentru eroare
- ✅ Separați parametrii cu spații în linia de comandă

În capitolul următor, vom învăța despre citirea și scrierea fișierelor, extinzând capacitățile programelor noastre de a lucra cu date persistente!
