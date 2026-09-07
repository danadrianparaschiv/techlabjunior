# Capitolul 26: Referință rapidă C

*Folosiți aceste fișe de referință și exemple de cod la îndemână*

## Structuri de control

### If

```c
if (<test>)
  <cod executat dacă testul este adevărat>
```

### If-else

```c
if (<test>)
  <cod executat dacă testul este adevărat>
else
  <cod executat dacă testul este fals>
```

### If-else multiplu

```c
if (<test1>)
  <cod executat dacă test1 este adevărat>
else if (<test2>)
  <cod executat dacă test1 este fals și test2 este adevărat>
else
  <cod executat dacă test1 este fals și test2 este fals>
```

### Switch

```c
switch (<variabilă>)
{
  case <valoare1> :  <cod executat dacă variabila este valoare1>
                     break;
  case <valoare2> :  <cod executat dacă variabila este valoare2>
                     break;
  default :          <cod executat dacă variabila nu este nici valoare1,
                         nici valoare2>
                     break;
}
```

### Switch cu trecere mai departe (fall-through)

```c
switch (<variabilă>)
{
  case <valoare1> :  <cod executat dacă variabila este valoare1>
  case <valoare2> :  <cod executat dacă variabila este fie valoare1,
                         fie valoare2>
                     break;
  default :          <cod executat dacă variabila nu este nici valoare1,
                         nici valoare2>
                     break;
}
```

### While

```c
while (<test>)
  <cod executat repetat cât timp testul este adevărat>
```

### Do-while

```c
do
  <cod executat o dată și apoi repetat cât timp testul este adevărat>
while (<test>);
```

### For

```c
for (<condiție inițială>; <condiție de terminare>; <incrementare>)
        <cod executat repetat până când condiția de terminare
            este falsă>
```

> **NOTA TRADUCĂTORULUI**
>
> În cartea originală, cele trei părți ale buclei `for` sunt listate în ordinea „condiție inițială; incrementare; condiție de terminare”. Ordinea corectă în C, folosită și în exemplele din capitolul 4, este cea de mai sus: inițializare, condiția care este testată înaintea fiecărei iterații (bucla continuă cât timp este adevărată) și, la sfârșit, incrementarea.

În toate buclele, cuvântul cheie `break` poate fi folosit pentru a ieși din buclă și a relua execuția imediat după buclă.

În toate buclele, cuvântul cheie `continue` poate fi folosit pentru a sări peste codul rămas în corpul buclei și a relua execuția la următoarea iterație a testului buclei.

## Tipuri de variabile

| Nume | Descriere | Mărime (bytes) |
|---|---|---|
| `char` | Un singur caracter alfanumeric | 1 |
| `signed char` | Întreg cu semn pe 8 biți (-128 – 127) | 1 |
| `unsigned char` | Întreg fără semn pe 8 biți (0 – 255) | 1 |
| `short`, `signed short` | Întreg cu semn pe 16 biți (-32768 – 32767) | 2 |
| `unsigned short` | Întreg fără semn pe 16 biți (0 – 65535) | 2 |
| `int`, `signed int` | Întreg cu semn pe 32 de biți (-2147483648 – 2147483647) | 4 |
| `unsigned int` | Întreg fără semn pe 32 de biți (0 – 4294967295) | 4 |
| `long`, `signed long` | Întreg cu semn pe 32 de biți (-2147483648 – 2147483647) | 4 |
| `unsigned long` | Întreg fără semn pe 32 de biți (0 – 4294967295) | 4 |
| `float` | Valoare în virgulă mobilă (± 3,402823 × 10^38) | 4 |
| `double` | Valoare în virgulă mobilă cu precizie dublă (± 10^308) | 8 |

În funcție de platformă, `int` poate fi fie un `short int` (16 biți), fie un `long int` (32 de biți); pe Raspberry Pi OS, conform tabelului de mai sus, `int` este o valoare întreagă `long` (32 de biți).

> **NOTA TRADUCĂTORULUI**
>
> Tabelul reflectă Raspberry Pi OS pe 32 de biți, pentru care a fost scrisă cartea. Pe sistemele Linux pe 64 de biți, inclusiv Raspberry Pi OS pe 64 de biți, `long` și `unsigned long` au 8 bytes (64 de biți), iar `int` rămâne pe 4 bytes. Puteți verifica oricând mărimea unui tip cu `sizeof`, de exemplu `printf ("%zu\n", sizeof (long));`.

## Specificatori de format

