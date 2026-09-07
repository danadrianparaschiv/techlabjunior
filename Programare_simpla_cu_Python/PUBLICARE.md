# Publicarea în TechLab Junior

Textul se editează aici, în GitHub. `carte.json` păstrează titlul, autorii, prezentarea și ordinea capitolelor. ID-urile și slugurile capitolelor publicate rămân stabile când schimbi un titlu sau textul. Câmpurile `cover`, `year` și `translation` pot fi `null` când nu se aplică sau nu sunt cunoscute.

După integrarea unui PR în `main`, workflow-ul cărții validează sursele și deschide un PR care actualizează numai lock-ul ei în site. Publicarea automată așteaptă testele și build-ul înainte de integrarea în `test` (staging). Producția se promovează separat, după revizuire.

Publicare manuală prin CLI:

```sh
gh workflow run publish-python-adventure.yml --repo danadrianparaschiv/techlabjunior --ref main -f source_ref=main
gh run list --repo danadrianparaschiv/techlabjunior --workflow publish-python-adventure.yml
```

Poți folosi un SHA complet în loc de `main`, inclusiv pentru revenire. Repetarea ediției curente nu creează un PR nou. Imaginile se păstrează în `imagini/`; exemplele de cod se scriu în blocuri Markdown delimitate. Documentele nu execută cod în site.

Pagina de lectură: /biblioteca/programare-simpla-cu-python.
