#include <stdio.h>
#include <string.h>

void main (void) 
{
    char first[20] = "Hello";
    char second[20] = "World";
    char combined[40];
    
    // Copiază primul șir
    strcpy(combined, first);
    
    // Adaugă un spațiu
    strcat(combined, " ");
    
    // Adaugă al doilea șir
    strcat(combined, second);
    
    // Afișează rezultatul și lungimea
    printf("Result: %s\n", combined);
    printf("Length: %d\n", strlen(combined));
    
    // Compară șiruri
    if (strcmp(first, "Hello") == 0) 
    {
        printf("First string is 'Hello'\n");
    }
}