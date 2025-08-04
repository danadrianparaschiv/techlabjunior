# Esențialul limbajului C
© Nick Parlante, 1996. Gratuit pentru uz necomercial.

Acest document rezumă practic toate caracteristicile majore ale limbajului C. Nu explică cum funcționează lucrurile în detaliu, dar oferă suficiente informații pentru a fi, sperăm, util. A fost bazat inițial pe un document al lui Mike Cleron și acum este un fel de proiect în desfășurare al meu. Am făcut numeroase modificări și îmbunătățiri de-a lungul anilor în timp ce am predat CS107. Vă rog să trimiteți orice feedback la nick@cs.stanford.edu.

C este un limbaj de programare profesional. Limbajul este conceput să stea cât mai puțin în calea programatorului. C favorizează un stil expresiv și concis în detrimentul siguranței sau lizibilității. Din această cauză, C tinde să fie neiertător cu greșelile. C este "simplu" în sensul că numărul de componente ale limbajului este mic - dacă două caracteristici ale limbajului realizează aproximativ același lucru, C va include doar una. C este expresiv, concis și nu restricționează ceea ce este "permis", astfel încât permite unui programator care știe exact ce vrea să exprime algoritmul în timpul minim. C include de asemenea manipularea biților la nivel scăzut, ceea ce îl face popular pentru anumite sarcini de nivel scăzut precum driver-ele de dispozitive sau părți din sistemele de operare.

În orice caz, C este extrem de popular și influent. Aceasta se datorează în principal stilului curat (chiar dacă minimal) al lui C, lipsei de constructe enervante sau regretabile și ușurinței relative de a scrie un compilator C. C este o unealtă puternică. Depinde de programator să nu taie nimic prea important cu ea.

## Tipuri de date

C oferă un set destul de minimal de tipuri de date. Există un set mic de tipuri de bază din care sunt construite toate celelalte tipuri. Dimensiunile indicate sunt doar alegeri comune - limbajul nu depinde de dimensiuni specifice.

### Tipuri întregi

| Tip | Descriere |
|-----|-----------|
| `char` | caractere (1 byte) |
| `short` | întregi mici (2 bytes) |
| `int` | întreg implicit (2 sau 4 bytes) |
| `long` | întregi mari (de asemenea 4 bytes) |

Tipurile întregi pot fi precedate de calificatorul "unsigned" care face imposibilă reprezentarea numerelor negative, dar dublează dimensiunea celui mai mare număr pozitiv posibil. Pointerii sunt o formă de unsigned int. Tipurile întregi sunt toate "compatibile" între ele deoarece toate sunt de fapt doar întregi. Caracterele și diferiții întregi pot fi combinați în expresii aritmetice precum ('b' + 5).

### Tipuri în virgulă mobilă

| Tip | Descriere |
|-----|-----------|
| `float` | număr real (4 bytes) |
| `double` | număr real (8 bytes) |

## Variabile

În declarația de variabile și parametri C, tipul vine primul. Variabilele multiple pot fi declarate să fie de același tip separându-le cu virgule. Instrucțiunea de atribuire este semnul egal simplu (=).

C nu are un tip Boolean distinct - în schimb sunt folosiți întregi. Compilatorul tratează 0 ca fals și orice altceva ca adevărat. Astfel instrucțiunea:

```c
i = 0;
while (i - 10) {
    ...
}
```

va executa până când variabila i ia valoarea 10, moment în care expresia (i - 10) va deveni falsă (adică 0).

## Tipuri de date compuse

C are facilitățile obișnuite pentru gruparea tipurilor împreună pentru a forma alte tipuri - array-uri și înregistrări (care se numesc "structuri"). Următoarea definiție declară un tip numit "struct fraction" care are două câmpuri întregi. Dacă uiți punct-virgula tinde să producă ceva ce este sintactic corect dar care nu este deloc ceea ce aveai în minte.

```c
struct fraction {
    int numerator;
    int denominator;
}; /* Don't forget the semi-colon!! */
```

După această declarație, poți declara variabile, parametri etc. să fie de tipul "struct fraction" (ambele cuvinte sunt necesare). C folosește punctul (.) pentru a accesa câmpurile dintr-o înregistrare. Poți copia două înregistrări de același tip folosind o singură instrucțiune de atribuire.

```c
{
    struct fraction f1, f2; /* declare two fractions */
    f1.numerator = 22;
    f1.denominator = 7;
    f2 = f1; /* this copies over the whole struct */
}
```

## Array-uri

Array-urile de variabile locale sunt simple în C. Există utilizări mai arcane ale array-urilor pe care le vom păstra pentru mai târziu. Următoarea declară un array pentru a conține 100 de întregi.

```c
int scores[100];
```

Array-urile C sunt întotdeauna indexate de la 0. Deci primul element din array-ul de mai sus este scores[0] și ultimul este scores[99]. Este o greșeală comună în buclă să încerci să te referi la elementul inexistent scores[100]. C nu face niciun fel de verificare a limitelor la timpul execuției sau al compilării în array-uri. Convenția de numerotare a lucrurilor cu numerele 0..(numărul de lucruri - 1) pătrunde în limbaj. Deci pentru a te integra cel mai bine cu C și alți programatori C, ar trebui să urmezi convenția de a începe numerotarea cu 0 în propriile tale structuri de date de asemenea.

Următoarea declară un array tridimensional 10 pe 10 pe 10 de întregi și setează primul și ultimul element să fie 13.

```c
int board[10][10][10];
board[0][0][0] = 13;
board[9][9][9] = 13;
```

Următoarea declară un array de 1000 struct fractions.

```c
struct fraction numbers[1000];
```

Iată un truc general pentru decodificarea declarațiilor de variabile C: uită-te la partea dreaptă - imaginează-ți că este o expresie. Tipul acelei expresii este partea stângă. Pentru declarațiile de mai sus, o expresie care arată ca partea dreaptă (numbers[1000], sau de fapt orice de forma numbers[...]) va fi tipul din partea stângă (struct fraction).

## Pointeri

C folosește asteriscul sau "steaua" * pentru pointeri. Pentru a declara o variabilă pointer, adaugă un * în stânga variabilei.

```c
int *intPtr;        /* declare an integer pointer variable intPtr */
char *charPtr;      /* declares a character pointer */
                    /* a very common type of pointer */
struct fraction *f1, *f2; /* declares two pointers to struct fractions */
```

### Steaua plutitoare

De fapt steaua este permisă să fie oriunde între tipul de bază și numele variabilei. Deci declarația de mai sus pentru intPtr ar putea fi scrisă echivalent...

```c
int *intPtr;    /* these are all the same */
int * intPtr;
int* intPtr;
```

Programatorii au propriile lor convenții - în general lipesc * de variabilă.

### Dereferențierea pointerilor

