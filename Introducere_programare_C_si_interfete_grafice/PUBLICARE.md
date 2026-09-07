# Publicarea în TechLab Junior

Textul se editează aici, în GitHub. `carte.json` păstrează titlul, autorii, prezentarea și ordinea capitolelor. ID-urile și slugurile capitolelor publicate rămân stabile când schimbi un titlu sau textul. Câmpurile `cover`, `year` și `translation` pot fi `null` când nu se aplică sau nu sunt cunoscute.

După integrarea unui PR în `main`, workflow-ul cărții validează sursele și deschide un PR care actualizează numai lock-ul ei în site. Publicarea automată așteaptă testele și build-ul înainte de integrarea în `test` (staging). Producția se promovează separat, după revizuire.

Publicare manuală prin CLI:

```sh
gh workflow run publish-c-introduction.yml --repo danadrianparaschiv/techlabjunior --ref main -f source_ref=main
gh run list --repo danadrianparaschiv/techlabjunior --workflow publish-c-introduction.yml
```

Poți folosi un SHA complet în loc de `main`, inclusiv pentru revenire. Repetarea ediției curente nu creează un PR nou. Imaginile se păstrează în `imagini/`; exemplele de cod se scriu în blocuri Markdown delimitate. Documentele nu execută cod în site.

Pagina de lectură: /biblioteca/introducere-in-c.

La adăugarea unui capitol, înregistrează fișierul în `carte.json`, cu un ID și un slug noi, apoi adaugă ID-ul în grupul potrivit din `groups`. Păstrează ID-urile și slugurile capitolelor existente. Actualizează și prezentarea cărții dacă se schimbă conținutul disponibil.

Ediția completă include capitolele 1–26. Programele C/GTK și fișierul Glade rămân în `codul_sursa/`, iar PDF-ul original rămâne în sursă; cititorul oferă legături către aceeași ediție GitHub.
