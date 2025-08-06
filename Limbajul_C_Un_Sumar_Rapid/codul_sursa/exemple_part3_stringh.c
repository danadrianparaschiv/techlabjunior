#include <stdio.h>
#include <string.h>

int main() {
    char str1[100] = "Salut";
    char str2[100] = " lume!";
    char copie[100];
    char buffer[100] = "Curs de programare in C";
    char *gasit;
    int lungime;

    // 1. strlen - calculează lungimea unui șir
    lungime = strlen(str1);
    printf("Lungimea lui str1 este: %d caractere\n\n", lungime);

    // 2. strcpy - copiază un șir complet
    strcpy(copie, str1); // copie <- "Salut"
    printf("Dupa copiere, 'copie' este: %s\n", copie);

    // 3. strncpy - copiază primele N caractere
    strncpy(copie, buffer, 4); // copiază primele 4 caractere din buffer
    copie[4] = '\0'; // adăugăm terminator de șir
    printf("Primele 4 caractere din buffer: %s\n\n", copie);

    // 4. strcat - concatenează două șiruri
    strcat(str1, str2); // str1 <- "Salut lume!"
    printf("Dupa concatenare, str1 este: %s\n", str1);

    // 5. strncat - concatenează doar primele N caractere
    strncat(str1, " Extra text", 6); // adaugă doar " Extra"
    printf("Dupa strncat, str1 este: %s\n\n", str1);

    // 6. strcmp - compară două șiruri
    if (strcmp(str1, copie) == 0) {
        printf("str1 si copie sunt egale.\n");
    } else {
        printf("str1 si copie NU sunt egale.\n");
    }

    // 7. strncmp - compară doar primele N caractere
    if (strncmp("Salutare", "Salut", 5) == 0) {
        printf("Primele 5 caractere sunt egale.\n\n");
    }

    // 8. strchr - caută prima apariție a unui caracter
    gasit = strchr(str1, 'u');
    if (gasit != NULL) {
        printf("Caracterul 'u' a fost gasit la pozitia: %ld\n", gasit - str1);
    }

    // 9. strrchr - caută ultima apariție a unui caracter
    gasit = strrchr(str1, 'u');
    if (gasit != NULL) {
        printf("Ultima aparitie a lui 'u' este la pozitia: %ld\n\n", gasit - str1);
    }

    // 10. strstr - caută un sub-șir într-un șir
    gasit = strstr(str1, "lume");
    if (gasit != NULL) {
        printf("Subsirul 'lume' a fost gasit la pozitia: %ld\n", gasit - str1);
    }

    // 11. strtok - împarte un șir în token-uri separate de spațiu
    char text[50] = "Ana are mere rosii";
    char *token = strtok(text, " ");
    printf("\nCuvintele din text sunt:\n");
    while (token != NULL) {
        printf("%s\n", token);
        token = strtok(NULL, " ");
    }

    // 12. memset - setează toate caracterele unui șir la o valoare
    char spatiu[20];
    memset(spatiu, '*', 10); // primele 10 caractere devin '*'
    spatiu[10] = '\0';
    printf("\nSir creat cu memset: %s\n", spatiu);

    // 13. memcpy - copiază un bloc de memorie
    char sursa[] = "Copiere cu memcpy";
    char destinatie[30];
    memcpy(destinatie, sursa, strlen(sursa) + 1); // copiem inclusiv '\0'
    printf("Dupa memcpy, destinatia este: %s\n", destinatie);

    return 0;
}
