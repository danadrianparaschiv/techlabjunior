# O introducere în programarea C și a interfețelor grafice
## Autor: Simon Long
## Tradus în limba română

---

## Despre această carte

Această carte este o traducere în limba română a cărții "An Introduction to C and GUI Programming" (2nd Edition), actualizată pentru GTK 3. Cartea oferă o introducere completă în programarea C, de la concepte de bază până la crearea de aplicații grafice complexe folosind biblioteca GTK.

## Structura cărții

Cartea este împărțită în două părți principale:

### Partea I: Programare C (Capitolele 1-12)
Primele 12 capitole acoperă fundamentele limbajului C:

1. [**Introducere**](Capitol_01_Introducere.md) - Ce este C și de ce să-l învățați 
2. [**Variabile și aritmetica**](Capitol_02_Variabile_si_aritmetica.md)- Tipuri de date și operații matematice
3. [**Condiții și comparații**](Capitol_03_Conditii_si_comparatii.md) - Instrucțiuni if-else și bucle while
4. [**Control avansat al fluxului**](Capitol_04_Control_flux_avansat.md) - Bucle for și instrucțiuni switch
5. [**Pointeri**](Capitol_05_Pointeri.md) - Lucrul cu adrese de memorie
6. [**Funcții**](Capitol_06_Functii.md) - Organizarea codului în funcții reutilizabile
7. [**Tablouri și șiruri**](Capitol_07_Tablouri_si_siruri.md) - Lucrul cu tablouri de valori și text
8. [**Biblioteca de șiruri**](Capitol_08_Biblioteca_manipulare_siruri.md) - Funcții utile pentru manipularea textului
9. [**Interactiunea cu utilizatorul**](Capitol_09_Interactiunea_cu_utilizatorul.md) - Citirea și procesarea datelor de la utilizator
10. [**Fișiere de Intrare/Ieșire**](Capitol_10_Fisiere_de_intrare_iesire.md) - Lucrul cu fișiere
11. [**Mai multe despre tipuri și variabile**](Capitol_11_Mai_multe_despre_tipuri_variabile.md) - Concepte avansate de tipuri
12. [**Fișiere antet și preprocesor**](Capitol_12_Fisiere_antet_preprocesor.md) - Organizarea proiectelor mari

### Partea a II-a: Programare GUI cu GTK (Capitolele 13-26)
Capitolele 13-26 se concentrează pe crearea de interfețe grafice cu GTK 3:

13. [**Introducere în GTK**](Capitol_13_Introducere_in_GTK.md) - Ce este GTK, versiunile lui și temele
14. [**Primul program GTK**](Capitol_14_Primul_program_GTK.md) - Prima fereastră și compilarea cu pkg-config
15. [**Butoane**](Capitol_15_Butoane.md) - Containere, semnale și funcții callback
16. [**Etichete și aspect**](Capitol_16_Etichete_si_aspect.md) - GtkLabel, GtkBox și un contor de apăsări
17. [**Aspect avansat**](Capitol_17_Aspect_avansat.md) - expand, fill, padding și GtkGrid
18. [**Introducerea datelor în GUI**](Capitol_18_Introducerea_datelor_in_GUI.md) - Câmpuri de text, butoane rotative, casete de bifat și butoane radio
19. [**Casete combo și list store-uri**](Capitol_19_Casete_combo_si_list_store.md) - GtkComboBoxText, GtkListStore și sortarea datelor
20. [**Vizualizări arborescente**](Capitol_20_Vizualizari_arborescente.md) - GtkTreeView cu text și pictograme, citirea selecției
21. [**Meniuri**](Capitol_21_Meniuri.md) - Bare de meniu și meniuri contextuale
22. [**Dialoguri**](Capitol_22_Dialoguri.md) - GtkDialog, zona de acțiune și zona de conținut
23. [**Dialoguri încorporate**](Capitol_23_Dialoguri_incorporate.md) - Alegerea fișierelor, a culorilor și a fonturilor
24. [**Personalizarea widgeturilor**](Capitol_24_Personalizarea_widgeturilor.md) - Proprietăți cu g_object_set și teme CSS
25. [**Glade**](Capitol_25_Glade.md) - Editorul de aspect și GtkBuilder
26. [**Referință rapidă C**](Capitol_26_Referinta_rapida_C.md) - Structuri de control, tipuri, specificatori de format și operatori

