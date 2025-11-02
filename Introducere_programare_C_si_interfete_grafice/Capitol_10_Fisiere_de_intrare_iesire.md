# Capitolul 10: Fișiere de intrare și ieșire - Lucrul cu fișiere

În capitolul anterior, am analizat cum să obținem intrări de la utilizator la consolă. În acest capitol, vom analiza cealaltă metodă comună de intrare și ieșire în C: citirea și scrierea fișierelor.

Multe programe trebuie să poată accesa fișiere de pe discul computerului gazdă; chiar dacă este doar pentru salvarea preferințelor utilizatorului și altele asemănătoare, accesul la fișiere este o cerință fundamentală pentru multe sarcini de programare.

## Pointeri de fișiere (FILE pointers)

În C, fișierele sunt accesate prin utilizarea **pointerilor de fișiere**. Un pointer de fișier conține toate informațiile necesare pentru a accesa un fișier:
- Numele și locația sa pe sistemul de fișiere
- Poziția curentă în fișier la care datele vor fi citite sau scrise

Deci primul lucru pe care trebuie să-l facem este să obținem un pointer de fișier. Acest lucru se face folosind funcția C `fopen`, care primește două argumente:
1. **Calea către fișier**, inclusiv numele și extensia sa
2. **Modul de acces la fișier** - un cod care indică dacă intenționați să citiți din fișier sau să scrieți în el

> **VERIFICAȚI ÎNTOTDEAUNA POINTERUL DE FIȘIER**
> 
> Nu presupuneți niciodată că fopen a funcționat – verificați întotdeauna că valoarea pe care o returnează este un pointer valid (adică nu zero). Dacă încercați să citiți dintr-un pointer zero, veți obține nonsens aleatoriu; dacă scrieți într-un pointer zero, probabil veți bloca computerul!

## Citirea unui fișier

Să ne uităm la un exemplu de citire a unui fișier. Folosiți editorul de text pentru a crea un fișier numit `input.txt` în directorul `/home/pi` pe Raspberry Pi, și tastați orice doriți în el. Salvați-l, și apoi creați și rulați următorul program:

```c
#include <stdio.h>

void main (void) 
{ 
  FILE *fp; 
  int value;
  
  fp = fopen ("/home/pi/input.txt", "rb"); 
  if (fp) 
  { 
    while (1) 
    { 
      value = fgetc (fp); 
      if (value == EOF) break; 
      else printf ("%c", value); 
    } 
    fclose (fp); 
  } 
}
```

### Explicația codului:

1. **Declarăm variabilele:**
   - Un pointer de fișier numit `fp`, care are tipul `FILE *`
   - Un întreg care îl vom folosi pentru a păstra caracterele citite din fișier

2. **Creăm pointerul de fișier:**
   ```c
   fp = fopen ("/home/pi/input.txt", "rb");
   ```
   - Deschidem fișierul la `/home/pi/input.txt`
   - Setăm modul la `"rb"`, care indică 'read binary' (citire binară)
   - Aceasta creează pointerul de fișier și îl inițializează la începutul fișierului

3. **Verificăm dacă fișierul s-a deschis:**
   ```c
   if (fp)
   ```
   - Verificăm dacă pointerul de fișier este diferit de zero
   - Dacă pointerul este returnat ca zero, fișierul nu a fost deschis cu succes
   - Pentru citire, aceasta indică de obicei că fișierul nu există

4. **Citim fișierul:**
   ```c
   value = fgetc (fp);
   ```
   - Apelăm funcția `fgetc` ('file get character') într-o buclă
   - De fiecare dată când această funcție este apelată, citește un singur byte din fișier
   - Apoi avansează pointerul de fișier la următorul byte din fișier
   - Când pointerul de fișier ajunge la sfârșitul fișierului, returnează valoarea specială `EOF` ('end of file')
   - Tipărim valoarea returnată de fgetc de fiecare dată până când returnează EOF

5. **Închidem fișierul:**
   ```c
   fclose (fp);
   ```
   - Odată ce am terminat citirea fișierului, finalizăm accesul la el
   - Aceasta eliberează pointerul de fișier și vă permite să-l reutilizați pentru a accesa alt fișier

> **NOTĂ IMPORTANTĂ**
> 
> Deși fgetc citește caractere, returnează un întreg; acest lucru se datorează faptului că codul pentru EOF se află în afara intervalului valid al unei variabile char (0–255). Cu excepția cazului când este la sfârșitul unui fișier, fgetc returnează o valoare întreagă care poate fi întotdeauna tratată ca un char.

## Scrierea într-un fișier

Pentru a scrie într-un fișier, folosim un pointer de fișier în exact același mod, dar îl deschidem într-un mod pentru scriere.

