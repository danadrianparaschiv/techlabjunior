# Capitolul 13 – Referință rapidă

> *Ca să îți fie mai ușor la început, iată un ghid la îndemână pentru interfața Scratch, funcționalitatea GPIO și toate blocurile de cod*

## Interfața Scratch

![Interfața Scratch](imagini/cap13_imagine00.png)

- **Paleta de blocuri (Blocks Palette):** conține blocurile pentru programare, pe care le tragi în Zona de scripturi ca să le adaugi în codul tău. Există opt categorii, colorate diferit și selectate din partea de sus, fiecare oferind o altă selecție de blocuri.
- **Zona de scripturi (Scripts Area):** aici se asamblează scripturile. Poate fi accesată de la personaje sau de la Scenă, selectând fila Scripts. Reține că poți crea mai multe scripturi pentru fiecare personaj. Apasă pe filele de deasupra pentru a trece la costume sau la sunete.
- **Scena (Stage):** aici prind viață creațiile tale Scratch. Personajele plasate aici pot fi redimensionate cu pictogramele de mărire și micșorare de deasupra. Apasă pe steagul verde pentru a porni proiectul și pe cercul roșu pentru a-l opri. Există și pictograme pentru schimbarea modului de afișare, inclusiv modul de prezentare pe tot ecranul.
- **Lista de personaje (Sprite List):** conține miniaturile tuturor personajelor tale. Apasă pe unul pentru a-l selecta și a-i modifica scripturile, costumele și sunetele. Pictogramele de deasupra îți permit să desenezi un personaj nou, să imporți unul sau să alegi unul la întâmplare.

## Formele blocurilor

Blocurile au forme diferite, în funcție de felul în care sunt folosite. Există șase tipuri principale…

| Formă | Descriere |
|---|---|
| <img src="imagini/cap13_forma_hat.png" alt="hat block" width="130"> | **Blocurile pălărie (Hat Blocks):** blocurile Control cu care începe fiecare script – când se apasă steagul verde, când se apasă o tastă, când se apasă pe personaj sau când se primește un mesaj. |
| <img src="imagini/cap13_forma_stack.png" alt="stack block" width="130"> | **Blocurile stivă (Stack Blocks):** în formă de piese de puzzle, ca să se îmbine sub și deasupra altora, acestea execută comenzile principale din scripturi. |
| <img src="imagini/cap13_forma_c.png" alt="C block" width="130"> | **Blocurile C (C Blocks):** seamănă, în general, cu litera C; aceste blocuri Control se pot înfășura în jurul altora pentru a crea bucle sau pentru a verifica condiții. |
| <img src="imagini/cap13_forma_boolean.png" alt="boolean block" width="130"> | **Blocurile booleene (Boolean Blocks):** aceste blocuri hexagonale conțin condiții care, atunci când sunt evaluate, raportează valoarea adevărat sau fals. |
| <img src="imagini/cap13_forma_reporter.png" alt="reporter block" width="130"> | **Blocurile raportor (Reporter Blocks):** cu margini rotunjite, acestea conțin valori – numere sau șiruri de text. Includ variabilele și listele. |
| <img src="imagini/cap13_forma_cap.png" alt="cap block" width="130"> | **Blocurile capac (Cap Blocks):** există doar două, la sfârșitul categoriei Control; sunt folosite pentru a opri un script sau toate scripturile. |

## Scratch GPIO

*Scratch pe Raspberry Pi include acum un server GPIO pentru „physical computing”*

