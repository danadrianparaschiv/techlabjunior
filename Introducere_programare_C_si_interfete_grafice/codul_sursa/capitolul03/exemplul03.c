#include <stdio.h>

int main (void) 
{ 
  int a = 0;
  
  do 
  { 
    printf ("a este egal cu %d\n", a); 
    a++; 
  } while (a < 5); 
  
  printf ("a este egal cu %d si am terminat\n", a); 
}