#include <stdio.h>

void main (void) 
{ 
  char input[256]; 
  int age;    
  
  printf ("Cum te cheama?\n"); 
  scanf ("%s", input);    
  
  printf ("Salut, %s. Cati ani ai?\n", input); 
  scanf ("%d", &age);    
  
  printf ("Hmmm, %s, n-as fi zis ca ai %d ani...\n", input, age); 
}