# Capitolul 2 – Bazele Pygame

La fel cum Python vine cu mai multe module precum random, math sau time care oferă funcții suplimentare pentru programele tale, framework-ul Pygame include mai multe module cu funcții pentru desenarea graficilor, redarea sunetelor, gestionarea intrării de la mouse și alte lucruri.

Acest capitol va acoperi modulele și funcțiile de bază pe care le oferă Pygame și presupune că știi deja programarea de bază în Python. Dacă ai probleme cu unele dintre conceptele de programare, poți citi cartea "Invent Your Own Computer Games with Python" online la [http://invpy.com/book](//invpy.com/book). Această carte se adresează începătorilor completi în programare.

Cartea "Invent with Python" are de asemenea câteva capitole care acoperă Pygame. Le poți citi online la [https://inventwithpython.com/invent4thed/chapter17.html](https://inventwithpython.com/invent4thed/chapter17.html).

Odată ce înveți mai multe despre Pygame, poți vizualiza celelalte module pe care le oferă Pygame din documentația online de la [http://pygame.org/docs](http://pygame.org/docs).

## Programele GUI vs CLI

Programele Python pe care le poți scrie cu funcțiile încorporate ale Python se ocupă doar cu textul prin funcțiile print() și input(). Programul tău poate afișa text pe ecran și să lase utilizatorul să tasteze text de la tastatură. Acest tip de program are o interfață de linie de comandă, sau CLI (care se pronunță ca prima parte din "climb" și rimează cu "sky"). Aceste programe sunt oarecum limitate pentru că nu pot afișa grafice, nu au culori sau nu pot folosi mouse-ul. Aceste programe CLI primesc intrări doar de la tastatură cu funcția input() și chiar și atunci utilizatorul trebuie să apese Enter înainte ca programul să poată răspunde la intrare. Aceasta înseamnă că jocurile de acțiune în timp real (adică, să continue să ruleze cod fără să aștepte utilizatorul) sunt imposibil de făcut.

Pygame oferă funcții pentru crearea programelor cu o interfață grafică pentru utilizator, sau GUI (pronunțat "gooey"). În loc de un CLI bazat pe text, programele cu GUI bazat pe grafice pot afișa o fereastră cu imagini și culori.

## Programul "Hello World"

Primul nostru program făcut cu Pygame este un program mic care face să apară pe ecran o fereastră care spune "Hello World!". Deschide o fereastră nouă de editor de fișiere făcând clic pe meniul File al IDLE, apoi New Window. Tastează următorul cod în editorul de fișiere IDLE și salvează-l ca blankpygame.py. Apoi rulează programul apăsând F5 sau selectând Run > Run Module din meniul de sus al editorului de fișiere.

Amintește-ți, nu tasta numerele sau punctele de la începutul fiecărei linii (acestea sunt doar pentru referință în această carte).

```python
import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
```

Când rulezi acest program, va apărea o fereastră neagră ca aceasta:

Bravo! Tocmai ai făcut cel mai plictisitor joc video din lume! Este doar o fereastră goală cu "Hello World!" în partea de sus a ferestrei (în ceea ce se numește bara de titlu a ferestrei, care conține textul de antet). Dar crearea unei ferestre este primul pas în crearea jocurilor grafice. Când faci clic pe butonul X din colțul ferestrei, programul se va încheia și fereastra va dispărea.

Apelarea funcției print() pentru a face textul să apară în fereastră nu va funcționa pentru că print() este o funcție pentru programele CLI. La fel și pentru input() pentru a obține intrare de la tastatură de la utilizator. Pygame folosește alte funcții pentru intrare și ieșire care sunt explicate mai târziu în acest capitol. Pentru moment, să ne uităm la fiecare linie din programul nostru "Hello World" în detaliu.

### Instrucțiuni import

Primele câteva linii de cod din programul Hello World sunt linii care vor începe aproape fiecare program pe care îl scrii și care folosește Pygame.

```python
import pygame, sys
```

Linia 1 este o instrucțiune import simplă care importă modulele pygame și sys astfel încât programul nostru să poată folosi funcțiile din ele. Toate funcțiile Pygame care se ocupă cu grafica, sunetul și alte caracteristici pe care le oferă Pygame sunt în modulul pygame.

Observă că atunci când importi modulul pygame, importi automat și toate modulele care sunt în modulul pygame, precum pygame.images și pygame.mixer.music. Nu este nevoie să importi aceste module-în-module cu instrucțiuni import suplimentare.

```python
from pygame.locals import *
```

Linia 2 este de asemenea o instrucțiune import. Totuși, în loc de formatul `import modulename`, folosește formatul `from modulename import *`. În mod normal, dacă vrei să apelezi o funcție care este într-un modul, trebuie să folosești formatul `modulename.functionname()` după importarea modulului. Totuși, cu `from modulename import *`, poți sări partea `modulename.` și să folosești pur și simplu `functionname()` (la fel ca funcțiile încorporate ale Python).

Motivul pentru care folosim această formă de instrucțiune import pentru pygame.locals este că pygame.locals conține mai multe variabile constante care sunt ușor de identificat ca fiind în modulul pygame.locals fără `pygame.locals.` în fața lor. Pentru toate celelalte module, în general vrei să folosești formatul obișnuit `import modulename`. (Există mai multe informații despre de ce vrei să faci asta la [http://invpy.com/namespaces](//invpy.com/namespaces).)

### Inițializarea Pygame

```python
pygame.init()
```

Linia 4 este apelul funcției pygame.init(), care trebuie întotdeauna apelată după importarea modulului pygame și înainte de apelarea oricărei alte funcții Pygame. Nu trebuie să știi ce face această funcție, trebuie doar să știi că trebuie apelată prima pentru ca multe funcții Pygame să funcționeze. Dacă vezi vreodată un mesaj de eroare precum `pygame.error: font not initialized`, verifică să vezi dacă ai uitat să apelezi pygame.init() la începutul programului tău.

### Setarea ferestrei de afișare

```python
DISPLAYSURF = pygame.display.set_mode((400, 300))
```

Linia 5 este un apel la funcția pygame.display.set_mode(), care returnează obiectul pygame.Surface pentru fereastră. (Obiectele Surface sunt descrise mai târziu în acest capitol.) Observă că pasăm o valoare tuple de două întregi funcției: (400, 300). Acest tuple îi spune funcției set_mode() cât de lată și cât de înaltă să facă fereastra în pixeli. (400, 300) va face o fereastră cu o lățime de 400 pixeli și înălțime de 300 pixeli.

Amintește-ți să pasezi un tuple de două întregi la set_mode(), nu doar două întregi în sine. Modalitatea corectă de a apela funcția este așa: `pygame.display.set_mode((400, 300))`. Un apel de funcție precum `pygame.display.set_mode(400, 300)` va cauza o eroare care arată așa: `TypeError: argument 1 must be 2-item sequence, not int`.

Obiectul pygame.Surface (le vom numi doar obiecte Surface pe scurt) returnat este stocat într-o variabilă numită DISPLAYSURF.

```python
pygame.display.set_caption('Hello World!')
```

Linia 6 setează textul de antet care va apărea în partea de sus a ferestrei apelând funcția pygame.display.set_caption(). Valoarea string 'Hello World!' este pasată în acest apel de funcție pentru a face acel text să apară ca antet.

### Bucla principală de joc

```python
while True: # main game loop
    for event in pygame.event.get():
```

Linia 7 este o buclă while care are o condiție de pur și simplu valoarea True. Aceasta înseamnă că nu iese niciodată din cauza condiției sale care se evaluează la False. Singura modalitate prin care execuția programului va ieși vreodată din buclă este dacă o instrucțiune break este executată (care mută execuția la prima linie după buclă) sau sys.exit() (care termină programul). Dacă o buclă ca aceasta era în interiorul unei funcții, o instrucțiune return va muta de asemenea execuția din buclă (precum și din funcție).

Jocurile din această carte au toate aceste bucle `while True` în ele împreună cu un comentariu care o numește "bucla principală de joc". O buclă de joc (numită și buclă principală) este o buclă unde codul face trei lucruri:

1. Gestionează evenimentele.
2. Actualizează starea jocului.  
3. Desenează starea jocului pe ecran.

Starea jocului este pur și simplu o modalitate de a se referi la un set de valori pentru toate variabilele dintr-un program de joc. În multe jocuri, starea jocului include valorile din variabilele care urmăresc sănătatea și poziția jucătorului, sănătatea și poziția oricăror inamici, ce marcaje au fost făcute pe o tablă, scorul sau a cui este rândul. Ori de câte ori se întâmplă ceva precum jucătorul care suferă daune (care îi scade valoarea sănătății), sau un inamic se mută undeva, sau se întâmplă ceva în lumea jocului, spunem că starea jocului s-a schimbat.

Dacă ai jucat vreodată un joc care te-a lăsat să salvezi, "save state"-ul este starea jocului în punctul în care l-ai salvat. În majoritatea jocurilor, întreruperea jocului va împiedica starea jocului să se schimbe.

Deoarece starea jocului este de obicei actualizată ca răspuns la evenimente (precum clicuri de mouse sau apăsări de taste) sau trecerea timpului, bucla de joc verifică constant și re-verifică de multe ori pe secundă pentru orice evenimente noi care s-au întâmplat. În interiorul buclei principale este cod care se uită la care evenimente au fost create (cu Pygame, aceasta se face apelând funcția pygame.event.get()). Bucla principală are de asemenea cod care actualizează starea jocului bazat pe care evenimente au fost create. Aceasta se numește de obicei gestionarea evenimentelor.

### Gestionarea evenimentelor

Ori de câte ori utilizatorul face una din mai multe acțiuni (sunt listate mai târziu în acest capitol) precum apăsarea unei taste de la tastatură sau mișcarea mouse-ului pe fereastra programului, un obiect pygame.event.Event este creat de biblioteca Pygame pentru a înregistra acest "eveniment". (Acesta este un tip de obiect numit Event care există în modulul event, care în sine este în modulul pygame.) Putem afla care evenimente s-au întâmplat apelând funcția pygame.event.get(), care returnează o listă de obiecte pygame.event.Event (pe care le vom numi pur și simplu obiecte Event pe scurt).

Lista obiectelor Event va fi pentru fiecare eveniment care s-a întâmplat de la ultima dată când funcția pygame.event.get() a fost apelată. (Sau, dacă pygame.event.get() nu a fost niciodată apelată, evenimentele care s-au întâmplat de la începutul programului.)

```python
while True: # main game loop
    for event in pygame.event.get():
```

Linia 8 este o buclă for care va itera peste lista obiectelor Event care a fost returnată de pygame.event.get(). La fiecare iterație prin bucla for, o variabilă numită event va fi atribuită valoarea următorului obiect event din această listă. Lista obiectelor Event returnată de pygame.event.get() va fi în ordinea în care evenimentele s-au întâmplat. Dacă utilizatorul a făcut clic pe mouse și apoi a apăsat o tastă de la tastatură, obiectul Event pentru clicul de mouse ar fi primul element din listă și obiectul Event pentru apăsarea tastei ar fi al doilea. Dacă nu s-au întâmplat evenimente, atunci pygame.event.get() va returna o listă goală.

```python
if event.type == QUIT:
    pygame.quit()
    sys.exit()
```

Obiectele Event au o variabilă membru (numită și atribute sau proprietăți) numită type care ne spune ce fel de eveniment reprezintă obiectul. Pygame are o variabilă constantă pentru fiecare din tipurile posibile în modulele pygame.locals. Linia 9 verifică dacă tipul obiectului Event este egal cu constanta QUIT. Amintește-ți că deoarece am folosit forma `from pygame.locals import *` a instrucțiunii import, trebuie doar să tastăm QUIT în loc de pygame.locals.QUIT.

Dacă obiectul Event este un eveniment quit, atunci funcțiile pygame.quit() și sys.exit() sunt apelate. Funcția pygame.quit() este cam opusul funcției pygame.init(): rulează cod care dezactivează biblioteca Pygame. Programele tale ar trebui să apeleze întotdeauna pygame.quit() înainte să apeleze sys.exit() pentru a termina programul. În mod normal nu contează cu adevărat deoarece Python o închide când programul se închide oricum. Dar există o eroare în IDLE care face IDLE să se blocheze dacă un program Pygame se termină înainte ca pygame.quit() să fie apelată.

Deoarece nu avem instrucțiuni if care rulează cod pentru alte tipuri de obiecte Event, nu există cod de gestionare a evenimentelor pentru când utilizatorul face clic pe mouse, apasă taste de la tastatură sau cauzează orice alt tip de obiecte Event să fie create. Utilizatorul poate face lucruri pentru a crea aceste obiecte Event dar nu schimbă nimic în program pentru că programul nu are niciun cod de gestionare a evenimentelor pentru aceste tipuri de obiecte Event. După ce bucla for de la linia 8 a terminat de gestionat toate obiectele Event care au fost returnate de pygame.event.get(), execuția programului continuă la linia 12.

### Desenarea pe ecran

```python
pygame.display.update()
```

Linia 12 apelează funcția pygame.display.update(), care desenează obiectul Surface returnat de pygame.display.set_mode() pe ecran (amintește-ți că am stocat acest obiect în variabila DISPLAYSURF). Deoarece obiectul Surface nu s-a schimbat (de exemplu, prin unele din funcțiile de desenare care sunt explicate mai târziu în acest capitol), aceeași imagine neagră este redesenată pe ecran de fiecare dată când pygame.display.update() este apelată.

Acesta este întregul program. După ce linia 12 este gata, bucla while infinită începe din nou de la început. Acest program nu face nimic în afară de a face să apară o fereastră neagră pe ecran, să verifice constant pentru un eveniment QUIT și apoi să redeseneze fereastra neagră neschimbată pe ecran din nou și din nou. Să învățăm cum să facem lucruri interesante să apară pe această fereastră în loc de doar negru prin învățarea despre pixeli, obiecte Surface, obiecte Color, obiecte Rect și funcțiile de desenare Pygame.

## Pixeli

Fereastra pe care o creează programul "Hello World" este doar compusă din puncte pătrate mici pe ecranul tău numite pixeli. Fiecare pixel începe ca negru dar poate fi setat la o culoare diferită. Imaginează-ți că în loc de un obiect Surface care este lat de 400 pixeli și înalt de 300 pixeli, am avea doar un obiect Surface care era de 8 pixeli pe 8 pixeli. Dacă acea Surface mică de 8x8 era mărită astfel încât fiecare pixel să arate ca un pătrat într-o grilă, și am adăuga numere pentru axele X și Y, atunci o reprezentare bună a ei ar putea arăta cam așa:

Putem să ne referim la un pixel specific folosind un sistem de coordonate carteziene. Fiecare coloană a axei X și fiecare rând al axei Y va avea o "adresă" care este un întreg de la 0 la 7 astfel încât să putem localiza orice pixel specificând întregii axelor X și Y.

De exemplu, în imaginea 8x8 de mai sus, putem vedea că pixelii la coordonatele XY (4, 0), (2, 2), (0, 5) și (5, 6) au fost pictați negri, pixelul la (2, 4) a fost pictat gri, în timp ce toți ceilalți pixeli sunt pictați albi. Coordonatele XY sunt numite și puncte. Dacă ai luat o oră de matematică și ai învățat despre coordonatele carteziene, s-ar putea să observi că axa Y începe la 0 în partea de sus și apoi crește mergând în jos, mai degrabă decât să crească pe măsură ce merge în sus. Așa funcționează pur și simplu coordonatele carteziene în Pygame (și aproape fiecare limbaj de programare).

Framework-ul Pygame reprezintă adesea coordonatele carteziene ca un tuple de două întregi, precum (4, 0) sau (2, 2). Primul întreg este coordonata X și al doilea este coordonata Y. (Coordonatele carteziene sunt acoperite în mai multe detalii în capitolul 12 din "Invent Your Own Computer Games with Python" la [https://inventwithpython.com/invent4thed/chapter12.html](https://inventwithpython.com/invent4thed/chapter12.html))

## Diferența între funcții și metode

Funcțiile și metodele sunt aproape același lucru. Ambele pot fi apelate pentru a executa codul din ele. Diferența dintre o funcție și o metodă este că o metodă va fi întotdeauna atașată unui obiect. De obicei metodele schimbă ceva despre acel obiect particular (poți să te gândești la obiectul atașat ca la un fel de argument permanent pasat metodei).

Acesta este un apel de funcție al unei funcții numite foo():

```python
foo()
```

Acesta este un apel de metodă al unei metode numite de asemenea foo(), care este atașată unui obiect stocat într-o variabilă numită duckie:

```python
duckie.foo()
```

Un apel la o funcție în interiorul unui modul poate arăta ca un apel de metodă. Pentru a spune diferența, trebuie să te uiți la primul nume și să vezi dacă este numele unui modul sau numele unei variabile care conține un obiect. Poți spune că sys.exit() este un apel la o funcție în interiorul unui modul, pentru că în partea de sus a programului va fi o instrucțiune import precum import sys.

O funcție constructor este același lucru ca un apel de funcție normal, cu excepția că valoarea sa de retur este un obiect nou. Doar uitându-te la codul sursă, o funcție și o funcție constructor arată la fel. Funcțiile constructor (numite și pur și simplu "constructor" sau uneori "ctor" ("see-tor") pe scurt) sunt doar un nume dat funcțiilor care returnează un obiect nou. Dar de obicei ctor-ii încep cu o literă mare. Din acest motiv când îți scrii propriile programe, numele funcțiilor tale ar trebui să înceapă doar cu o literă mică.

De exemplu, pygame.Rect() și pygame.Surface() sunt ambele funcții constructor în interiorul modulului pygame care returnează obiecte Rect și Surface noi. (Aceste obiecte sunt descrise mai târziu.)

Iată un exemplu de apel de funcție, apel de metodă și apel la o funcție în interiorul unui modul:

```python
import whammy

fizzy()
egg = Wombat()
egg.bluhbluh()
whammy.spam()
```

Chiar dacă aceste nume sunt toate inventate, poți spune care este un apel de funcție, un apel de metodă și un apel la o funcție în interiorul unei metode. Numele whammy se referă la un modul, deoarece poți vedea că este importat pe prima linie. Numele fizzy nu are nimic înainte și paranteze după, deci știi că este un apel de funcție.

Wombat() este de asemenea un apel de funcție, în acest caz este o funcție constructor care returnează un obiect. (Litera mare cu care începe nu este o garanție că este o funcție constructor mai degrabă decât o funcție obișnuită, dar este o pariere sigură.) Obiectul este stocat într-o variabilă numită egg. Apelul egg.bluhbluh() este un apel de metodă, pe care îl poți spune pentru că bluhbluh este atașat unei variabile cu un obiect în ea.

Între timp, whammy.spam() este un apel de funcție, nu un apel de metodă. Poți spune că nu este o metodă pentru că numele whammy a fost importat ca modul mai devreme.

## Obiecte Surface

Obiectele Surface sunt obiecte care reprezintă o imagine 2D dreptunghiulară. Pixelii obiectului Surface pot fi schimbați apelând funcțiile de desenare Pygame (descrise mai târziu în acest capitol) și apoi afișați pe ecran. Bordura ferestrei, bara de titlu și butoanele nu fac parte din obiectul Surface de afișare.

În particular, obiectul Surface returnat de pygame.display.set_mode() se numește Surface de afișare. Orice este desenat pe obiectul Surface de afișare va fi afișat pe fereastră când funcția pygame.display.update() este apelată. Este mult mai rapid să desenezi pe un obiect Surface (care există doar în memoria calculatorului) decât să desenezi un obiect Surface pe ecranul calculatorului. Memoria calculatorului este mult mai rapidă de schimbat decât pixelii pe un monitor.

Adesea programul tău va desena mai multe lucruri diferite pe un obiect Surface. Odată ce ai terminat de desenat totul pe obiectul Surface de afișare pentru această iterație a buclei de joc (numit un cadru, la fel cum o imagine fixă pe un DVD întrerupt se numește) pe un obiect Surface, poate fi desenat pe ecran. Calculatorul poate desena cadre foarte repede, și programele noastre vor rula adesea în jur de 30 cadre pe secundă (adică, 30 FPS). Aceasta se numește "rata cadrului" și este explicată mai târziu în acest capitol.

Desenarea pe obiecte Surface va fi acoperită în secțiunile "Funcții de desenare primitive" și "Desenarea imaginilor" mai târziu în acest capitol.

## Culori

Există trei culori primare ale luminii: roșu, verde și albastru. (Roșu, albastru și galben sunt culorile primare pentru vopsele și pigmenți, dar monitorul calculatorului folosește lumină, nu vopsea.) Prin combinarea diferitelor cantități din aceste trei culori poți forma orice altă culoare. În Pygame, reprezentăm culorile cu tuple de trei întregi. Prima valoare din tuple este câtă roșu este în culoare. O valoare întreagă de 0 înseamnă că nu există roșu în această culoare, și o valoare de 255 înseamnă că există cantitatea maximă de roșu în culoare. A doua valoare este pentru verde și a treia valoare este pentru albastru. Aceste tuple de trei întregi folosite pentru a reprezenta o culoare sunt adesea numite valori RGB.

Pentru că poți folosi orice combinație de 0 la 255 pentru fiecare dintre cele trei culori primare, aceasta înseamnă că Pygame poate desena 16.777.216 culori diferite (adică, 256 x 256 x 256 culori). Totuși, dacă încerci să folosești un număr mai mare de 255 sau un număr negativ, vei primi o eroare care arată ca "ValueError: invalid color argument".

De exemplu, vom crea tuple-ul (0, 0, 0) și îl vom stoca într-o variabilă numită BLACK. Fără nicio cantitate de roșu, verde sau albastru, culoarea rezultată este complet neagră. Culoarea neagră este absența oricărei culori. Tuple-ul (255, 255, 255) pentru o cantitate maximă de roșu, verde și albastru pentru a rezulta alb. Culoarea albă este combinația completă de roșu, verde și albastru. Tuple-ul (255, 0, 0) reprezintă cantitatea maximă de roșu dar nicio cantitate de verde și albastru, deci culoarea rezultată este roșie. Similar, (0, 255, 0) este verde și (0, 0, 255) este albastru.

Poți amesteca cantitatea de roșu, verde și albastru pentru a forma alte culori. Iată valorile RGB pentru câteva culori comune:

| Culoare | Valori RGB |
|---------|------------|
| Aqua | (0, 255, 255) |
| Negru | (0, 0, 0) |
| Albastru | (0, 0, 255) |
| Fuchsia | (255, 0, 255) |
| Gri | (128, 128, 128) |
| Verde | (0, 128, 0) |
| Lime | (0, 255, 0) |
| Maro | (128, 0, 0) |
| Albastru închis | (0, 0, 128) |
| Măsliniu | (128, 128, 0) |
| Violet | (128, 0, 128) |
| Roșu | (255, 0, 0) |
| Argintiu | (192, 192, 192) |
| Teal | (0, 128, 128) |
| Alb | (255, 255, 255) |
| Galben | (255, 255, 0) |

### Transparența și valori Alpha

Când te uiți printr-o fereastră de sticlă care are o nuanță roșie adâncă, toate culorile din spatele ei au o nuanță roșie adăugată la ele. Poți imita acest efect adăugând o a patra valoare întreagă de 0 la 255 la valorile tale de culoare.

Această valoare este cunoscută ca valoarea alpha. Este o măsură a cât de opacă (adică, nu transparentă) este o culoare. În mod normal când desenezi un pixel pe un obiect surface, noua culoare înlocuiește complet orice culoare era deja acolo. Dar cu culori care au o valoare alpha, poți în schimb să adaugi doar o nuanță colorată la culoarea care este deja acolo.

De exemplu, acest tuple de trei întregi este pentru culoarea verde: (0, 255, 0). Dar dacă adăugăm un al patrulea întreg pentru valoarea alpha, putem face aceasta o culoare verde semi-transparentă: (0, 255, 0, 128). O valoare alpha de 255 este complet opacă (adică, deloc transparentă). Culorile (0, 255, 0) și (0, 255, 0, 255) arată exact la fel. O valoare alpha de 0 înseamnă că culoarea este complet transparentă. Dacă desenezi orice culoare care are o valoare alpha de 0 pe un obiect surface, nu va avea niciun efect, pentru că această culoare este complet transparentă și invizibilă.

Pentru a desena folosind culori transparente, trebuie să creezi un obiect Surface cu metoda convert_alpha(). De exemplu, următorul cod creează un obiect Surface pe care culorile transparente pot fi desenate:

```python
anotherSurface = DISPLAYSURF.convert_alpha()
```

Odată ce lucrurile au fost desenate pe obiectul Surface stocat în anotherSurface, atunci anotherSurface poate fi "blit-uit" (adică, copiat) la DISPLAYSURF astfel încât să apară pe ecran. (Vezi secțiunea "Desenarea imaginilor cu pygame.image.load() și blit()" mai târziu în acest capitol.)

Este important să observi că nu poți folosi culori transparente pe obiecte Surface care nu sunt returnate dintr-un apel convert_alpha(), incluzând Surface-ul de afișare care a fost returnat de pygame.display.set_mode().

Dacă am crea un tuple de culoare pentru a desena legendarul Unicorn Roz Invizibil, am folosi (255, 192, 192, 0), care ajunge să arate complet invizibil la fel ca orice altă culoare care are un 0 pentru valoarea sa alpha. Este, după toate, invizibil.

### Obiecte pygame.Color

Trebuie să știi cum să reprezinți o culoare pentru că funcțiile de desenare ale Pygame au nevoie de o modalitate să știe cu ce culoare vrei să desenezi. Un tuple de trei sau patru întregi este o modalitate. O altă modalitate este ca un obiect pygame.Color. Poți crea obiecte Color apelând funcția constructor pygame.Color() și pasând fie trei fie patru întregi. Poți stoca acest obiect Color în variabile la fel cum poți stoca tuple-uri în variabile. Încearcă să tastezi următorul în shell-ul interactiv:

```python
>>> import pygame
>>> pygame.Color(255, 0, 0)
(255, 0, 0, 255)
>>> myColor = pygame.Color(255, 0, 0, 128)
>>> myColor == (255, 0, 0, 128)
True
>>>
```

Orice funcție de desenare în Pygame (pe care le vom învăța într-un pic) care are un parametru pentru culoare poate avea fie forma tuple fie forma obiect Color a unei culori pasată pentru ea. Chiar dacă sunt tipuri de date diferite, un obiect Color este egal cu un tuple de patru întregi dacă ambele reprezintă aceeași culoare (la fel cum 42 == 42.0 se va evalua la True).

## Obiecte Rect

Acum că știi cum să reprezinți culori (ca un obiect pygame.Color sau un tuple de trei sau patru întregi pentru roșu, verde, albastru și opțional alpha) și coordonate (ca un tuple de două întregi pentru X și Y), să învățăm despre obiectele pygame.Rect astfel încât să putem începe să folosim funcțiile de desenare ale Pygame.

Pygame are două modalități de a reprezenta zone dreptunghiulare (la fel cum există două modalități de a reprezenta culori). Prima este un tuple de patru întregi:

1. Coordonata X a colțului din stânga sus.
2. Coordonata Y a colțului din stânga sus.
3. Lățimea (în pixeli) a dreptunghiului.
4. Înălțimea (în pixeli) a dreptunghiului.

A doua modalitate este ca un obiect pygame.Rect, pe care îl vom numi obiecte Rect pe scurt. De exemplu, codul de mai jos creează un obiect Rect cu un colț din stânga sus la (10, 20) care este lat de 200 pixeli și înalt de 300 pixeli:

```python
>>> import pygame
>>> spamRect = pygame.Rect(10, 20, 200, 300)
>>> spamRect == (10, 20, 200, 300)
True
```

Lucrul util despre aceasta este că obiectul Rect calculează automat coordonatele pentru alte caracteristici ale dreptunghiului. De exemplu, dacă ai nevoie să știi coordonata X a marginii drepte a obiectului pygame.Rect pe care l-am stocat în variabila spamRect, poți pur și simplu accesa atributul right al obiectului Rect:

```python
>>> spamRect.right
210
```

Codul Pygame pentru obiectul Rect a calculat automat că dacă marginea stângă este la coordonata X 10 și dreptunghiul este lat de 200 pixeli, atunci marginea dreaptă trebuie să fie la coordonata X 210. Dacă reatribui atributul right, toate celelalte atribute sunt recalculate automat:

```python
>>> spamRect.right = 350
>>> spamRect.left
150
```

Iată o listă cu toate atributele pe care le oferă obiectele pygame.Rect (în exemplul nostru, variabila unde obiectul Rect este stocat într-o variabilă numită spamRect):

| Nume atribut | Descriere |
|--------------|-----------|
| myRect.left | Valoarea int a coordonatei X a laturii stângi a dreptunghiului. |
| myRect.right | Valoarea int a coordonatei X a laturii drepte a dreptunghiului. |
| myRect.top | Valoarea int a coordonatei Y a laturii de sus a dreptunghiului. |
| myRect.bottom | Valoarea int a coordonatei Y a laturii de jos. |
| myRect.centerx | Valoarea int a coordonatei X a centrului dreptunghiului. |
| myRect.centery | Valoarea int a coordonatei Y a centrului dreptunghiului. |
| myRect.width | Valoarea int a lățimii dreptunghiului. |
| myRect.height | Valoarea int a înălțimii dreptunghiului. |
| myRect.size | Un tuple de două int-uri: (width, height) |
| myRect.topleft | Un tuple de două int-uri: (left, top) |
| myRect.topright | Un tuple de două int-uri: (right, top) |
| myRect.bottomleft | Un tuple de două int-uri: (left, bottom) |
| myRect.bottomright | Un tuple de două int-uri: (right, bottom) |
| myRect.midleft | Un tuple de două int-uri: (left, centery) |
| myRect.midright | Un tuple de două int-uri: (right, centery) |
| myRect.midtop | Un tuple de două int-uri: (centerx, top) |
| myRect.midbottom | Un tuple de două int-uri: (centerx, bottom) |

## Funcții de desenare primitive

Pygame oferă mai multe funcții diferite pentru desenarea diferitelor forme pe un obiect surface. Aceste forme precum dreptunghiuri, cercuri, elipse, linii sau pixeli individuali sunt adesea numite primitive de desenare. Deschide editorul de fișiere IDLE și tastează următorul program, și salvează-l ca drawing.py.

```python
import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# draw on the surface object
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
```

Când acest program este rulat, următoarea fereastră este afișată până când utilizatorul închide fereastra:

Observă cum facem variabile constante pentru fiecare dintre culori. Făcând aceasta face codul nostru mai lizibil, pentru că a vedea GREEN în codul sursă este mult mai ușor de înțeles ca reprezentând culoarea verde decât (0, 255, 0).

Funcțiile de desenare sunt numite după formele pe care le desenează. Parametrii pe care îi pasezi acestor funcții le spun pe ce obiect Surface să deseneze, unde să deseneze forma (și ce dimensiune), în ce culoare și cât de late să facă liniile. Poți vedea cum sunt apelate aceste funcții în programul drawing.py, dar iată o scurtă descriere a fiecărei funcții:

### Funcții de desenare disponibile

- **fill(color)** – Metoda fill() nu este o funcție ci o metodă a obiectelor pygame.Surface. Va umple complet întregul obiect Surface cu orice valoare de culoare pasezi pentru parametrul color.

- **pygame.draw.polygon(surface, color, pointlist, width)** – Un poligon este o formă făcută doar din laturi plate. Parametrii surface și color spun funcției pe ce surface să deseneze poligonul și ce culoare să îl facă.

  Parametrul pointlist este un tuple sau listă de puncte (adică, tuple sau listă de tuple de două întregi pentru coordonatele XY). Poligonul este desenat prin desenarea liniilor între fiecare punct și punctul care vine după el în tuple. Apoi o linie este desenată de la ultimul punct la primul punct. Poți pasa de asemenea o listă de puncte în loc de un tuple de puncte.

  Parametrul width este opțional. Dacă îl lași afară, poligonul care este desenat va fi umplut, la fel cum poligonul nostru verde de pe ecran este umplut cu culoare. Dacă pasezi o valoare întreagă pentru parametrul width, doar conturul poligonului va fi desenat. Întregul reprezintă câți pixeli lățime va avea conturul poligonului. Pasarea 1 pentru parametrul width va face un poligon subțire, în timp ce pasarea 4 sau 10 sau 20 va face poligoane mai groase. Dacă pasezi întregul 0 pentru parametrul width, poligonul va fi umplut (la fel ca și cum ai fi lăsat parametrul width complet afară).

- **pygame.draw.line(surface, color, start_point, end_point, width)** – Această funcție desenează o linie între parametrii start_point și end_point.

- **pygame.draw.lines(surface, color, closed, pointlist, width)** – Această funcție desenează o serie de linii de la un punct la următorul, mult ca pygame.draw.polygon(). Singura diferență este că dacă pasezi False pentru parametrul closed, nu va fi o linie de la ultimul punct din parametrul pointlist la primul punct. Dacă pasezi True, atunci va desena o linie de la ultimul punct la primul.

- **pygame.draw.circle(surface, color, center_point, radius, width)** – Această funcție desenează un cerc. Centrul cercului este la parametrul center_point. Întregul pasat pentru parametrul radius setează dimensiunea cercului.

- **pygame.draw.ellipse(surface, color, bounding_rectangle, width)** – Această funcție desenează o elipsă (care este ca un cerc strâns sau întins). Această funcție are toți parametrii obișnuiți, dar pentru a spune funcției cât de mare și unde să deseneze elipsa, trebuie să specifici dreptunghiul de delimitare al elipsei.

- **pygame.draw.rect(surface, color, rectangle_tuple, width)** – Această funcție desenează un dreptunghi. Parametrul rectangle_tuple este fie un tuple de patru întregi (pentru coordonatele XY ale colțului din stânga sus și lățimea și înălțimea) sau un obiect pygame.Rect poate fi pasat în schimb.

### Desenarea pixelilor individuali

Din păcate, nu există o singură funcție pe care o poți apela care va seta un singur pixel la o culoare (cu excepția cazului în care apelezi pygame.draw.line() cu același punct de start și sfârșit). Framework-ul Pygame trebuie să ruleze ceva cod în culise înainte și după desenarea pe un obiect Surface. Dacă ar trebui să facă aceasta pentru fiecare pixel pe care vrei să îl setezi, programul tău ar rula mult mai încet.

În schimb, ar trebui să creezi un obiect pygame.PixelArray (le vom numi obiecte PixelArray pe scurt) al unui obiect Surface și apoi să setezi pixeli individuali. Crearea unui obiect PixelArray al unui obiect Surface va "bloca" obiectul Surface. În timp ce un obiect Surface este blocat, funcțiile de desenare pot fi încă apelate pe el, dar nu poate avea imagini precum imagini PNG sau JPG desenate pe el cu metoda blit().

Obiectul PixelArray care este returnat de pygame.PixelArray() poate avea pixeli individuali setați prin accesarea lor cu două indexuri. De exemplu, linia 28's `pixObj[480][380] = BLACK` va seta pixelul la coordonata X 480 și coordonata Y 380 să fie negru.

Pentru a spune Pygame că ai terminat de desenat pixeli individuali, șterge obiectul PixelArray cu o instrucțiune del. Aceasta este ceea ce face linia 33. Ștergerea obiectului PixelArray va "debloca" obiectul Surface astfel încât să poți desena din nou imagini pe el.

După ce ai terminat de apelat funcțiile de desenare pentru a face obiectul Surface de afișare să arate cum vrei, trebuie să apelezi pygame.display.update() pentru a face Surface-ul de afișare să apară efectiv pe monitorul utilizatorului.

## Animație

Acum că știm cum să facem framework-ul Pygame să deseneze pe ecran, să învățăm cum să facem imagini animate. Un joc cu doar imagini fixe, care nu se mișcă ar fi destul de plictisitor. Imaginile animate sunt rezultatul desenării unei imagini pe ecran, apoi o fracțiune de secundă mai târziu desenarea unei imagini puțin diferite pe ecran.

Iată un exemplu de program care demonstrează o animație simplă. Tastează acest cod în editorul de fișiere IDLE și salvează-l ca catanimation.py. Va necesita de asemenea fișierul imagine cat.png să fie în același folder ca fișierul catanimation.py. Poți descărca această imagine de la [http://invpy.com/cat.png](//invpy.com/cat.png).

```python
import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)
    
    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'
    
    DISPLAYSURF.blit(catImg, (catx, caty))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    fpsClock.tick(FPS)
```

### Rata cadrului și pygame.time.Clock

Rata cadrului sau rata de reîmprospătare este numărul de imagini pe care programul le desenează pe secundă și este măsurată în FPS sau cadre pe secundă. O rată scăzută a cadrului în jocurile video poate face jocul să pară tăiat sau săltăreț. Dacă programul are prea mult cod de rulat pentru a desena pe ecran suficient de frecvent, atunci FPS-ul scade.

Un obiect pygame.time.Clock ne poate ajuta să ne asigurăm că programul nostru rulează la un anumit FPS maxim. Acest obiect Clock va asigura că programele noastre de joc nu rulează prea repede prin punerea unor pauze mici la fiecare iterație a buclei de joc.

Obiectul Clock este creat pe linia 7 a programului catanimation.py:

```python
fpsClock = pygame.time.Clock()
```

Metoda tick() a obiectului Clock ar trebui apelată la sfârșitul buclei de joc, după apelul la pygame.display.update(). În programul de animație, este rulată pe linia 47 ca ultima instrucțiune din bucla de joc:

```python
fpsClock.tick(FPS)
```

Tot ce trebuie să știi este că ar trebui să apelezi metoda tick() o dată pe iterație prin bucla de joc la sfârșitul buclei.

## Desenarea imaginilor cu pygame.image.load() și blit()

Funcțiile de desenare sunt bune dacă vrei să desenezi forme simple pe ecran, dar multe jocuri au imagini (numite și sprite-uri). Pygame poate încărca imagini pe obiecte Surface din fișiere de imagine PNG, JPG, GIF și BMP.

Imaginea pisicii a fost stocată într-un fișier numit cat.png. Pentru a încărca imaginea acestui fișier, string-ul 'cat.png' este pasat funcției pygame.image.load(). Apelul funcției pygame.image.load() va returna un obiect Surface care are imaginea desenată pe el. Acest obiect Surface va fi un obiect Surface separat de obiectul Surface de afișare, deci trebuie să "blit-uim" (adică, să copiem) obiectul Surface al imaginii la obiectul Surface de afișare. Blit-uirea este desenarea conținutului unui Surface pe altul. Se face cu metoda blit() a obiectului Surface.

```python
DISPLAYSURF.blit(catImg, (catx, caty))
```

Linia 39 a programului de animație folosește metoda blit() pentru a copia catImg la DISPLAYSURF. Există doi parametri pentru blit(). Primul este obiectul Surface sursă, care este ceea ce va fi copiat pe obiectul Surface DISPLAYSURF. Al doilea parametru este un tuple de două întregi pentru valorile X și Y ale colțului din stânga sus unde imaginea ar trebui să fie blit-uită.

## Fonturile și redarea textului

Dacă vrei să desenezi text pe ecran, ai putea scrie mai multe apeluri la pygame.draw.line() pentru a desena liniile fiecărei litere. Aceasta ar fi o durere de cap să tastezi toate acele apeluri pygame.draw.line() și să îți dai seama de toate coordonatele XY, și probabil nu ar arăta foarte bine.

În schimb, Pygame oferă funcții mult mai simple pentru fonturi și crearea textului. Iată un program mic Hello World folosind funcțiile de font ale Pygame. Tastează-l în editorul de fișiere IDLE și salvează-l ca fonttext.py:

```python
import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

while True: # main game loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
```

Există șase pași pentru a face textul să apară pe ecran:

1. Creează un obiect pygame.font.Font.
2. Creează un obiect Surface cu textul desenat pe el apelând metoda render() a obiectului Font.
3. Creează un obiect Rect din obiectul Surface apelând metoda get_rect() a obiectului Surface.
4. Setează poziția obiectului Rect prin schimbarea unuia din atributele sale.
5. Blit-uiește obiectul Surface cu textul pe obiectul Surface returnat de pygame.display.set_mode().
6. Apelează pygame.display.update() pentru a face Surface-ul de afișare să apară pe ecran.

Anti-aliasing-ul este o tehnică grafică pentru a face textul și formele să arate mai puțin blocate prin adăugarea unui pic de blur la marginile lor. Pentru a face textul Pygame să folosească anti-aliasing, pur și simplu pasează True pentru al doilea parametru al metodei render().

## Redarea sunetelor

Redarea sunetelor care sunt stocate în fișiere de sunet este chiar mai simplă decât afișarea imaginilor din fișiere de imagine. Primul, trebuie să creezi un obiect pygame.mixer.Sound apelând funcția constructor pygame.mixer.Sound(). Ia un parametru string, care este numele fișierului de sunet. Pygame poate încărca fișiere WAV, MP3 sau OGG.

Pentru a reda acest sunet, apelează metoda play() a obiectului Sound. Dacă vrei să oprești imediat obiectul Sound de la redare, apelează metoda stop(). Iată un cod exemplu:

```python
soundObj = pygame.mixer.Sound('beeps.wav')
soundObj.play()
import time
time.sleep(1) # wait and let the sound play for 1 second
soundObj.stop()
```

### Muzica de fundal

Obiectele Sound sunt bune pentru efecte sonore pentru când jucătorul suferă daune, taie cu o sabie sau colectează o monedă. Dar jocurile tale ar putea fi de asemenea mai bune dacă ar avea muzică de fundal care se redă indiferent de ce se întâmpla în joc. Pygame poate încărca doar un fișier muzical pentru a reda în fundal la un moment dat.

Pentru a încărca un fișier muzical de fundal, apelează funcția pygame.mixer.music.load() și pasează-i un argument string al fișierului de sunet de încărcat. Pentru a începe redarea fișierului de sunet încărcat ca muzică de fundal, apelează funcția pygame.mixer.music.play(-1, 0.0).

```python
# Loading and playing a sound effect:
soundObj = pygame.mixer.Sound('beepingsound.wav')
soundObj.play()

# Loading and playing background music:
pygame.mixer.music.load('backgroundmusic.mp3')
pygame.mixer.music.play(-1, 0.0)
# ...some more of your code goes here...
pygame.mixer.music.stop()
```

## Concluzie

Aceasta acoperă bazele creării jocurilor grafice cu framework-ul Pygame. Desigur, doar cititul despre aceste funcții probabil nu este suficient pentru a te ajuta să înveți cum să faci jocuri folosind aceste funcții. Restul capitolelor din această carte se concentrează fiecare pe codul sursă pentru un joc mic și complet. Aceasta îți va da o idee despre cum "arată" programele de joc complete, astfel încât să poți apoi să obții niște idei pentru cum să codezi propriile tale programe de joc.

Spre deosebire de cartea "Invent Your Own Computer Games with Python", această carte presupune că știi bazele programării Python. Dacă ai probleme să îți amintești cum funcționează variabilele, funcțiile, buclele, instrucțiunile if-else și condițiile, probabil poți să îți dai seama doar văzând ce este în cod și cum se comportă programul. Dar dacă ești încă blocat, poți citi cartea "Invent with Python" (este pentru oamenii care sunt complet noi în programare) gratuit online la [http://inventwithpython.com](//inventwithpython.com).