# Capitolul 1 – Instalarea Python și Pygame

Ar ajuta dacă știi puțin despre programarea în Python (sau cum să programezi în alt limbaj pe lângă Python) înainte să citești această carte; totuși, chiar dacă nu știi, poți citi această carte oricum. Programarea nu este nici pe departe atât de grea pe cât cred oamenii. Dacă întâmpini probleme, poți citi cartea gratuită "Invent Your Own Computer Games with Python" online la http://inventwithpython.com sau să cauți un subiect care te confuzează pe wiki-ul Invent with Python la http://inventwithpython.com/wiki.

Nu trebuie să știi cum să folosești biblioteca Pygame înainte să citești această carte. Următorul capitol este un scurt tutorial despre toate caracteristicile și funcțiile majore ale Pygame.

Pentru cazul în care nu ai citit prima carte și nu ai instalat deja Python și Pygame pe calculator, instrucțiunile de instalare sunt în acest capitol. Dacă ai instalat deja pe amândouă, poți sări peste acest capitol.

## Instalarea Python

Înainte să putem începe programarea, va trebui să instalezi un software numit interpretorul Python pe calculatorul tău. (S-ar putea să ai nevoie să ceri ajutorul unui adult aici.) Interpretorul este un program care înțelege instrucțiunile pe care le vei scrie (sau mai degrabă, le vei tasta) în limbajul Python. Fără interpretor, calculatorul tău nu va putea rula programele tale Python. Ne vom referi la "interpretorul Python" pur și simplu ca "Python" de acum înainte.

Software-ul interpretorului Python poate fi descărcat de pe site-ul oficial al limbajului de programare Python, http://www.python.org. S-ar putea să vrei ajutorul altcuiva pentru a descărca și instala software-ul Python. Instalarea este puțin diferită în funcție de sistemul de operare al calculatorului tău - Windows, Mac OS X sau un OS Linux precum Ubuntu. Poți găsi și videoclipuri online cu oameni care instalează software-ul Python pe calculatoarele lor la http://invpy.com/installing.

### Instalarea pe Windows

Când accesezi http://python.org, ar trebui să vezi o listă de link-uri în stânga (precum "About", "News", "Documentation", "Download", etc.). Fă clic pe link-ul Download pentru a merge la pagina de descărcare, apoi caută fișierul numit "Python 3.2 Windows Installer (Windows binary -- does not include source)" și fă clic pe link-ul său pentru a descărca Python pentru Windows.

Fă dublu-clic pe fișierul python-3.2.msi pe care tocmai l-ai descărcat pentru a porni instalatorul Python. (Dacă nu pornește, încearcă să faci clic dreapta pe fișier și alege Install.) Odată ce instalatorul pornește, pur și simplu continuă să faci clic pe butonul Next și acceptă opțiunile din instalator pe măsură ce mergi (nu e nevoie să faci modificări). Când instalarea s-a terminat, fă clic pe Finish.

### Instalarea pe Mac OS X

Mac OS X 10.5 vine cu Python 2.5.1 pre-instalat de Apple. În prezent, Pygame suportă doar Python 2 și nu Python 3. Totuși, programele din această carte funcționează atât cu Python 2 cât și cu 3.

Site-ul Python are de asemenea informații suplimentare despre folosirea Python pe Mac la http://docs.python.org/dev/using/mac.html.

### Instalarea pe Linux

Pygame pentru Linux de asemenea suportă doar Python 2, nu Python 3. Dacă sistemul tău de operare este Ubuntu, poți instala Python deschizând o fereastră de terminal (de pe desktop fă clic pe Applications > Accessories > Terminal) și introducând "sudo apt-get install python2.7" apoi apăsând Enter. Va trebui să introduci parola de root pentru a instala Python, așa că cere persoanei care deține calculatorul să tasteze această parolă dacă nu o știi.

De asemenea trebuie să instalezi software-ul IDLE. Din terminal, tastează "sudo apt-get install idle". Parola de root este de asemenea necesară pentru a instala IDLE (cere proprietarului calculatorului să tasteze această parolă pentru tine).

## Pornirea IDLE

Vom folosi software-ul IDLE pentru a tasta programele noastre și a le rula. IDLE înseamnă Interactive DeveLopment Environment (Mediu de Dezvoltare Interactiv). Mediul de dezvoltare este un software care face ușoară scrierea programelor Python, la fel cum software-ul de procesare de text face ușoară scrierea cărților.

- **Dacă sistemul tău de operare este Windows XP**, ar trebui să poți rula Python făcând clic pe butonul Start, apoi selectând Programs, Python 3.1, IDLE (Python GUI). Pentru Windows Vista sau Windows 7, pur și simplu fă clic pe butonul Windows din colțul din stânga jos, tastează "IDLE" și selectează "IDLE (Python GUI)".

