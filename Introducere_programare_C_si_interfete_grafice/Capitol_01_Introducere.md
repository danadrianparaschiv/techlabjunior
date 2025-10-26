# Capitolul 1: Noțiuni de bază

## Ce este atât de grozav la C?

C este un limbaj de programare foarte versatil și utilizat pe scară largă. A fost folosit pentru a scrie practic orice, de la rutine de nivel jos pentru controlul hardware-ului în microcontrolere încorporate până la sisteme de operare complete precum Linux, cu interfețe grafice pentru utilizatori. În ciuda acestei flexibilități uriașe, este și relativ simplu – limbajul are doar aproximativ 20 de cuvinte cheie, dar există biblioteci uriașe de funcții suplimentare pe care le puteți apela când aveți nevoie de ele. În prima parte a acestei cărți, ne vom concentra pe învățarea cuvintelor cheie, cu câteva dintre funcțiile de bibliotecă mai frecvent utilizate; a doua parte a cărții arată cum să folosiți biblioteca GTK pentru a facilita scrierea interfețelor grafice în C.

Multe dintre limbajele pe care le-ați putea fi văzut, cum ar fi Python, sunt ceea ce se numesc limbaje interpretate. Aceasta înseamnă că codul pe care îl scrieți este executat direct: fiecare linie de cod este citită și interpretată pe măsură ce îl executați. C este diferit: este un limbaj compilat. Aceasta înseamnă că codul pe care îl scrieți, cunoscut sub numele de cod sursă, nu este niciodată executat direct. Codul sursă este transmis printr-un program numit compilator, care îl convertește într-o versiune lizibilă de mașină numită executabil sau binar; apoi rulați executabilul rezultat.

Acest lucru poate părea complex, dar are câteva avantaje mari. În primul rând, înseamnă că nu aveți nevoie de o copie a lui C pe fiecare computer pe care doriți să rulați programul; odată compilat, executabilul este independent și autonom. În al doilea rând, procesul de compilare va găsi multe erori înainte chiar să rulați programul (dar de obicei nu le va găsi pe toate). Cel mai important, procesul de compilare înseamnă că traducerea consumatoare de timp a codului lizibil de om în instrucțiuni lizibile de mașină a avut deja loc, ceea ce înseamnă că codul compilat rulează în general de multe ori mai rapid decât ar rula codul interpretat.

> **ALEGEȚI-VĂ EDITORUL**
> 
> Puteți utiliza orice editor doriți pentru a introduce codul, atâta timp cât îl salvează ca text simplu. Editorul Geany inclus în Raspberry Pi OS este o alegere bună, dar puteți folosi și Leafpad, nano sau orice altele pe care le preferați.

## Hello World – primul tău program C

Cu toate acestea clarificate – ceea ce sperăm că v-a făcut să credeți că C ar putea merita învățat – să aruncăm o privire la primul program pe care toată lumea îl scrie în orice limbaj, cel care tipărește „Hello World" pe ecran. Apropo, tradiția de a scrie un program Hello World a fost introdusă pentru prima dată cu documentația originală care descrie C în sine. Gândiți-vă doar: fără C, fără Hello World...

```c
#include <stdio.h>

void main (void) 
{ 
  /* A print statement */ 
  printf ("Hello world!\n"); 
}
```

Sperăm că nu este prea înfricoșător! Să îl analizăm linie cu linie.

```c
#include <stdio.h>
```

Aceasta este cunoscută ca o hash-include (includere cu diez). După cum s-a menționat mai sus, limbajul C are o bibliotecă mare de funcții care pot fi incluse, și trebuie să folosim una dintre ele în acest program: comanda printf (print formatat). Aceasta face parte din biblioteca standard de intrare-ieșire, sau stdio pe scurt. Deci ceea ce face această linie este să avertizeze compilatorul că programul trebuie să aibă biblioteca stdio inclusă ca parte a procesului de compilare.

```c
void main (void)
```

C este un limbaj bazat pe funcții; fiecare program este format din mai multe funcții. Fiecare funcție primește zero sau mai multe argumente și returnează o singură valoare. O definiție de funcție constă dintr-o specificare a ceea ce returnează funcția (în acest caz, un void), un nume de funcție (în acest caz, main), și o listă de argumente închise în paranteze rotunde (din nou, un void).

Fiecare program C trebuie să includă o funcție numită main; când rulați programul compilat, funcția main este primul lucru care se execută.

> **SPAȚIILE ALBE NU CONTEAZĂ!**
> 
> Spre deosebire de Python, spațiile albe nu au semnificație în C – puteți pune spații, tab-uri și linii noi oriunde doriți într-un program C pentru a-l face lizibil.

Cuvântul void este numit specificator de tip; un void este un tip special care înseamnă „nicio valoare necesară". Vom analiza mai multe despre tipuri în capitolul următor.

