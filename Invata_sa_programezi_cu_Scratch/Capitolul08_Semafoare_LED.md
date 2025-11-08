## Capitolul 8: Semafoare LED

Continuând de la capitolul anterior, vom folosi trei LED-uri și un buton push pentru a face o trecere de pietoni.

### Ai nevoie de:
- Placă breadboard fără lipire
- 3× LED-uri: roșu, galben și verde
- 3× rezistori 330Ω
- Buton push
- Buzzer piezo
- 5× fire jumper male-către-female
- 2× fire jumper male-către-male

### PASUL 01: Conectează LED-urile

Este mai bine să oprești Pi când construiești circuitul. Breadboard-ul conține coloane numerotate, fiecare cuprinzând cinci găuri conectate. Adaugă LED-urile pe el, așa cum se arată în diagramă. Dacă tocmai ai terminat capitolul 7, poți lăsa acele componente, inclusiv LED-ul roșu, pe loc. Ca înainte, piciorul mai scurt (negativ) al fiecărui LED ar trebui să fie conectat printr-un rezistor la rândul '–' (șină de masă comună), care este conectată la un pin GND pe Pi. Piciorul mai lung (pozitiv) al fiecărui LED ar trebui să fie conectat la pinul GPIO respectiv printr-un cablu jumper male-către-female.

**Note despre circuit:**
- Fiecare LED este conectat la un pin GPIO diferit, astfel încât poate fi declanșat în timpul secvenței semaforului
- Un buzzer piezo este conectat la șina de masă și la pinul GPIO 16, pentru bipurile trecerii de pietoni
- Când butonul este apăsat, circuitul este întrerupt și Scratch detectează o valoare zero de la pinul GPIO 21

### PASUL 02: Configurează GPIO în Scratch

Mai întâi, trebuie să activăm serverul GPIO al Scratch. Sub un bloc `when green flag clicked`, adaugă un bloc Control `broadcast`, dă click pe săgeata sa, selectează new/edit și introdu `gpioserveron`. De asemenea, trebuie să configurăm pinii GPIO ai LED-urilor ca ieșiri, așa că adaugă încă trei blocuri `broadcast` și schimbă-le în `config17out`, `config23out` și `config25out` respectiv. În timp ce suntem aici, vom configura pinii pentru buzzer-ul (`config16out`) și butonul (`config21in`) pe care le vom folosi mai târziu – codul tău ar trebui să arate ca Listingul 1.

### PASUL 03: Secvența semaforului

Acum vom testa circuitul nostru creând o secvență de semafor: roșu, roșu/portocaliu, verde, portocaliu. Adaugă codul din Listingul 2. Aici, într-un bloc `forever`, sunt blocuri pentru a aprinde și opri LED-urile în secvența corectă, așteptând câteva secunde între fiecare schimbare. Încearcă să îl rulezi pentru a verifica că toate LED-urile sunt conectate corect și funcționează.

### PASUL 04: Conectează butonul

Pentru trecerea noastră de pietoni, vom avea nevoie de un buton push. Din nou, poți folosi cel deja plasat în capitolul 7, care este așezat peste șanțul central al breadboard-ului și este conectat la șina de masă și la pinul GPIO 21. L-am configurat deja ca ieșire în pasul 2; rulează și oprește acel cod.

### PASUL 05: Oprește luminile

Trebuie să facem ca apăsarea butonului să determine semaforele să rămână pe roșu pentru câteva secunde. Selectează Variables din stânga sus, apoi dă click pe 'Make a variable' și introdu 'pushed' în câmpul de text. Adaugă codul din Listingul 3, păstrându-l separat de rest. Folosind un bloc `if`, acesta setează `pushed` la `True` când valoarea detectată de la pinul GPIO 21 este zero, adică atunci când butonul este apăsat. În continuare, trebuie să adăugăm un bloc `if...else` la codul nostru de secvență a semaforului, pentru a-l opri când `pushed` este `True`. După ce scoți blocurile de secvență a luminilor din blocul `forever` (păstrându-le în zona Scripts), adaugă un bloc `if...else` și pune blocurile de secvență a luminilor înapoi sub `if`. În câmpul `if`, folosește un bloc Operator `=` cu `pushed` în câmpul stâng și 'False' în cel drept. Sub `else`, adaugă un bloc `broadcast and wait` setat la 'beep' – vom folosi aceasta pentru buzzer-ul nostru în pasul următor. Codul tău de secvență a luminilor ar trebui acum să semene cu Listingul 4.

### PASUL 06: Adaugă un buzzer

În final, vom adăuga un buzzer piezo, conectat la șina de masă (piciorul scurt) și la pinul GPIO 16 (piciorul lung), pentru a face un sunet de bipăit când este sigur să traversezi strada. Adaugă codul din Listingul 5 ca un script separat. Acesta rulează ori de câte ori `beep` este difuzat, după ce butonul este apăsat și secvența luminilor se termină. Arată o lumină roșie și folosește o buclă `repeat` pentru a porni și opri buzzer-ul pentru un sunet de bipăit. În final, oprește LED-ul roșu și resetează variabila `pushed` la `False`. Testează-ți trecerea de pietoni apăsând butonul!

