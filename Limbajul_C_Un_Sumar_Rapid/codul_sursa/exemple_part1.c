#include <stdio.h>
#include <string.h>

// Definim un tip de date compus (struct) pentru a reprezenta o persoană
struct Persoana {
    char nume[50];
    int varsta;
};

int main() {
    // ---- Tipuri de date și variabile ----
    int a = 10;          // tip întreg
    float b = 5.5;       // tip real
    char c = 'Z';        // caracter
    double d = 3.14159;  // număr în virgulă mobilă cu precizie dublă

    printf("Valoarea lui a: %d\n", a);
    printf("Valoarea lui b: %.2f\n", b);
    printf("Valoarea lui c: %c\n", c);
    printf("Valoarea lui d: %.5lf\n", d);

    // ---- Array-uri ----
    int numere[5] = {1, 2, 3, 4, 5}; // array de 5 elemente
    printf("\nElementele array-ului numere:\n");
    for(int i = 0; i < 5; i++) {
        printf("numere[%d] = %d\n", i, numere[i]);
    }

    // ---- Pointeri ----
    int x = 42;
    int *ptr = &x; // pointer către variabila x
    printf("\nValoarea lui x prin pointer: %d\n", *ptr);
    printf("Adresa lui x: %p\n", (void*)ptr);

    // Modificăm valoarea lui x folosind pointerul
    *ptr = 100;
    printf("Valoarea lui x după modificare prin pointer: %d\n", x);

    // ---- Tipuri de date compuse (struct) ----
    struct Persoana p1;                  // declarăm o variabilă de tip Persoana
    strcpy(p1.nume, "Ana");              // atribuim un nume
    p1.varsta = 25;                      // atribuim o vârstă

    printf("\nPersoana:\n");
    printf("Nume: %s, Varsta: %d\n", p1.nume, p1.varsta);

    // Array de structuri
    struct Persoana persoane[2];
    strcpy(persoane[0].nume, "Ion");
    persoane[0].varsta = 30;
    strcpy(persoane[1].nume, "Maria");
    persoane[1].varsta = 28;

    printf("\nLista persoane:\n");
    for(int i = 0; i < 2; i++) {
        printf("Nume: %s, Varsta: %d\n", persoane[i].nume, persoane[i].varsta);
    }

    return 0;
}