Deci această linie definește funcția main pentru acest program; afirmă că funcția main nu primește argumente și nu returnează nicio valoare.

Codul care alcătuiește funcția în sine este inclus între cele două acolade `{}` care urmează definiției funcției.

```c
/* A print statement */
```

Mai întâi, avem un comentariu care ne spune ce se întâmplă. Comentariile în C încep cu simbolul `/*` și se termină cu `*/` – orice între aceste două simboluri este ignorat de compilator.

Codul în sine este doar o linie:

```c
printf ("Hello world!\n");
```

Acesta este un apel la funcția printf („print formatat") din biblioteca stdio. În acest caz, ia un singur argument, care este un șir de text inclus între ghilimele duble. După cum s-a menționat mai sus, argumentele funcției sunt incluse în paranteze rotunde.

Observați că linia se termină cu un punct și virgulă. Toate instrucțiunile din C trebuie să se termine cu un punct și virgulă; aceasta spune compilatorului că acesta este sfârșitul unei instrucțiuni. Una dintre cele mai frecvente greșeli pentru începători în C este uitarea unui punct și virgulă undeva!

Ce zici de șirul în sine? Partea Hello World! este destul de clară, dar ce zici de acel `\n` de la sfârșit? Amintiți-vă că această funcție se numește „print formatat"? Ei bine, `\n` este un pic de formatare; este simbolul pentru un caracter de linie nouă. Deci această linie va tipări șirul „Hello World!", urmat de o linie nouă.

> **VERIFICAȚI-VĂ PARANTEZELE**
> 
> Asigurați-vă întotdeauna că fiecare paranteză deschisă `{` are o paranteză închisă corespunzătoare `}`. Este ușor să le pierdeți în programe mari!

## Compilarea programului

Să compilăm și să rulăm acest program. Raspberry Pi OS include un compilator C numit gcc, deci nu este nimic de instalat; doar porniți Raspberry Pi OS pe Raspberry Pi și sunteți gata să începeți. Utilizați editorul de text preferat pentru a crea un fișier numit `hello.c`, copiați programul de mai sus în el și salvați-l. Apoi, dintr-un terminal, intrați în directorul unde ați salvat `hello.c` și introduceți:

```bash
gcc -o myprog hello.c
```

Acest lucru rulează compilatorul gcc (GNU C Compiler) pe fișierul `hello.c`. Opțiunea `-o` spune compilatorului să creeze un executabil numit `myprog`. Dacă totul merge bine, nu veți vedea niciun mesaj – compilatorul va produce pur și simplu fișierul executabil. Dacă există erori în cod, compilatorul va afișa mesaje de eroare pentru a vă ajuta să le găsiți și să le corectați.

Pentru a rula programul compilat, tastați:

```bash
./myprog
```

Și ar trebui să vedeți:

```
Hello world!
```

Felicitări – ați scris și executat primul dvs. program C!

## Ce s-a întâmplat?

Când ați rulat comanda gcc, compilatorul a luat fișierul sursă `hello.c` și l-a transformat într-un executabil numit `myprog`. Acest proces a implicat mai multe etape:

1. **Preprocesare** – Toate directivele `#include` sunt procesate, inserând conținutul fișierelor antet în codul dvs.
2. **Compilare** – Codul sursă C este transformat în cod de asamblare.
3. **Asamblare** – Codul de asamblare este transformat în cod mașină (cod obiect).
4. **Linking** – Codul obiect este combinat cu bibliotecile necesare pentru a crea executabilul final.

Toate aceste etape se întâmplă automat când rulați gcc, deci nu trebuie să vă faceți griji pentru ele deocamdată.

## Găsirea și corectarea erorilor

Dacă ați făcut o greșeală în cod, compilatorul vă va spune. De exemplu, dacă uitați punct și virgula de la sfârșitul instrucțiunii printf:

```c
printf ("Hello world!\n")
```

Veți primi o eroare de compilare care arată cam așa:

```
hello.c: In function 'main':
hello.c:7:5: error: expected ';' before '}' token
```

Aceasta vă spune că este o problemă în funcția main, la linia 7, coloana 5, și că compilatorul se aștepta să găsească un punct și virgulă înainte de simbolul `}`.

Erorile de compilare pot părea intimidante la început, dar cu practica veți învăța să le citiți și să înțelegeți rapid ce trebuie corectat.

## Rezumat

În acest capitol, ați învățat:

- Ce este C și de ce este util
- Diferența dintre limbajele interpretate și compilate
- Structura de bază a unui program C
- Cum să compilați și să rulați un program C
- Cum să găsiți și să corectați erorile de bază

În capitolul următor, vom învăța despre variabile și operații aritmetice în C.