În cea mai nouă versiune de Raspbian Jessie, Scratch include un server GPIO Raspberry Pi, care face mai ușoară comandarea LED-urilor, buzzer-elor, plăcilor HAT și a altor dispozitive și componente conectate. Mai întâi trebuie să pornești serverul, din meniul Edit sau rulând un bloc `broadcast gpioserveron`. Apoi poți folosi blocuri `broadcast` pentru a configura și a comanda pinii GPIO individuali și pentru a folosi modulația în lățime de impuls (PWM) pe pinul 18. Alte funcții includ realizarea unei fotografii cu Modulul Cameră și obținerea orei și a adresei IP. Sunt suportate și anumite plăci de extensie și HAT-uri pentru Raspberry Pi, configurate prin crearea unei variabile `AddOn` și setarea ei la numele plăcii respective. Pentru detalii complete despre aceasta și despre alte funcții GPIO, vizitează [magpi.cc/1TYX7Jg](https://magpi.cc/1TYX7Jg).

![Folosirea pinilor GPIO](imagini/cap13_imagine01.png)

*Folosirea pinilor GPIO ai Raspberry Pi din Scratch*

> **NOTA TRADUCĂTORULUI**
> În Scratch 3 pentru Raspberry Pi OS, aceste mesaje `broadcast` sunt înlocuite de extensiile „Raspberry Pi GPIO” și „Raspberry Pi Simple Electronics”, cu blocuri dedicate.

## Ghidul de referință al blocurilor

Un ghid pentru toate blocurile din fiecare dintre cele opt categorii colorate, cu sfaturi pentru folosirea lor…


### Motion (Mișcare)

Blocurile Motion se ocupă de mișcarea personajelor. Ele se referă în principal la poziția x și y și la direcția personajului.

| Bloc | Ce face |
|---|---|
| <img src="imagini/cap13_motion_01.png" alt="move 10 steps" width="177"> | **move 10 steps** – Mută personajul înainte cu numărul de pași specificat, sau înapoi (cu un număr negativ). Util în orice proiect cu mișcare. |
| <img src="imagini/cap13_motion_02.png" alt="turn ↻ 15 degrees" width="223"> | **turn ↻ 15 degrees** – Rotește personajul în sensul acelor de ceasornic cu numărul de grade specificat. |
| <img src="imagini/cap13_motion_03.png" alt="turn ↺ 15 degrees" width="223"> | **turn ↺ 15 degrees** – Rotește personajul în sens invers acelor de ceasornic cu numărul de grade specificat. |
| <img src="imagini/cap13_motion_04.png" alt="point in direction 90" width="244"> | **point in direction 90** – Îndreaptă personajul în direcția specificată: 0 = sus, 90 = dreapta, 180 = jos, -90 = stânga. Se pot folosi și alte numere. |
| <img src="imagini/cap13_motion_05.png" alt="point towards" width="207"> | **point towards** – Îndreaptă personajul spre cursorul mouse-ului sau spre alt personaj. Poate fi folosit pentru a conduce un personaj cu mouse-ul. |
| <img src="imagini/cap13_motion_06.png" alt="go to x: 0 y: 0" width="186"> | **go to x: 0 y: 0** – Mută personajul la poziția x și y specificată pe scenă. Util pentru a-i reseta poziția la începutul unui proiect. |
| <img src="imagini/cap13_motion_07.png" alt="go to" width="126"> | **go to** – Mută personajul la poziția cursorului mouse-ului sau a altui personaj. Util pentru a ține împreună un grup de personaje. |
| <img src="imagini/cap13_motion_08.png" alt="glide 1 secs to x: 0 y: 0" width="247"> | **glide 1 secs to x: 0 y: 0** – Mută lin personajul la o poziție specificată, într-un interval de timp specificat. Un dezavantaj: pune scriptul pe pauză cât timp personajul alunecă. |
| <img src="imagini/cap13_motion_09.png" alt="change x by 10" width="183"> | **change x by 10** – Schimbă poziția x a personajului cu valoarea specificată. Folosit des la comenzile din jocuri. |
| <img src="imagini/cap13_motion_10.png" alt="set x to 10" width="142"> | **set x to 10** – Setează poziția x a personajului la valoarea specificată. Poate fi folosit pentru derulare orizontală. |
| <img src="imagini/cap13_motion_11.png" alt="change y by 10" width="183"> | **change y by 10** – Schimbă poziția y a personajului cu valoarea specificată. Folosit des la comenzile din jocuri. |
| <img src="imagini/cap13_motion_12.png" alt="set y to 10" width="142"> | **set y to 10** – Setează poziția y a personajului la valoarea specificată. Poate fi folosit pentru derulare verticală. |
| <img src="imagini/cap13_motion_13.png" alt="if on edge, bounce" width="200"> | **if on edge, bounce** – Întoarce personajul în direcția opusă când atinge marginea scenei. Util pentru a-l împiedica să iasă parțial din ecran. |
| <img src="imagini/cap13_motion_14.png" alt="x position" width="128"> | **x position** – Raportează poziția x a personajului (între -240 și 240). Bifează căsuța pentru a o afișa pe scenă. |
| <img src="imagini/cap13_motion_15.png" alt="y position" width="129"> | **y position** – Raportează poziția y a personajului (între -180 și 180). Bifează căsuța pentru a o afișa pe scenă. |
| <img src="imagini/cap13_motion_16.png" alt="direction" width="118"> | **direction** – Raportează direcția personajului: 0 = sus, 90 = dreapta, 180 = jos, -90 = stânga. Bifează căsuța pentru a o afișa pe scenă. |

### Looks (Aspect)

Blocurile Looks sunt folosite pentru a controla aspectul personajelor și al scenei. Printre funcții se numără schimbarea costumelor și aplicarea de efecte grafice.

| Bloc | Ce face |
|---|---|
| <img src="imagini/cap13_looks_01.png" alt="switch to costume" width="248"> | **switch to costume** – Schimbă aspectul personajului trecând la un alt costum. Util pentru animație. |
| <img src="imagini/cap13_looks_02.png" alt="next costume" width="152"> | **next costume** – Schimbă costumul personajului cu următorul din listă (dacă a ajuns la sfârșit, revine la primul costum). |
| <img src="imagini/cap13_looks_03.png" alt="costume#" width="134"> | **costume#** – Raportează numărul costumului curent al personajului. Bifează căsuța pentru a-l afișa pe scenă. |
| <img src="imagini/cap13_looks_04.png" alt="say Hello! for 2 secs" width="239"> | **say Hello! for 2 secs** – Afișează balonul de vorbire al personajului pentru durata specificată. |
| <img src="imagini/cap13_looks_05.png" alt="say Hello!" width="126"> | **say Hello!** – Afișează balonul de vorbire al personajului. (Pentru a elimina balonul, rulează acest bloc fără niciun text.) |
| <img src="imagini/cap13_looks_06.png" alt="think Hmm... for 2 secs" width="248"> | **think Hmm... for 2 secs** – Afișează balonul de gândire al personajului pentru durata specificată. |
| <img src="imagini/cap13_looks_07.png" alt="think Hmm..." width="151"> | **think Hmm...** – Afișează balonul de gândire al personajului. (Pentru a elimina balonul, rulează acest bloc fără niciun text.) |
| <img src="imagini/cap13_looks_08.png" alt="change color effect by 25" width="248"> | **change color effect by 25** – Schimbă efectul vizual selectat al personajului cu valoarea specificată. Alege dintre efectele color (culoare), fisheye (ochi de pește), whirl (vârtej), pixelate (pixelare), mosaic (mozaic), brightness (luminozitate) și ghost (fantomă). |
| <img src="imagini/cap13_looks_09.png" alt="set color effect to 0" width="248"> | **set color effect to 0** – Setează efectul vizual selectat la o valoare dată. |
| <img src="imagini/cap13_looks_10.png" alt="clear graphic effects" width="218"> | **clear graphic effects** – Elimină toate efectele grafice ale personajului. |
| <img src="imagini/cap13_looks_11.png" alt="change size by 10" width="209"> | **change size by 10** – Schimbă mărimea personajului cu valoarea specificată. |
| <img src="imagini/cap13_looks_12.png" alt="set size to 100 %" width="201"> | **set size to 100 %** – Setează mărimea personajului la procentul specificat din mărimea originală. |
| <img src="imagini/cap13_looks_13.png" alt="size" width="74"> | **size** – Raportează mărimea personajului ca procent din mărimea originală. Bifează căsuța pentru a o afișa pe scenă. |
| <img src="imagini/cap13_looks_14.png" alt="show" width="78"> | **show** – Face personajul să apară pe scenă (după ce a fost ascuns). |
| <img src="imagini/cap13_looks_15.png" alt="hide" width="77"> | **hide** – Face personajul să dispară de pe scenă. (Reține că, atunci când un personaj este ascuns, celelalte personaje nu îl pot detecta cu un bloc `touching?`.) |
| <img src="imagini/cap13_looks_16.png" alt="go to front" width="130"> | **go to front** – Aduce personajul în fața tuturor celorlalte personaje. Dacă este destul de mare, poate acoperi întreaga scenă. |
| <img src="imagini/cap13_looks_17.png" alt="go back 1 layers" width="197"> | **go back 1 layers** – Trimite personajul înapoi cu numărul de straturi specificat, ca să poată fi ascuns în spatele altor personaje. |

### Sound (Sunet)

Aceste blocuri se ocupă de redarea diverselor sunete, care pot fi înregistrate sau importate. Sunt disponibile și 128 de instrumente MIDI încorporate.

| Bloc | Ce face |
|---|---|
| <img src="imagini/cap13_sound_01.png" alt="play sound meow" width="217"> | **play sound meow** – Începe redarea sunetului ales din meniul derulant și trece imediat la blocul următor, chiar dacă sunetul încă se aude. |
| <img src="imagini/cap13_sound_02.png" alt="play sound meow until done" width="249"> | **play sound meow until done** – Redă un sunet și așteaptă să se termine înainte de a continua cu blocul următor. |
| <img src="imagini/cap13_sound_03.png" alt="stop all sounds" width="170"> | **stop all sounds** – Oprește redarea tuturor sunetelor. |
| <img src="imagini/cap13_sound_04.png" alt="play drum 48 for 0.2 beats" width="248"> | **play drum 48 for 0.2 beats** – Redă sunetul de tobă selectat pentru numărul de bătăi (*beats*) specificat. |
| <img src="imagini/cap13_sound_05.png" alt="rest for 0.2 beats" width="202"> | **rest for 0.2 beats** – Face o pauză (nu redă nimic) pentru numărul de bătăi specificat. |
| <img src="imagini/cap13_sound_06.png" alt="play note 60 for 0.5 beats" width="248"> | **play note 60 for 0.5 beats** – Redă nota muzicală selectată pentru numărul de bătăi specificat. (Săgeata meniului derulant deschide o claviatură de două octave, dar poți introduce direct și numere mai mici sau mai mari.) |
| <img src="imagini/cap13_sound_07.png" alt="set instrument to 1" width="239"> | **set instrument to 1** – Setează instrumentul pe care personajul îl folosește pentru blocurile `play note`. (Fiecare personaj are propriul instrument.) |
| <img src="imagini/cap13_sound_08.png" alt="change volume by -10" width="249"> | **change volume by -10** – Schimbă volumul sunetului personajului cu valoarea specificată. Volumul este între 0 și 100. |
| <img src="imagini/cap13_sound_09.png" alt="volume" width="103"> | **volume** – Raportează volumul sunetului personajului. Bifează căsuța pentru a-l afișa pe scenă. |
| <img src="imagini/cap13_sound_10.png" alt="change tempo by 20" width="230"> | **change tempo by 20** – Schimbă tempoul personajului cu valoarea specificată (în bătăi pe minut). |
| <img src="imagini/cap13_sound_11.png" alt="set tempo to 60 bpm" width="236"> | **set tempo to 60 bpm** – Setează tempoul personajului la valoarea specificată, în bătăi pe minut. |
| <img src="imagini/cap13_sound_12.png" alt="tempo" width="95"> | **tempo** – Raportează tempoul personajului în bătăi pe minut. Bifează căsuța pentru a-l afișa pe scenă. |

### Pen (Creion)

Blocurile Pen permit unui personaj să deseneze linii și forme pe scenă, inclusiv propria imagine „ștampilată”, atunci când se mișcă.

| Bloc | Ce face |
|---|---|
| <img src="imagini/cap13_pen_01.png" alt="clear" width="77"> | **clear** – Șterge toate urmele de creion și ștampilele de pe scenă. |
| <img src="imagini/cap13_pen_02.png" alt="pen down" width="119"> | **pen down** – Coboară creionul personajului, astfel că acesta va desena când se mișcă. |
| <img src="imagini/cap13_pen_03.png" alt="pen up" width="93"> | **pen up** – Ridică creionul personajului, astfel că acesta nu va mai desena când se mișcă. |
| <img src="imagini/cap13_pen_04.png" alt="set pen color to [culoare]" width="205"> | **set pen color to [culoare]** – Setează culoarea creionului, aleasă din selectorul de culori. Alegerea culorii schimbă și nuanța creionului. |
| <img src="imagini/cap13_pen_05.png" alt="change pen color by 10" width="248"> | **change pen color by 10** – Schimbă culoarea creionului cu valoarea specificată. |
| <img src="imagini/cap13_pen_06.png" alt="set pen color to 0" width="208"> | **set pen color to 0** – Setează culoarea creionului la valoarea specificată (între 0 și 200). |
| <img src="imagini/cap13_pen_07.png" alt="change pen shade by 10" width="248"> | **change pen shade by 10** – Schimbă nuanța creionului (de la întunecat la deschis) cu valoarea specificată. |
| <img src="imagini/cap13_pen_08.png" alt="set pen shade to 50" width="226"> | **set pen shade to 50** – Setează nuanța creionului la valoarea specificată, între 0 (foarte întunecat) și 100 (foarte deschis). Valoarea implicită este 50, dacă nu a fost setată din selectorul de culori. |
| <img src="imagini/cap13_pen_09.png" alt="change pen size by 1" width="240"> | **change pen size by 1** – Schimbă grosimea liniei creionului. |
| <img src="imagini/cap13_pen_10.png" alt="set pen size to 1" width="200"> | **set pen size to 1** – Setează grosimea liniei creionului. |
| <img src="imagini/cap13_pen_11.png" alt="stamp" width="86"> | **stamp** – Ștampilează imaginea personajului pe scenă. |

### Control

Blocurile Control oferă funcții pentru repetarea scripturilor și pentru rularea lor doar dacă sunt îndeplinite anumite condiții. Blocul `broadcast` poate fi folosit cu pinii GPIO ai Raspberry Pi.

| Bloc | Ce face |
|---|---|
| <img src="imagini/cap13_control_01.png" alt="when [steag verde] clicked" width="191"> | **when [steag verde] clicked** – Rulează scriptul de dedesubt când se apasă steagul verde pentru a porni proiectul. |
| <img src="imagini/cap13_control_02.png" alt="when space key pressed" width="249"> | **when space key pressed** – Rulează scriptul de dedesubt când este apăsată tasta specificată. Util pentru comenzile jucătorului în jocuri. |
| <img src="imagini/cap13_control_03.png" alt="when Sprite1 clicked" width="221"> | **when Sprite1 clicked** – Rulează scriptul de dedesubt când se apasă pe personaj. Util pentru butoane și opțiuni de meniu. |
| <img src="imagini/cap13_control_04.png" alt="wait 1 secs" width="147"> | **wait 1 secs** – Așteaptă numărul de secunde specificat, apoi continuă cu blocul următor. Folosește-l oriunde ai nevoie de o pauză. Nu este la fel de precis ca folosirea cronometrului (`timer`). |
| <img src="imagini/cap13_control_05.png" alt="forever" width="155"> | **forever** – Unul dintre cele mai folosite blocuri: rulează blocurile din interiorul lui iar și iar, într-o buclă fără sfârșit. |
| <img src="imagini/cap13_control_06.png" alt="repeat 10" width="155"> | **repeat 10** – Rulează blocurile din interior de numărul de ori specificat. Folosit des pentru animația și mișcarea personajelor. |
| <img src="imagini/cap13_control_07.png" alt="broadcast" width="168"> | **broadcast** – Trimite un mesaj tuturor personajelor, apoi continuă cu blocul următor fără să aștepte scripturile declanșate. Poate fi folosit și pentru a configura și comanda pinii GPIO ai Raspberry Pi și pentru a face o fotografie cu Modulul Cameră al Raspberry Pi. |
| <img src="imagini/cap13_control_08.png" alt="broadcast and wait" width="248"> | **broadcast and wait** – Trimite un mesaj tuturor personajelor, declanșându-le să facă ceva, și așteaptă ca toate să termine înainte de a continua cu blocul următor. |
| <img src="imagini/cap13_control_09.png" alt="when I receive" width="212"> | **when I receive** – Rulează scriptul de dedesubt când primește mesajul specificat. |
| <img src="imagini/cap13_control_10.png" alt="forever if" width="176"> | **forever if** – Echivalentul unui bloc `if` în interiorul unui bloc `forever`. Verifică încontinuu dacă condiția este adevărată; de fiecare dată când este, rulează blocurile din interior. |
| <img src="imagini/cap13_control_11.png" alt="if" width="155"> | **if** – Unul dintre cele mai folosite blocuri. Dacă condiția lui este adevărată, rulează blocurile din interior. |
| <img src="imagini/cap13_control_12.png" alt="if … else" width="155"> | **if … else** – Dacă condiția este adevărată, rulează blocurile din partea `if`; dacă nu, rulează blocurile din partea `else`. |
| <img src="imagini/cap13_control_13.png" alt="wait until" width="177"> | **wait until** – Așteaptă până când condiția devine adevărată, apoi rulează blocurile de dedesubt. Util pentru a aștepta ca un personaj să ajungă undeva, ca o valoare să depășească un anumit prag sau ca un alt script să răspundă. |
| <img src="imagini/cap13_control_14.png" alt="repeat until" width="197"> | **repeat until** – Verifică dacă condiția este falsă; dacă da, rulează blocurile din interior și verifică din nou. Când condiția devine adevărată, trece la blocurile care urmează. |
| <img src="imagini/cap13_control_15.png" alt="stop script" width="128"> | **stop script** – Oprește scriptul. Util pentru a dezactiva scripturi, care pot fi repornite cu un mesaj `broadcast` sau cu o apăsare de tastă. |
| <img src="imagini/cap13_control_16.png" alt="stop all" width="142"> | **stop all** – Oprește toate scripturile din toate personajele. Poate fi folosit pentru a încheia sau a pune pe pauză un proiect. |

### Sensing (Detectare)

Blocurile Sensing pot fi folosite pentru a detecta când un personaj atinge alt personaj. Blocul `sensor value` poate fi folosit pentru a citi intrarea unui pin GPIO al Raspberry Pi.

| Bloc | Ce face |
|---|---|
| <img src="imagini/cap13_sensing_01.png" alt="touching ?" width="191"> | **touching ?** – Raportează adevărat dacă personajul atinge personajul, marginea sau cursorul mouse-ului specificat. Util pentru detectarea coliziunilor în jocuri. |
| <img src="imagini/cap13_sensing_02.png" alt="touching color ?" width="224"> | **touching color ?** – Raportează adevărat dacă personajul atinge culoarea specificată (aleasă cu pipeta). Din nou, util pentru detectarea coliziunilor. |
| <img src="imagini/cap13_sensing_03.png" alt="color is touching ?" width="248"> | **color is touching ?** – Raportează adevărat dacă prima culoare (din personaj) atinge a doua culoare (din fundal sau din alt personaj). Ambele culori se aleg cu pipeta. |
| <img src="imagini/cap13_sensing_04.png" alt="ask and wait" width="182"> | **ask and wait** – Pune o întrebare pe ecran și păstrează textul introdus de la tastatură în `answer`. Programul așteaptă până se apasă tasta ENTER sau bifa. |
| <img src="imagini/cap13_sensing_05.png" alt="answer" width="102"> | **answer** – Raportează textul introdus de la tastatură la cea mai recentă folosire a blocului `ask and wait` (comun tuturor personajelor). |
| <img src="imagini/cap13_sensing_06.png" alt="mouse x" width="114"> | **mouse x** – Raportează poziția x a cursorului mouse-ului. |
| <img src="imagini/cap13_sensing_07.png" alt="mouse y" width="114"> | **mouse y** – Raportează poziția y a cursorului mouse-ului. |
| <img src="imagini/cap13_sensing_08.png" alt="mouse down?" width="172"> | **mouse down?** – Raportează adevărat dacă butonul mouse-ului este apăsat. |
| <img src="imagini/cap13_sensing_09.png" alt="key space pressed?" width="251"> | **key space pressed?** – Raportează adevărat dacă tasta specificată este apăsată. Util pentru controlul obiectelor în mișcare, de exemplu în jocuri. |
| <img src="imagini/cap13_sensing_10.png" alt="distance to" width="181"> | **distance to** – Raportează distanța până la personajul specificat sau până la cursorul mouse-ului. Util în proiectele care au nevoie de detectare și mișcare precise. |
| <img src="imagini/cap13_sensing_11.png" alt="reset timer" width="130"> | **reset timer** – Setează cronometrul la zero. Util când începe un proiect sau un nivel nou al unui joc. |
| <img src="imagini/cap13_sensing_12.png" alt="timer" width="84"> | **timer** – Raportează valoarea cronometrului, în secunde. (Cronometrul rulează tot timpul.) |
| <img src="imagini/cap13_sensing_13.png" alt="x position of Sprite1" width="251"> | **x position of Sprite1** – Raportează o proprietate sau o variabilă a altui personaj. Alege dintre: x position, y position, direction, costume #, size și volume. Ajută la legătura dintre personajele unui proiect. |
| <img src="imagini/cap13_sensing_14.png" alt="loudness" width="120"> | **loudness** – Raportează volumul (de la 1 la 100) al sunetelor detectate de microfonul calculatorului. Mai precis decât `loud?`, poate fi folosit pentru a face personajele să reacționeze la un anumit nivel al vocii. |
| <img src="imagini/cap13_sensing_15.png" alt="loud?" width="97"> | **loud?** – Raportează adevărat dacă microfonul calculatorului detectează un volum mai mare de 30 (pe o scară de la 1 la 100). |
| <img src="imagini/cap13_sensing_16.png" alt="slider sensor value" width="230"> | **slider sensor value** – Raportează valoarea senzorului specificat, cum ar fi unul dintre pinii GPIO ai Raspberry Pi (sau printr-o placă PicoBoard ori LEGO WeDo conectată). |
| <img src="imagini/cap13_sensing_17.png" alt="sensor button pressed ?" width="248"> | **sensor button pressed ?** – Raportează adevărat dacă senzorul specificat este apăsat. Se folosește doar cu o placă PicoBoard conectată. |

### Operators (Operatori)

Acestea oferă diverse operații matematice și logice (booleene), împreună cu funcții pentru lucrul cu șiruri de text.

| Bloc | Ce face |
|---|---|
| <img src="imagini/cap13_operators_01.png" alt="+" width="100"> | **+** – Adună două numere. |
| <img src="imagini/cap13_operators_02.png" alt="-" width="97"> | **-** – Scade al doilea număr din primul. |
| <img src="imagini/cap13_operators_03.png" alt="*" width="95"> | ***** – Înmulțește două numere. |
| <img src="imagini/cap13_operators_04.png" alt="/" width="97"> | **/** – Împarte primul număr la al doilea. |
| <img src="imagini/cap13_operators_05.png" alt="pick random 1 to 10" width="245"> | **pick random 1 to 10** – Alege un număr întreg aleatoriu din intervalul specificat. |
| <img src="imagini/cap13_operators_06.png" alt="<" width="118"> | **<** – Raportează adevărat dacă prima valoare este mai mică decât a doua. |
| <img src="imagini/cap13_operators_07.png" alt="=" width="118"> | **=** – Raportează adevărat dacă cele două valori sunt egale. |
| <img src="imagini/cap13_operators_08.png" alt=">" width="118"> | **>** – Raportează adevărat dacă prima valoare este mai mare decât a doua. |
| <img src="imagini/cap13_operators_09.png" alt="and" width="179"> | **and** – Raportează adevărat dacă ambele condiții sunt adevărate. |
| <img src="imagini/cap13_operators_10.png" alt="or" width="165"> | **or** – Raportează adevărat dacă oricare dintre condiții este adevărată. |
| <img src="imagini/cap13_operators_11.png" alt="not" width="126"> | **not** – Raportează adevărat dacă condiția este falsă și fals dacă condiția este adevărată. |
| <img src="imagini/cap13_operators_12.png" alt="join hello world" width="188"> | **join hello world** – Concatenează (unește) cele două șiruri de text. |
| <img src="imagini/cap13_operators_13.png" alt="letter 1 of world" width="200"> | **letter 1 of world** – Raportează litera de la poziția specificată dintr-un șir de text. |
| <img src="imagini/cap13_operators_14.png" alt="length of world" width="176"> | **length of world** – Raportează numărul de litere dintr-un șir de text. |
| <img src="imagini/cap13_operators_15.png" alt="mod" width="126"> | **mod** – Raportează restul împărțirii primului număr la al doilea. |
| <img src="imagini/cap13_operators_16.png" alt="round" width="116"> | **round** – Raportează cel mai apropiat număr întreg de un număr. |
| <img src="imagini/cap13_operators_17.png" alt="sqrt of 10" width="156"> | **sqrt of 10** – Raportează rezultatul funcției selectate (abs, sqrt, sin, cos, tan, asin, acos, atan, ln, log, e^ sau 10^) aplicate numărului specificat. |

### Variables (Variabile)

Aceste blocuri apar în paletă doar după ce este creată o variabilă nouă (o valoare care se poate schimba) sau o listă (care conține mai multe elemente).

| Bloc | Ce face |
|---|---|
| <img src="imagini/cap13_variables_01.png" alt="variable" width="109"> | **variable** – Raportează valoarea variabilei. Fiecare variabilă creată are un astfel de bloc. Bifează căsuța pentru a o afișa pe scenă. Crearea unei variabile numite „AddOn” permite folosirea plăcilor de extensie Raspberry Pi (vezi [magpi.cc/1TYX7Jg](https://magpi.cc/1TYX7Jg)). |
| <img src="imagini/cap13_variables_02.png" alt="set variable to 0" width="221"> | **set variable to 0** – Setează variabila la valoarea specificată. Util pentru a o reseta la începutul unui proiect. Poate fi folosit și pentru a seta variabila AddOn, pentru plăci de extensie precum Explorer HAT, Pibrella, PiFace, PiGlow și Sense HAT. |
| <img src="imagini/cap13_variables_03.png" alt="change variable by 1" width="248"> | **change variable by 1** – Schimbă variabila selectată cu valoarea specificată. Folosit, de exemplu, pentru a modifica viteza unui obiect, numărul nivelului sau scorul jocului. |
| <img src="imagini/cap13_variables_04.png" alt="show variable" width="248"> | **show variable** – Afișează pe scenă monitorul variabilei selectate. |
| <img src="imagini/cap13_variables_05.png" alt="hide variable" width="247"> | **hide variable** – Ascunde monitorul variabilei selectate, ca să nu fie vizibil pe scenă. |
| <img src="imagini/cap13_variables_06.png" alt="mylist" width="93"> | **mylist** – Raportează toate elementele listei. (Elementele sunt separate prin spații. Totuși, dacă elementele sunt litere sau cifre individuale, spațiile sunt omise.) |
| <img src="imagini/cap13_variables_07.png" alt="add thing to mylist" width="233"> | **add thing to mylist** – Adaugă elementul specificat la sfârșitul listei. Elementul poate fi un număr sau un șir de litere și alte caractere. |
| <img src="imagini/cap13_variables_08.png" alt="delete 1 of mylist" width="247"> | **delete 1 of mylist** – Șterge unul sau toate elementele listei. Alegând „last” se șterge ultimul element, iar „all” șterge tot. Ștergerea scade lungimea listei. |
| <img src="imagini/cap13_variables_09.png" alt="insert thing at 1 of mylist" width="248"> | **insert thing at 1 of mylist** – Inserează un element la poziția specificată din listă. Alegând „any” se inserează într-un loc aleatoriu, iar „last” adaugă elementul la sfârșit. Lungimea listei crește cu 1. |
| <img src="imagini/cap13_variables_10.png" alt="replace item 1 of mylist with thing" width="249"> | **replace item 1 of mylist with thing** – Înlocuiește un element din listă cu valoarea specificată. Alegând „any” se înlocuiește un element aleatoriu. Lungimea listei nu se schimbă. |
| <img src="imagini/cap13_variables_11.png" alt="item 1 of mylist" width="233"> | **item 1 of mylist** – Raportează elementul de la poziția specificată din listă. Alegând „any” se raportează un element aleatoriu. |
| <img src="imagini/cap13_variables_12.png" alt="length of mylist" width="202"> | **length of mylist** – Raportează câte elemente are lista. |
| <img src="imagini/cap13_variables_13.png" alt="mylist contains thing" width="248"> | **mylist contains thing** – Raportează adevărat dacă lista conține elementul specificat. Reține că elementul trebuie să se potrivească exact. |