Într-o expresie, un * în stânga unui pointer dereferențiază pointerul. C este unic prin aceea că operatorul de dereferențiere al pointerului merge în stânga variabilei în loc de dreapta ca în Pascal și Ada. Având în vedere declarația de mai sus pentru f1:

| Expresie | Tip |
|----------|-----|
| `f1` | `(struct fraction*)` adică un pointer la struct fraction |
| `*f1` | `struct fraction` |
| `(*f1).numerator` | `int` |

Există o sintaxă alternativă, mai lizibilă disponibilă pentru a dereferenția un pointer la o structură. Un "->" în dreapta pointerului poate accesa oricare dintre câmpurile din structură. Deci referința la câmpul numerator ar putea fi scrisă `f1->numerator`.

Declarațiile de tip pointer urmează aceeași regulă generală ca și array-urile - gândește-te la partea dreaptă ca la o expresie eșantion unde partea stângă este tipul acelei expresii. Iată câteva tipuri de variabile mai obscure:

```c
struct fraction **fp;  /* a pointer to a pointer to a struct fraction */
struct fraction fract_array[20]; /* an array of 20 struct fractions */
struct fraction *fract_ptr_array[20]; /* an array of 20 pointers to */
                                      /* struct fractions */
```

Un lucru frumos despre sintaxa tipurilor C este că evită problemele de definiție circulară care apar când o structură pointer trebuie să se refere la ea însăși. Următoarea definiție definește un nod într-o listă legată. Observă că nu sunt necesare referințe înainte.

```c
struct node {
    int data;
    struct node *next;
}
```

## Operatori de adresă

| Operator | Descriere |
|----------|-----------|
| `*` | Dereferențiere |
| `->` | Dereferențiere pointer și selectare câmp din înregistrare |
| `&` | Adresa a ceva |

Operatorul & ia adresa argumentului său. Argumentul poate fi orice variabilă care ocupă spațiu în stivă sau heap. Deci &i și &(p->next) sunt ok, dar &6 nu este. Folosește & când ai un obiect și vrei un pointer la acel obiect.

```c
void foo() {
    int *p;    /* p is a pointer to an integer */
    int i;     /* i is an integer */
    
    p = &i;    /* Make p point to i */
    *p = 0;    /* Change what p points to -- in this case i -- to 0 */
    ...
}
```

Când folosești pointer la un obiect creat cu &, este important să folosești pointerul doar atât timp cât obiectul există. O variabilă locală există doar atât timp cât funcția în care este declarată se execută încă. În exemplul de mai sus, i există doar atât timp cât foo se execută. Prin urmare, orice pointeri care au fost inițializați cu &i sunt valizi doar atât timp cât foo se execută.

## Eroarea pointerului neinițializat

Declararea unui pointer alocă spațiu pentru pointerul în sine, dar nu alocă spațiu pentru ceea ce indică pointerul. Pointerul trebuie setat să indice către ceva înainte să îl poți dereferenția. Uitatul să inițializezi un pointer să indice către ceva este probabil cea mai comună eroare în C.

```c
{
    int *p;
    *p = 13;    // NO NO NO p does not point to an int yet
                // this just overwrites a random word in memory
}
```

Desigur codul tău nu va fi atât de trivial, dar eroarea are aceeași formă de bază. Declari un pointer local, dar uiți să îl inițializezi să indice către ceva. Codul ar trebui să arate cam așa...

```c
{
    int *p;
    int i;
    
    p = &i;     // set p to point to an int somewhere
    *p = 13;    // Follow p and...it points to something!(i in this case).
                // Set *p to 13.
}
```

## TypeDef

O instrucțiune typedef introduce un nume prescurtat pentru un tip. Sintaxa este:

```c
typedef <type> <name>;
```

Următoarea definește tipul Fraction să fie tipul (struct fraction). C este sensibil la majuscule, deci fraction este diferit de Fraction. Este convenabil să folosești typedef pentru a crea tipuri cu nume cu majuscule și să folosești versiunea cu litere mici a aceluiași cuvânt ca variabilă.

```c
typedef struct fraction Fraction;
Fraction fraction; /* declare the variable "fraction" of type "Fraction" */
                  /* which is really just a name for "struct fraction". */
```

Următoarea definește un tip de arbore binar Tree:

```c
typedef struct treenode *Tree;
struct treenode {
    int data;
    Tree smaller, larger; /* equivalently, this line could say */
};                       /* "struct treenode *smaller, *larger" */
```

## Conversii

Există câteva conversii incorporate care convertesc între diferite tipuri numerice. Compilatorul le va folosi când atribui tipuri diferite dar convertibile. Atribuirea de la un întreg la un întreg mai mic (de ex. long la int, sau int la char) elimină biții cei mai semnificativi. Atribuirea de la un tip în virgulă mobilă la un întreg elimină partea fracționară a numărului.

```c
char c;
int i;
i = 321;
c = i;
```

Atribuirea va elimina biții superiori ai întregului 321. Cei 8 biți inferiori ai numărului 321 reprezintă numărul 65 (321 - 256). Deci valoarea lui c va fi (char)65 care este 'A'.

```c
float pi;
int i;
pi = 3.14159;
i = pi;
```

Atribuirea de la un float la un întreg va elimina partea fracționară a numărului, deci rezultatul va fi să dea lui i valoarea 3. Această conversie se va întâmpla ori de câte ori ai o expresie de tip float dar ai nevoie de un int. Aceasta se întâmplă când atribui un float unui int sau pasezi un float unei funcții care ia un int. Această conversie automată poate cauza erori dacă nu ai intenționat ca partea fracționară să fie eliminată.

Iată un exemplu din tipul de cod unde truncherea poate cauza erori: următoarea instrucțiune este menită să scaleze un scor de temă care era în intervalul 0..20 să fie în intervalul 0..100.

```c
{
    int score;
    ...
    score = (score / 20) * 100;
    ...
}
```

Din păcate, va seta aproape întotdeauna scorul la 0 deoarece expresia (score / 20) va trunchia aproape întotdeauna la 0. Regula generală: împarte la sfârșit pentru a evita truncherea prematură. Sau convertește lucrurile la float pentru a preveni truncherea:

```c
score = ((float)score / 20) * 100;
```

sau...

```c
score = (score / 20.0) * 100;
```

## Conversii de tip (Type Casting)

C permite schimbarea tipului folosind un mecanism numit conversie. O conversie este pur și simplu un nume de tip inclus în paranteză care îi spune compilatorului ce tip să considere expresia din dreapta. Dacă tipurile sunt convertibile așa cum s-a descris mai sus, compilatorul va face conversia corespunzătoare. Altfel, conversia este luată de compilator ca o ordine să interpreteze biții ca tipul dat. Următorul exemplu stochează 0 într-un întreg de 4 byte. Conversia schimbă interpretarea acelor 4 byte de la un întreg la o structură de caractere. Compilatorul poate refuza o conversie dacă tipurile nu au aceeași dimensiune, sau dacă compilatorul este în modul "strict".

