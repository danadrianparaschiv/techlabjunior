# Actualizarea cărții pe TechLab Junior

Editează cartea în acest repository. Site-ul preia o versiune exactă din GitHub; nu trebuie să copiezi textul sau imaginile în repository-ul site-ului.

1. Modifică fișierele Markdown și imaginile din `Primii_pasi_cu_Arduino/`, prin editorul GitHub sau local.
2. Trimite modificările printr-un pull request către `main` și integrează-l când textul este gata.
3. Workflow-ul **Publică Arduino pe staging** importă și verifică ediția, apoi deschide în `techlab-junior.ro` un PR care schimbă numai versiunea Arduino.
4. După testele unitare, testele de navigare ale cititorului și build-ul Azure, PR-ul se integrează automat în `test`. Deploy-ul pe staging pornește imediat; așteaptă să fie verde în Actions la site.
5. Revizuiește [cartea pe staging](https://black-dune-09f766403.4.azurestaticapps.net/biblioteca/primii-pasi-cu-arduino). Publicarea în producție rămâne separată: PR `test` → `main` în repository-ul site-ului, după aprobarea ta.

## Cuprins și metadate

`carte.json` păstrează titlul cărții, autorii, licența, textele de prezentare, coperta, sursa creditelor și cuprinsul. Nu conține cod executabil.

- Titlul fiecărui capitol este primul titlu `#` din fișierul lui Markdown. Îl poți modifica acolo.
- `chapters[].file` indică fișierul Markdown; actualizează-l dacă redenumești fișierul și corectează legăturile din celelalte capitole.
- **Nu schimba `id` sau `slug` pentru un capitol existent.** Acestea păstrează adresa publicată, chiar dacă îi schimbi titlul.
- Ordinea de lectură este ordinea grupurilor și a ID-urilor din `groups[].chapters`. Fiecare ID trebuie să apară exact o dată.
- Pentru un capitol nou, adaugă fișierul, o intrare cu ID și slug noi și ID-ul în grupul dorit. Numerotarea și Anterior/Următor se generează automat. Actualizează și numerotarea editorială/trimiterile din text dacă reordonezi capitole.
- Imaginile JPEG se păstrează în `imagini/`, cu nume simple fără spații. Folosește căi relative și texte alternative în Markdown.
- Păstrează creditele și licența din README. `edition.heading` identifică începutul informațiilor afișate despre ediție; actualizează-l dacă redenumești acel subtitlu.

## Publicare manuală și revenire

În **Actions → Publică Arduino pe staging → Run workflow**, alege `main` pentru ultima ediție sau SHA-ul complet al unei ediții anterioare pentru revenire. Se aplică aceleași verificări și tot staging este destinația. Repetarea aceleiași versiuni nu creează un PR nou.

Dacă validarea eșuează, ediția existentă rămâne online. Consultă pasul roșu din Actions, corectează sursa și integrează corecția. Dacă ramura site-ului avansează în timpul verificărilor, rulează din nou workflow-ul pentru a valida pe noua bază. Dacă un PR automat a fost modificat manual, revizuiește-l; automatizarea nu îl integrează peste modificări neașteptate.

## Configurare (o singură dată)

Aplicația GitHub dedicată se instalează numai în `techlab-junior.ro`, cu Contents și Pull requests: read/write, Checks: read. În acest repository se configurează variabila Actions `BOOK_PUBLISHER_CLIENT_ID` și secretul `BOOK_PUBLISHER_PRIVATE_KEY`. Cheia privată nu se salvează în fișierele cărții. Workflow-ul emite un token de instalare temporar și îl revocă după execuție.

Pilotul publică numai Arduino. Celelalte cărți nu sunt preluate de acest workflow.
