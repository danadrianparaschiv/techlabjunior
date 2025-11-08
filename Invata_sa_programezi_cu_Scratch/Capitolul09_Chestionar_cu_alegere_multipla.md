## Capitolul 9: Chestionar cu Alegere Multiplă

Uimește-ți prietenii cu propriul tău joc de chestionar, conținând sute de întrebări! Câte pot răspunde corect în 30 de secunde?

### Ai nevoie de:
- LibreOffice – dacă nu este instalat, deschide un terminal și tastează `sudo apt-get install libreoffice`
- Listă de capitale după mărime – wki.pe/List_of_national_capitals_by_population
- Acces la internet

### Caracteristici principale:
- Jocul rulează timp de 30 de secunde înainte de a se termina
- Dă click pentru a răspunde; datele de răspuns provin dintr-o listă de pe Wikipedia

Listele sunt folosite pentru a reține multe informații, dar adăugarea de elemente la ele bloc cu bloc poate dura mult timp și mult cod Scratch. În acest proiect, vei vedea cum poți importa (sau aduce) liste mari din alte locuri, astfel încât să poți face cu ușurință un joc de chestionar cu sute de întrebări. Pe măsură ce creezi acest joc, poți folosi propriul tău fundal și sprite-uri favorite și să le aranjezi cu suficient spațiu pentru ca răspunsurile să apară. Poate ai putea adăuga propria ta listă de întrebări? Orice funcționează, atâta timp cât fiecare răspuns se aplică doar unei întrebări.

### PASUL 01: Adună datele tale

Pentru acest joc, vei avea nevoie de două fișiere text: unul pentru întrebări și unul pentru răspunsuri. Vom face un chestionar despre orașe capitale, așa că un fișier va conține o listă de capitale, iar celălalt va conține țările în care se află, în aceeași ordine. Începe prin a găsi lista de orașe capitale după populație pe Wikipedia. Dă click și trage peste tabel pentru a-l evidenția, apoi apasă CTRL+C pentru a-l copia. Este mai ușor dacă evidențiezi de jos în sus. Ai răbdare când ecranul derulează!

### PASUL 02: Creează fișierele de întrebări

Deschide LibreOffice Calc și lipește tabelul folosind CTRL+V. Dă click pe OK. Acest lucru ar putea dura un minut sau două. Dă click deasupra coloanei tale de orașe pentru a o evidenția. Apasă CTRL+C pentru a copia coloana. Deschide editorul tău de text, Leafpad, care se află în meniul Accessories. Apasă CTRL+V pentru a lipi. Acum ar trebui să ai un fișier text care conține doar orașe capitale, fiecare pe o linie nouă. Dacă ai un titlu în partea de sus (cuvântul 'Capital'), șterge-l și elimină orice linii goale de la sfârșit. Salvează acest fișier ca `cities.txt`. Deschide un fișier nou în Leafpad și repetă procesul cu coloana de țări din LibreOffice Calc. De data aceasta, salvează fișierul Leafpad ca `countries.txt`.

### PASUL 03: Importarea datelor în Scratch

Pornește Scratch. Dă click pe butonul Variables și creează o listă. Numește-o `cities` și asigură-te că este pentru toate sprite-urile. Când lista goală apare pe Scenă, dă click dreapta pe ea și dă click pe `import` în meniu. Navighează la fișierele pe care tocmai le-ai creat și dă dublu-click pe fișierul tău de text cu orașe. Lista de pe Scenă va fi umplută cu orașele din fișierul tău. Repetă procesul pentru a face o listă numită `countries` și umple-o cu fișierul tău de țări. Fișierele tale de listă ar trebui să aibă aceeași lungime. Dă click dreapta pe căsuțele de listă de pe Scenă și alege `hide`.

### PASUL 04: Configurează variabilele tale

Prin partea Variables a Paletei de Blocuri, creează variabile numite:
- `question number` (folosită pentru a reține care pereche întrebare/răspuns întrebăm)
- `score` (scor)
- `shuffle choice` și `temporary storage` (folosite pentru amestecarea listei de opțiuni)
- `wrong answer` (folosit când facem lista de opțiuni greșite)

De asemenea, trebuie să creezi o variabilă numită `player guessed` pentru a reține răspunsul ales de jucător, și o listă numită `possible answers`. Fă toate aceste variabile și lista 'For all sprites'.

### PASUL 05: Creează codul principal al jocului

Codul principal al jocului folosește trei script-uri (Listinguri 1-3). Adaugă-le pe toate la sprite-ul pisicii. Jocul folosește broadcast-uri pentru a transmite controlul la diferite părți ale programului, inclusiv pe același sprite. Secțiunea 'ask a question' alege un număr aleatoriu de întrebare din lista de țări și face o listă de răspunsuri posibile. Include răspunsul corect și două răspunsuri greșite care trebuie să fie diferite de răspunsul corect. Codul apoi amestecă această listă pentru a pune răspunsurile într-o ordine aleatorie, înainte de a folosi un broadcast pentru a face sprite-urile de răspuns să apară și să își arate răspunsurile.

### PASUL 06: Creează sprite-urile de răspuns

Importă un sprite nou de folosit pentru afișarea răspunsului; noi folosim Gobo. Acest sprite are cinci script-uri scurte (Listingul 4). Creează variabila `answer choice`, dar dă click pe butonul pentru a o face 'For this sprite only'. Dacă jocul arată toate aceleași răspunsuri când îl rulezi, probabil ai făcut o greșeală aici! Când ai terminat acest sprite, dă click dreapta pe el și duplică-l de două ori. În copii, schimbă valoarea variabilei `answer choice` de sus la 2 pentru prima copie și 3 pentru a doua. Chestionare fericite!