| Specificator | Format / tip |
|---|---|
| `%c` | Caracter alfanumeric / `char` |
| `%d` | Valoare zecimală cu semn / `int` |
| `%ld` | Valoare zecimală cu semn / `long int` |
| `%u` | Valoare zecimală fără semn / `int` |
| `%lu` | Valoare zecimală fără semn / `long int` |
| `%o` | Valoare octală / `int` |
| `%lo` | Valoare octală / `long int` |
| `%x`, `%X` | Valoare hexazecimală / `int` ¹ |
| `%lx`, `%lX` | Valoare hexazecimală / `long int` ¹ |
| `%f` | Valoare în virgulă mobilă / `float` |
| `%e` | Valoare exponențială / `float` |
| `%s` | Șir de text / pointer la `char` |

¹ `%x` afișează o valoare în hexazecimal cu literele mici a-f; `%X` o afișează cu literele mari A-F.

Lățimea (sau numărul minim de caractere tipărite) poate fi setată inserând un număr între `%` și literă; aceasta va completa cu spații la început o valoare mai scurtă. Pentru a completa cu spații la sfârșit, inserați un `-` între `%` și număr. Pentru a completa cu zerouri la început, inserați un `0` între `%` și număr.

De exemplu, pentru a tipări o variabilă întreagă cu valoarea 42, specificatorul de format `"%5d"` va tipări 42 cu trei spații înainte. Specificatorul de format `"%-5d"` va tipări 42 cu trei spații după. Specificatorul de format `"%05d"` îl va tipări ca 00042.

Numărul de zecimale afișate pentru o valoare în virgulă mobilă sau exponențială poate fi setat inserând un punct zecimal urmat de un număr între `%` și literă; acesta poate fi combinat cu o lățime, punând lățimea înaintea punctului zecimal.

De exemplu, pentru a tipări o variabilă în virgulă mobilă cu valoarea 76.54321, specificatorul de format `"%.2f"` o va tipări ca 76.54. Specificatorul de format `"%08.2f"` o va tipări ca 00076.54. (Observați că punctul zecimal ocupă un caracter din lățimea specificată.)

## Operatori

Operatorii din tabelul de mai jos produc un rezultat care poate fi atribuit unei alte variabile, de exemplu `c = a + b`, dar nu afectează valorile lui `a` sau `b`.

| Simbol | Funcție |
|---|---|
| `a + b` | Adunare |
| `a - b` | Scădere |
| `a * b` | Înmulțire |
| `a / b` | Împărțire |
| `a % b` | Modulo (restul împărțirii `a / b`) |
| `a & b` | ȘI pe biți |
| `a \| b` | SAU pe biți |
| `a ^ b` | SAU exclusiv (XOR) pe biți |
| `a << b` | Deplasare a biților la stânga |
| `a >> b` | Deplasare a biților la dreapta |
| `~a` | Complement față de 1, pe biți |
| `!a` | NU logic |

Operatorii din tabelul de mai jos modifică direct valoarea lui `a`.

| Simbol | Funcție |
|---|---|
| `a++` | Incrementează `a` cu unu ² |
| `a--` | Decrementează `a` cu unu ² |
| `++a` | Incrementează `a` cu unu ² |
| `--a` | Decrementează `a` cu unu ² |
| `a += b` | Incrementează `a` cu `b` |
| `a -= b` | Decrementează `a` cu `b` |
| `a *= b` | Înmulțește `a` cu `b` |
| `a /= b` | Împarte `a` la `b` |
| `a %= b` | `a` = restul împărțirii `a / b` |
| `a &= b` | ȘI pe biți între `a` și `b` |
| `a \|= b` | SAU pe biți între `a` și `b` |
| `a ^= b` | XOR pe biți între `a` și `b` |
| `a <<= b` | Deplasează biții lui `a` la stânga cu `b` |
| `a >>= b` | Deplasează biții lui `a` la dreapta cu `b` |

² Diferența dintre `a++` și `++a` este că, dacă sunt folosite într-un test, cum ar fi `if (a++)`, `a++` testează valoarea și apoi o incrementează, în timp ce `++a` incrementează mai întâi valoarea și apoi testează valoarea incrementată.

Operatorii din tabelul de mai jos sunt folosiți pentru comparații în teste.

| Simbol | Funcție |
|---|---|
| `==` | Este egal cu |
| `!=` | Nu este egal cu |
| `>` | Este mai mare decât |
| `<` | Este mai mic decât |
| `>=` | Este mai mare sau egal cu |
| `<=` | Este mai mic sau egal cu |

**Felicitări! Ați ajuns la sfârșitul cărții.** Aveți acum atât bazele limbajului C, cât și uneltele pentru a construi aplicații grafice cu GTK. Cel mai bun pas următor este un proiect al dumneavoastră: combinați widgeturile din partea a doua cu funcțiile și fișierele din prima parte și consultați documentația GTK ori de câte ori aveți nevoie de un widget nou.