```c
#include <stdio.h>

void main (void) 
{ 
  FILE *fp; 
  int value;
  
  fp = fopen ("/home/pi/output.txt", "wb");
  if (fp) 
  { 
    for (value = 48; value < 58; value++) 
    { 
      fputc (value, fp); 
    } 
    fclose (fp); 
  } 
}
```

În acest caz, deschidem fișierul `/home/pi/output.txt` cu modul `"wb"`, care indică 'write binary' (scriere binară). Aceasta deschide fișierul pentru scriere; dacă acest fișier există deja, conținutul este șters.

Apoi apelăm funcția `fputc` ('file put character') într-o buclă, scriind bytes-ii 48, 49...57 în fișier. (Acestea sunt codurile de caractere pentru caracterele de text pentru cele zece cifre 0, 1...9).

Ca înainte, apoi închidem pointerul de fișier. Dacă rulați acest lucru și apoi vă uitați în directorul dvs. home, ar trebui să găsiți fișierul `output.txt`, conținând șirul `0123456789`.

> **AMINTIȚI-VĂ SĂ APELAȚI FCLOSE**
> 
> Este ușor să uitați să apelați fclose pe fișierul dvs., dar este important să o faceți. Pe unele sisteme, când scrieți în sistemul de fișiere, scrierea nu se finalizează de fapt până când fclose este apelat; dacă programul dvs. nu apelează fclose, ați putea descoperi că scrieți în fișiere și nimic nu apare.

## Ieșire formatată - fprintf

`fputc` este util pentru scrierea bytes-ilor într-un fișier, dar este un mod incomod de a scrie text într-un fișier. Pentru aceasta, putem folosi funcția `fprintf` ('file print formatted').

```c
#include <stdio.h>

void main (void) 
{ 
  FILE *fp;
  
  fp = fopen ("/home/pi/output.txt", "wb");
  if (fp) 
  { 
    fprintf (fp, "This is some text.\n"); 
    fclose (fp); 
  } 
}
```

`fprintf` funcționează în exact același mod ca `sprintf`, dar primul argument este un pointer de fișier în loc de un șir.

**Notă:** Citirea sau scrierea unui fișier necesită ca un pointer de fișier să fie deschis cu fopen, iar pointerul rezultat este apoi folosit în toate operațiile. Amintiți-vă să închideți pointerul după aceea cu fclose.

## Moduri de acces la fișiere

### Moduri de bază:

| Mod | Descriere | Comportament |
|-----|-----------|--------------|
| `"rb"` | Read Binary | Citește fișier existent |
| `"wb"` | Write Binary | Creează/suprascrie fișier |
| `"ab"` | Append Binary | Adaugă la sfârșitul fișierului |

### Moduri de citire și scriere simultană:

| Mod | Descriere |
|-----|-----------|
| `"rb+"` | Citește și suprascrie fișier existent |
| `"wb+"` | Creează fișier nou pentru citire/scriere |
| `"ab+"` | Deschide pentru adăugare și citire |

> **CITIȚI ȘI SCRIEȚI ÎN ACELAȘI FIȘIER**
> 
> Puteți deschide un fișier pentru citire și scriere simultană cu același pointer. Setați modul de acces la fișier la `"rb+"` pentru a citi un fișier existent și pentru a-l suprascrie; setați-l la `"wb+"` pentru a crea un fișier nou și pentru a putea citi înapoi ceea ce ați scris în el; setați-l la `"ab+"` pentru a deschide un fișier pentru a adăuga la sfârșit și a citi din el.

## Mișcarea în cadrul unui fișier

Destul de des, în loc să suprascriem un fișier, vrem doar să adăugăm la sfârșitul acestuia. Pentru a face acest lucru, deschideți-l cu:

```c
fopen ("/home/pi/output.txt", "ab")
```

Dacă fișierul există, ieșirea va fi apoi adăugată după conținutul existent al fișierului; dacă fișierul nu există, va fi creat și ieșirea va începe la început.

### Funcția fseek

Uneori când accesăm un fișier, nu dorim neapărat să începem de la început. Funcția `fseek` ('file seek') poate fi folosită pentru a repoziționa pointerul de fișier în cadrul fișierului.

```c
#include <stdio.h>

void main (void) 
{ 
  FILE *fp; 
  int value;
  
  fp = fopen ("/home/pi/input.txt", "rb"); 
  if (fp) 
  { 
    fseek (fp, 10, SEEK_CUR); 
    while (1) 
    { 
      value = fgetc (fp); 
      if (value == EOF) break; 
      else printf ("%c", value); 
    } 
    fclose (fp); 
  } 
}
```

### Parametrii fseek:

