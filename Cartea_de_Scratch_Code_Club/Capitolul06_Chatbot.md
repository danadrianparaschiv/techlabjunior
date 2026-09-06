# Capitolul 6 – Chatbot

> *Creează-ți propriul personaj vorbitor, care pune întrebări și răspunde la răspunsurile pe care i le dai*

> 🤖 *Programează-ți propriul chatbot! E ca și cum ai vorbi cu o persoană adevărată!*

Vei învăța cum să adaugi „selecție” în codul tău, folosind blocurile `if` (dacă) și `if…else` (dacă… altfel), ca să schimbi felul în care răspunde personajul tău, în funcție de răspunsurile primite.

> **CE VEI ÎNVĂȚA**
> - Selecția (blocurile `if` și `if…else`)
> - Introducerea de la tastatură, cu blocul `ask` (întreabă)
> - Folosirea blocului `join` (unește) ca să lipești bucăți de text

> **SFAT: FIȘIERELE PROIECTELOR**
> Ca să descarci o arhivă zip cu toate fișierele proiectelor Scratch 2 (.sb2) din această carte, intră pe: [rpf.io/book-s1-assets](https://rpf.io/book-s1-assets)

## Proiectul terminat

![Proiectul terminat: chatbotul pune întrebări](imagini/cap06_imagine00.jpg)

- Personajul îi pune utilizatorului întrebări
- Apare o casetă în care utilizatorul își scrie răspunsul
- Chatbotul tău poate fi orice personaj vrei, dar ar trebui să aibă patru costume

## Pasul 1: Chatbotul tău

*Alege personalitatea și înfățișarea personajului tău.*

- [ ] Înainte să începi să îți faci chatbotul, trebuie să îi hotărăști personalitatea. Gândește-te:
  - Cum îl cheamă?
  - Unde locuiește?
  - E vesel? serios? amuzant? timid? prietenos?
  - Ce îi place și ce nu îi place?
- [ ] Deschide un browser și intră pe [rpf.io/book-chatbot](https://rpf.io/book-chatbot) ca să deschizi proiectul „Chatbot”. Apasă pe butonul **Remix**.
- [ ] În lista de personaje sunt două personaje: **Chatter** și **Natter**. Dacă preferi să folosești personajul Natter, poți apăsa clic dreapta pe el și alege **show** (arată). Poți apăsa clic dreapta și ca să ascunzi personajul Chatter.

![Lista de personaje, cu meniul show pentru Natter](imagini/cap06_imagine02.jpg)

> **SFAT: ALEGE-ȚI PROPRIUL PERSONAJ**
> Dacă preferi, poți alege un alt personaj din biblioteca Scratch (sau chiar să îl desenezi tu). Pentru acest proiect, personajul folosit ar trebui să aibă patru costume, cum au personajele de mai jos.

![Personaje cu patru costume: Tera, Giga, Pico, Nano](imagini/cap06_imagine01.jpg)

- [ ] Alege un fundal al scenei care să se potrivească cu personalitatea chatbotului. Există deja două din care poți alege, sau poți selecta un alt fundal din biblioteca Scratch. Noi rămânem la fundalul **Outside** (afară).

![Fundalurile Outside și Library](imagini/cap06_imagine03.png)

## Pasul 2: Un chatbot vorbitor

*Acum că ai un chatbot cu personalitate, hai să îl programăm să vorbească cu tine.*

- [ ] Apasă pe personajul tău chatbot și adaugă acest cod:

![Scriptul: when this sprite clicked, ask Hey! What's your name? and wait, say What a lovely name! for 2 secs](imagini/cap06_imagine04.png)

*Blocul `ask` așteaptă ca utilizatorul să scrie un răspuns*

- [ ] Apasă pe chatbot ca să îl testezi. Când ești întrebat cum te cheamă, scrie-ți numele în caseta din partea de jos a scenei.

![Chatbotul întreabă „Hey! What's your name?”](imagini/cap06_imagine05.jpg)

- [ ] Chatbotul tău răspunde pur și simplu „What a lovely name!” (Ce nume frumos!) de fiecare dată. Poți personaliza răspunsul chatbotului folosind răspunsul utilizatorului. Schimbă codul chatbotului, ca să arate așa:

![Scriptul cu say join Hi answer for 2 secs](imagini/cap06_imagine08.png)

> **SFAT: COMBINAREA BLOCURILOR**
> Ca să creezi ultimul bloc din script, va trebui mai întâi să tragi un bloc verde `join` și să îl lași în blocul `say`. Apoi poți schimba textul „hello” în „Hi” și poți trage blocul albastru deschis `answer` (răspuns), din categoria **Sensing** (senzori), peste textul „world”.
>
> Dacă vrei să adaugi text după răspuns, poți folosi încă un bloc `join` în al doilea câmp al primului.

![Blocul say cu join hello world](imagini/cap06_imagine06.jpg)

![Blocul answer tras peste textul world](imagini/cap06_imagine07.jpg)

![Un al doilea join, pentru text după răspuns](imagini/cap06_imagine09.jpg)

> **DEPANARE: FUNCȚIONEAZĂ?**
> Testează acest program nou. Funcționează cum te aștepți? Poți repara problemele pe care le observi?
>
> <details><summary><b>INDICIU</b> (apasă ca să îl vezi)</summary>
>
> Poți încerca să adaugi un spațiu pe undeva!
> </details>

- [ ] Dacă păstrezi răspunsul într-o variabilă, îl vei putea folosi în tot proiectul. Creează o variabilă nouă, numită **name** (nume).

![Variabila name și blocurile ei](imagini/cap06_imagine10.jpg)

- [ ] Ar trebui să vezi noua variabilă și în stânga sus a scenei.

![Afișajul variabilei name pe scenă](imagini/cap06_imagine12.jpg)

- [ ] După ce ai creat noua variabilă, modifică codul chatbotului, ca să arate așa:

![Scriptul cu set name to answer și say join Hi name](imagini/cap06_imagine14.png)

- [ ] Dacă îți testezi din nou programul, vei observa că răspunsul este păstrat în variabila `name` și este arătat în stânga sus a scenei. (Ca să îl ascunzi, debifează pur și simplu căsuța de lângă `name` din paleta de blocuri.)

> **PROVOCARE: MAI MULTE ÎNTREBĂRI**
> Poți programa chatbotul să pună încă o întrebare? Poți păstra răspunsul într-o variabilă?
>
> <details><summary><b>INDICIU</b> (apasă ca să îl vezi)</summary>
>
> Va trebui să folosești încă un bloc `ask` ca să pui altă întrebare, și încă o variabilă ca să păstrezi răspunsul.
> </details>

![Chatbotul întreabă „Where do you live?”](imagini/cap06_imagine11.jpg)

![Chatbotul spune „I've never been to Stockport”](imagini/cap06_imagine13.jpg)

## Pasul 3: Luarea deciziilor

*Poți programa chatbotul să decidă ce să facă, în funcție de răspunsurile utilizatorului.*

- [ ] Hai să facem chatbotul să pună utilizatorului o întrebare cu răspuns da sau nu. Iată un exemplu, dar poți schimba întrebarea, dacă vrei:

![Scriptul cu ask join Are you OK name, if answer = yes then say That's great to hear! else say Oh no!](imagini/cap06_imagine15.png)

Observă că, acum că ai păstrat numele utilizatorului într-o variabilă, îl poți folosi de câte ori vrei.

> **SFAT: BLOCURILE IF ȘI IF…ELSE**
> Până acum, scripturile pe care le-ai scris au făcut exact același lucru de fiecare dată când au rulat. Blocurile `if` și `if…else` le permit scripturilor tale să decidă ce să facă în continuare.
>
> Un bloc `if` include o condiție, iar codul din interiorul blocului `if` rulează doar dacă acea condiție este adevărată. Dacă este falsă (nu e adevărată), codul din interiorul blocului `if` este sărit.

![Exemplu: if place = Birmingham then say I live in Birmingham too!](imagini/cap06_imagine16.png)

> Un bloc `if…else` va rula întotdeauna fie primul, fie al doilea set de blocuri. Dacă condiția este adevărată, rulează primul set de blocuri. Dacă este falsă, rulează în schimb al doilea set.

![Exemplu: if score > 10 then say Well done! else say Try again](imagini/cap06_imagine17.png)

- [ ] Dacă îți testezi codul, vei vedea că acum primești un răspuns când răspunzi cu yes (da) sau no (nu). Chatbotul ar trebui să răspundă „That's great to hear!” (Mă bucur să aud asta!) când răspunzi yes (nu contează dacă scrii cu litere mari sau mici), dar va răspunde „Oh no!” (Vai, nu!) dacă scrii orice altceva.

![Chatbotul spune „That's great to hear!”](imagini/cap06_imagine18.jpg)

![Chatbotul spune „Oh no!”](imagini/cap06_imagine19.jpg)

- [ ] Poți pune orice cod în interiorul unui bloc `if` sau `else`, nu doar cod care să facă chatbotul să vorbească. De exemplu, poți schimba costumul chatbotului, ca să se potrivească cu răspunsul. Dacă te uiți la costumele chatbotului, ar trebui să vezi că sunt patru. (Dacă nu, poți oricând să adaugi tu altele!)

![Cele patru costume ale chatbotului](imagini/cap06_imagine20.png)

- [ ] Poți folosi aceste costume ca parte a răspunsului chatbotului, adăugând acest cod:

![Scriptul complet cu switch costume to Chatter-b, Chatter-c și Chatter-d](imagini/cap06_imagine22.png)

> **TESTEAZĂ-ȚI PROIECTUL**
> Testează-ți programul și ar trebui să vezi cum fața chatbotului se schimbă în funcție de răspunsul pe care i-l dai.

![Chatbotul zâmbește la „That's great to hear!”](imagini/cap06_imagine23.jpg)

![Chatbotul e trist la „Oh no!”](imagini/cap06_imagine24.jpg)

> **PROVOCARE: MAI MULTE DECIZII**
> Programează chatbotul să pună încă o întrebare, ceva cu răspuns da sau nu. Poți face chatbotul să reacționeze la răspuns?
>
> <details><summary><b>INDICIU</b> (apasă ca să îl vezi)</summary>
>
> Va trebui să adaugi încă un bloc `ask`, cu încă un bloc `if…else` care să reacționeze la răspuns.
> </details>

![Chatbotul întreabă „Would you like to hear a joke?”](imagini/cap06_imagine21.jpg)

## Pasul 4: Schimbarea locului

*Poți programa chatbotul și să își schimbe locul.*

- [ ] Apasă pe scenă și apoi pe fila **Backdrops** (fundaluri). Ar trebui să vezi că scena are două fundaluri. Adaugă încă un fundal scenei, dacă vezi doar unul.

![Fila Backdrops, cu fundalurile Outside și Library](imagini/cap06_imagine25.png)

- [ ] Acum poți programa chatbotul să își schimbe locul, adăugându-i acest cod:

![Scriptul: ask I'm going to the library. Do you want to come with me?, if answer = yes then switch backdrop to Library](imagini/cap06_imagine26.png)

- [ ] Trebuie să te asiguri și că chatbotul este în locul lui original când începi să vorbești cu el. Adaugă acest bloc la începutul codului chatbotului:

![Începutul scriptului, cu switch backdrop to Outside](imagini/cap06_imagine27.png)

- [ ] Testează-ți programul și răspunde yes când ești întrebat dacă vrei să mergi la bibliotecă. Ar trebui să vezi că locul chatbotului s-a schimbat.

![Chatbotul în bibliotecă](imagini/cap06_imagine28.jpg)

> ✏️ Își schimbă chatbotul locul dacă scrii **no**? Dar dacă scrii **I'm not sure** (nu sunt sigur)?

- [ ] Poți adăuga și acest cod în interiorul blocului `if`, ca să faci chatbotul să sară în sus și în jos de patru ori, dacă răspunsul este yes:

![Scriptul cu repeat 4, change y by 10, wait 0.1 secs, change y by -10, wait 0.1 secs](imagini/cap06_imagine29.png)

- [ ] Testează-ți din nou codul. Sare chatbotul în sus și în jos dacă răspunzi yes?

> **PROVOCARE: FĂ-ȚI PROPRIUL CHATBOT**
> Programează chatbotul să pună încă o întrebare, ceva cu răspuns da sau nu. Poți face chatbotul să reacționeze la răspuns?
>
> După ce ai terminat de făcut chatbotul, pune-ți prietenii să poarte o conversație cu el! Le place personajul tău? Au observat vreo problemă?
>
> Desenează propriul tău personaj și fă-i o poză, ca să îl folosești în proiectul tău Scratch!

![Chatbotul întreabă „Should I put on my hat?”](imagini/cap06_imagine30.jpg)

![Chatbotul întreabă „Should I dance?”](imagini/cap06_imagine31.jpg)

## Chatbot: codul complet

### Chatter

Robotul Chatter pune întrebări și reacționează la răspunsuri.

![Scriptul complet al chatbotului](imagini/cap06_imagine32.png)

- Personajul rostește textul dat și așteaptă un răspuns
- Păstrând primul răspuns într-o variabilă, îl putem refolosi în vorbirea și întrebările următoare
- Trecerea la costume cu expresii diferite ale feței dă mai mult efect
- Putem chiar să schimbăm fundalul, ca să mutăm personajul într-un loc nou

> 🏅 **PROIECT TERMINAT!** Chatbot: complet

## Acum ai putea face…

*Cu abilitățile pe care le-ai învățat, încearcă să faci aceste proiecte…*

### Quiz

Creează un quiz care pune întrebări și verifică dacă răspunsul jucătorului este corect. Se adaugă un punct la scorul jucătorului dacă răspunde corect la o întrebare.

![Quiz: „What's the capital of France?”](imagini/cap06_imagine33.jpg)

![Scriptul quizului: ask, if answer = Paris then say That's correct, change score by 1, else say Try again](imagini/cap06_imagine34.png)

### Aplicație de desenat

Folosește mouse-ul ca să desenezi pe scenă! Personajul ascuns va urmări cursorul mouse-ului, iar creionul desenează doar dacă butonul mouse-ului este apăsat.

![Un desen făcut cu aplicația](imagini/cap06_imagine35.jpg)

![Scriptul: clear, hide, forever, go to mouse-pointer, if mouse down? then pen down else pen up](imagini/cap06_imagine37.png)

### Joc de ghicit

Se alege la întâmplare un număr între 1 și 100, iar jucătorul trebuie să încerce să ghicească numărul ales. Ai putea chiar să adaptezi jocul ca să țină evidența numărului de încercări, ca să te poți întrece cu prietenii.

![Scriptul jocului de ghicit](imagini/cap06_imagine36.png)

![Peștele spune „Higher”](imagini/cap06_imagine38.jpg)

> 🤖 *Vrei să înveți despre coordonate? Treci la capitolul următor ca să faci un joc distractiv…*
