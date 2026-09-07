# Publicarea cărții pe TechLab Junior

Editează textul, imaginile și metadatele în acest repository. După integrarea modificărilor în `main`, workflow-ul **Publică jocurile clasice pe staging** verifică ediția, creează un PR în repository-ul site-ului și îl integrează în `test` numai după testele unitare, testele ambelor cititoare și build-ul Azure. Așteaptă deployment-ul de staging, apoi verifică [pagina cărții](https://black-dune-09f766403.4.azurestaticapps.net/biblioteca/programeaza-jocurile-clasice).

## Ce poți modifica

- Textul și exemplele de cod se editează în fișierele Markdown. Titlul fiecărui capitol vine din primul `#` al fișierului; subtitlurile „Programăm azi” sunt adaptate ierarhic în cititor, fără schimbarea textului.
- Imaginile JPEG și PNG se păstrează în `imagini/`, cu texte alternative descriptive și legături relative. Fișierele lipsă opresc publicarea.
- `carte.json` definește prezentarea, autorii, licența, coperta și cuprinsul. `preparationChapter` indică pagina cu instrucțiunile de instalare.
- Păstrează ID-urile și slugurile paginilor deja publicate. Ele mențin adresele stabile chiar dacă schimbi titlul. Un fișier redenumit trebuie actualizat în metadate și în legăturile din text.
- Cuvântul înainte are `kind: "preface"`, este primul în cuprins și nu primește număr. Cele opt capitole păstrează numerotarea originală. Ordinea grupurilor determină navigarea Anterior/Următor.
- Păstrează creditele și licența din README. Secțiunea publicată despre ediție începe la subtitlul indicat în `edition.heading`.

Codul jocurilor din `codul_sursa/` rămâne disponibil în GitHub. Legăturile din cititor către directoare și fișiere indică exact commitul ediției publicate, astfel încât explicațiile și codul să poată fi consultate împreună. Codul afișat în carte poate fi copiat și rulat pe calculator cu Python și Pygame Zero.

## Rulare manuală și revenire

În **Actions → Publică jocurile clasice pe staging → Run workflow**, selectează `main` sau un SHA complet pentru ediția dorită. Repetarea aceleiași ediții nu creează PR nou. O versiune anterioară trece prin aceleași verificări înainte de revenirea pe staging.

La eșec, consultă pasul roșu din Actions. Ediția existentă rămâne online. Dacă ramura `test` avansează în timpul validării, reia workflow-ul; nu modifica manual PR-ul automat. Rulările Arduino și ale acestei cărți folosesc aceeași coadă GitHub, cu cel mult 100 de rulări în așteptare, pentru a evita integrarea simultană în site.

Aplicația GitHub și secretul sunt comune cu pilotul Arduino; nu trebuie creată altă cheie. Tokenurile sunt temporare și limitate la repository-ul site-ului. Fiecare publicator poate modifica numai lock-ul cărții selectate. Publicarea în producție se face separat, după revizuire și aprobare, prin PR `test` → `main` în repository-ul site-ului.