```c
struct chars4 {
    char a,b,c,d;
};

long i;
chars4 c;
i = 0;
c = (struct chars4)i;
```

În acest caz, nu se efectuează nicio conversie, doar permite liniei să treacă de verificatorul de tip la timpul compilării.

Ai voie întotdeauna să convertești un tip de pointer la altul. Aceasta îți oferă o ușă din spate prin care poți forța compilatorul să facă orice. De exemplu, să presupunem că ai un caracter și, din vreo cauză, vrei să îl pasezi funcției Foo care ia un struct fraction.

```c
/* declaration of Foo */
void Foo(struct fraction passedInFraction);

char ch;

/* attempt to call #1 -- hope the compiler converts automatically*/
Foo(ch);
```

Compilatorul nu va permite apelul de mai sus deoarece char și struct fraction sunt tipuri diferite și compilatorul nu cunoaște o conversie automată pentru a converti un char la un struct fraction. Deci am putea încerca să punem o conversie pentru a schimba pur și simplu char-ul la struct fraction. Probabil că nu va funcționa nici (depinde de setarea "stricteții" curentă a compilatorului) deoarece char și struct fraction nu au aceeași dimensiune în bytes.

```c
/* attempt to call #2 -- tell the compiler to cast */
Foo((struct fraction)ch);
```

Modalitatea sigură de a o face este să iei adresa caracterului care va fi de tipul (char*). Tipurile de pointeri sunt liber convertibile între ele, deci convertește (char*) să fie un (struct fraction*). Acum dereferențiază noul pointer înapoi astfel încât să fie un struct fraction.

```c
/* attempt to call #3 -- tell the compiler to cast the pointers */
Foo(*((struct fraction*)&ch)); /*This is probably quite unwise */
```

Aceasta se va compila, dar este probabil o idee proastă. Char-ul este un byte. Un struct fraction este 8 bytes. Deci pentru a obține cei 8 bytes pentru a compune argumentul, aceasta va lua char-ul ca primul byte și va lua următorii 7 bytes din memorie, orice ar fi ei, pentru a face restul. În acest exemplu, doar luarea următorilor 7 bytes aleatori este foarte puțin probabil să fie o idee bună. Totuși, uneori când chiar știi ce se întâmplă cu aranjamentul memoriei tale și trebuie să forțezi compilatorul să ia interpretarea ta, aceasta este modalitatea de a o forța.

## Clase de stocare

Variabilele pot veni într-una din cinci clase de stocare. Patru din clasele de stocare sunt specificate precedând declarația variabilei cu unul dintre următoarele cuvinte cheie:

| Clasă | Descriere |
|-------|-----------|
| `auto` | Variabilă bazată pe stivă. Aceasta este alocarea implicită dacă nu este specificată nicio clasă de stocare. Nimeni nu pune vreodată "auto" în fața variabilelor locale. |
| `static` | Variabila este "deținută" de o funcție. Valoarea variabilei este păstrată între apeluri. Variabila este ca o variabilă globală prin aceea că își păstrează valoarea între apeluri, dar este ca o locală deoarece poate fi văzută doar în funcție. Variabilele statice sunt preferabile variabilelor globale. |
| `extern` | Variabila este declarată în afara funcției curente. Aceasta este utilă în special dacă există multiple fișiere sursă într-un program. Îi spune linker-ului să încerce să rezolve referința la timpul link-ării, dar să nu se îngrijoreze despre asta înainte. |
| `register` | Aceasta este un sfat pentru compilator că variabila va fi accesată foarte mult și deci ar trebui stocată într-un registru. Compilatorul este liber să facă ce crede că este mai bine. Aceasta avea sens când compilatoarele de optimizare erau slabe, deci sfatul de la programator avea șanse să fie util. Compilatoarele de optimizare contemporane sunt suficient de avansate încât declarațiile register sunt mai puțin probabil să ajute la ceva. |

A cincea clasă de stocare, dinamică, se referă la variabile alocate la timpul execuției în heap - analog celor create folosind "new" în Pascal.

Următorul exemplu arată cum variabilele statice pot face o funcție mult mai convenabilă. Funcția de numere aleatoare de mai jos folosește două variabile statice: prima înregistrează dacă utilizatorul a introdus o sămânță; a doua înregistrează valoarea sămânței. Proprietatea importantă pe care seed și have_seed o au este că își mențin valorile între apelurile la random.

```c
#include <stdio.h>

main()
{
    int r;
    int i;
    for(i=0;i<=10;i++) {
        r = random(1,100);
        printf("%d\n", r);
    }
}

int random(int lo, int hi)
{
    static int seed;
    static int have_seed = 0;
    
    if (!have_seed) {
        printf("Please enter a seed >");
        scanf("%d", &seed);
        have_seed = 1;
    }
    seed = (29 * seed + 1) % 1024;
    return ((seed/1024.0) * (hi - lo + 1)) + lo;
}
```

## Atribuire

Instrucțiunea de atribuire (=) servește unui scop dublu în C. Pe lângă punerea valorii din dreapta în variabila din stânga, o atribuire returnează noua valoare a părții stângi. (c = a + 2) pune valoarea (a + 2) în c și de asemenea reprezintă valoarea (a + 2) pentru folosire într-o altă expresie. De exemplu, următoarea pune (a + 2) în c și efectiv (a + 5) în b:

```c
b = ((c = (a + 2)) + 3);
```

Această caracteristică poate fi folosită pentru a inițializa mai multe variabile deodată, sau pentru a imbrica o atribuire într-o instrucțiune if. Al doilea exemplu apelează funcția getchar() care citește un caracter din intrare. Apoi pune acel caracter în variabila ch și apoi testează dacă acel caracter este mai mare decât 'A'. Acest fel de utilizare atribuie-și-testează a lui = este destul de acceptabilă printre programatorii C cool. Alte utilizări mai obscure care implică =-uri imbricate sunt considerate un pic vulgare.

```c
x = y = z = 10;                    /* Multiple assignment */
if ((ch = getchar()) >= 'A') ...   /* Assign and test */
```

O greșeală tragic de comună este să folosești un egal simplu când vroiai să folosești un egal dublu. Consideră acest cod:

```c
if (x = 3) ...
```

Acest cod nu testează dacă x are valoarea 3. Mai degrabă, atribuie 3 lui x, apoi deoarece 3 este o valoare non-zero condiția if-ului este întotdeauna adevărată.

C include de asemenea o mulțime de alți operatori de atribuire care includ o operație cu atribuirea. De exemplu "+=" adaugă expresia din dreapta la variabilă. `x = x + 10;` poate fi redus la `x += 10;`. Aceasta este cel mai utilă dacă x este o expresie lungă precum `person->relatives.mom.numChildren += 2;`. Nu se va compila în cod mai rapid, cu excepția cazului în care compilatorul tău este în mod special slab - este într-adevăr doar o prescurtare notațională.

