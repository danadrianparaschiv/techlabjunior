#include <stdio.h>

void main (void) 
{ 
  char input[256], name[256]; 
  int age;    
  
  printf ("Cum te cheama?\n"); 
  fgets (input, 256, stdin); 
  sscanf (input, "%s", name);    
  
  printf ("Salut, %s. Cati ani ai?\n", name); 
  while (1) 
  { 
    fgets (input, 256, stdin); 
    if (sscanf (input, "%d%d", &age) == 1) break; 
    printf ("Nu ai introdus varsta corect!\n"); 
  }    
  
  printf ("Hmmm, %s, n-as fi zis ca ai %d ani...\n", name, age); 
}