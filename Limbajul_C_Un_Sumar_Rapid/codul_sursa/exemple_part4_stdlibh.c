#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Funcție de comparație pentru qsort și bsearch
int compara(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main() {
    // 1. Conversii de la șir la numere
    char strNum[] = "1234";
    char strFloat[] = "3.14";
    char strLong[] = "987654321";

    int numar = atoi(strNum);          // Conversie la int
    double pi = atof(strFloat);        // Conversie la double
    long numarMare = strtol(strLong, NULL, 10); // Conversie la long (baza 10)

    printf("atoi: %s -> %d\n", strNum, numar);
    printf("atof: %s -> %.2f\n", strFloat, pi);
    printf("strtol: %s -> %ld\n\n", strLong, numarMare);

    // 2. Generare numere aleatoare
    srand((unsigned)time(NULL)); // Seed din timpul curent
    printf("Numere aleatoare intre 0 si 99: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", rand() % 100);
    }
    printf("\n\n");

    // 3. Valoarea absolută și diviziunea
    int x = -25;
    int y = 7;
    printf("abs(%d) = %d\n", x, abs(x));

    div_t rezultat = div(x, y); // returnează câtul și restul
    printf("div(%d, %d) = cat: %d, rest: %d\n\n", x, y, rezultat.quot, rezultat.rem);

    // 4. Alocare memorie cu malloc și calloc
    int n = 5;
    int *vector = malloc(n * sizeof(int));
    if (!vector) {
        printf("Eroare la alocare memorie!\n");
        exit(1); // Termină programul cu cod de eroare
    }

    // Inițializare cu valori aleatoare
    for (int i = 0; i < n; i++) {
        vector[i] = rand() % 50;
    }

    printf("Vector initial:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", vector[i]);
    }
    printf("\n\n");

    // 5. Re-alocare memorie
    n = 8;
    vector = realloc(vector, n * sizeof(int));
    if (!vector) {
        printf("Eroare la realocare memorie!\n");
        exit(1);
    }

    for (int i = 5; i < n; i++) {
        vector[i] = rand() % 50;
    }

    printf("Vector dupa realocare (8 elemente):\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", vector[i]);
    }
    printf("\n\n");

    // 6. Sortare cu qsort
    qsort(vector, n, sizeof(int), compara);
    printf("Vector sortat:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", vector[i]);
    }
    printf("\n\n");

    // 7. Căutare cu bsearch
    int cheie = vector[3]; // folosim un element existent
    int *gasit = bsearch(&cheie, vector, n, sizeof(int), compara);
    if (gasit != NULL) {
        printf("Elementul %d a fost gasit in vector.\n\n", *gasit);
    } else {
        printf("Elementul %d nu a fost gasit.\n\n", cheie);
    }

    // 8. system() - execută o comandă a sistemului de operare
    printf("Continutul directorului curent:\n");
    system("ls"); // Pentru Windows folosiți "dir"

    // 9. Eliberare memorie
    free(vector);

    // 10. exit() - încheie programul
    printf("\nProgram terminat cu succes.\n");
    exit(0);
}
