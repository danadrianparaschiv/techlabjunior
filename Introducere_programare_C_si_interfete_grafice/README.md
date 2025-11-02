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
Capitolele 13-26 se concentrează pe crearea de interfețe grafice:

13. **Toolkit-ul GTK** - Introducere în GTK
14. **Primul tău program GTK** - Crearea primei ferestre
15. **Butoane** - Adăugarea de butoane interactive
16. **Etichete și aspect** - Organizarea layout-ului
17. **Mai multe opțiuni de aspect** - Opțiuni avansate de layout
18. **Intrare text și butoane comutare** - Widget-uri pentru input
19. **Casete combo și butoane spin** - Widget-uri de selecție
20. **Vizualizări arborescentă** - Afișarea datelor structurate
21. **Meniuri** - Crearea meniurilor aplicației
22. **Dialoguri** - Ferestre de dialog personalizate
23. **Dialoguri încorporate** - Dialoguri standard GTK
24. **Personalizarea widget-urilor** - Modificarea aspectului
25. **Glade** - Construirea interfețelor vizual
26. **Referință** - Ghid de referință rapid

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

## Resurse suplimentare

- [Documentația oficială GTK](https://docs.gtk.org/)
- [Tutorial C în limba engleză](https://www.learn-c.org/)
- [Comunitatea Raspberry Pi](https://www.raspberrypi.org/forums/)

## Despre autor

Simon Long este un programator experimentat care a lucrat la dezvoltarea Raspberry Pi OS și a multor aplicații pentru platformă.

## Licență

Conținutul original este licențiat sub Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0).
