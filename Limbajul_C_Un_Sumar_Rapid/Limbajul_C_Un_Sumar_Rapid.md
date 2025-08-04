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

