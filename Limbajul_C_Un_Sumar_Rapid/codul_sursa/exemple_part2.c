#include <stdio.h>

int main() {
    int numar;

    // 1. IF
    printf("Introdu un numar: ");
    scanf("%d", &numar);

    if (numar > 0) {
        printf("Numarul este pozitiv.\n");
    } else if (numar < 0) {
        printf("Numarul este negativ.\n");
    } else {
        printf("Numarul este zero.\n");
    }

    // 2. Operator ternar
    // Verificam daca numarul este par sau impar
    (numar % 2 == 0) ? printf("Numarul este par.\n") : printf("Numarul este impar.\n");

    // 3. SWITCH
    // Testam cateva valori specifice
    switch (numar) {
        case 1:
            printf("Ai introdus numarul 1.\n");
            break;
        case 2:
            printf("Ai introdus numarul 2.\n");
            break;
        case 3:
            printf("Ai introdus numarul 3.\n");
            break;
        default:
            printf("Numarul nu este nici 1, nici 2, nici 3.\n");
    }

    // 4. WHILE
    // Afisam numerele de la 1 la 5 folosind while
    int i = 1;
    printf("Afisare cu while: ");
    while (i <= 5) {
        printf("%d ", i);
        i++;
    }
    printf("\n");

    // 5. DO-WHILE
    // Afisam numerele de la 5 la 1 folosind do-while
    i = 5;
    printf("Afisare cu do-while: ");
    do {
        printf("%d ", i);
        i--;
    } while (i > 0);
    printf("\n");

    // 6. FOR
    // Afisam numerele de la 1 la 10, sarind peste cele pare
    printf("Afisare cu for (sarim peste numerele pare): ");
    for (i = 1; i <= 10; i++) {
        if (i % 2 == 0) {
            continue;  // Sare peste numerele pare
        }
        printf("%d ", i);
    }
    printf("\n");

    // 7. BREAK
    // Cautam primul numar divizibil cu 7 intre 1 si 20
    printf("Primul numar divizibil cu 7 intre 1 si 20: ");
    for (i = 1; i <= 20; i++) {
        if (i % 7 == 0) {
            printf("%d\n", i);
            break;  // Iesim din bucla cand am gasit primul numar
        }
    }

    return 0;
}