| Operator | Descriere |
|----------|-----------|
| `=` | Atribuie - returnează de asemenea valoarea atribuită astfel încât poți spune "x = (y = foo(6))" |
| `+=` | Incrementează cu |
| `-=` | Decrementează cu |
| `*=` | Înmulțește cu |
| `/=` | Împarte la |
| `%=` | Modulo cu |
| `>>=` | Deplasare dreapta cu |
| `<<=` | Deplasare stânga cu |
| `&=` | ȘI pe biți cu |
| `^=` | XOR pe biți cu |
| `\|=` | SAU pe biți cu |

## Operatori matematici

| Operator | Descriere |
|----------|-----------|
| `+` | Adunare |
| `-` | Scădere |
| `/` | Împărțire |
| `*` | Înmulțire |
| `%` | Rest |
| `var++` | Post-incrementare |
| `++var` | Pre-incrementare |
| `var--` | Post-decrementare |
| `--var` | Pre-decrementare |

"/" cu două argumente întregi va face împărțire întreagă. Dacă oricare argument este un float, face împărțire în virgulă mobilă. Deci "6 / 4" se evaluează la 1 în timp ce "6 / 4.0" se evaluează la 1.5. Pre-incrementarea schimbă valoarea variabilei înainte să fie folosită; post-incrementarea schimbă valoarea după ce este folosită. Post-incrementarea este cu depărtare forma cea mai comună folosită.

```c
x = 1;
y = 1;
printf("%d\n", x++);    /* Output: 1 */
printf("%d\n", ++y);    /* Output: 2 */
printf("%d\n", x);      /* Output: 2 */
printf("%d\n", y);      /* Output: 2 */
```

## Operatori logici

Amintește-ți că o valoare de 0 este considerată falsă, orice altceva este considerat adevărat. Operatorii evaluează de la stânga la dreapta și se opresc de îndată ce adevărul sau falsitatea expresiei poate fi dedusă. (Astfel de operatori sunt numiți "scurt-circuitați") În ANSI C, aceștia sunt în plus garantați să folosească 1 pentru a reprezenta adevărat, și nu doar vreo înșiruire aleatorie de biți. Totuși, există multe programe C acolo care folosesc alte valori decât 1 pentru adevărat (pointeri non-zero de exemplu), deci când programezi, nu ar trebui să presupui că un boolean adevărat este neapărat exact 1.

| Operator | Descriere |
|----------|-----------|
| `!` | NU logic |
| `&&` | ȘI logic |
| `\|\|` | SAU logic |

## Operatori relacionali

| Operator | Descriere |
|----------|-----------|
| `>` | Mai mare decât |
| `<` | Mai mic decât |
| `>=` | Mai mare sau egal |
| `<=` | Mai mic sau egal |
| `==` | Egal |
| `!=` | Nu este egal |

C folosește un egal dublu (==) pentru a testa egalitatea. Pentru a vedea dacă x este egal cu trei, scrie ceva de genul:

```c
if (x == 3) ...
```

Nu scrie:

```c
if (x = 3) ...
```

= va atribui x la 3 care este interpretat ca adevărat. Folosirea = când vroiai == este probabil cea mai comună eroare făcută de programatorii C începători. Amintește-ți "= == ".

## Operatori pe biți

C include operatori pentru a manipula memoria la nivelul de bit. Aceasta este utilă pentru scrierea de cod de sistem de nivel scăzut hardware sau de operare unde abstracțiunile obișnuite de numere, caractere, pointeri, etc... sunt insuficiente. Codul de manipulare a biților tinde să fie mai puțin "portabil". Codul este "portabil" dacă fără intervenția programatorului se compilează și rulează corect pe diferite tipuri de calculatoare.

| Operator | Descriere |
|----------|-----------|
| `~` | Negare pe biți |
| `&` | ȘI pe biți |
| `\|` | SAU pe biți |
| `^` | SAU exclusiv pe biți |
| `>>` | Deplasare dreapta (împărțire la 2) |
| `<<` | Deplasare stânga (înmulțire cu 2) |

Nu confunda operatorii pe biți cu operatorii logici. Conectivele pe biți sunt late de un caracter (&, |) în timp ce conectivele boolean sunt late de două caractere (&&, ||). Compilatorul nu te va ajuta niciodată cu o eroare de tip dacă folosești & când vroiai &&. În ceea ce privește verificatorul de tip, ele sunt identice - ambele iau și produc întregi deoarece nu există un tip Boolean distinct.

## Structuri de control

### Instrucțiunea If

Atât un if cât și un if-else sunt disponibile în C. <expression> poate fi orice expresie C validă. Parantezele din jurul expresiei sunt obligatorii, chiar dacă este doar o singură variabilă.

```c
if (<expression>) {
    <statements>
}

if (<expression>) {
    <statements>
} else {
    <statements>
}
```

### Expresia condițională -sau- Operatorul ternar

Expresia condițională poate fi folosită ca o prescurtare pentru unele instrucțiuni if-else. Sintaxa generală a operatorului condițional este:

```c
<expression> ? <expression> : <expression>
```

Aceasta este o expresie, nu o instrucțiune, deci reprezintă o valoare. Operatorul funcționează evaluând prima expresie. Dacă este adevărată (non-zero), evaluează și returnează a doua expresie. Altfel, prima expresie este falsă (0) și operatorul evaluează și returnează a treia expresie.

Exemplul clasic al operatorului ternar este să returneze mai mică dintre două variabile. În loc de...

```c
if (x < y) {
    min = x;
}
else {
    min = y;
}
```

Doar spui...

```c
min = (x < y) ? x : y;
```

Din când în când, aceasta este destul de utilă.

### Instrucțiunea Switch

Instrucțiunea switch este un "if" generalizat de-a lungul liniilor instrucțiunii case din Pascal. Expresia este evaluată și controlul sare la punctul corespunzător în cod.

```c
switch (<expression>) {
    case <expression-1>:
    case <expression-2>:
    ...
    case <expression-n>:
        <statements>
        break; /* Not required, but a good idea */
    case <expression>:
        ...
    default:
        <statements>
}
```

Totuși, odată ce execuția a sărit la un anumit punct, programul va continua să ruleze de la acel punct înainte. De exemplu, dacă response = 'Y' în programul de mai jos, programul va afișa "Yes", urmat de "No", urmat de "Huh?"

```c
switch (response) {
    case 'Y':
    case 'y':
        printf("Yes\n");
    case 'N':
    case 'n':
        printf("No\n");
    default:
        printf("Huh?\n");
}
```

Pentru a evita acest lucru, aproape întotdeauna vrei să pui instrucțiuni break după fiecare case:

