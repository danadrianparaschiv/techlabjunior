#include <stdio.h>

void main (void) 
{ 
    int val = 12; 
    char string[50];

    sprintf (string, "The value of val is %d\n", val); 
    printf ("%s", string); 

    // Declarare
    int numbers[5];              // Tablou de 5 întregi
    int matrix[3][4];            // Tablou 2D: 3 rânduri × 4 coloane

    // Inițializare
    int values[5] = {1, 2, 3, 4, 5};

    // Accesare
    numbers[0] = 10;             // Primul element (indexul 0)
    numbers[4] = 50;             // Ultimul element (indexul 4)

    // Declarare și inițializare
    char name[20] = "John";      // Șir de max 19 caractere + '\0'

    // Accesare caractere individuale
    name[0] = 'J';               // Primul caracter
    name[1] = 'o';               // Al doilea caracter

    // Scriere în șir
    sprintf(name, "Hello %s", "World");

    // Afișare
    printf("%s\n", name);        // Afișează întregul șir
    printf("%c\n", name[0]);     // Afișează primul caracter

}