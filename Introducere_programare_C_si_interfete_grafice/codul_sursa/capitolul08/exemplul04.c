#include <stdio.h>

void main (void) 
{ 
  int val; 
  char string[10] = "250";
  
  sscanf (string, "%d", &val); 
  printf ("The value in the string is %d\n", val); 
}