```c
switch (response) {
    case 'Y':
    case 'y':
        printf("Yes\n");
        break;
    case 'N':
    case 'n':
        printf("No\n");
        break;
    default:
        printf("Huh?\n");
}
```

### Bucla While

Evaluează testul înainte de fiecare buclă, deci poate executa zero ori dacă condiția este inițial falsă. Necesită întotdeauna parantezele ca if-ul.

```c
while (<expression>) {
    <statements>
}
```

### Bucla Do-While

Ca un while, dar cu condiția de test la sfârșitul buclei. Corpul buclei va executa întotdeauna cel puțin o dată.

```c
do {
    <statements>
} while (<expression>)
```

### Bucla For

Bucla for din C este cea mai generală construcție de buclă. Antetul buclei conține trei părți: o inițializare, o condiție de continuare și o acțiune.

```c
for (<Initialization>; <Continuation Condition>; <Action>) {
    <statements>
}
```

Inițializarea se întâmplă o dată înainte ca corpul buclei să fie introdus. Bucla continuă să ruleze atât timp cât condiția de continuare rămâne adevărată (non-zero). După fiecare execuție a buclei, acțiunea este executată. Următorul exemplu execută de 10 ori numărând de la 0..9.

```c
for (i = 0; i < 10; i++) {
    ...
}
```

Este idiommatic în C să începi de la 0 și să folosești < în test. În alte limbaje ai putea începe de la 1 și să folosești <= în test. Vezi multe serii de tipul 0..(un_număr-1).

Fiecare din cele trei părți poate fi alcătuită din multiple instrucțiuni separate de virgule. Regula este că instrucțiunile separate de virgule sunt executate în ordine, de la stânga la dreapta. Au o reputație proastă, deci folosește-le cu parsimonie.

Acest exemplu inversează un string în loc. (Strlen este o funcție furnizată în una din bibliotecile C care returnează lungimea unui string.)

```c
for (i = 0, j = strlen(s) - 1; i < j; i++, j--) {
    temp = s[i];
    s[i] = s[j];
    s[j] = temp;
}
```

### Break

C permite două mecanisme pentru a ieși din bucle. Instrucțiunea break va muta controlul în afara unei bucle sau instrucțiuni switch. Din punct de vedere stilistic, ambii acești operatori au potențialul să fie un pic vulgari. Ai grijă să nu produci cod nelizibil. Ar trebui să apelez la un break doar dacă, așa cum se întâmplă uneori, testul poate apărea doar undeva în mijlocul instrucțiunilor din corpul buclei.

```c
while (<expression>) {
    ...
    if (SomethingAwful)
        break;
    ...
    ...
    ...
}
.../* Control ends up here on a break. */
```

Break nu iese dintr-un if. Funcționează doar în bucle și switch-uri. Să greșești aceasta poate cauza niște erori spectaculoase.

### Continue

Instrucțiunea continue face ca controlul să sară la sfârșitul buclei, sărind efectiv peste orice cod de sub continue. Ca și cu break, aceasta are o reputație de a fi vulgară, deci folosește-o cu parsimonie. Aproape întotdeauna poți obține efectul mai clar folosind un if în bucla ta.

```c
while (<expression>) {
    ...
    if (SomethingAwful)
        continue;
    ...
    ...
    ...
    /* Control ends up here on a continue. */
}
```

## Funcții

În C, nu există proceduri, doar funcții. Funcțiile sunt întotdeauna declarate la cel mai exterior nivel lexical. Este ilegal să imbricii definițiile de funcții. Funcția numită "main" este locul unde începe execuția programului. Unii programatori le place să își înceapă numele funcțiilor cu litere mari, folosind litere mici pentru variabile și parametri. Iată o funcție C simplă:

```c
int UselessFunction(int x, char y, struct node *z)
{
    int a;      /* These are local variables */
    char *b;
    ...
}
```

Toți parametrii sunt pasați prin valoare. Depinde de programator să potrivească numărul și tipurile parametrilor corect când apelează funcția, deși compilatorul ar trebui să dea o avertizare dacă unele tipuri nu se potrivesc.

Înainte de ANSI C, declarația parametrilor obișnuia să arate ca următoarea. În acele zile, de fapt nu trebuia să declari tipurile parametrilor. Dacă declarația era omisă, compilatorul ar presupune doar că era un int. Această laxitate a dus la atât de multe erori pe care compilatorul le-ar fi putut prinde încât a fost abandonată cu revizia ANSI a limbajului. Pentru compatibilitatea înapoi, majoritatea compilatoarelor vor accepta încă stilul vechi, dar nu este recomandat. Și dacă vreodată îl folosești, ceilalți programatori te vor arăta cu degetul și vor râde în spatele tău.

```c
int OldStyleFunction(x,y,z)  /* Specify return type and params */
int x;                       /* Parameter types are given here */
char y;                      /* but not checked later. */
struct node *z;
{
    ...
}
```

## C și neantul — void

"Void" este un tip formalizat în ANSI C care înseamnă "nimic". Pentru a indica că o funcție nu returnează nimic, listează void ca tipul de retur. De asemenea, prin convenție, un pointer care nu indică către niciun tip particular este declarat ca (void*). Uneori (void*) este folosit pentru a implementa ADT-uri unde (void*) se traduce aproximativ în "aceasta indică către ceva, dar nu îți spun (clientului) ce." Dacă o funcție nu ia niciun parametru, lista sa de parametri este goală, este politicos să o listezi ca void de asemenea.

```c
int TakesNothingAndReturnsAnInt(void) {
    ...
}
```

## Pasarea funcțiilor ca parametri

C îți permite să iei adresa unei funcții și să apelezi funcția mai târziu folosind acea adresă. Există unele utilizări inteligente ale acestui lucru care implică stocarea pointerilor de funcții în structuri de date, sau pasarea lor la alte funcții. În acest exemplu, funcția "map" va aplica funcția "f" la fiecare element al array-ului "a".

```c
#include <stdio.h>
#define MAXSIZE 10

int AddOne(int x)
{
    return ++x;
}

int Square(int x)
{
    return (x*x);
}

void Map(int a[], int (*f)(int))
/* f is a pointer to a function which takes and int */
/* and returns an int */
{
    int i;
    for (i=0; i<MAXSIZE; i++) {
        a[i] = (*f)(a[i]); /* Call the function that f points to */
    }
}

main()
{
    int i;
    int theArray[10];
    
    for (i=0; i<MAXSIZE; i++) {
        theArray[i] = i;
    }
    
    Map(theArray, AddOne);  /* Pass pointer to AddOne */
    Map(theArray, Square);  /* Pass pointer to Square */
}
```

## Simularea apelării prin referință

Deoarece C pasează argumente la funcții prin valoare, nu există o modalitate directă pentru funcția apelată să altereze o variabilă din funcția apelantă. De exemplu, o rutină de sortare ar putea schimba două elemente care nu sunt în ordine cu o funcție numită swap. Nu este suficient să scrii:

