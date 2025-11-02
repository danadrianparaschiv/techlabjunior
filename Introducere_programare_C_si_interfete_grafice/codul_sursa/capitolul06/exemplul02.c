#include <stdio.h>

/*
Puteți returna mai mult de un rezultat dintr-o funcție? Puteți returna doar o singură valoare, 
dar puteți folosi și pointeri pentru a transmite mai multe elemente de date înapoi la funcția apelantă. Luați în considerare acest exemplu:
*/

int sum_and_diff (int a, int b, int *res) 
{ 
  int sum; 
  sum = a + b; 
  *res = a - b; 
  return sum; 
}

void main (void) 
{ 
  int b = 2; 
  int diff;
  
  printf ("Rezultatul adunarii lui 5 cu %d este %d\n", b,  
      sum_and_diff (5, b, &diff)); 
  printf ("Diferenata dintre 5 si  %d este %d\n", b, diff); 
}