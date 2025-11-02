#include <stdio.h>

// Declarații de funcții
int sum (int a, int b);
int sum_and_diff (int a, int b, int *res);

// Funcția main
void main (void) 
{ 
  int y = 2;
  int z = sum (5, y);
  int diff;
  
  printf ("The sum of 5 and %d is %d\n", y, z);
  
  printf ("The sum of 5 and %d is %d\n", y,  
      sum_and_diff (5, y, &diff));
  printf ("The difference of 5 and %d is %d\n", y, diff);
}

// Definiții de funcții
int sum (int a, int b) 
{ 
  return a + b; 
}

int sum_and_diff (int a, int b, int *res) 
{ 
  *res = a - b; 
  return a + b; 
}