```c
Swap(a, b);
```

unde funcția Swap este definită ca:

```c
void Swap(int x, int y)  /* Wrong! */
{
    int temp;
    temp = x;
    x = y;      /* just changes local copy */
    y = temp;
}
```

Pentru că parametrii sunt pasați prin valoare, Swap nu poate afecta argumentele a și b din rutina care a apelat-o. Funcția de mai sus doar schimbă copiile lui a și b din rutina Swap însăși.

Deși C nu oferă parametri de apel prin referință, oferă instrumente care permit programatorului să obțină același efect. Pentru a pasa un obiect X ca parametru de referință, programatorul pasează de obicei adresa lui X. Cu alte cuvinte, un pointer la X este trimis. Aceasta se realizează folosind operatorul address-of &. Pe partea de primire, operatorul de dereferențiere * este folosit pentru a urma pointerul înapoi la obiectul original X. Iată un exemplu de apel corect la o funcție Swap:

```c
Swap(&a, &b);
```

Deoarece operatorul & produce adresa unei variabile, &a este un pointer la a. În Swap însăși, parametrii sunt declarați să fie pointeri, și operanzii sunt accesați indirect prin ei.

```c
Swap(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}
```

Următorul exemplu ilustrează pasarea unui parametru de referință de două ori. În acest exemplu, Swap este apelat pentru a schimba x și y. După ce Swap execută, IncrementAndSwap este apelat. IncrementAndSwap pasează a și b (în opoziție cu &a și &b) la Swap. Aceasta este pentru că ambele aceste variabile sunt deja pointeri.

```c
#include <stdio.h>

main()
{
    int x = 10;
    int y = 20;
    
    Swap(&x, &y);
    printf("%d %d\n", x, y);
    
    increment_and_swap(&x, &y);
    printf("%d %d\n", x, y);
}

Swap(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

IncrementAndSwap(int *a, int *b)
{
    (*a)++;
    (*b)++;
    Swap(a, b); /* don't need & here since a and b are already */
                /* int*'s */
}
```

## Apelul prin referință și pointeri

Simularea parametrilor de referință când pasezi pointeri folosește exact aceleași tehnici arătate mai sus, dar sintaxa este în mod special confuză pentru că trebuie să te ocupi cu pointeri la pointeri. Dacă obiectul este un pointer, atunci adresa sa va fi un pointer la un pointer. Dacă vrei să pasezi un obiect ca parametru de referință, pasează adresa acelui obiect. S-ar putea să ai nevoie sau să nu ai nevoie să folosești operatorul & în funcție de dacă expresia pe care o ai deja reprezintă un pointer la obiectul de interes.

Următoarea este o funcție C recursivă care inserează un caracter într-o listă legată sortată. Este un exemplu de folosire a parametrilor care sunt pointeri la pointeri.

```c
struct listrec {
    char data;
    struct listrec *next;
};

main()
{
    struct listrec *head;
    head = NULL;
    
    insert(&head, 'a'); /* Pass the address of head */
    insert(&head, 'b');
}

void Insert(struct listrec **headRef, char c)
/* L is a pointer to a pointer */
{
    if ((!*headRef) ||
        (c < (*headRef)->data)) { /* Dereference headRef before use */
        InsertFront(headRef, c); /* Here it's already the right type. */
    } else {
        insert(&((*headRef)->next), c);
        /* Dereference headRef to get a pointer. Follow the pointer
           to a record and get its next field. Then take the
           address of the next field. */
    }
}

void InsertFront(struct listrec **headRef, char c)
{
    struct listrec *temp;
    temp = (struct listrec *)malloc(sizeof(struct listrec));
    temp->data = c;
    temp->next = *headRef;
    *headRef = temp;
}
```

## Malloc

Funcția malloc, de mai sus în InsertFront, este folosită pentru a aloca spațiu în heap. Este foarte similară cu funcția new din Pascal. Diferența este că malloc ia un parametru întreg care reprezintă numărul de bytes necesari în loc de un tip. Operatorul de timpul compilării sizeof este util aici, deoarece returnează câți bytes sunt folosiți de un tip particular. Funcția free îndeplinește același rol ca și dispose.

Ca un alt exemplu, iată cod recursiv pentru a insera elemente într-un arbore binar fără noduri duplicat.

```c
#include <stdio.h>

struct node {
    char which;
    int howmany;
    struct node *smaller, *bigger;
};

static void Insert(struct node **root, char c)
{
    if (!*root) {
        *root= (struct node *)malloc(sizeof(struct node));
        (*root)->which = c;
        (*root)->howmany = 1;
        (*root)->smaller = (*root)->bigger = NULL;
    }
    else if ((*root)->which == c) {
        (*root)->howmany++;
    }
    else if ((*root)->which > c) {
        Insert(&((*root)->smaller), c);
    }
    else {
        Insert(&((*root)->bigger), c);
    }
}

static void show(struct node *root)
{
    if (root != NULL) {
        show(root->smaller);
        printf("%c: %d \n", root->which, root->howmany);
        show(root->bigger);
    }
}

main()
{
    struct node *root;
    char c;
    
    root = NULL;
    while ((c = getchar()) != EOF) {
        Insert(&root, c);
    }
    show(root);
}
```

## Array-uri avansate în C

În C, un array este format prin aranjarea tuturor elementelor în mod contiguu în memorie. Sintaxa cu paranteze pătrate poate fi folosită pentru a se referi la elementele din array. Array-ul ca întreg este menționat prin adresa primului element.

```c
{
    int array[6];
    int sum = 0;
    sum += array[0] + array[1]; // refer to elements using []
}
```

Programatorul poate să se refere la elementele din array cu sintaxa simplă [] precum array[1]. Această schemă funcționează prin combinarea adresei de bază a întregului array cu indexul pentru a calcula adresa de bază a elementului dorit din array. Necesită doar puțină aritmetică. Fiecare element ocupă un număr fix de bytes care este cunoscut la timpul compilării. Deci adresa celui de-al n-lea element din array (indexare bazată pe 0) va fi la un offset de (n * element_size) bytes de la adresa de bază a întregului array.

```
adresa celui de-al n-lea element = adresa_elementului_0 + (n * dimensiunea_elementului_în_bytes)
```

Sintaxa cu paranteze pătrate [] se ocupă cu această aritmetică de adrese pentru tine, dar este util să știi ce face. [] ia indexul întreg, înmulțește cu dimensiunea elementului, adaugă offset-ul rezultat la adresa de bază a array-ului și în final dereferențiază pointerul rezultat pentru a ajunge la elementul dorit.

### Sintaxa '+'

Într-o sintaxă înrudită, un + între un pointer și un întreg face aceeași calculație de offset, dar lasă rezultatul ca pointer. Sintaxa cu paranteze pătrate dă cel de-al n-lea element în timp ce sintaxa + dă un pointer la cel de-al n-lea element.