- **Dacă sistemul tău de operare este Mac OS X**, pornește IDLE deschizând fereastra Finder și fă clic pe Applications, apoi fă clic pe Python 3.2, apoi fă clic pe iconița IDLE.

- **Dacă sistemul tău de operare este Ubuntu sau Linux**, pornește IDLE deschizând o fereastră de terminal și apoi tastează "idle3" și apasă Enter. S-ar putea să poți face clic și pe Applications în partea de sus a ecranului, și apoi să selectezi Programming, apoi IDLE 3.

Fereastra care apare când rulezi IDLE pentru prima dată se numește shell interactiv. Un shell este un program care îți permite să tastezi instrucțiuni în calculator. Shell-ul Python îți permite să tastezi instrucțiuni Python, iar shell-ul trimite aceste instrucțiuni interpretorului Python pentru a fi executate.

## Instalarea Pygame

Pygame nu vine cu Python. Ca și Python, Pygame este disponibil gratuit. Va trebui să descarci și să instalezi Pygame, ceea ce este la fel de ușor ca descărcarea și instalarea interpretorului Python. Într-un browser web, mergi la URL-ul http://pygame.org și fă clic pe link-ul "Downloads" din partea stângă a site-ului. Această carte presupune că ai sistemul de operare Windows, dar Pygame funcționează la fel pentru fiecare sistem de operare. Trebuie să descarci instalatorul Pygame pentru sistemul tău de operare și versiunea de Python pe care o ai instalată.

Nu vrei să descarci "source"-ul pentru Pygame, ci mai degrabă "binary"-ul Pygame pentru sistemul tău de operare.

- **Pentru Windows**, descarcă fișierul pygame-1.9.1.win32-py3.2.msi. (Acesta este Pygame pentru Python 3.2 pe Windows. Dacă ai instalat o versiune diferită de Python (precum 2.7 sau 2.6) descarcă fișierul .msi pentru versiunea ta de Python.) Versiunea curentă de Pygame la momentul scrierii acestei cărți este 1.9.1. Dacă vezi o versiune mai nouă pe site, descarcă și instalează Pygame-ul mai nou.

- **Pentru Mac OS X**, descarcă fișierul .zip sau .dmg pentru versiunea de Python pe care o ai și rulează-l.

- **Pentru Linux**, deschide un terminal și rulează "sudo apt-get install python-pygame".

Pe Windows, fă dublu-clic pe fișierul descărcat pentru a instala Pygame. Pentru a verifica că Pygame este instalat corect, tastează următorul în shell-ul interactiv:

```python
>>> import pygame
```

Dacă nu apare nimic după ce apeși tasta Enter, atunci știi că Pygame a fost instalat cu succes. Dacă apare eroarea `ImportError: No module named pygame`, atunci încearcă să instalezi Pygame din nou (și asigură-te că ai tastat `import pygame` corect).

## Cum să folosești această carte

Acest capitol are cinci programe mici care demonstrează cum să folosești diferitele caracteristici pe care le oferă Pygame. În ultimul capitol, vei folosi aceste caracteristici pentru un joc complet scris în Python cu Pygame.

Un tutorial video despre cum să instalezi Pygame este disponibil pe site-ul acestei cărți la http://invpy.com/videos.

"Making Games with Python & Pygame" este diferită de alte cărți de programare pentru că se concentrează pe codul sursă complet pentru mai multe programe de jocuri. În loc să te învețe concepte de programare și să te lase pe tine să îți dai seama cum să faci programe cu acele concepte, această carte îți arată niște programe și apoi explică cum sunt puse împreună.

În general, ar trebui să citești aceste capitole în ordine. Sunt multe concepte care sunt folosite din nou și din nou în aceste jocuri, și sunt explicate în detaliu doar în primul joc în care apar. Dar dacă există un joc care ți se pare interesant, du-te înainte și sari la acel capitol. Poți citi întotdeauna capitolele anterioare mai târziu dacă ai luat-o înainte.

### Descărcarea și tastarea codului sursă

Fiecare capitol se concentrează pe un singur program de joc și explică cum funcționează diferite părți ale codului. Este foarte util să copiezi aceste programe tastând codul linie cu linie din această carte.

Totuși, poți de asemenea descărca fișierul cu codul sursă de pe site-ul acestei cărți. Într-un browser web, mergi la URL-ul http://invpy.com/source și urmează instrucțiunile pentru a descărca fișierul cu codul sursă. Dar tastarea codului singur chiar te ajută să înveți codul mai bine.

