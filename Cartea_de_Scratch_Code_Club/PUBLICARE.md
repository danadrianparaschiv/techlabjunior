# Publicarea pe TechLab Junior

Editează cartea în acest folder, apoi integrează PR-ul în `main`. Workflow-ul **Publică Scratch Code Club pe staging** importă ediția și o validează. Aplicația GitHub existentă creează un PR în site care modifică numai `content/scratch-code-club.lock.json`, așteaptă testele unitare, testele cititoarelor și build-ul Azure, apoi îl integrează în `test`.

## Formatul sursei

- `carte.json` definește prezentarea, autorii, licența și cele 10 capitole. Titlurile vin din primul H1 al fișierelor Markdown. Păstrează ID-urile și slugurile pentru a păstra adresele deja publicate.
- Păstrează blocurile Scratch ca imagini JPEG/PNG în `imagini/`, cu texte alternative. Nu sunt cod text executabil în cititor. Proiectele se deschid prin legăturile existente către Scratch și Raspberry Pi.
- Pașii `- [ ]` devin căsuțe de bifat în site. Bifele sunt temporare pentru pagina deschisă; se resetează la schimbarea capitolului sau reîncărcare.
- Indiciile folosesc exact forma existentă `<details><summary><b>INDICIU</b> (apasă ca să îl vezi)</summary>`, urmată de conținut Markdown și `</details>` pe linie separată. Păstrează prefixele `>` dacă indiciul se află într-o casetă. Site-ul recunoaște numai acest format limitat, fără a executa HTML.
- Păstrează notele despre Scratch 2 și 3, creditele și licența din README.

## Folosirea CLI-ului

```sh
gh workflow run publish-scratch-code-club.yml --repo danadrianparaschiv/techlabjunior --ref main -f source_ref=main
gh run list --repo danadrianparaschiv/techlabjunior --workflow publish-scratch-code-club.yml --limit 5
gh run watch <RUN_ID> --repo danadrianparaschiv/techlabjunior
```

`source_ref` acceptă `main` sau un SHA complet. Pentru revenire, selectează un commit anterior care conține metadatele; verificările sunt aceleași. Repetarea ediției deja selectate nu creează PR nou. La eșec verifică logul Actions; dacă baza site-ului a avansat, reia workflow-ul. Nu modifica manual PR-ul automat.

Workflow-ul folosește aplicația, secretul și coada comună deja existente. Publicarea cărților este serializată. După deployment, verifică [cartea pe staging](https://black-dune-09f766403.4.azurestaticapps.net/biblioteca/cartea-de-scratch-code-club). Promovarea în producție se face separat, prin PR `test` → `main`, după revizuire și aprobare.