```c
fseek (pointer_fisier, offset, origine);
```

1. **Pointer de fișier** - `fp`
2. **Offset** - numărul de bytes cu care să se deplaseze (poate fi pozitiv sau negativ)
3. **Origine** - punctul de referință:
   - `SEEK_SET` - de la începutul fișierului
   - `SEEK_CUR` - de la poziția curentă
   - `SEEK_END` - de la sfârșitul fișierului

### Exemple:

```c
fseek (fp, 10, SEEK_CUR);   // 10 bytes înainte de poziția curentă
fseek (fp, -5, SEEK_CUR);   // 5 bytes înapoi de la poziția curentă
fseek (fp, 12, SEEK_SET);   // 12 bytes de la începutul fișierului
fseek (fp, -17, SEEK_END);  // 17 bytes înapoi de la sfârșitul fișierului
```

Linia `fseek (fp, 10, SEEK_CUR)` mută pointerul de fișier cu 10 bytes înaintea poziției curente, deci acest program va tipări toate caracterele cu excepția primelor zece din fișier.

## Funcții suplimentare pentru fișiere

> **VERIFICAȚI BIBLIOTECA**
> 
> Biblioteca C oferă o gamă largă de funcții pentru citirea și scrierea datelor din și în fișiere; am analizat doar câteva dintre ele. Dacă trebuie să accesați un fișier, aruncați o privire la unele dintre celelalte funcții de bibliotecă, cum ar fi `fread`, `fwrite`, `fscanf`, `fputs` și `fgets`, pentru a vedea dacă sunt mai potrivite decât `fputc` și `fgetc` de bază pe care le-am folosit aici.

## Rezumat

### Funcții principale pentru fișiere:

| Funcție | Descriere | Exemplu |
|---------|-----------|---------|
| `fopen(cale, mod)` | Deschide un fișier | `fp = fopen("file.txt", "rb");` |
| `fclose(fp)` | Închide un fișier | `fclose(fp);` |
| `fgetc(fp)` | Citește un caracter | `c = fgetc(fp);` |
| `fputc(c, fp)` | Scrie un caracter | `fputc('A', fp);` |
| `fprintf(fp, format, ...)` | Scrie text formatat | `fprintf(fp, "%d\n", val);` |
| `fscanf(fp, format, ...)` | Citește text formatat | `fscanf(fp, "%d", &val);` |
| `fseek(fp, offset, origine)` | Mută poziția în fișier | `fseek(fp, 0, SEEK_SET);` |
| `fread(buffer, size, n, fp)` | Citește blocuri de date | `fread(buf, 1, 100, fp);` |
| `fwrite(buffer, size, n, fp)` | Scrie blocuri de date | `fwrite(buf, 1, 100, fp);` |

### Constante importante:

| Constantă | Descriere |
|-----------|-----------|
| `EOF` | End of File (sfârșitul fișierului) |
| `SEEK_SET` | Începutul fișierului |
| `SEEK_CUR` | Poziția curentă |
| `SEEK_END` | Sfârșitul fișierului |

### Exemplu complet - Copierea unui fișier:

```c
#include <stdio.h>

int main (int argc, char *argv[]) 
{
    FILE *source, *dest;
    int ch;
    
    if (argc != 3) 
    {
        printf("Usage: %s <source> <destination>\n", argv[0]);
        return 1;
    }
    
    // Deschide fișierul sursă pentru citire
    source = fopen(argv[1], "rb");
    if (!source) 
    {
        printf("Error: Cannot open source file\n");
        return 1;
    }
    
    // Deschide fișierul destinație pentru scriere
    dest = fopen(argv[2], "wb");
    if (!dest) 
    {
        printf("Error: Cannot create destination file\n");
        fclose(source);
        return 1;
    }
    
    // Copiază byte cu byte
    while ((ch = fgetc(source)) != EOF) 
    {
        fputc(ch, dest);
    }
    
    // Închide ambele fișiere
    fclose(source);
    fclose(dest);
    
    printf("File copied successfully!\n");
    return 0;
}
```

### Puncte cheie de reținut:

- ✅ Verificați întotdeauna dacă `fopen()` a reușit
- ✅ Apelați întotdeauna `fclose()` când terminați
- ✅ Folosiți modul corect (`"rb"`, `"wb"`, `"ab"`, etc.)
- ✅ `fgetc()` returnează `int`, nu `char`
- ✅ `EOF` indică sfârșitul fișierului
- ✅ Folosiți `fseek()` pentru a naviga în fișier
- ✅ `fprintf()` este util pentru text formatat
- ✅ Gestionați erorile corespunzător

În capitolul următor, vom învăța mai multe despre tipuri și variabile avansate în C!