Deci expresia (intArray + 3) este un pointer la întregul intArray[3]. (intArray + 3) este de tipul (int*) în timp ce intArray[3] este de tipul int. Cele două expresii diferă doar prin aceea că pointerul este dereferențiat sau nu. Deci expresia (intArray + 3) este exact echivalentă cu expresia (&(intArray[3])). De fapt acele două probabil se compilează în exact același cod. Ambele reprezintă un pointer la elementul de la indexul 3.

Orice expresie [] poate fi scrisă cu sintaxa + în schimb. Trebuie doar să adăugăm dereferențierea pointerului. Deci intArray[3] este exact echivalent cu *(intArray + 3). Pentru majoritatea scopurilor, este cel mai ușor și mai lizibil să folosești sintaxa []. Din când în când + este convenabil dacă aveai nevoie de un pointer la element în loc de elementul în sine.

### Pointer++

Dacă p este un pointer la un element într-un array, atunci (p+1) indică către următorul element din array. Codul poate exploata aceasta folosind construcția p++ pentru a muta un pointer peste elementele într-un array. Nu ajută lizibilitatea deloc, deci nu pot recomanda tehnica, dar s-ar putea să o vezi în cod scris de alții.

Iată o secvență de versiuni ale strcpy scrise în ordine: de la cel mai verbos la cel mai criptic. În primul, bucla while normal simplă este de fapt cam complicată pentru a se asigura că caracterul null de terminare este copiat. Al doilea elimină acea complicație mutând atribuirea în test. Ultimele două sunt drăguțe (și demonstrează folosirea ++ pe pointeri), dar nu sunt într-adevăr tipul de cod pe care vrei să îl menții. Dintre cele patru, cred că al doilea este cel mai bun din punct de vedere stilistic. Cu un compilator inteligent, toate patru se vor compila în practic același cod cu aceeași eficiență.

```c
// Unfortunately, a straight while or for loop won't work.
// The best we can do is use a while (1) with the test
// in the middle of the loop.
void strcpy1(char dest[], const char source[])
{
    int i = 0;
    while (1) {
        dest[i] = source[i];
        if (dest[i] == '\0') break; // we're done
        i++;
    }
}

// Move the assignment into the test
void strcpy2(char dest[], const char source[])
{
    int i = 0;
    while ((dest[i] = source[i]) != '\0') {
        i++;
    }
}

// Get rid of i and just move the pointers.
// Relies on the precedence of * and ++.
void strcpy3(char dest[], const char source[])
{
    while ((*dest++ = *source++) != '\0') ;
}

// Rely on the fact that '\0' is equivalent to FALSE
void strcpy4(char dest[], const char source[])
{
    while (*dest++ = *source++) ;
}
```

### Efectele tipului de pointer

Atât [] cât și + folosesc implicit tipul de timpul compilării al pointerului pentru a calcula element_size care afectează aritmetica de offset. Când te uiți la cod, este ușor să presupui că totul este în unitățile de bytes.

```c
int *p;
p = p + 12; // at run-time, what does this add to p? 12?
```

Codul de mai sus nu adaugă numărul 12 la adresa din p - aceea ar incrementa p cu 12 bytes. Codul de mai sus incrementează p cu 12 int-uri. Fiecare int ia 4 bytes, deci la timpul execuției codul va incrementa efectiv adresa din p cu 48. Compilatorul calculează totul aceasta bazat pe tipul pointerului.

Folosind conversii, următorul cod într-adevăr doar adaugă 12 la adresa din pointerul p. Funcționează spunând compilatorului că pointerul indică către char în loc de int. Dimensiunea char-ului este definită să fie exact 1 byte (sau orice cea mai mică unitate adresabilă este pe calculator). Cu alte cuvinte, sizeof(char) este întotdeauna 1. Apoi convertim (char*) rezultat înapoi la un (int*). Poți folosi conversia așa pentru a schimba codul pe care îl generează compilatorul. Compilatorul doar urmează orb ordinele tale.

```c
p = (int*) ( ((char*)p) + 12);
```

## Array-uri și pointeri

Un efect al schemei de array C este că compilatorul nu distinge în mod semnificativ între array-uri și pointeri - ambele arată doar ca pointeri. În următorul exemplu, valoarea intArray este un pointer la primul element din array deci este un (int*). Valoarea variabilei intPtr este de asemenea (int*) și este setată să indice către un singur întreg i. Deci care este diferența între intArray și intPtr? Nu prea mult în ceea ce privește compilatorul. Ambele sunt doar pointeri (int*), și compilatorul este perfect fericit să aplice sintaxa [] sau + la oricare. Este responsabilitatea programatorului să se asigure că elementele la care se referă o operație [] sau + sunt într-adevăr acolo. Într-adevăr este doar aceeași regulă veche că C nu face nicio verificare a limitelor.

C se gândește la întregul singular i ca doar un fel de array degenerat de dimensiunea 1.

```c
{
    int intArray[6];
    int *intPtr;
    int i;
    
    intPtr = &i;
    
    intArray[3] = 13;   // ok
    intPtr[0] = 12;     // odd, but ok. Changes i.
    intPtr[3] = 13;     // BAD! There is no integer reserved here!
}
```

## Assert

Referințele array în afara limitelor sunt o formă extrem de comună de eroare C la timpul execuției. Poți folosi funcția assert() pentru a împrăștia codul tău cu propriile verificări de limite. Câteva secunde punând instrucțiuni assert îți pot economisi ore de depanare.

```c
#include <assert.h>
{
    int ints[MAX_INTS];
    i = foo(<something complicated>); // i should be in bounds,
                                     // but is it really?
    assert(i>=0);
    assert(i<MAX_INTS);
    ints[i] = 0;
}
```

## Numele array-urilor sunt Const

O distincție subtilă între un array și un pointer este că pointerul care reprezintă adresa de bază a unui array nu poate fi schimbat în cod. Tehnic, adresa de bază a array-ului este un pointer const. Constrângerea se aplică la numele array-ului unde este declarat în cod - variabila ints în exemplul de mai jos.

```c
{
    int ints[100];
    int *p;
    int i;
    
    array = NULL;           // no, cannot change the base addr ptr
    array = &i;             // no
    array = array + 1;      // no
    array++;                // no
    
    p = array;              // ok, p is a regular pointer which can be changed
                           // here it is getting a copy of the value of ARRAY
    p++;                    // ok, p can still be changed (and array cannot)
    p = NULL;               // ok
    p = &i;                 // ok
    
    foo(array);             // ok (possible foo definitions are below)
}
```

Parametrii array sunt pasați ca pointeri. Următoarele două definiții ale foo arată diferit, dar pentru compilator înseamnă exact același lucru. Este preferabil să folosești orice sintaxă este mai precisă pentru lizibilitate. Dacă pointerul care vine într-adevăr este adresa de bază a unui array întreg, atunci folosește [].

