#include <stdio.h>

/*
Un pointer este doar adresa unui bloc de memorie cu o variabilă în el; asta e tot. Deci, dacă declarați o variabilă și un pointer
 la acea variabilă, puteți accesa valoarea din acel bloc de memorie în două moduri: fie cu numele variabilei, fie cu pointerul.
*/


void main (void) 
{ 
  int a; 
  int *ptr_to_a;
  
  ptr_to_a = &a;
  
  a = 5; 
  printf ("Valoarea lui a este %d\n", a);
  
  *ptr_to_a = 6; 
  printf ("Valoarea lui a este %d\n", a);
  
  printf ("Valoarea lui ptr_to_a este %d\n", ptr_to_a); 
  printf ("Si stocheaza valoare %d\n", *ptr_to_a); 
  printf ("Adresa variabilei a este %d\n", &a); 
}