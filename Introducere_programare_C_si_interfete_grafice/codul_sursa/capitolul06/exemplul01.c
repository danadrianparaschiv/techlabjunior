#include <stdio.h>

int sum (int a, int b) 
{ 
  int res; 
  res = a + b; 
  return res; 
}

void main (void) 
{ 
  int y = 2; 
  int z = sum (5, y);
  printf ("Rezultatul adunarii lui 5 cu %d este %d\n", y, z); 
}