```c
void foo(int arrayParam[]) {
    arrayParam = NULL; // Silly but valid. Just changes the local pointer
}

void foo(int *arrayParam) {
    arrayParam = NULL; // ditto
}
```

## Array-uri dinamice

Deoarece array-urile sunt doar zone contigue de bytes, poți aloca propriile array-uri în heap folosind malloc. Următorul cod alocă două array-uri de 1000 int-uri - unul în stivă în mod obișnuit, și unul în heap folosind malloc. În afară de alocările diferite, cele două sunt sintactic similare în utilizare.

```c
{
    int a[1000];
    int *b;
    
    b = malloc(sizeof(int) * 1000);
    
    a[123] = 13;    // Just use good ol' [] to access elements
    b[123] = 13;    // in both arrays.
    
    free(b);
}
```

Există câteva diferențe cheie:

### Avantajele de a fi în heap

• Dimensiunea (în acest caz 1000) poate fi definită la timpul execuției. Nu la fel pentru un array ca "a".

• Array-ul va exista până când este dealocat explicit cu un apel la free().

• Poți schimba dimensiunea array-ului după voie la timpul execuției folosind realloc(). Următoarea schimbă dimensiunea array-ului la 2000. Realloc() se ocupă cu copierea elementelor vechi.

```c
...
b = realloc(b, sizeof(int) * 2000);
```

### Dezavantajele de a fi în heap

• Trebuie să îți amintești să aloci array-ul, și trebuie să o faci corect.

• Trebuie să îți amintești să îl dealoci exact o dată când ai terminat cu el, și trebuie să faci și asta corect.

• Cele două dezavantaje de mai sus au același profil de bază: dacă le greșești, codul tău încă arată bine. Se compilează frumos. Chiar rulează pentru cazuri mici, dar pentru unele cazuri de intrare doar se prăbușește neașteptat pentru că memoria aleatorie este suprascrisă undeva ca fața zâmbitoare. Acest fel de eroare "spărgător de memorie aleatoare" poate fi o adevărată ordalie de urmărit.

## Anexa: Bibliotecile C

Darul meu pentru comunitatea de programare C: O listă de o pagină cu detalii de care sunt sătul să le caut...

### Precedența și asociativitatea

| Operatori | Asociativitate |
|-----------|----------------|
| `function-call()` `[]` `->` `.` | S la D |
| `!` `~` `++` `--` `+` `-` `*(ptr)` `sizeof` (amintește-ți: toți operatorii unari sunt aceiași) | D la S |
| `*` `/` `%` (operatorii binari aritmetici) | S la D |
| `+` `-` | S la D |
| `<` `<=` `>` `>=` | S la D |
| `==` `!=` | S la D |
| și apoi în ordine: `&` `^` `|` `&&` `||` | S la D |
| `=` și toate variantele sale | D la S |
| `,` cea mai mică precedență. Un operator pe care doar un tocilar l-ar putea iubi. | S la D |

O combinație care nu funcționează niciodată corect fără paranteză: `*structptr.field`

### stdio.h

```c
FILE *fopen(const char *fname, const char*mode); // "r"read,"w" write,"a"append, NULL on err
int fclose(FILE *file); // Returns EOF on error.
int fgetc(FILE *in); // Returns next char, or EOF token if no more.
int fputc(int ch, FILE *out); // Writes char to file, returns EOF on err.
int ungetc(int ch, FILE *in); // Push one fgetc char back, may not ungetc EOF, EOF on err
```

#### printf
`%d` int, `%s` (char*), `%f` double, `%e` (double, scientific notation)

FILE*-uri standard, deschise automat: stdin, stdout, stderr

ex: `printf("%d %s\n", 4, "string");` ==> printează: 4 string

printf merge la stdout în mod implicit, fprintf(FILE *out,...) ia un parametru FILE *

### ctype.h

Macro-uri pentru testarea tipului unui caracter: `isalpha(ch)` alfabetic mare sau mic, `islower(ch)`, `isupper()`, `isspace(ch)` tab spațiu newline etc., `isdigit(ch)`

`tolower(ch)` și `toupper(ch)` conversii - funcționează pe orice char, nu e nevoie să testezi primul

### string.h

Niciuna din rutinele de string nu alocă memorie, clientul este responsabil să se asigure că există suficient spațiu. Majoritatea acestora returnează string-ul tocmai scris care este în mare parte inutil.

```c
size_t strlen(const char* string); // ret numărul de chars. strlen("abc")==3
char *strcpy(char *dest, const char* source); // Copiază un string. Amintește-ți: Merge D la S ca =.
char *strncpy(char *dest, const char* source, int n); // Copiază cel mult n chars.
char *strcat(char *dest, const char* source); // Adaugă la sfârșitul dest.
int strcmp(const char *a, const char *b); // Compară și returnează <0:a<b, >0:a>b, ==0:a==b
// amintește-ți: să presupunem că b este 0, returnează locul relativ al lui a.
char *strchr(const char* str, char ch); // ret ptr la prima apariție a ch în str, NULL dacă nu
void* memcpy(void *dest, const void *source, size_t n); // Copiază bytes care nu se suprapun
void* memmove(void *dest, const void *source, size_t n); // Funcționează chiar dacă se suprapun.
```

Aceste două sunt probabil implementate eficient pe orice mașină pe care ești.

### stdlib.h

```c
int rand(void); // returnează numere pseudo-aleatoare (non-negative)
void srand(unsigned int seed); // Setează seed pentru rand. Folosește valoarea time(NULL) din <time.h>.
void *malloc(size_t size); // alocă bloc heap, NULL la eșec. size_t ess. = unsigned long
void *realloc(void *block, size_t size); // mută blocul la noua dimensiune, Returnează noul ptr de folosit
void free(void *block); // Returnează un bloc malloc sau realloc la heap
void exit(int status); // Oprește programul. Pasează EXIT_SUCCESS sau EXIT_FAILURE.

// compare folosit în bsearch și qsort: int cmp(const void *key, const void *x) ret ca strcmp
void *bsearch(const void *key, const void *base, size_t len, size_t elem_size, cmp above);
// returnează adresa elementului găsit, sau NULL dacă nu este găsit
void qsort(void *base, size_t len, size_t elem_size, cmp fn above);
// convenții nume var: "len" sau "n" = numărul de elemente, "size" = numărul de bytes
```

---

Aceasta completează traducerea documentului "Essential C" în limba română. Documentul acoperă toate aspectele fundamentale ale limbajului C, de la tipurile de date de bază până la concepte avansate precum pointerii, managementul memoriei și utilizarea bibliotecilor standard. Este un ghid complet și concis pentru programatorii care doresc să înțeleagă sau să-și reîmprospăteze cunoștințele despre limbajul C.