## Cum să folosiți această carte

### Cerințe preliminare
- Un Raspberry Pi cu Raspberry Pi OS (sau orice sistem Linux)
- Compilatorul gcc (inclus în majoritatea distribuțiilor Linux)
- Un editor de text (Geany, Leafpad, nano, etc.)

### Compilarea programelor

Pentru a compila un program C simplu:
```bash
gcc -o program_meu fisier.c
```

Pentru programe GTK:
```bash
gcc -o program_meu fisier.c `pkg-config --cflags --libs gtk+-3.0`
```

### Rularea programelor
```bash
./program_meu
```

## Codul sursă și imaginile

Folderul [codul_sursa](codul_sursa/) conține programele din carte, câte un folder pe capitol (`capitolulNN/exemplulNN.c`). Pentru partea a doua, toate programele GTK din capitolele 14-25 sunt incluse ca fișiere complete, gata de compilat, inclusiv un fișier de aspect `mylayout.glade` pentru capitolul 25. Capturile de ecran din capitolele 13-25 se găsesc în folderul [imagini](imagini/), cu numele `capNN_imagineNN.jpg`.

Cartea originală, în limba engleză, este inclusă aici: [C_and_GUI_Programming_2nd_Edition_EN_ORIGINAL.pdf](C_and_GUI_Programming_2nd_Edition_EN_ORIGINAL.pdf). Ea poate fi descărcată gratuit și din depozitul Raspberry Pi Press: [github.com/raspberrypipress/released-pdfs](https://github.com/raspberrypipress/released-pdfs).

## Convenții folosite în carte

### Formatare cod
Toate exemplele de cod sunt formatate cu sintaxă evidențiată și sunt funcționale.

### Casete informative
Cartea conține mai multe tipuri de casete informative:

> **NOTĂ**
> Informații importante de reținut

> **ATENȚIE**
> Avertismente despre greșeli comune

> **SFAT**
> Sugestii și best practices

> **NOTA TRADUCĂTORULUI**
> Explicații adăugate în traducere: nume de funcții sau pachete tipărite greșit în original, diferențe față de versiunile actuale de Raspberry Pi OS și GTK

> **CODUL SURSĂ**
> Unde se găsesc, în folderul `codul_sursa`, programele din capitolul respectiv

### Ce s-a schimbat față de original

- **Imagini.** Capitolele de C nu au ilustrații; pentru capitolele de GTK, capturile de ecran din carte au fost extrase în folderul `imagini` și au legendele traduse.
- **Corecturi.** Câteva greșeli de tipar din original sunt semnalate în note: numele pachetului `gtk+-3.0`, funcția `G_CALLBACK`, widgetul `GtkEntry` și ordinea părților buclei `for` din referința rapidă.
- **Rezumate.** Fiecare capitol se încheie cu o listă „Puncte cheie”, adăugată în traducere.

## Resurse suplimentare

- [Documentația oficială GTK](https://docs.gtk.org/)
- [Tutorial C în limba engleză](https://www.learn-c.org/)
- [Comunitatea Raspberry Pi](https://www.raspberrypi.org/forums/)

## Despre autor

Simon Long este inginer la Raspberry Pi, responsabil de Raspberry Pi Desktop și de aplicațiile lui. Înainte de Raspberry Pi a lucrat la Broadcom, unde l-a cunoscut pe Eben Upton, iar înainte de asta a petrecut zece ani ca inginer software și designer de interfețe la o mare firmă de consultanță. Cartea a fost publicată de Raspberry Pi Press (Raspberry Pi Trading Ltd) în 2019 (ISBN 978-1-912047-45-1), cu Russell Barnes ca director de publicare și Phil King ca redactor; ediția a doua este actualizată pentru GTK 3.

Traducerea și adaptarea în limba română au fost realizate de Dan Paraschiv, inițiatorul proiectului TechLab Junior.

## Licență

Conținutul original este licențiat sub Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0).
