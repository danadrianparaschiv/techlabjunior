## Capitolul 7: Aprinde un LED

Scratch poate fi folosit cu pinii GPIO ai Pi pentru proiecte de computing fizic. Aici, vom conecta un LED activat prin buton.

### Ai nevoie de:
- Placă breadboard fără lipire (solderless)
- LED
- Rezistor 330Ω
- Buton push
- 3× fire jumper male-către-female
- Fir jumper male-către-male

### PASUL 01: Conectează LED-ul

Este mai bine să oprești Pi când construiești circuitul tău. Breadboard-ul conține coloane numerotate, fiecare cuprinzând cinci găuri conectate. Plasează picioarele LED-ului tău în coloane numerotate adiacente, așa cum se arată în diagramă. Observă că piciorul mai scurt al LED-ului este capătul negativ; în coloana sa de pe breadboard, introdu un capăt al rezistorului, apoi plasează celălalt capăt în rândul exterior marcat '–' (șina de masă - ground rail). Folosește un fir jumper male-către-female pentru a conecta o altă gaură din acea șină de masă la un pin GND pe Pi. În final, folosește un fir jumper pentru a conecta o gaură din coloana piciorului mai lung (pozitiv) al LED-ului la pinul GPIO 17.

**Note importante despre circuit:**
- Piciorul mai lung al LED-ului este conectat la GPIO 17, în timp ce celălalt este conectat printr-un rezistor la șina de masă
- Prin conectarea rândului '–', sau șina de masă, la un pin GND, mai multe componente pot partaja conexiunea
- Când butonul este apăsat, circuitul este întrerupt și Scratch detectează o valoare zero de la pinul GPIO 21

### PASUL 02: Configurează GPIO în Scratch

Înainte de a putea folosi pinii GPIO din Scratch, trebuie să activăm serverul GPIO. Deși acest lucru poate fi făcut din meniul Edit, în schimb vom face ca codul nostru să îl activeze. Sub un bloc `when green flag clicked`, adaugă un bloc Control `broadcast`, dă click pe săgeata sa, selectează new/edit și introdu `gpioserveron`. De asemenea, trebuie să configurăm pinul GPIO 17 ca pin de ieșire (output) (pentru a declanșa LED-ul), așa că adaugă un alt bloc `broadcast` și schimbă-l în `config17out`.

### PASUL 03: Aprinde LED-ul

Acum vom testa circuitul nostru folosind o buclă pentru a face LED-ul să clipească. Adaugă un bloc `forever` la sfârșitul codului tău. În interior, adaugă următoarele blocuri: `broadcast gpio17on`, `wait 1 secs`, `broadcast gpio17off` și `wait 1 secs`. Acum încearcă să rulezi codul (Listingul 1) și LED-ul tău ar trebui să clipească continuu pornit și oprit.

### PASUL 04: Conectează butonul

Putem controla LED-ul nostru adăugând un buton push. Din nou, te sfătuim să oprești Pi în timp ce conectezi componente noi. Adaugă butonul push pe breadboard, cu pinii săi peste șanțul central (așa cum se arată în diagramă). Conectează un fir jumper male-către-female de la coloana unui pin la pinul GPIO 21 pe Pi. Conectează un jumper male-către-male de la celălalt pin (de aceeași parte a șanțului) la șina de masă pe care o folosești pentru circuitul LED (pentru a partaja conexiunea sa la pinul GND).

### PASUL 05: Configurează butonul

Înainte ca Scratch să poată reacționa la noul tău buton, trebuie să i se spună care pin este inputul său. Șterge bucla `forever` din codul LED-ului tău clipitor, trăgând-o afară din zonă. Adaugă un alt bloc `broadcast` cu `config21in` pentru a configura pinul GPIO 21 ca input – vezi Listingul 2. Rulează și oprește codul. Acum, dă click pe categoria Sensing din panoul stânga sus. Găsește blocul `sensor value` și schimbă-l în `gpio21`. Dă click pe căsuța lui de bifare pentru a afișa valoarea sa pe scenă: ori de câte ori butonul este apăsat, ar trebui să se schimbe de la 1 la 0.

### PASUL 06: Leagă de LED

Cu butonul funcțional, este timpul să îl facem să declanșeze LED-ul. Adaugă codul din Listingul 3 la sfârșitul codului tău. Din nou, folosim un bloc `forever` pentru o buclă continuă. În interior adăugăm un bloc `if...else`. În câmpul `if`, plasăm un bloc Operator `=`; în câmpul său stâng, adăugăm `gpio21 sensor value`, cu 1 în câmpul drept. Dedesubt, inserăm `broadcast gpio17off`. În acest fel, când butonul nu este apăsat, LED-ul va fi oprit. Sub `else`, inserăm `broadcast gpio17on`, pentru a aprinde LED-ul când butonul este apăsat. Rulează codul (ca în Listingul 4), apasă butonul și urmărește-ți LED-ul! În capitolul următor, vom adăuga mai multe LED-uri la circuit pentru a face o trecere de pietoni.