Deși poți pur și simplu să tastezi codul pe care îl citești din această carte, va trebui să descarci fișierele grafice și de sunet folosite de jocurile din această carte de la http://invpy.com/downloads. Asigură-te că aceste fișiere imagine și sunet sunt localizate în același folder ca fișierul .py Python, altfel programul tău Python nu va putea găsi aceste fișiere.

### Nu tasta numerele de linie

Când introduci codul sursă singur, nu tasta numerele de linie care apar la începutul fiecărei linii. De exemplu, dacă vezi acest lucru în carte:

```
1. number = random.randint(1, 20)
2. spam = 42
3. print('Hello world!')
```

Nu trebuie să tastezi "1." din partea stângă, sau spațiul care îl urmează imediat. Pur și simplu tastează așa:

```python
number = random.randint(1, 20)
spam = 42
print('Hello world!')
```

Acele numere sunt folosite doar pentru ca această carte să poată face referire la linii specifice din cod. Nu sunt parte din programul propriu-zis.

### Indentarea contează în Python

Pe lângă numerele de linie, asigură-te să introduci codul exact cum apare. Observă că unele dintre linii nu încep la marginea din stânga a paginii, ci sunt indentate cu patru sau opt sau mai multe spații. Asigură-te să pui numărul corect de spații la începutul fiecărei linii. (Deoarece fiecare caracter în IDLE are aceeași lărgime, poți număra spațiile numărând numărul de caractere deasupra sau dedesubtul liniei la care te uiți.)

De exemplu, în codul de mai jos, poți vedea că a doua linie este indentată cu patru spații pentru că cele patru caractere ("whil") de pe linia de deasupra sunt peste spațiul indentat. A treia linie este indentată cu încă patru spații (cele patru caractere, "if n" sunt deasupra spațiului indentat al celei de-a treia linii):

```python
while spam < 10:
    if number == 42:
        print('Hello')
```

### Linia lungă de cod

Unele linii de cod sunt prea lungi pentru a încăpea pe o linie pe paginile din această carte, și textul codului se va înfășura pe linia următoare. Când tastezi aceste linii în editorul de fișiere, introdu codul tot pe o linie fără să apeși Enter.

Poți spune când începe o linie nouă uitându-te la numerele de linie din partea stângă a codului. De exemplu, codul de mai jos are doar două linii de cod, chiar dacă prima linie se înfășoară:

```
1. print('This is the first line! xxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxx')
2. print('This is the second line, not the third line.')
```

### Găsirea erorilor cu instrumentul Diff online

Unele dintre programele din această carte sunt puțin lungi. Deși este foarte util să înveți Python tastând codul sursă pentru aceste programe, s-ar putea să faci accidental greșeli de tastare care fac programele tale să se prăbușească. S-ar putea să nu fie evident unde este greșeala de tastare.

Poți copia și lipi textul codului tău sursă în instrumentul diff online de pe site-ul cărții. Instrumentul diff va arăta orice diferențe dintre codul sursă din carte și codul sursă pe care l-ai tastat. Aceasta este o modalitate ușoară de a găsi orice greșeli de tastare din programul tău.

Copierea și lipirea textului este o abilitate foarte utilă la calculator, în special pentru programarea pe calculator. Există un tutorial video despre copierea și lipirea pe site-ul acestei cărți la http://invpy.com/copypaste.

Instrumentul diff online este la această pagină web: http://invpy.com/diff/pygame. Există de asemenea un tutorial video despre cum să folosești acest instrument pe site-ul cărții.

## Link-urile "More Info"

Există multe lucruri pe care le poți învăța despre programare. Dar nu trebuie să le înveți pe toate acum. Sunt de mai multe ori în această carte când s-ar putea să vrei să înveți aceste detalii și explicații suplimentare, dar dacă le-aș fi inclus în această carte, atunci ar fi adăugat multe pagini în plus. Dacă această carte mai mare și mai grea ar cădea accidental pe tine, greutatea acestor multe pagini suplimentare te-ar zdrobi, rezultând în moarte. În schimb, am inclus link-uri "more info" în această carte pe care le poți urma pe site-ul acestei cărți. Nu trebuie să citești aceste informații suplimentare pentru a înțelege ceva din această carte, dar sunt acolo dacă ești curios. Aceste link-uri (și altele) au fost scurtate și încep cu http://invpy.com.

Toate informațiile din aceste link-uri "more info" pot fi de asemenea descărcate de la http://invpy.com/pygamemoreinfo.

Chiar dacă această carte nu este periculos de grea, te rog să nu o lași să cadă pe tine oricum.